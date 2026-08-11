#!/usr/bin/env python3
"""Verify the universal HT^2 annihilator of Markman's RM secant four-plane.

Exact rational arithmetic; standard library only.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction
from itertools import combinations


Monomial = tuple[int, ...]
Exterior = dict[Monomial, Fraction]
Label = tuple[str, int, int]


def add(left: Exterior, right: Exterior) -> Exterior:
    out = defaultdict(Fraction)
    for m, c in left.items():
        out[m] += c
    for m, c in right.items():
        out[m] += c
    return {m: c for m, c in out.items() if c}


def scale(value: Exterior, scalar: int | Fraction) -> Exterior:
    scalar = Fraction(scalar)
    return {m: c * scalar for m, c in value.items() if c * scalar}


def gen(index: int) -> Exterior:
    return {(index,): Fraction(1)}


def wedge_monomials(left: Monomial, right: Monomial):
    if set(left) & set(right):
        return None, 0
    inversions = sum(1 for i in left for j in right if i > j)
    return tuple(sorted(left + right)), -1 if inversions % 2 else 1


def wedge(left: Exterior, right: Exterior) -> Exterior:
    out = defaultdict(Fraction)
    for ml, cl in left.items():
        for mr, cr in right.items():
            monomial, sign = wedge_monomials(ml, mr)
            if monomial is not None:
                out[monomial] += cl * cr * sign
    return {m: c for m, c in out.items() if c}


def contract(value: Exterior, index: int) -> Exterior:
    out = defaultdict(Fraction)
    for monomial, coefficient in value.items():
        if index not in monomial:
            continue
        position = monomial.index(index)
        reduced = monomial[:position] + monomial[position + 1 :]
        out[reduced] += coefficient * (-1 if position % 2 else 1)
    return {m: c for m, c in out.items() if c}


def power(value: Exterior, exponent: int) -> Exterior:
    result: Exterior = {(): Fraction(1)}
    for _ in range(exponent):
        result = wedge(result, value)
    return result


def theta(indices: tuple[int, ...]) -> Exterior:
    result: Exterior = {}
    for i in indices:
        result = add(result, wedge(gen(i), gen(4 + i)))
    return result


def op_b(value: Exterior, i: int, j: int) -> Exterior:
    return wedge(wedge(gen(i), gen(j)), value)


def op_m(value: Exterior, i: int, j: int) -> Exterior:
    return wedge(gen(i), contract(value, 4 + j))


def op_p(value: Exterior, i: int, j: int) -> Exterior:
    return contract(contract(value, 4 + i), 4 + j)


def basis_classes(q: Fraction):
    theta_1 = theta((0, 1))
    theta_2 = theta((2, 3))
    total = add(theta_1, theta_2)
    tilde = add(theta_1, scale(theta_2, -1))

    def even(x: Exterior) -> Exterior:
        return add(
            {(): Fraction(1)},
            add(scale(power(x, 2), -q / 2), scale(power(x, 4), q * q / 24)),
        )

    def odd(x: Exterior) -> Exterior:
        return add(x, scale(power(x, 3), -q / 6))

    return even(total), odd(total), even(tilde), odd(tilde)


def action(value: Exterior):
    labels: list[Label] = []
    columns: list[Exterior] = []
    for i, j in combinations(range(4), 2):
        labels.append(("B", i, j))
        columns.append(op_b(value, i, j))
    for i in range(4):
        for j in range(4):
            labels.append(("M", i, j))
            columns.append(op_m(value, i, j))
    for i, j in combinations(range(4), 2):
        labels.append(("P", i, j))
        columns.append(op_p(value, i, j))
    basis = sorted(set().union(*(set(c) for c in columns)), key=lambda m: (len(m), m))
    matrix = [[column.get(m, Fraction(0)) for column in columns] for m in basis]
    return labels, basis, matrix


def rref(matrix):
    value = [row[:] for row in matrix]
    rows = len(value)
    cols = len(value[0]) if value else 0
    pivots = []
    pivot_row = 0
    for col in range(cols):
        chosen = next((r for r in range(pivot_row, rows) if value[r][col]), None)
        if chosen is None:
            continue
        value[pivot_row], value[chosen] = value[chosen], value[pivot_row]
        pivot = value[pivot_row][col]
        value[pivot_row] = [x / pivot for x in value[pivot_row]]
        for r in range(rows):
            if r == pivot_row or not value[r][col]:
                continue
            factor = value[r][col]
            value[r] = [value[r][j] - factor * value[pivot_row][j] for j in range(cols)]
        pivots.append(col)
        pivot_row += 1
        if pivot_row == rows:
            break
    return value, pivots


def rank(matrix) -> int:
    return len(rref(matrix)[1])


def mat_vec(matrix, vector):
    return [sum((a * b for a, b in zip(row, vector)), Fraction(0)) for row in matrix]


def universal_vectors(labels: list[Label], q: Fraction):
    index = {label: i for i, label in enumerate(labels)}

    def make(terms):
        vector = [Fraction(0)] * len(labels)
        for label, coefficient in terms.items():
            vector[index[label]] = Fraction(coefficient)
        return vector

    return [
        make({("M", 0, 0): 1}),
        make({("M", 0, 1): 1, ("M", 1, 0): 1}),
        make({("M", 1, 1): 1}),
        make({("M", 2, 2): 1}),
        make({("M", 2, 3): 1, ("M", 3, 2): 1}),
        make({("M", 3, 3): 1}),
        make({("B", 0, 1): -q, ("P", 0, 1): 1}),
        make({("B", 2, 3): -q, ("P", 2, 3): 1}),
    ]


def determinant(matrix):
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("square matrix required")
    value = [row[:] for row in matrix]
    result = Fraction(1)
    for col in range(n):
        chosen = next((r for r in range(col, n) if value[r][col]), None)
        if chosen is None:
            return Fraction(0)
        if chosen != col:
            value[col], value[chosen] = value[chosen], value[col]
            result = -result
        pivot = value[col][col]
        result *= pivot
        for r in range(col + 1, n):
            if not value[r][col]:
                continue
            factor = value[r][col] / pivot
            for j in range(col + 1, n):
                value[r][j] -= factor * value[col][j]
            value[r][col] = 0
    return result


def verify(q: Fraction) -> bool:
    if q == 0:
        return False
    classes = basis_classes(q)
    stacked = []
    matrices = []
    labels = None
    for value in classes:
        current_labels, _, matrix = action(value)
        labels = current_labels if labels is None else labels
        matrices.append(matrix)
        stacked.extend(matrix)

    assert labels is not None
    vectors = universal_vectors(labels, q)
    if rank(vectors) != 8:
        return False
    for matrix in matrices:
        for vector in vectors:
            if any(mat_vec(matrix, vector)):
                return False

    if rank(stacked) != 20:
        return False

    # A generic rational combination has the same 8-dimensional kernel.
    generic = {}
    for coefficient, value in zip((1, 2, 3, 4), classes):
        generic = add(generic, scale(value, coefficient))
    _, _, generic_matrix = action(generic)
    if rank(generic_matrix) != 20:
        return False

    # The positive-rank symmetric choice alpha + tilde(alpha) is special:
    # rank 18, hence kernel dimension 10.
    positive_rank = add(classes[0], classes[2])
    _, _, positive_matrix = action(positive_rank)
    if rank(positive_matrix) != 18:
        return False

    return True


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--q", type=Fraction, default=Fraction(3))
    args = parser.parse_args()
    if not verify(args.q):
        raise SystemExit("verification failed")
    print("common annihilator dimension: 8")
    print("generic B-class action rank: 20")
    print("rank-2 class alpha + tilde(alpha): action rank 18, kernel 10")
    print("universal mixed directions: P01-q B01 and P23-q B23")
    print("verification: OK")


if __name__ == "__main__":
    main()
