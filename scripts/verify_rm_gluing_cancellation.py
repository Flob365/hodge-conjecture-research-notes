#!/usr/bin/env python3
"""Verify the divisor/curve decomposition of the RM Chern-action kernel."""

from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import combinations

from verify_rm_semiregularity_kernel import (
    add,
    basis,
    contract_bivector,
    contract_one,
    matvec,
    power,
    rank,
    scale,
    wedge,
)


def theta_form(A: Fraction):
    theta_plus = add(basis(0, 4), basis(1, 5))
    theta_minus = add(basis(2, 6), basis(3, 7))
    return add(scale(theta_plus, A), scale(theta_minus, 1 / A))


def alpha_form(A: Fraction, d: Fraction):
    theta = theta_form(A)
    return add(theta, scale(power(theta, 3), -d / 6))


def gamma_form(A: Fraction, d: Fraction, q: Fraction):
    theta = theta_form(A)
    inverse_theta = theta_form(1 / A)
    return add(
        scale(power(theta, 3), d / 6),
        scale(power(inverse_theta, 3), -q / 6),
    )


def action_matrix(form):
    columns = []
    labels = []

    for i, j in combinations(range(4), 2):
        columns.append(wedge(basis(i + 4, j + 4), form))
        labels.append(f"B{i+1}{j+1}")

    for i in range(4):
        for j in range(4):
            columns.append(wedge(basis(j + 4), contract_one(form, i)))
            labels.append(f"D{i+1}{j+1}")

    for i, j in combinations(range(4), 2):
        columns.append(contract_bivector(form, i, j))
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


def stacked_rank(*matrices):
    return rank([row for matrix in matrices for row in matrix])


def action_form(form, labels, specification):
    positions = {label: i for i, label in enumerate(labels)}
    pieces = []
    for label, coefficient in specification.items():
        _ = positions[label]
        if label.startswith("B"):
            i, j = int(label[1]) - 1, int(label[2]) - 1
            pieces.append(scale(wedge(basis(i + 4, j + 4), form), coefficient))
        elif label.startswith("D"):
            i, j = int(label[1]) - 1, int(label[2]) - 1
            pieces.append(scale(wedge(basis(j + 4), contract_one(form, i)), coefficient))
        elif label.startswith("P"):
            i, j = int(label[1]) - 1, int(label[2]) - 1
            pieces.append(scale(contract_bivector(form, i, j), coefficient))
        else:
            raise ValueError(label)
    return add(*pieces)


def vector(labels, specification):
    positions = {label: i for i, label in enumerate(labels)}
    out = [Fraction(0)] * len(labels)
    for label, coefficient in specification.items():
        out[positions[label]] = Fraction(coefficient)
    return out


def six_common_vectors(labels):
    specs = [
        {"D11": 1},
        {"D22": 1},
        {"D12": 1, "D21": 1},
        {"D33": 1},
        {"D44": 1},
        {"D34": 1, "D43": 1},
    ]
    return [vector(labels, spec) for spec in specs]


def two_cancellation_vectors(labels, q):
    return [
        vector(labels, {"B12": 1, "P12": -1 / q}),
        vector(labels, {"B34": 1, "P34": -1 / q}),
    ]


def verify(A: Fraction, d: Fraction, q: Fraction) -> bool:
    if not A or not q:
        return False

    alpha = alpha_form(A, d)
    gamma = gamma_form(A, d, q)
    total = add(alpha, gamma)

    ma, labels, _ = action_matrix(alpha)
    mg, labels_g, _ = action_matrix(gamma)
    mt, labels_t, _ = action_matrix(total)
    if labels != labels_g or labels != labels_t:
        return False

    if rank(ma) != 12:
        return False

    generic = d != 4 * q and 4 * d != q
    if generic:
        if rank(mg) != 12:
            return False
        if stacked_rank(ma, mg) != 22:
            return False

    if A != 1 and rank(mt) != 20:
        return False

    for v in six_common_vectors(labels):
        if any(matvec(ma, v)) or any(matvec(mg, v)):
            return False

    cancellation_specs = [
        {"B12": 1, "P12": -1 / q},
        {"B34": 1, "P34": -1 / q},
    ]
    for spec in cancellation_specs:
        on_alpha = action_form(alpha, labels, spec)
        on_gamma = action_form(gamma, labels, spec)
        on_total = action_form(total, labels, spec)
        if on_total:
            return False
        if add(on_alpha, on_gamma):
            return False
        if generic and not on_alpha:
            return False

    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--A", default="2")
    parser.add_argument("--d", default="5")
    parser.add_argument("--q", default="3")
    args = parser.parse_args()

    A = Fraction(args.A)
    d = Fraction(args.d)
    q = Fraction(args.q)

    alpha = alpha_form(A, d)
    gamma = gamma_form(A, d, q)
    total = add(alpha, gamma)
    ma, labels, _ = action_matrix(alpha)
    mg, _, _ = action_matrix(gamma)
    mt, _, _ = action_matrix(total)

    print(f"A={A}, d={d}, q={q}")
    print("rank alpha:", rank(ma))
    print("rank gamma:", rank(mg))
    print("rank stacked:", stacked_rank(ma, mg))
    print("rank total:", rank(mt))

    common_ok = all(
        not any(matvec(ma, v)) and not any(matvec(mg, v))
        for v in six_common_vectors(labels)
    )
    cancel_ok = all(
        not any(matvec(mt, v))
        for v in two_cancellation_vectors(labels, q)
    )
    print("six common kernel vectors:", "OK" if common_ok else "FAILED")
    print("two total cancellation vectors:", "OK" if cancel_ok else "FAILED")

    if not verify(A, d, q):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
