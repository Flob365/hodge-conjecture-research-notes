#!/usr/bin/env python3
"""Exact checks for the nested RM elementary-transform construction.

The script verifies the intersection identities and the numerical containment
criterion used in notes/rm-nested-elementary-transform.md.
"""

from __future__ import annotations

import argparse
from fractions import Fraction


def intersection(a1: Fraction, a2: Fraction,
                 b1: Fraction, b2: Fraction,
                 c1: Fraction, c2: Fraction,
                 d1: Fraction, d2: Fraction) -> Fraction:
    """Integrate four divisor classes ai*theta1+ai2*theta2.

    Only theta1^2 theta2^2 survives and its integral is 4.
    """
    vectors = [(a1, a2), (b1, b2), (c1, c2), (d1, d2)]
    total = Fraction(0)
    # choose which two factors contribute theta1; remaining two theta2
    for i in range(4):
        for j in range(i + 1, 4):
            term = Fraction(1)
            for k, (u, v) in enumerate(vectors):
                term *= u if k in (i, j) else v
            total += term
    return 4 * total


def check_intersections(rho: Fraction) -> tuple[Fraction, Fraction, Fraction]:
    if rho <= 0 or rho == 1:
        raise ValueError("rho must be positive and different from 1")
    A = (rho, 1 / rho)
    C = (1 / rho, rho)
    A4 = intersection(*A, *A, *A, *A)
    C4 = intersection(*C, *C, *C, *C)
    AC3 = intersection(*A, *C, *C, *C)
    s = rho * rho + 1 / (rho * rho)
    assert A4 == 24
    assert C4 == 24
    assert AC3 == 12 * s
    return A4, C4, AC3


def containment_margin(rho: Fraction, q: int, M: int) -> Fraction:
    """Coefficient of m^8 in the lower bound for h0(I_U(M A~))."""
    if q <= 0 or M <= 0:
        raise ValueError("q and M must be positive")
    s = rho * rho + 1 / (rho * rho)
    return Fraction(M**4) - q * M * (12 * M * s - 36)


def sufficient_conditions(rho: Fraction, q: int, M: int) -> bool:
    s = rho * rho + 1 / (rho * rho)
    return M * s > 6 and M * M > 12 * q * s and containment_margin(rho, q, M) > 0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rho-num", type=int, default=2)
    parser.add_argument("--rho-den", type=int, default=1)
    parser.add_argument("--q", type=int, default=1)
    parser.add_argument("--M", type=int, default=10)
    args = parser.parse_args()

    rho = Fraction(args.rho_num, args.rho_den)
    A4, C4, AC3 = check_intersections(rho)
    s = rho * rho + 1 / (rho * rho)

    print("intersection identities: OK")
    print("A^4 =", A4)
    print("C^4 =", C4)
    print("A*C^3 =", AC3)
    print("s = rho^2 + rho^-2 =", s)
    print("containment margin / m^8 =", containment_margin(rho, args.q, args.M))
    print("sufficient conditions:", sufficient_conditions(rho, args.q, args.M))


if __name__ == "__main__":
    main()
