# A bounded-rank matrix criterion for the final RM middle extension

> **Status.** This note turns Milestone B of the Kodaira--Spencer divisor-bundle construction into a finite-dimensional rank problem when the divisor is a smooth principal theta divisor (`N=1`). It gives rigorous sufficient dimension thresholds for the existence of a nondegenerate middle pairing. It does not yet prove that the geometric extension map reaches those thresholds.

## 1. The `N=1` middle pairing

Assume Milestone A for a smooth principal theta divisor `D`, and let

\[
0\to O_D^{\oplus3}\to E\to\Omega_D^1\to0
\]

be the rank-six Kodaira--Spencer bundle. Put

\[
A_D=E^\vee\otimes K_D.
\]

For a nontrivial two-torsion point

\[
P\in Pic^0(X)[2]
\]

in the open set where the first cancellation has the expected rank, set

\[
V_P=H^1(D,A_D\otimes P).
\]

The construction in `rm-kodaira-spencer-divisor-bundle.md` gives

\[
\dim V_P=8.
\]

An extension

\[
0\to E\to W_D\to A_D\to0
\]

with class

\[
\varepsilon\in H^1(E\otimes E\otimes K_D^{-1})
\]

induces, by the connecting map and Serre duality, a bilinear form

\[
B_{\varepsilon,P}:V_P\otimes V_P\to C.
\]

The extension tensor decomposes as

\[
H^1(E\otimes E K_D^{-1})
=
H^1(Sym^2E\,K_D^{-1})
\oplus
H^1(\Lambda^2E\,K_D^{-1}).
\]

Because the two cohomological inputs have odd degree, the tensor symmetry is reversed in the induced form:

- `Sym^2 E` extension classes induce alternating forms on `V_P`;
- `Lambda^2 E` extension classes induce symmetric forms on `V_P`.

Write the resulting linear maps as

\[
\lambda_P^+:
H^1(Sym^2E\,K_D^{-1})
\to \Lambda^2V_P^*,
\]

and

\[
\lambda_P^-:
H^1(\Lambda^2E\,K_D^{-1})
\to Sym^2V_P^*.
\]

Milestone B is solved as soon as either image contains a nondegenerate form.

## 2. Symmetric forms: dimension `29` is enough

The vector space `Sym^2 V_P^*` is the space of symmetric `8 x 8` matrices and has dimension

\[
\binom{8+1}{2}=36.
\]

Suppose every matrix in a linear subspace `L` is singular. Then its upper rank is at most `7`.

The Meshulam--Loewy--Radwan bound, in the sharp general form proved by de Seguins Pazzis, says for symmetric `n x n` matrices of upper rank `r=2s+1<n` over characteristic zero that

\[
\dim L\le
\max\left\{
\binom{r+1}{2},
\binom{s+1}{2}+s(n-s)+1
\right\}.
\]

For

\[
n=8,\qquad r=7,\qquad s=3,
\]

this gives

\[
\dim L\le\max\{28,22\}=28.
\]

Consequently

\[
\boxed{
\dim Im(\lambda_P^-)\ge29
\Longrightarrow
Im(\lambda_P^-)
\text{ contains a nonsingular symmetric form}.
}
\]

Such a form makes the middle connecting map an isomorphism and settles Milestone B.

## 3. Alternating forms: an even smaller threshold

The target

\[
\Lambda^2V_P^*
\]

has dimension

\[
\binom82=28.
\]

A singular alternating `8 x 8` matrix has rank at most `6`.

For alternating matrices with upper rank `6=2s` (`s=3`), the sharp bounded-rank theorem gives a maximal dimension

\[
\max\left\{
\binom{2s+1}{2},
\binom{s}{2}+s(8-s)
\right\}
=
\max\{21,18\}=21.
\]

Therefore

\[
\boxed{
\dim Im(\lambda_P^+)\ge22
\Longrightarrow
Im(\lambda_P^+)
\text{ contains a symplectic form}.
}
\]

Since `dim V_P=8` is even, a nondegenerate alternating form is possible.

## 4. The two new finite-dimensional targets

The former condition

\[
\det(\partial_{\varepsilon,P})\ne0
\]

can now be replaced by either one of the rank inequalities

\[
\boxed{
rank(\lambda_P^- )\ge29
}
\]

or

\[
\boxed{
rank(\lambda_P^+ )\ge22.
}
\]

These are sufficient, not necessary. A lower-dimensional image can still contain a nondegenerate form.

The advantage is that the new conditions are linear-rank statements. They can be attacked by duality as Petri/cup-product maps.

## 5. Dual Petri formulation

Serre duality identifies the dual of

\[
H^1(\Lambda^2E\,K_D^{-1})
\]

with

\[
H^2(\Lambda^2E^*\,K_D^2).
\]

Using `det(E)=K_D`,

\[
\Lambda^2E^*\otimes K_D^2
\cong
\Lambda^4E\otimes K_D.
\]

Thus the dual of the symmetric-form map is a natural Petri-type multiplication map

\[
\boxed{
\mu_P^-:
Sym^2V_P
\longrightarrow
H^2(D,\Lambda^4E\otimes K_D).
}
\]

and

\[
rank(\mu_P^-)=rank(\lambda_P^-).
\]

Similarly the alternating-form branch is dual to the corresponding alternating cup-product map.

Hence a concrete sufficient target is

\[
rank(\mu_P^- )\ge29
\]

inside a source of dimension `36`, or rank at least `22` in the alternating branch.

This is substantially smaller than computing the full derived endomorphism algebra of the final object.

## 6. Numerical context

The Riemann--Roch calculation from `rm-middle-extension-numerics.md` gives, for `N=1`,

\[
\chi(Sym^2E\,K_D^{-1})=35,
\qquad
\chi(\Lambda^2E\,K_D^{-1})=-35.
\]

These numbers do not by themselves determine the dimensions of the relevant `H^1`, but they show that the extension problem is numerically large enough that the thresholds `22` and `29` are not absurdly out of scale.

The next calculation should therefore compute the actual Petri ranks after choosing three Kodaira--Spencer classes satisfying Milestone A.

## Reference

C. de Seguins Pazzis, *Affine spaces of symmetric or alternating matrices with bounded rank*, arXiv:1507.06213, especially the sharp bounded-rank dimension theorems for symmetric and alternating matrix spaces.
