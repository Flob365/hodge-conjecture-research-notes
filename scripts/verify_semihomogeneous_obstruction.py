#!/usr/bin/env python3
"""Exact checks for the scalar semihomogeneous monad obstruction.

This uses only the Python standard library.  It verifies the algebraic identities
used in notes/semihomogeneous-monad-obstruction.md and can exhaustively test the
even-level divisibility certificate over a finite box.
"""

from __future__ import annotations

import argparse
from math import gcd


def target_moments(d: int) -> tuple[int, int, int, int, int]:
    """Return j! times the x^j coefficients of the corrected secant character."""
    return (1, 1, -d, -d, d * d)


def central_moments(d: int) -> tuple[int, int, int, int, int]:
    """Moments after replacing a by (a-b)+b, i.e. centering at slope one."""
    m0, m1, m2, m3, m4 = target_moments(d)
    return (
        m0,
        m1 - m0,
        m2 - 2 * m1 + m0,
        m3 - 3 * m2 + 3 * m1 - m0,
        m4 - 4 * m3 + 6 * m2 - 4 * m1 + m0,
    )


def semihomogeneous_moments(a: int, b: int) -> tuple[int, int, int, int, int]:
    """Moment vector of b^4 exp((a/b)x) on a fourfold."""
    return (b**4, a * b**3, a * a * b * b, a**3 * b, a**4)


def certificate_coefficients(N: int, h: int) -> tuple[int, int, int, int, int]:
    """Coefficients of R_{N,h}(a,b) in a^j b^(4-j), j=0,...,4."""
    return (
        2 * N - h,
        -6 * N + 4 * h,
        -2 * N**3 + N * N * h + 6 * N - 6 * h,
        2 * N**3 - 2 * N * N * h - 2 * N + 4 * h,
        N * N * h - h,
    )


def certificate_polynomial(a: int, b: int, N: int, h: int) -> int:
    """The factored quartic certificate R_{N,h}(a,b)."""
    return (
        (a - b)
        * ((N - 1) * a + b)
        * ((N + 1) * a - b)
        * (h * a + (2 * N - h) * b)
    )


def certificate_from_moments(a: int, b: int, N: int, h: int) -> int:
    coefficients = certificate_coefficients(N, h)
    moments = semihomogeneous_moments(a, b)
    return sum(c * m for c, m in zip(coefficients, moments, strict=True))


def certificate_on_target(d: int, N: int, h: int) -> int:
    coefficients = certificate_coefficients(N, h)
    moments = target_moments(d)
    return sum(c * m for c, m in zip(coefficients, moments, strict=True))


def certificate_target_formula(d: int, N: int, h: int) -> int:
    return (d + 1) * (h * (N * N - 1) * d - 4 * N + 3 * h)


def choose_h(N: int) -> int:
    """Choose an odd certificate parameter coprime to an even level N."""
    if N <= 0 or N % 2:
        raise ValueError("N must be a positive even integer")

    for h in range(1, 12 * N + 21, 2):
        if gcd(h, N) != 1:
            continue
        if N % 3:
            if (h + N) % 3:
                continue
        elif h % 3 == 0:
            continue
        return h
    raise RuntimeError("failed to choose h")


def symmetry_divisor(N: int) -> int:
    """Proved divisor of q=d+1 for a common scalar level-N torsion symmetry."""
    if N <= 0:
        raise ValueError("N must be positive")
    if N % 2:
        return 2 * N**4
    if N % 4 == 2:
        return 3 * N**4 // 2
    return 6 * N**4


def quadratic_target_exceeds_common_torsion(N: int) -> bool:
    """Check the numerical no-go at the smallest q allowed by the proof."""
    q = symmetry_divisor(N)
    return q * (q - 1) > N**8


def verify_even_certificate_box(N: int, radius: int = 20) -> bool:
    """Exhaustively test 24*N^4 divisibility on primitive slopes in a box."""
    h = choose_h(N)
    modulus = 24 * N**4
    for b in range(1, radius + 1):
        for k in range(-radius, radius + 1):
            a = b + N * k
            if gcd(abs(a), b) != 1:
                continue
            if certificate_polynomial(a, b, N, h) % modulus:
                return False
    return True


def verify_symbolic_identities() -> bool:
    for N in range(2, 18, 2):
        h = choose_h(N)
        for b in range(1, 10):
            for k in range(-5, 6):
                a = b + N * k
                if certificate_polynomial(a, b, N, h) != certificate_from_moments(
                    a, b, N, h
                ):
                    return False
        for d in (1, 3, 5, 23, 191, 1535):
            if certificate_on_target(d, N, h) != certificate_target_formula(
                d, N, h
            ):
                return False
    return True


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, default=4, help="torsion level to inspect")
    parser.add_argument("--radius", type=int, default=20, help="finite verification box")
    args = parser.parse_args()

    if args.N <= 0:
        raise SystemExit("N must be positive")

    print("central moments for d=5:", central_moments(5))
    print("symbolic certificate identities:", "OK" if verify_symbolic_identities() else "FAIL")
    print("proved divisor of d+1:", symmetry_divisor(args.N))
    print("common torsion order N^8:", args.N**8)
    q = symmetry_divisor(args.N)
    print("minimum-filter d(d+1):", q * (q - 1))
    print(
        "quadratic symmetry target exceeds common torsion:",
        "YES" if quadratic_target_exceeds_common_torsion(args.N) else "NO",
    )

    if args.N % 2 == 0:
        print("chosen h:", choose_h(args.N))
        ok = verify_even_certificate_box(args.N, args.radius)
        print(f"even certificate box radius {args.radius}:", "OK" if ok else "FAIL")
        if not ok:
            raise SystemExit(1)

    if not verify_symbolic_identities():
        raise SystemExit(1)


if __name__ == "__main__":
    main()
