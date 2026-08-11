#!/usr/bin/env python3
"""Exact verifier for the real-multiplication infinitesimal kernel.

We model the HKR/Clifford action of

    HT^2(X) = H^2(O_X) + H^1(T_X) + H^0(wedge^2 T_X)

on the Markman real-multiplication secant class

    beta = A - (q/6) C^3,

where
    A = t*theta_1 + t^{-1}*theta_2,
    C = t^{-1}*theta_1 + t*theta_2.

All arithmetic is exact (fractions); no third-party packages are required.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from typing import Dict, Iterable, Tuple


Monomial = Tuple[int, ...]
Exterior = Dict[Monomial, Fraction]
Label = Tuple[str, int, int]


def add(left: Exterior, right: Exterior) -> Exterior:
    result: defaultdict[Monomial, Fraction] = defaultdict(Fraction)
    for monomial, coefficient in left.items():
        result[monomial] += coefficient
    for monomial, coefficient in right.items():
        result[monomial] += coefficient
    return {m: c for m, c in result.items() if c}


def scale(value: Exterior, scalar: Fraction | int) -> Exterior:
    scalar = Fraction(scalar)
    return {m: c * scalar for m, c in value.items() if c * scalar}


def generator(index: int) -> Exterior:
    return {(index,): Fraction(1)}


def wedge_monomials(left: Monomial, right: Monomial) -> tuple[Monomial | None, int]:
    if set(left) & set(right):
        return None, 0
    inversions = sum(1 for i in left for j in right if i > j)
    return tuple(sorted(left + right)), -1 if inversions % 2 else 1


def wedge(left: Exterior, right: Exterior) -> Exterior:
    result: defaultdict[Monomial, Fraction] = defaultdict(Fraction)
    for m_left, c_left in left.items():
        for m_right, c_right in right.items():
            monomial, sign = wedge_monomials(m_left, m_right)
            if monomial is not None:
                result[monomial] += c_left * c_right * sign
    return {m: c for m, c in result.items() if c}


def contract(value: Exterior, form_index: int) -> Exterior:
    """Contract by the tangent vector dual to one x_i generator."""
    result: defaultdict[Monomial, Fraction] = defaultdict(Fraction)
    for monomial, coefficient in value.items():
        if form_index not in monomial:
            continue
        position = monomial.index(form_index)
        reduced = monomial[:position] + monomial[position + 1 :]
        result[reduced] += coefficient * (-1 if position % 2 else 1)
    return {m: c for m, c in result.items() if c}


def power(value: Exterior, exponent: int) -> Exterior:
    result: Exterior = {(): Fraction(1)}
    for _ in range(exponent):
        result = wedge(result, value)
    return result


def theta(indices: Iterable[int], coefficient: Fraction | int = 1) -> Exterior:
    result: Exterior = {}
    for i in indices:
        result = add(
            result,
            scale(wedge(generator(i), generator(4 + i)), coefficient),
        )
    return result


def build_beta(t: Fraction, q: Fraction) -> Exterior:
    if t == 0 or q == 0:
        raise ValueError("t and q must be nonzero")
    theta_1 = theta((0, 1))
    theta_2 = theta((2, 3))
    a = add(scale(theta_1, t), scale(theta_2, 1 / t))
    c = add(scale(theta_1, 1 / t), scale(theta_2, t))
    return add(a, scale(power(c, 3), -q / 6))


def op_b(value: Exterior, i: int, j: int) -> Exterior:
    return wedge(wedge(generator(i), generator(j)), value)


def op_m(value: Exterior, i: int, j: int) -> Exterior:
    return wedge(generator(i), contract(value, 4 + j))


def op_p(value: Exterior, i: int, j: int) -> Exterior:
    # This fixes one HKR/Clifford sign convention. Reversing the convention
    # changes the sign of the mixed B/P kernel generators, not the rank.
    return contract(contract(value, 4 + i), 4 + j)


def action_matrix(t: Fraction, q: Fraction):
    beta = build_beta(t, q)
    labels: list[Label] = []
    columns: list[Exterior] = []

    for i, j in combinations(range(4), 2):
        labels.append(("B", i, j))
        columns.append(op_b(beta, i, j))
    for i in range(4):
        for j in range(4):
            labels.append(("M", i, j))
            columns.append(op_m(beta, i, j))
    for i, j in combinations(range(4), 2):
        labels.append(("P", i, j))
        columns.append(op_p(beta, i, j))

    basis = sorted(
        set().union(*(set(column) for column in columns)),
        key=lambda monomial: (len(monomial), monomial),
    )
    matrix = [
        [column.get(monomial, Fraction(0)) for column in columns]
        for monomial in basis
    ]
    return labels, basis, matrix


def rref(matrix: list[list[Fraction]]) -> tuple[list[list[Fraction]], list[int]]:
    value = [row[:] for row in matrix]
    row_count = len(value)
    column_count = len(value[0]) if value else 0
    pivots: list[int] = []
    pivot_row = 0

    for column in range(column_count):
        chosen = next(
            (row for row in range(pivot_row, row_count) if value[row][column]),
            None,
        )
        if chosen is None:
            continue

        value[pivot_row], value[chosen] = value[chosen], value[pivot_row]
        pivot = value[pivot_row][column]
        value[pivot_row] = [entry / pivot for entry in value[pivot_row]]

        for row in range(row_count):
            if row == pivot_row or not value[row][column]:
                continue
            factor = value[row][column]
            value[row] = [
                value[row][j] - factor * value[pivot_row][j]
                for j in range(column_count)
            ]

        pivots.append(column)
        pivot_row += 1
        if pivot_row == row_count:
            break

    return value, pivots


def matrix_rank(matrix: list[list[Fraction]]) -> int:
    return len(rref(matrix)[1])


def mat_vec(matrix: list[list[Fraction]], vector: list[Fraction]) -> list[Fraction]:
    return [sum((a * b for a, b in zip(row, vector)), Fraction(0)) for row in matrix]


def explicit_kernel_vectors(labels: list[Label], q: Fraction) -> list[list[Fraction]]:
    index = {label: i for i, label in enumerate(labels)}
    vectors: list[list[Fraction]] = []

    def vector(terms: dict[Label, Fraction | int]) -> list[Fraction]:
        result = [Fraction(0)] * len(labels)
        for label, coefficient in terms.items():
            result[index[label]] = Fraction(coefficient)
        return result

    vectors.extend(
        [
            vector({("M", 0, 0): 1}),
            vector({("M", 0, 1): 1, ("M", 1, 0): 1}),
            vector({("M", 1, 1): 1}),
            vector({("M", 2, 2): 1}),
            vector({("M", 2, 3): 1, ("M", 3, 2): 1}),
            vector({("M", 3, 3): 1}),
            vector({("B", 0, 1): -q, ("P", 0, 1): 1}),
            vector({("B", 2, 3): -q, ("P", 2, 3): 1}),
        ]
    )
    return vectors


SELECTED_ROWS: tuple[Monomial, ...] = (
    (0, 1),
    (0, 2),
    (0, 3),
    (1, 2),
    (1, 3),
    (2, 3),
    (0, 1, 2, 4),
    (0, 1, 2, 5),
    (0, 1, 2, 6),
    (0, 1, 3, 4),
    (0, 1, 3, 5),
    (0, 2, 3, 4),
    (0, 2, 3, 6),
    (0, 2, 3, 7),
    (1, 2, 3, 6),
    (1, 2, 3, 7),
    (0, 1, 2, 3, 4, 6),
    (0, 1, 2, 3, 4, 7),
    (0, 1, 2, 3, 5, 6),
    (0, 1, 2, 3, 5, 7),
)

SELECTED_COLUMNS: tuple[Label, ...] = (
    ("B", 0, 1),
    ("B", 0, 2),
    ("B", 0, 3),
    ("B", 1, 2),
    ("B", 1, 3),
    ("B", 2, 3),
    ("M", 0, 1),
    ("M", 0, 2),
    ("M", 0, 3),
    ("M", 1, 2),
    ("M", 1, 3),
    ("M", 2, 0),
    ("M", 2, 1),
    ("M", 2, 3),
    ("M", 3, 0),
    ("M", 3, 1),
    ("P", 0, 2),
    ("P", 0, 3),
    ("P", 1, 2),
    ("P", 1, 3),
)


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    if not matrix:
        return Fraction(1)
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("determinant requires a square matrix")

    value = [row[:] for row in matrix]
    result = Fraction(1)

    for column in range(n):
        chosen = next((row for row in range(column, n) if value[row][column]), None)
        if chosen is None:
            return Fraction(0)
        if chosen != column:
            value[column], value[chosen] = value[chosen], value[column]
            result = -result

        pivot = value[column][column]
        result *= pivot
        for row in range(column + 1, n):
            if not value[row][column]:
                continue
            factor = value[row][column] / pivot
            for j in range(column + 1, n):
                value[row][j] -= factor * value[column][j]
            value[row][column] = 0

    return result


def certificate_minor(
    labels: list[Label],
    basis: list[Monomial],
    matrix: list[list[Fraction]],
) -> Fraction:
    row_index = {row: i for i, row in enumerate(basis)}
    column_index = {label: i for i, label in enumerate(labels)}
    submatrix = [
        [matrix[row_index[row]][column_index[column]] for column in SELECTED_COLUMNS]
        for row in SELECTED_ROWS
    ]
    return determinant(submatrix)


def expected_minor(t: Fraction, q: Fraction) -> Fraction:
    return (
        q**8
        * (t - 1) ** 8
        * (t + 1) ** 8
        * (t * t + 1) ** 8
        / t**16
    )


def verify(t: Fraction, q: Fraction) -> bool:
    labels, basis, matrix = action_matrix(t, q)
    if len(labels) != 28 or len(basis) != 24:
        return False

    kernel = explicit_kernel_vectors(labels, q)
    if matrix_rank(kernel) != 8:
        return False
    if any(any(mat_vec(matrix, vector)) for vector in kernel):
        return False

    # For t != +/-1 (and over Q automatically t^2 + 1 != 0), this minor
    # gives rank >= 20. The eight kernel vectors give rank <= 20.
    minor = certificate_minor(labels, basis, matrix)
    if minor != expected_minor(t, q):
        return False
    expected_rank = 20 if t not in (1, -1) else 12
    return matrix_rank(matrix) == expected_rank


def parse_fraction(text: str) -> Fraction:
    return Fraction(text)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--t", type=parse_fraction, default=Fraction(2))
    parser.add_argument("--q", type=parse_fraction, default=Fraction(3))
    args = parser.parse_args()

    if args.t == 0 or args.q == 0:
        raise SystemExit("t and q must be nonzero")
    if not verify(args.t, args.q):
        raise SystemExit("verification failed")

    labels, basis, matrix = action_matrix(args.t, args.q)
    print(f"matrix: {len(basis)} x {len(labels)}")
    print(f"rank: {matrix_rank(matrix)}")
    print(f"kernel dimension: {len(labels) - matrix_rank(matrix)}")
    print(f"certificate minor: {certificate_minor(labels, basis, matrix)}")
    print("explicit kernel: 6 symmetric H^1(T) directions + 2 mixed B/P directions")
    print("verification: OK")


if __name__ == "__main__":
    main()
