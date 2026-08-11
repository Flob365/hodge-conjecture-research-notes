#!/usr/bin/env python3
"""Exact verifier for the positive RM cubic identity.

The two-dimensional cubic space is represented in the basis (u^2 v, u v^2).
All calculations use Fraction arithmetic.
"""

from __future__ import annotations

import argparse
from fractions import Fraction


Vec = tuple[Fraction, Fraction]


def add(a: Vec, b: Vec) -> Vec:
    return a[0] + b[0], a[1] + b[1]


def scale(a: Vec, c) -> Vec:
    c = Fraction(c)
    return c * a[0], c * a[1]


def cubic_vectors(rho: Fraction):
    if rho <= 0:
        raise ValueError("rho must be positive")

    # A = rho*u + rho^-1*v
    # C = rho^-1*u + rho*v
    # H = rho^-2*u + rho^2*v
    c3 = (Fraction(3, 1) / rho, Fraction(3, 1) * rho)
    ac2 = (
        2 * rho + rho ** -3,
        rho**3 + 2 / rho,
    )
    ah2 = (
        2 * rho + rho ** -5,
        rho**5 + 2 / rho,
    )
    return c3, ac2, ah2


def coefficients(rho: Fraction):
    T = rho**2 + rho**-2
    delta = 2 * T**2 - 2 * T - 1
    r = 3 * (T - 2) / delta
    s = 3 / delta
    return T, delta, r, s


def verify(rho: Fraction) -> bool:
    if rho <= 0 or rho == 1:
        return False
    c3, ac2, ah2 = cubic_vectors(rho)
    T, delta, r, s = coefficients(rho)

    if T <= 2 or delta <= 0 or r <= 0 or s <= 0:
        return False

    rhs = add(scale(ac2, r), scale(ah2, s))
    if rhs != c3:
        return False

    integral_form_rhs = add(
        scale(ac2, 3 * (T - 2)),
        scale(ah2, 3),
    )
    if integral_form_rhs != scale(c3, delta):
        return False

    # The older one-step identity contains a negative A^3 coefficient.
    a3 = (3 * rho, 3 / rho)
    old_rhs = scale(add(scale(ac2, 3), scale(a3, -1)), 1 / T)
    if old_rhs != c3:
        return False

    return True


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rho", default="2", help="positive rational RM eigenvalue > 1")
    args = parser.parse_args()
    rho = Fraction(args.rho)

    if not verify(rho):
        raise SystemExit(1)

    T, delta, r, s = coefficients(rho)
    print(f"rho={rho}")
    print(f"T=rho^2+rho^-2={T}")
    print(f"Delta=2T^2-2T-1={delta}")
    print(f"positive coefficient of A C^2: {r}")
    print(f"positive coefficient of A H^2: {s}")
    print("positive cubic identity: OK")


if __name__ == "__main__":
    main()
