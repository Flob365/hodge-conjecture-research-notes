# A common-factor Kodaira--Spencer construction forcing a surviving middle extension

> **Status.** This note removes the new risk that the final extension space of the Kodaira--Spencer divisor bundle might vanish. For a special but natural choice of the three defining Kodaira--Spencer classes, a nonzero rank-one deformation class lifts explicitly to `H^1(Lambda^2 E tensor K_D^{-1})`. The remaining compatibility condition is that the same four-dimensional common-factor subspace have rank at least three under the twisted map `rho_P`.

## 1. Polarized deformation tensors

Let `D=Theta` be a smooth principal theta divisor in a principally polarized abelian fourfold `X`.

Use the polarization to identify the ten-dimensional space of infinitesimal ppav deformations with

\[
H^1(T_D)\cong Sym^2 W,
\qquad \dim W=4.
\]

Concretely, after choosing coordinates, write

\[
D_{ij}=\bar z_j\otimes\partial_{z_i}.
\]

A symmetric tensor `v odot w` is represented by the corresponding symmetric combination of the `D_ij`.

Fix a nonzero vector

\[
v\in W.
\]

Define

\[
\boxed{
\xi=v^2\in Sym^2W
}
\]

and the four-dimensional common-factor subspace

\[
\boxed{
L_v=v\cdot W
=\{v\odot w:w\in W\}\subset Sym^2W.
}
\]

## 2. Pointwise wedge annihilation

Choose coordinates with `v=partial_1`. Then

\[
\xi=D_{11}
=\bar z_1\otimes\partial_1.
\]

For a basis vector `partial_j`, the corresponding element of `L_v` is

\[
e_j=D_{1j}+D_{j1}
=\bar z_j\otimes\partial_1
+\bar z_1\otimes\partial_j
\]

(up to an irrelevant scalar when `j=1`).

In the differential graded algebra of `(0,*)`-forms with values in polyvector fields,

\[
\xi\wedge e_j=0
\]

**pointwise**:

- the first summand contains `partial_1 wedge partial_1`;
- the second contains `bar z_1 wedge bar z_1`.

By linearity,

\[
\boxed{
\xi\wedge e=0
\qquad\text{for every }e\in L_v.
}
\]

The same common-factor argument gives

\[
\boxed{
\xi\wedge e\wedge f=0
\qquad\text{for every }e,f\in L_v.
}
\]

The latter identity is also immediate by expanding in the chosen coordinates: a nonzero antiholomorphic wedge would have to select the terms with distinct `bar z` factors, but those terms all carry the holomorphic vector `partial_1`, so the holomorphic wedge vanishes.

## 3. Put the three defining classes in `L_v`

Choose three linearly independent classes

\[
e_1,e_2,e_3\in L_v
\]

and define the rank-six Kodaira--Spencer bundle

\[
0\to U\otimes O_D\to E\to Omega_D^1\to0,
\qquad U\cong C^3,
\]

with extension class

\[
e=u_1\otimes e_1+u_2\otimes e_2+u_3\otimes e_3.
\]

A smooth splitting identifies the Dolbeault operator with

\[
\bar\partial_E
=
\begin{pmatrix}
\bar\partial & e\\
0 & \bar\partial
\end{pmatrix}.
\]

The induced Dolbeault operator on `Lambda^2 E` is the derivation obtained from this operator. In particular, on the top associated-graded term

\[
Lambda^2Omega_D^1\otimes K_D^{-1}\cong T_D
\]

the only off-diagonal term is linear in `e` and is given by contraction/wedge with the three classes `e_a`.

## 4. The rank-one class lifts as an actual cocycle

Represent `xi=v^2` by the restriction to `D` of its translation-invariant ambient Dolbeault tensor.

Lift it in the smooth splitting of

\[
Lambda^2E\otimes K_D^{-1}
\]

by putting zero in the lower filtration pieces.

Because

\[
e_a\wedge\xi=0
\]

pointwise for all three `a`, the off-diagonal Dolbeault term vanishes identically. Therefore the lifted tensor is already `bar partial_E`-closed; no correction term or secondary obstruction is required.

Hence `xi` determines a class

\[
\boxed{
\widetilde\xi
\in
H^1(D,Lambda^2E\otimes K_D^{-1}).
}
\]

It is nonzero: its image under the natural projection to

\[
H^1(T_D)
\]

is the original nonzero class `xi`.

Thus

\[
\boxed{
H^1(D,Lambda^2E\otimes K_D^{-1})\ne0
}
\]

for every triple `e_1,e_2,e_3` contained in one common-factor subspace `L_v`.

This explicitly passes the falsification test from `rm-middle-extension-cohomology-filter.md`.

## 5. The first spectral-sequence differential

The same calculation identifies the first differential of the filtration for an arbitrary test class

\[
\eta\in H^1(T_D).
\]

It is

\[
\boxed{
d_1(\eta)
=
(e_1\wedge\eta,
 e_2\wedge\eta,
 e_3\wedge\eta)
\in
H^2(Lambda^2T_D)^{\oplus3}.
}
\]

The operation is symmetric in the two degree-one deformation classes: interchanging them changes sign both in the Dolbeault wedge and in the wedge of tangent vectors.

For the common-factor class `xi=v^2`, every component is zero already before passing to cohomology.

## 6. The outer-rank problem and the extension-survival problem merge

The three classes defining `E` still have to satisfy Milestone A. For a nontrivial degree-zero twist `P`, write

\[
\rho_P:H^1(T_D)\to H^1(Omega_D^2\otimes P).
\]

The common-factor construction succeeds if and only if one can find `v` and `P` such that

\[
\boxed{
rank\left(\rho_P|_{L_v}\right)\ge3.
}
\]

Indeed, choose any three classes in `L_v` whose images are independent. Then:

1. their Kodaira--Spencer extension cancels the three outer cohomology dimensions;
2. the rank-one class `xi=v^2` automatically survives in the final extension space.

This is substantially stronger than treating Milestones A and B independently.

## 7. A natural bilinear form on the remaining eleven-dimensional space

Assume now that `P` is two-torsion and put

\[
Y_P=H^1(D,Omega_D^2\otimes P),
\qquad \dim Y_P=11.
\]

The rank-one deformation `xi` induces the standard infinitesimal-variation map

\[
\boxed{
B_{\xi,P}:Y_P\longrightarrow Y_P^*,
}
\]

obtained by cup product with `xi` and contraction of forms. By Serre duality this is a symmetric bilinear form on `Y_P`.

The three-dimensional subspace

\[
S=\rho_P(\langle e_1,e_2,e_3\rangle)
\]

is expected, and by Higgs-field integrability is forced at the associated-graded level, to lie in the radical of `B_{xi,P}` whenever `e_a wedge xi=0`.

Therefore the most economical final target is now

\[
\boxed{
rank(B_{\xi,P})=8
\quad\text{and}\quad
rad(B_{\xi,P})=S.
}
\]

If this holds, the form descends to a nondegenerate symmetric form on

\[
Y_P/S,
\qquad \dim(Y_P/S)=8,
\]

which is exactly the middle pairing required by the final extension `W_D`.

The inclusion `S subset rad(B_{xi,P})` should be written carefully through the Higgs/Yoneda formalism before it is used as a theorem; the pointwise common-factor wedge identity is the underlying mechanism.

## 8. New unified target

The previous two separate milestones have been replaced by the following highly structured problem:

> Find `v` and a nontrivial two-torsion `P` such that
> \[
> rank(rho_P|_{vW})=3
> \]
> and the rank-one IVHS form
> \[
> B_{v^2,P}
> \]
> has rank `8`.

The dimensions `4 -> 3` and `11 -> 8` are complementary, suggesting that the two statements may be different faces of one exact Hessian/Gaussian-map calculation.
