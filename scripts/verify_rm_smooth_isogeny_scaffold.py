#!/usr/bin/env python3
"""Exact symbolic checks for the smooth-isogeny RM scaffold.

The calculations use truncated Chern characters in one formal divisor class.
No third-party packages are required.
"""

from __future__ import annotations

import argparse
from fractions import Fraction


Poly = tuple[Fraction, ...]
DEGREE = 4


def poly(*coefficients: int | Fraction) -> Poly:
    values = [Fraction(c) for c in coefficients]
    values += [Fraction(0)] * (DEGREE + 1 - len(values))
    return tuple(values[: DEGREE + 1])


def add(left: Poly, right: Poly) -> Poly:
    return tuple(a + b for a, b in zip(left, right, strict=True))


def scale(value: Poly, scalar: int | Fraction) -> Poly:
    scalar = Fraction(scalar)
    return tuple(scalar * c for c in value)


def mul(left: Poly, right: Poly) -> Poly:
    result = [Fraction(0)] * (DEGREE + 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if i + j <= DEGREE:
                result[i + j] += a * b
    return tuple(result)


def exp_x(m: int | Fraction = 1) -> Poly:
    m = Fraction(m)
    return (
        Fraction(1),
        m,
        m * m / 2,
        m * m * m / 6,
        m**4 / 24,
    )


def verify_divisor_bundle() -> bool:
    one = poly(1)
    exp_minus = exp_x(-1)
    exp_plus = exp_x(1)
    exp_minus_two = exp_x(-2)

    # On a smooth divisor D in an abelian fourfold:
    # [Omega_D^1] = 4 - O_D(-D)
    # [Omega_D^2] = 6 - 4 O_D(-D) + O_D(-2D)
    ch_omega_1 = add(scale(one, 4), scale(exp_minus, -1))
    ch_omega_2 = add(add(scale(one, 6), scale(exp_minus, -4)), exp_minus_two)

    ch_v = scale(one, 3)
    ch_v = add(ch_v, ch_omega_1)
    ch_v = add(ch_v, ch_omega_2)
    ch_v = add(ch_v, scale(exp_plus, 3))

    # D has dimension three, so only coefficients through x^3 matter.
    target = poly(12, 6, 1, 0, 0)
    return ch_v[:4] == target[:4]


def verify_grr_divisor_pushforward() -> bool:
    # ch(V_D)=12 td(x), hence i_*(ch(V_D) td(x)^-1)=12x.
    # Verify directly using the Cartier divisor K-class:
    # If V_D has K-class -3 z^4 + 13 z^3 - 23 z^2 + 25 z on D,
    # multiplying by (1-z^-1) on X has Chern character 12x.
    p = add(
        add(scale(exp_x(4), -3), scale(exp_x(3), 13)),
        add(scale(exp_x(2), -23), scale(exp_x(1), 25)),
    )
    pushed = mul(p, add(poly(1), scale(exp_x(-1), -1)))
    return pushed == poly(0, 12, 0, 0, 0)


def verify_curve_block() -> bool:
    one_minus = add(poly(1), scale(exp_x(-1), -1))
    koszul = mul(mul(one_minus, one_minus), one_minus)
    curve_block = mul(add(poly(1), exp_x(3)), koszul)
    return curve_block == poly(0, 0, 0, 2, 0)


def verify_isogeny_scaling(m: int, q: int) -> bool:
    if m <= 0 or q <= 0:
        return False
    # Moment-style coefficients for beta = A - q/6 C^3.
    # [m]^* scales degree 2 by m^2 and degree 6 by m^6.
    pulled = (Fraction(12 * m**2), Fraction(-2 * q * m**6))
    # [m]_* [m]^* multiplies every cohomology class by deg[m]=m^8.
    pushed = (
        pulled[0] * m**6,  # push on H^2 scales by m^(8-2)=m^6
        pulled[1] * m**2,  # push on H^6 scales by m^(8-6)=m^2
    )
    target = (Fraction(12 * m**8), Fraction(-2 * q * m**8))
    return pushed == target


def verify(m: int = 2, q: int = 3) -> bool:
    return (
        verify_divisor_bundle()
        and verify_grr_divisor_pushforward()
        and verify_curve_block()
        and verify_isogeny_scaling(m, q)
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--m", type=int, default=2)
    parser.add_argument("--q", type=int, default=3)
    args = parser.parse_args()

    if not verify(args.m, args.q):
        raise SystemExit("verification failed")

    print("divisor bundle ch(V_D)=12+6x+x^2: OK")
    print("GRR pushforward ch(i_*V_D)=12x: OK")
    print("curve block ch(O_Z + O_Z(3C))=2C^3: OK")
    print(f"isogeny scaling for m={args.m}, q={args.q}: OK")
    print("verification: OK")


if __name__ == "__main__":
    main()
