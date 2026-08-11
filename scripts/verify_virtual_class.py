#!/usr/bin/env python3
"""Verify the corrected virtual Chern character on a fourfold.

The calculation is exact and uses only Python's standard library. Coefficients
are polynomials in d with rational coefficients; x-polynomials are truncated at
degree four.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from typing import Iterable


PolyD = tuple[Fraction, ...]
PolyX = tuple[PolyD, ...]


def pd(*coefficients: int | Fraction) -> PolyD:
    """Create a polynomial in d from ascending coefficients."""
    values = [Fraction(value) for value in coefficients]
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values)


def pd_add(left: PolyD, right: PolyD) -> PolyD:
    size = max(len(left), len(right))
    return pd(*[
        (left[i] if i < len(left) else 0)
        + (right[i] if i < len(right) else 0)
        for i in range(size)
    ])


def pd_neg(value: PolyD) -> PolyD:
    return pd(*[-coefficient for coefficient in value])


def pd_mul(left: PolyD, right: PolyD) -> PolyD:
    result = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return pd(*result)


def pd_scale(value: PolyD, scalar: int | Fraction) -> PolyD:
    scalar = Fraction(scalar)
    return pd(*[coefficient * scalar for coefficient in value])


def px_add(left: PolyX, right: PolyX) -> PolyX:
    return tuple(pd_add(a, b) for a, b in zip(left, right, strict=True))


def px_scale(value: PolyX, scalar: PolyD) -> PolyX:
    return tuple(pd_mul(coefficient, scalar) for coefficient in value)


def px_neg(value: PolyX) -> PolyX:
    return tuple(pd_neg(coefficient) for coefficient in value)


ONE = pd(1)
D = pd(0, 1)

EXP_X: PolyX = tuple(pd(value) for value in (
    Fraction(1), Fraction(1), Fraction(1, 2), Fraction(1, 6), Fraction(1, 24)
))
B2: PolyX = tuple(pd(value) for value in (0, 0, 1, 0, Fraction(1, 12)))
B3: PolyX = tuple(pd(value) for value in (0, 0, 0, 1, Fraction(-1, 2)))
B4: PolyX = tuple(pd(value) for value in (0, 0, 0, 0, 1))


def virtual_character() -> tuple[PolyX, PolyX]:
    """Return computed and target characters, symbolically in d."""
    d_plus_one = pd_add(D, ONE)
    e = pd_scale(d_plus_one, Fraction(1, 2))
    b = pd_scale(d_plus_one, Fraction(1, 6))
    q = pd_scale(pd_mul(pd_add(D, pd(-2)), d_plus_one), Fraction(1, 24))

    computed = EXP_X
    computed = px_add(computed, px_neg(px_scale(B2, e)))
    computed = px_add(computed, px_neg(px_scale(B3, b)))
    computed = px_add(computed, px_scale(B4, q))

    target: PolyX = (
        ONE,
        ONE,
        pd_scale(D, Fraction(-1, 2)),
        pd_scale(D, Fraction(-1, 6)),
        pd_scale(pd_mul(D, D), Fraction(1, 24)),
    )
    return computed, target


def evaluate(poly: PolyD, d_value: int) -> Fraction:
    total = Fraction(0)
    power = Fraction(1)
    for coefficient in poly:
        total += coefficient * power
        power *= d_value
    return total


def evaluate_character(character: PolyX, d_value: int) -> tuple[Fraction, ...]:
    return tuple(evaluate(coefficient, d_value) for coefficient in character)


def verify(d_value: int | None = None) -> bool:
    computed, target = virtual_character()
    if computed != target:
        return False
    if d_value is None:
        return True
    return evaluate_character(computed, d_value) == evaluate_character(target, d_value)


def format_character(character: Iterable[PolyD], d_value: int) -> str:
    coefficients = [evaluate(poly, d_value) for poly in character]
    return "[" + ", ".join(str(value) for value in coefficients) + "]"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--d", type=int, help="Optional odd positive test value")
    args = parser.parse_args()

    computed, target = virtual_character()
    if computed != target:
        raise SystemExit("Symbolic identity failed")

    print("symbolic identity: OK")

    if args.d is not None:
        if args.d <= 0 or args.d % 2 == 0:
            raise SystemExit("d must be a positive odd integer")
        if not verify(args.d):
            raise SystemExit(f"Identity failed for d={args.d}")
        print("coefficients [1, x, x^2, x^3, x^4]:")
        print("computed:", format_character(computed, args.d))
        print("target:  ", format_character(target, args.d))
        print(f"numeric check for d={args.d}: OK")


if __name__ == "__main__":
    main()
