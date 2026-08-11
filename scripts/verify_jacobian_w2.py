#!/usr/bin/env python3
"""Verify the genus-4 Jacobian W_2 construction symbolically.

For n=d+1 copies of W_2(C), the construction glues two points per unordered
pair. The resulting sheaf G has

    ch(G) = n ch(O_W) - n(n-1) [pt],

with

    ch(O_W) = x^2/2 - x^3/3 + x^4/8,
    [pt] = x^4/24.

The two-term perfect complex E = [O_X -> G] tensor O_X(Theta) should have

    ch(E) = 1 + x - d x^2/2 - d x^3/6 + d^2 x^4/24.
"""

from __future__ import annotations

import argparse
from fractions import Fraction


def mul(a: tuple[Fraction, ...], b: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    out = [Fraction(0)] * 5
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            if i + j <= 4:
                out[i + j] += ai * bj
    return tuple(out)


def add(a: tuple[Fraction, ...], b: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    return tuple(x + y for x, y in zip(a, b, strict=True))


def scale(a: tuple[Fraction, ...], c: Fraction | int) -> tuple[Fraction, ...]:
    c = Fraction(c)
    return tuple(c * x for x in a)


EXP_X = (
    Fraction(1),
    Fraction(1),
    Fraction(1, 2),
    Fraction(1, 6),
    Fraction(1, 24),
)
CH_W = (
    Fraction(0),
    Fraction(0),
    Fraction(1, 2),
    Fraction(-1, 3),
    Fraction(1, 8),
)
PT = (Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(1, 24))
ONE = (Fraction(1), Fraction(0), Fraction(0), Fraction(0), Fraction(0))


def character(d: int) -> tuple[Fraction, ...]:
    if d <= 0 or d % 2 == 0:
        raise ValueError("d must be a positive odd integer")
    n = d + 1
    ch_g = add(scale(CH_W, n), scale(PT, -n * (n - 1)))
    return mul(add(ONE, scale(ch_g, -1)), EXP_X)


def target(d: int) -> tuple[Fraction, ...]:
    return (
        Fraction(1),
        Fraction(1),
        Fraction(-d, 2),
        Fraction(-d, 6),
        Fraction(d * d, 24),
    )


def verify(d: int) -> bool:
    return character(d) == target(d)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--d", type=int, default=3)
    args = parser.parse_args()

    if not verify(args.d):
        raise SystemExit(f"identity failed for d={args.d}")

    n = args.d + 1
    pair_intersection_points = 6
    selected_gluings = 2 * (n * (n - 1) // 2)
    unglued_points = 4 * (n * (n - 1) // 2)

    print(f"d={args.d}, n={n}")
    print("pairwise intersection number:", pair_intersection_points)
    print("selected gluing points:", selected_gluings)
    print("unglued points / length H^1:", unglued_points)
    print("computed:", character(args.d))
    print("target:  ", target(args.d))
    print("identity: OK")


if __name__ == "__main__":
    main()
