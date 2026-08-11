# High-rank nested RM coupling

> **Status.** This note strengthens `rm-nested-elementary-transform.md`. The rank-two curve quotient there proves that a nested elementary transform with the correct secant K-class exists, but a quotient supported only on the three trivial summands of `V_D` may leave positive summands visibly split. Here we remove that forced splitting by increasing the ranks while preserving the same secant ray exactly.

## 1. The issue with the smallest quotient

For a smooth divisor

\[
D\in|M\widetilde A|,
\]

the pure-divisor bundle

\[
V_D=
\mathcal O_D^{\oplus3}
\oplus\Omega_D^1
\oplus\Omega_D^2
\oplus K_D^{\oplus3}
\]

satisfies

\[
\operatorname{ch}(i_*V_D)=12M\widetilde A.
\]

The rank-two cubic block

\[
\mathcal O_Z\oplus\mathcal O_Z(3\widetilde C)
\]

can be generated using only the three trivial summands. If one chooses the quotient that way, the remaining summands can survive as direct summands of the elementary-transform kernel. That is undesirable for the mixed Atiyah-cancellation problem.

The numerical class does not force us to use a rank-two quotient.

## 2. Arbitrary-rank pure cubic sheaves on a complete-intersection curve

Let

\[
Z\subset X
\]

be a smooth complete intersection of three divisors in `|C_tilde|`. For a vector bundle `Q` of rank `r` on `Z`, GRR gives

\[
\operatorname{ch}(j_*Q)
=r\widetilde C^3
+\left(\deg Q-\frac{3r}{2}\widetilde C^4\right)[\mathrm{pt}]_{
\text{normalized}},
\]

where the final expression means the degree-eight coefficient after identifying a degree on `Z` with its pushed-forward point class.

Hence the quartic term vanishes exactly when

\[
\boxed{
\deg Q=\frac{3r}{2}\widetilde C^4.
}
\]

Since

\[
\widetilde C^4=24m^8,
\]

the required degree is `36 r m^8`.

For an even rank `r`, an explicit globally generated example is

\[
\boxed{
Q_r
=\mathcal O_Z^{\oplus(r-1)}
\oplus
\mathcal O_Z\!\left(\frac{3r}{2}\widetilde C\right).
}
\]

Its degree is exactly `(3r/2) C_tilde^4`, so

\[
\boxed{
\operatorname{ch}(j_*Q_r)=r\widetilde C^3.
}
\]

Thus the pure cubic block has a flexible rank parameter.

## 3. Scale the divisor block without changing the target ray

Take `t` copies of `V_D`:

\[
W_D:=V_D^{\oplus t}.
\]

Then

\[
\operatorname{ch}(i_*W_D)=12tM\widetilde A.
\]

Choose as in the previous note

\[
N=qM
\]

pairwise disjoint smooth complete-intersection curves `Z_j subset D`.

On every curve take rank

\[
r=2t
\]

and define

\[
Q_j
=\mathcal O_{Z_j}^{\oplus(2t-1)}
\oplus
\mathcal O_{Z_j}(3t\widetilde C).
\]

Then

\[
\operatorname{ch}(Q_j)=2t\widetilde C^3
\]

after pushforward to `X`, and therefore

\[
\sum_{j=1}^{qM}\operatorname{ch}(Q_j)
=2qtM\widetilde C^3.
\]

A kernel

\[
0\to K\to W_D\to\bigoplus_jQ_j\to0
\]

would consequently satisfy

\[
\boxed{
\operatorname{ch}(i_*K)
=12tM\left(
\widetilde A-\frac q6\widetilde C^3
\right)
=12tM\pi^*\beta'.
}
\]

So increasing the ranks costs nothing numerically except an overall integral multiple.

## 4. Surjectivity is still easy

The bundle `W_D` contains

\[
\mathcal O_D^{\oplus3t}.
\]

For one curve `Z_j`, use `2t-1` trivial generators for the trivial part of `Q_j`. The high line bundle

\[
L_j=\mathcal O_{Z_j}(3t\widetilde C)
\]

is basepoint free for the same sufficiently positive isogeny choice as before, and two general sections generate it on the curve.

Thus the trivial part alone already gives a surjection provided

\[
(2t-1)+2\le3t,
\]

which holds for every `t>=1`.

Because the curves are disjoint, the maps can be chosen independently, yielding

\[
W_D\twoheadrightarrow\bigoplus_jQ_j.
\]

## 5. The new freedom: positive divisor summands can participate

The point of the high-rank construction is not merely that a quotient exists. The target line `L_j` becomes arbitrarily positive as `t` grows.

On `Z_j`,

\[
\deg(K_D|_{Z_j})
=D\widetilde C^3
=12Ms\,m^8,
\]

where

\[
s=\rho^2+\rho^{-2}.
\]

Meanwhile

\[
\deg L_j
=3t\widetilde C^4
=72t\,m^8.
\]

Therefore

\[
\deg(L_j\otimes K_D^{-1}|_{Z_j})
=12(6t-Ms)m^8.
\]

If

\[
\boxed{6t-Ms>6,}
\]

this difference has degree larger than `2g(Z_j)-2=72m^8`. Hence

\[
H^1(Z_j,L_j\otimes K_D^{-1})=0
\]

and Riemann--Roch gives many nonzero morphisms

\[
K_D|_{Z_j}\longrightarrow L_j.
\]

The same large-positive-target argument applies to any fixed vector-bundle summand of `V_D`: after increasing `t`, Serre vanishing on the curve supplies morphisms from its restriction into `L_j`.

Consequently the quotient map can be chosen with **nonzero components from every summand of every copy of `V_D`**, rather than being forced to factor through `O_D^{3t}`.

This removes the obvious direct-summand defect of the minimal rank-two elementary transform.

## 6. A generic fully mixed elementary transform

Choose `M` large enough for the nested curves and smooth containing divisor to exist, then choose `t` so that

\[
6t-Ms>6.
\]

Select a surjection

\[
\phi:W_D\twoheadrightarrow\bigoplus_{j=1}^{qM}Q_j
\]

inside the open set of surjections and require every available component of `phi` to be nonzero. Define

\[
K_{M,m,t}:=\ker(\phi),
\qquad
E_{M,m,t}:=i_*K_{M,m,t}.
\]

Then

\[
\boxed{
\operatorname{ch}(E_{M,m,t})
=12tM\pi^*\beta',
\qquad
\operatorname{Ext}^{<0}(E_{M,m,t},E_{M,m,t})=0.
}
\]

The construction does not by itself prove that `E_{M,m,t}` is indecomposable or simple, but unlike the minimal quotient there is now **no decomposition forced by the chosen presentation**. Simplicity becomes a genuine open-condition / endomorphism calculation rather than an immediate failure.

## 7. Why this is a better Atiyah test object

The two mixed generalized directions

\[
P_{01}-qB_{01},
\qquad
P_{23}-qB_{23}
\]

annihilate the total Chern character. In the split scaffold they could not cancel inside the Atiyah obstruction because the two Chern-character contributions lived in separate direct summands.

In `E_{M,m,t}`, the negative cubic contribution is encoded by an elementary transformation of the same divisor-supported sheaf whose positive contribution gives the linear term. Moreover the quotient map can touch all the geometric summands used to manufacture the pure divisor character.

This does **not** prove Atiyah cancellation, but it removes both elementary categorical obstructions encountered so far:

1. the transverse parity obstruction;
2. the visibly untouched positive direct summands of the minimal nested quotient.

## 8. Exact next calculation

The remaining infinitesimal question is now attached to a concrete short exact sequence

\[
0\to K_{M,m,t}\to W_D\xrightarrow{\phi}Q_U\to0.
\]

The highest-value calculation is to express the generalized Atiyah obstruction of the kernel as the obstruction to deforming the triple

\[
(W_D,Q_U,\phi)
\]

and evaluate it on

\[
P_{01}-qB_{01},
\qquad
P_{23}-qB_{23}.
\]

Because `phi` is now a tunable parameter in a large Hom space, a plausible mechanism becomes testable: solve the two first-order obstruction equations **for the variation of `phi`**. If the resulting linear map from the tangent space of quotient morphisms onto the two obstruction components is surjective, the mixed directions can be killed by choosing first-order variations of the coupling.

That converts the remaining problem into a finite-dimensional linear-surjectivity calculation rather than another search for a new Chern character.