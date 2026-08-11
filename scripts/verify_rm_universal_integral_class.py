#!/usr/bin/env python3
"""Exact truncated Chern-character checks for the universal RM K-class."""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import factorial


Poly = tuple[Fraction, ...]


def poly(*coefficients) -> Poly:
    values = [Fraction(c) for c in coefficients]
    values += [Fraction(0)] * (5 - len(values))
    return tuple(values[:5])


def add(a: Poly, b: Poly) -> Poly:
    return tuple(a[i] + b[i] for i in range(5))


def scale(a: Poly, c) -> Poly:
    c = Fraction(c)
    return tuple(c * a[i] for i in range(5))


def mul(a: Poly, b: Poly) -> Poly:
    out = [Fraction(0)] * 5
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            if i + j <= 4:
                out[i + j] += ai * bj
    return tuple(out)


def power(a: Poly, n: int) -> Poly:
    out = poly(1)
    for _ in range(n):
        out = mul(out, a)
    return out


def exp(k) -> Poly:
    k = Fraction(k)
    return tuple(k**i / factorial(i) for i in range(5))


def complete_intersection_twist(k) -> Poly:
    one_minus_exp_minus = add(poly(1), scale(exp(-1), -1))
    return mul(exp(k), power(one_minus_exp_minus, 3))


def verify_one_variable_identities() -> bool:
    b1 = complete_intersection_twist(1)
    b2 = complete_intersection_twist(2)
    if b1 != poly(0, 0, 0, 1, Fraction(-1, 2)):
        return False
    if b2 != poly(0, 0, 0, 1, Fraction(1, 2)):
        return False
    if add(b1, b2) != poly(0, 0, 0, 2, 0):
        return False

    odd_exp = add(exp(1), scale(exp(-1), -1))
    if scale(odd_exp, 6) != poly(0, 12, 0, 2, 0):
        return False
    return True


def rm_moments(q: int | Fraction):
    """Return coefficients in the independent x/y monomials used by the RM identity.

    We only need the four nonzero slots x, x^3, y^3, and degree-4 point
    corrections. x and y are treated as independent divisor classes because the
    K-class is a sum of pure x-blocks and pure y-blocks, with no mixed products.
    """
    q = Fraction(q)

    x_line_block = scale(add(exp(1), scale(exp(-1), -1)), 6)
    x_ci_pair = add(complete_intersection_twist(1), complete_intersection_twist(2))
    y_ci_pair = x_ci_pair

    x_total = add(x_line_block, scale(x_ci_pair, -1))
    y_total = scale(y_ci_pair, -q)

    return x_total, y_total


def verify(q: int | Fraction) -> bool:
    q = Fraction(q)
    if q <= 0:
        return False
    if not verify_one_variable_identities():
        return False

    x_total, y_total = rm_moments(q)
    if x_total != poly(0, 12, 0, 0, 0):
        return False
    if y_total != poly(0, 0, 0, -2 * q, 0):
        return False

    # Determinantal 3x3 precursor: 3(e^x-e^-x)=6x+x^3.
    determinantal = scale(add(exp(1), scale(exp(-1), -1)), 3)
    if determinantal != poly(0, 6, 0, 1, 0):
        return False

    # Subtracting a curve class x^3 + q y^3 yields 6 beta'.
    x_after = add(determinantal, poly(0, 0, 0, -1, 0))
    y_after = poly(0, 0, 0, -q, 0)
    if x_after != poly(0, 6, 0, 0, 0):
        return False
    if y_after != poly(0, 0, 0, -q, 0):
        return False

    return True


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--q", default="3", help="positive rational/integer q")
    args = parser.parse_args()
    q = Fraction(args.q)

    if not verify(q):
        raise SystemExit(1)

    b1 = complete_intersection_twist(1)
    b2 = complete_intersection_twist(2)
    x_total, y_total = rm_moments(q)

    print(f"q={q}")
    print("B3 twist 1:", b1)
    print("B3 twist 2:", b2)
    print("B3 symmetric sum:", add(b1, b2))
    print("x-block after cancellation:", x_total)
    print("y-block:", y_total)
    print("universal integral RM identity: OK")
    print("determinantal scale-6 precursor: OK")


if __name__ == "__main__":
    main()
