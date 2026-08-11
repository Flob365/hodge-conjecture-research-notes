#!/usr/bin/env python3
"""Verify the local resolution and the degree-two Atiyah-square coefficients.

Local model:
    M = k[[a,b,c,d]] / (ab, ac, ad).

The script uses tiny symbolic polynomial / exterior-form helpers from the standard
library only.  It checks d1*d2 = d2*d3 = 0 and computes d(d1) wedge d(d2).
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass


VARS = ("a", "b", "c", "d")


@dataclass(frozen=True)
class Monomial:
    exps: tuple[int, int, int, int]


Poly = dict[Monomial, int]
Form = dict[tuple[int, ...], Poly]


def mono(var: int | None = None, coeff: int = 1) -> Poly:
    exps = [0, 0, 0, 0]
    if var is not None:
        exps[var] = 1
    return {Monomial(tuple(exps)): coeff} if coeff else {}


def p_add(*polys: Poly) -> Poly:
    out: defaultdict[Monomial, int] = defaultdict(int)
    for poly in polys:
        for m, c in poly.items():
            out[m] += c
    return {m: c for m, c in out.items() if c}


def p_scale(poly: Poly, scalar: int) -> Poly:
    return {m: scalar * c for m, c in poly.items() if scalar * c}


def p_mul(left: Poly, right: Poly) -> Poly:
    out: defaultdict[Monomial, int] = defaultdict(int)
    for lm, lc in left.items():
        for rm, rc in right.items():
            out[Monomial(tuple(x + y for x, y in zip(lm.exps, rm.exps)))] += lc * rc
    return {m: c for m, c in out.items() if c}


def p_deriv(poly: Poly, var: int) -> Poly:
    out: defaultdict[Monomial, int] = defaultdict(int)
    for m, c in poly.items():
        power = m.exps[var]
        if not power:
            continue
        exps = list(m.exps)
        exps[var] -= 1
        out[Monomial(tuple(exps))] += c * power
    return {m: c for m, c in out.items() if c}


def dpoly(poly: Poly) -> Form:
    out: Form = {}
    for i in range(4):
        derivative = p_deriv(poly, i)
        if derivative:
            out[(i,)] = derivative
    return out


def wedge(left: Form, right: Form) -> Form:
    out: dict[tuple[int, ...], Poly] = {}
    accum: defaultdict[tuple[int, ...], list[Poly]] = defaultdict(list)
    for li, lp in left.items():
        for ri, rp in right.items():
            if set(li) & set(ri):
                continue
            seq = list(li) + list(ri)
            inversions = sum(
                1
                for i in range(len(seq))
                for j in range(i + 1, len(seq))
                if seq[i] > seq[j]
            )
            key = tuple(sorted(seq))
            accum[key].append(p_scale(p_mul(lp, rp), -1 if inversions % 2 else 1))
    for key, polys in accum.items():
        value = p_add(*polys)
        if value:
            out[key] = value
    return out


def form_add(*forms: Form) -> Form:
    keys = set().union(*(f.keys() for f in forms))
    out: Form = {}
    for key in keys:
        value = p_add(*(f.get(key, {}) for f in forms))
        if value:
            out[key] = value
    return out


def fmt_poly(poly: Poly) -> str:
    terms = []
    for m, coeff in sorted(poly.items(), key=lambda item: item[0].exps):
        factors = []
        for name, power in zip(VARS, m.exps):
            if power == 1:
                factors.append(name)
            elif power:
                factors.append(f"{name}^{power}")
        body = "*".join(factors) or "1"
        terms.append(f"{coeff:+d}*{body}")
    return " ".join(terms).lstrip("+") or "0"


def fmt_form(form: Form) -> str:
    labels = {0: "da", 1: "db", 2: "dc", 3: "dd"}
    pieces = []
    for idx, poly in sorted(form.items()):
        pieces.append(f"({fmt_poly(poly)}) " + "^".join(labels[i] for i in idx))
    return " + ".join(pieces) or "0"


def zero() -> Poly:
    return {}


def matrix_product(left: list[list[Poly]], right: list[list[Poly]]) -> list[list[Poly]]:
    rows = len(left)
    mid = len(right)
    cols = len(right[0])
    assert len(left[0]) == mid
    out = [[zero() for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            out[i][j] = p_add(*(p_mul(left[i][k], right[k][j]) for k in range(mid)))
    return out


def main() -> None:
    one = mono()
    a, b, c, d = (mono(i) for i in range(4))

    d1 = [[p_mul(a, b), p_mul(a, c), p_mul(a, d)]]
    d2 = [
        [p_scale(c, -1), p_scale(d, -1), zero()],
        [b, zero(), p_scale(d, -1)],
        [zero(), b, c],
    ]
    d3 = [[d], [p_scale(c, -1)], [b]]

    assert all(not entry for row in matrix_product(d1, d2) for entry in row)
    assert all(not entry for row in matrix_product(d2, d3) for entry in row)
    print("resolution identities: OK")

    columns: list[Form] = []
    for j in range(3):
        terms = []
        for i in range(3):
            terms.append(wedge(dpoly(d1[0][i]), dpoly(d2[i][j])))
        columns.append(form_add(*terms))

    expected_strings = (
        "(-1*b) da^dc + (-2*a) db^dc + (1*c) da^db",
        "(-1*b) da^dd + (-2*a) db^dd + (1*d) da^db",
        "(-1*c) da^dd + (-2*a) dc^dd + (1*d) da^dc",
    )

    for idx, column in enumerate(columns, start=1):
        print(f"column {idx}: {fmt_form(column)}")

    # Structural assertion used in the note: after quotienting coefficients by
    # (b,c,d), the only survivors are -2a db^dc, -2a db^dd, -2a dc^dd.
    survivors = []
    for column in columns:
        kept: Form = {}
        for wedge_idx, poly in column.items():
            filtered: Poly = {}
            for m, coeff in poly.items():
                if m.exps[1] == m.exps[2] == m.exps[3] == 0:
                    filtered[m] = coeff
            if filtered:
                kept[wedge_idx] = filtered
        survivors.append(kept)

    assert fmt_form(survivors[0]) == "(-2*a) db^dc"
    assert fmt_form(survivors[1]) == "(-2*a) db^dd"
    assert fmt_form(survivors[2]) == "(-2*a) dc^dd"
    print("quotient-by-(b,c,d) Atiyah survivors: OK")


if __name__ == "__main__":
    main()
