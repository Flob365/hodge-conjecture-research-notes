#!/usr/bin/env python3
"""Exact verifier for the RM semiregularity Chern-action kernel.

The model is a genus-4 abelian variety with
    beta = A*Theta_+ + A^{-1}*Theta_-
           - q/2*(A^{-1} Theta_+^2 Theta_- + A Theta_+ Theta_-^2).

It builds the HKR action
HT^2 = H^2(O) + H^1(T) + H^0(wedge^2 T)
on beta in an exterior algebra on 8 generators, using exact Fraction
arithmetic. It verifies generic rank 20, the eight displayed kernel vectors,
a fixed 20x20 determinant certificate, and the rank drop at A=1.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import combinations


Form = dict[tuple[int, ...], Fraction]


def wedge_monom(left: tuple[int, ...], right: tuple[int, ...]):
    if set(left) & set(right):
        return None, 0
    inversions = sum(x > y for x in left for y in right)
    return tuple(sorted(left + right)), -1 if inversions % 2 else 1


def add(*forms: Form) -> Form:
    out: Form = {}
    for form in forms:
        for monomial, coefficient in form.items():
            out[monomial] = out.get(monomial, Fraction(0)) + coefficient
            if out[monomial] == 0:
                del out[monomial]
    return out


def scale(form: Form, scalar: Fraction | int) -> Form:
    scalar = Fraction(scalar)
    return {m: scalar * c for m, c in form.items() if scalar * c}


def basis(*indices: int) -> Form:
    indices = tuple(indices)
    if tuple(sorted(indices)) != indices or len(set(indices)) != len(indices):
        raise ValueError("basis indices must be strictly increasing")
    return {indices: Fraction(1)}


def wedge(left: Form, right: Form) -> Form:
    out: Form = {}
    for a, ca in left.items():
        for b, cb in right.items():
            monomial, sign = wedge_monom(a, b)
            if monomial is None:
                continue
            out[monomial] = out.get(monomial, Fraction(0)) + sign * ca * cb
    return {m: c for m, c in out.items() if c}


def power(form: Form, exponent: int) -> Form:
    out: Form = {(): Fraction(1)}
    for _ in range(exponent):
        out = wedge(out, form)
    return out


def contract_one(form: Form, holomorphic_index: int) -> Form:
    out: Form = {}
    for monomial, coefficient in form.items():
        if holomorphic_index not in monomial:
            continue
        position = monomial.index(holomorphic_index)
        reduced = monomial[:position] + monomial[position + 1 :]
        sign = -1 if position % 2 else 1
        out[reduced] = out.get(reduced, Fraction(0)) + sign * coefficient
    return {m: c for m, c in out.items() if c}


def contract_bivector(form: Form, i: int, j: int) -> Form:
    return contract_one(contract_one(form, i), j)


def beta_form(A: Fraction, q: Fraction) -> Form:
    if A == 0:
        raise ValueError("A must be nonzero")
    theta_plus = add(basis(0, 4), basis(1, 5))
    theta_minus = add(basis(2, 6), basis(3, 7))
    beta_1 = add(scale(theta_plus, A), scale(theta_minus, 1 / A))
    inverse_theta = add(scale(theta_plus, 1 / A), scale(theta_minus, A))
    beta_3 = scale(power(inverse_theta, 3), -q / 6)
    return add(beta_1, beta_3)


def build_matrix(A: Fraction, q: Fraction):
    beta = beta_form(A, q)
    columns: list[Form] = []
    labels: list[str] = []

    for i, j in combinations(range(4), 2):
        columns.append(wedge(basis(i + 4, j + 4), beta))
        labels.append(f"B{i+1}{j+1}")

    for i in range(4):
        for j in range(4):
            columns.append(wedge(basis(j + 4), contract_one(beta, i)))
            labels.append(f"D{i+1}{j+1}")

    for i, j in combinations(range(4), 2):
        columns.append(contract_bivector(beta, i, j))
        labels.append(f"P{i+1}{j+1}")

    output_basis = sorted(
        set().union(*(set(column) for column in columns)),
        key=lambda monomial: (len(monomial), monomial),
    )
    matrix = [
        [column.get(monomial, Fraction(0)) for column in columns]
        for monomial in output_basis
    ]
    return matrix, labels, output_basis


def rank(matrix: list[list[Fraction]]) -> int:
    work = [row[:] for row in matrix]
    if not work:
        return 0
    rows = len(work)
    cols = len(work[0])
    pivot_row = 0
    for column in range(cols):
        pivot = next(
            (r for r in range(pivot_row, rows) if work[r][column] != 0),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        pivot_value = work[pivot_row][column]
        work[pivot_row] = [x / pivot_value for x in work[pivot_row]]
        for r in range(rows):
            if r == pivot_row or work[r][column] == 0:
                continue
            factor = work[r][column]
            work[r] = [
                work[r][c] - factor * work[pivot_row][c] for c in range(cols)
            ]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("determinant requires a square matrix")
    work = [row[:] for row in matrix]
    det = Fraction(1)
    for column in range(n):
        pivot = next((r for r in range(column, n) if work[r][column]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            det = -det
        pivot_value = work[column][column]
        det *= pivot_value
        for r in range(column + 1, n):
            if not work[r][column]:
                continue
            factor = work[r][column] / pivot_value
            for c in range(column + 1, n):
                work[r][c] -= factor * work[column][c]
    return det


MINOR_ROWS = (
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
    10, 12, 13, 14, 16, 17, 19, 20, 21, 22,
)
MINOR_COLS = (
    0, 1, 2, 3, 4, 5, 7, 8, 9, 12,
    13, 14, 15, 17, 18, 19, 23, 24, 25, 26,
)


def certificate_minor(matrix: list[list[Fraction]]) -> Fraction:
    return determinant([[matrix[r][c] for c in MINOR_COLS] for r in MINOR_ROWS])


def expected_minor(A: Fraction, q: Fraction) -> Fraction:
    return -(q**8) * (A - 1) ** 8 * (A + 1) ** 8 * (A * A + 1) ** 8 / (A**16)


def matvec(matrix: list[list[Fraction]], vector: list[Fraction]):
    return [sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix]


def claimed_kernel_vectors(labels: list[str], q: Fraction):
    if q == 0:
        raise ValueError("q must be nonzero")
    position = {label: i for i, label in enumerate(labels)}
    specifications = [
        {"D11": 1},
        {"D22": 1},
        {"D12": 1, "D21": 1},
        {"D33": 1},
        {"D44": 1},
        {"D34": 1, "D43": 1},
        {"B12": 1, "P12": -1 / q},
        {"B34": 1, "P34": -1 / q},
    ]
    vectors = []
    for specification in specifications:
        vector = [Fraction(0)] * len(labels)
        for label, coefficient in specification.items():
            vector[position[label]] = Fraction(coefficient)
        vectors.append(vector)
    return vectors


def verify(A: Fraction, q: Fraction) -> bool:
    matrix, labels, _ = build_matrix(A, q)
    if q == 0 or A == 0:
        return False
    if A != 1 and rank(matrix) != 20:
        return False
    if A != 1 and certificate_minor(matrix) != expected_minor(A, q):
        return False
    if A != 1:
        for vector in claimed_kernel_vectors(labels, q):
            if any(matvec(matrix, vector)):
                return False
    return True


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--A", default="2", help="positive rational RM eigenvalue square")
    parser.add_argument("--q", default="3", help="nonzero rational q")
    args = parser.parse_args()

    A = Fraction(args.A)
    q = Fraction(args.q)
    matrix, labels, _ = build_matrix(A, q)

    print(f"A={A}, q={q}")
    print(f"matrix shape: {len(matrix)} x {len(labels)}")
    print(f"rank: {rank(matrix)}")

    if A != 1 and q != 0:
        actual = certificate_minor(matrix)
        expected = expected_minor(A, q)
        print(f"20x20 certificate minor: {actual}")
        print(f"closed-form expected:    {expected}")
        print("minor formula:", "OK" if actual == expected else "FAILED")
        kernel_ok = all(
            not any(matvec(matrix, vector))
            for vector in claimed_kernel_vectors(labels, q)
        )
        print("eight kernel vectors:", "OK" if kernel_ok else "FAILED")
        if rank(matrix) != 20 or actual != expected or not kernel_ok:
            raise SystemExit(1)

    if A == 1:
        print("excluded scalar case; expected rank 12")
        if rank(matrix) != 12:
            raise SystemExit(1)


if __name__ == "__main__":
    main()
