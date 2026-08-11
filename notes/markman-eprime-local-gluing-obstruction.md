# Local obstruction for the explicit glued sheaf in Markman's Example 11.2.7

> **Status.** This note isolates a local obstruction for the specific gluing construction used in Markman's Example 11.2.7 (arXiv:2509.23079). Under the natural generic local model in which the support divisor is smooth, the correcting curve is smooth, and they meet in a reduced transverse point, the two mixed real-multiplication generalized deformation directions cannot both lie in the Atiyah kernel. This rejects that generic gluing model as a solution to Question 11.2.2. It does **not** reject Question 11.2.2 itself, nor more derived/non-generic couplings.

## 1. Why this local model is the relevant one

Markman's Example 11.2.7 constructs a coherent sheaf `E'` by taking generic translates of a sheaf whose leading Chern character is a divisor class and gluing them to a line bundle on a correcting curve at isolated intersection points.

At a gluing point where

- the divisor support is smooth,
- the curve is smooth,
- the sheaves are line bundles on their respective supports,
- the intersection is a reduced point,

line-bundle twists are locally trivial and the glued module is the structure sheaf of the union of the divisor and the curve.

Choose regular parameters

\[
R=k[[a,b,c,d]]
\]

so that

\[
D:(a=0),
\qquad
C:(b=c=d=0).
\]

Then

\[
I_D\cap I_C=(ab,ac,ad)
\]

and the local glued module is

\[
\boxed{M=R/(ab,ac,ad).}
\]

## 2. Minimal free resolution

A minimal resolution is

\[
0\to R\xrightarrow{d_3}R^3\xrightarrow{d_2}R^3\xrightarrow{d_1}R\to M\to0,
\]

with

\[
d_1=\begin{pmatrix}ab&ac&ad\end{pmatrix},
\]

\[
d_2=
\begin{pmatrix}
-c&-d&0\\
b&0&-d\\
0&b&c
\end{pmatrix},
\qquad
 d_3=\begin{pmatrix}d\\-c\\b\end{pmatrix}.
\]

Direct multiplication gives

\[
d_1d_2=0,
\qquad
d_2d_3=0.
\]

The Betti table is therefore `1,3,3,1`.

## 3. Degree-two Atiyah component

Using the trivial connections on the free modules, the degree-two part of the Atiyah square is represented, up to the conventional global sign, by

\[
d(d_1)\wedge d(d_2):R^3\longrightarrow R\otimes\Omega_R^2.
\]

Its three columns are

\[
\begin{aligned}
\omega_1&=-b\,da\wedge dc-2a\,db\wedge dc+c\,da\wedge db,\\
\omega_2&=-b\,da\wedge dd-2a\,db\wedge dd+d\,da\wedge db,\\
\omega_3&=-c\,da\wedge dd-2a\,dc\wedge dd+d\,da\wedge dc.
\end{aligned}
\]

The factor `1/2` in `at_M^2/2` is irrelevant for vanishing.

Let `P` be a translation-invariant holomorphic bivector. Contracting gives an `Ext^2` cocycle whose three entries contain the terms

\[
-2aP(db,dc),
\qquad
-2aP(db,dd),
\qquad
-2aP(dc,dd).
\]

## 4. These `a`-terms cannot be boundaries

Apply `Hom_R(-,M)` to the resolution. Boundaries in degree two are rows obtained by multiplying by `d_2`. Every entry of `d_2` belongs to the ideal

\[
(b,c,d)\subset M.
\]

Hence every degree-two boundary maps to zero after quotienting by `(b,c,d)`.

But

\[
M/(b,c,d)\cong k[[a]],
\]

and the three displayed `a`-terms survive in this quotient. Therefore

\[
\boxed{
[P\lrcorner at_M^2]=0
\Longrightarrow
P(db,dc)=P(db,dd)=P(dc,dd)=0.
}
\]

Equivalently, the three-dimensional conormal space

\[
W_C^*=\operatorname{span}\{db,dc,dd\}
\]

to the correcting curve must be isotropic for `P`.

This is only a necessary condition, but it is already sufficient for the RM no-go below.

## 5. Apply the condition to the two RM bivectors

The real-multiplication splitting is

\[
V^*=U_+^*\oplus U_-^*,
\qquad
\dim U_+^*=\dim U_-^*=2.
\]

The two mixed directions found in `rm-semiregularity-kernel.md` contain nondegenerate bivectors

\[
P_+\in\wedge^2U_+,
\qquad
P_-\in\wedge^2U_-.
\]

For a three-dimensional subspace `W subset V^*`, isotropy for `P_+` is equivalent to

\[
\dim\operatorname{pr}_+(W)\le1,
\]

because `P_+` is nondegenerate on the two-dimensional space `U_+^*`. Likewise isotropy for `P_-` forces

\[
\dim\operatorname{pr}_-(W)\le1.
\]

If both held for `W=W_C^*`, then

\[
\dim W_C^*
\le
\dim\operatorname{pr}_+(W_C^*)
+
\dim\operatorname{pr}_-(W_C^*)
\le2,
\]

contradicting

\[
\dim W_C^*=3.
\]

Thus

\[
\boxed{
\text{at every ordinary divisor--curve gluing point, at least one of }
P_+,P_-
\text{ has nonzero local Atiyah obstruction.}
}
\]

## 6. The `B`-field parts cannot cancel this local edge class

The two full generalized kernel vectors are, up to the chosen HKR normalization,

\[
\xi_+=B_+-q^{-1}P_+,
\qquad
\xi_-=B_--q^{-1}P_-.
\]

The `B`-field part belongs to the global-cohomology filtration of the local-to-global Ext spectral sequence. Its image in the stalkwise edge term

\[
H^0(\mathcal Ext^2(M,M))
\]

is zero. Consequently a nonzero local bivector edge class cannot be cancelled by the `B`-field contribution.

Therefore at least one of `xi_+`, `xi_-` fails to lie in the Atiyah kernel at every ordinary gluing point.

## 7. Consequence for semiregularity of this explicit gluing model

The exact Chern-action calculation in `rm-semiregularity-kernel.md` proves

\[
\xi_+,\xi_-\in\ker(\mu_{\beta'}),
\qquad
\mu_{\beta'}=\sigma_{E'}\circ at_{E'}.
\]

If, say, `xi_+` has nonzero Atiyah image, then

\[
0\neq at_{E'}(\xi_+)
\in
\ker\left(\sigma_{E'}|_{\operatorname{im}(at_{E'})}\right).
\]

Hence the semiregularity map is not injective on the Atiyah image.

Under the ordinary smooth/reduced local regime above, we conclude

\[
\boxed{
\text{the specific divisor--curve fiber gluing of Example 11.2.7
cannot satisfy the semiregularity condition in Question 11.2.2.}
}
\]

This is a statement about the local architecture of that construction. A different coherent sheaf with the same Chern character, a derived coupling, or a gluing through nonreduced/derived local geometry is not covered by the obstruction.

## 8. Research consequence

The real-multiplication program has now eliminated two ordinary coherent couplings for the final mixed directions:

1. elementary transforms of a divisor sheaf along smooth curves;
2. ordinary fiber gluing of a divisor-supported sheaf to a curve sheaf at reduced points.

Both fail because a stalkwise `Ext^2` edge class detects the bivector component before the global `B`-field can cancel it.

A surviving construction must therefore remove this local `Ext^2` channel, or mix the two Fourier-conjugate obstruction channels before they reach the stalkwise edge term. This strongly favors locally free divisor blocks, nontrivial derived intersections, or the `q=1` Fourier-symmetry route.