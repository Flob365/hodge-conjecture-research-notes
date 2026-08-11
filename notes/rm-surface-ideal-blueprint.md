# Abelian-surface ideal sheaves as the local model for the mixed RM directions

> **Status.** This note gives an exact categorical model for one mixed `B`/bivector direction on an abelian surface and interprets the rank-two RM class `alpha + tilde(alpha)` as the norm of two such surface characters. The remaining problem is arithmetic/geometric descent to a fourfold with genuine real multiplication.

## 1. The surface character

Let `(A,theta)` be a principally polarized abelian surface and let `Z subset A` be a zero-dimensional subscheme of length `q>0`. Since

\[
\int_A\theta^2=2,
\]

we have

\[
[Z]=q[pt]=\frac q2\theta^2.
\]

For the ideal sheaf `I_Z`,

\[
\boxed{
\operatorname{ch}(I_Z)
=1-\frac q2\theta^2.
}
\]

This is exactly one of the two factors occurring in the rank-two RM class considered below.

## 2. Generalized infinitesimal action on a surface

For an abelian surface,

\[
HT^2(A)
=H^2(\mathcal O_A)
\oplus H^1(T_A)
\oplus H^0(\wedge^2T_A)
\]

has dimension `1+4+1=6`.

Choose a basis `u_0,u_1` of `H^1(O_A)` and dual holomorphic forms. Let

\[
B=u_0\wedge u_1\wedge(-),
\qquad
P=\iota_{e_1}\iota_{e_0}.
\]

For

\[
\delta=1-\frac q2\theta^2,
\]

the HKR/Clifford action has rank one and

\[
\boxed{
\ker(\mu_\delta)
=H^1(T_A)\oplus\langle P-qB\rangle
}
\]

up to the sign convention for the bivector action. Thus the mixed direction `P-qB` is already present in the simplest surface ideal-sheaf model.

## 3. The Atiyah kernel agrees automatically

The ideal sheaf `I_Z` is rank-one torsion-free, hence simple:

\[
\operatorname{Hom}(I_Z,I_Z)=\mathbf C.
\]

Since `K_A` is trivial, Serre duality gives

\[
\boxed{
\operatorname{Ext}^2(I_Z,I_Z)=\mathbf C.
}
\]

The generalized Atiyah/semiregularity compatibility is

\[
\sigma_{I_Z}\circ at_{I_Z}
=\mu_{\operatorname{ch}(I_Z)}.
\]

The right hand side is nonzero (indeed it has rank one). Therefore the map

\[
\sigma_{I_Z}:\operatorname{Ext}^2(I_Z,I_Z)\to H\Omega_*(A)
\]

is nonzero. Its source is one-dimensional, so it is injective. Consequently

\[
\boxed{
\ker(at_{I_Z})
=\ker(\mu_{\operatorname{ch}(I_Z)})
=H^1(T_A)\oplus\langle P-qB\rangle.
}
\]

Hence `I_Z` is not merely numerically compatible with the mixed generalized direction: it **categorifies it exactly**.

This is the two-dimensional prototype we want to descend/corestrict in the RM fourfold problem.

## 4. The rank-two RM class is a field norm

For a real quadratic RM fourfold write, over the two real embeddings,

\[
\Theta=\theta_1+\theta_2,
\qquad
\widetilde\Theta=\theta_1-\theta_2.
\]

Recall

\[
\alpha=1-\frac q2\Theta^2+\frac{q^2}{24}\Theta^4,
\]

and define `tilde(alpha)` using `tilde(Theta)`. Since `theta_i^3=0`,

\[
\boxed{
\alpha+\widetilde\alpha
=2\left(1-\frac q2\theta_1^2\right)
  \left(1-\frac q2\theta_2^2\right).
}
\]

Formally, if

\[
\delta_F=1-\frac q2\theta^2
\]

is viewed as the surface character over the real quadratic coefficient field, then

\[
\boxed{
\frac{\alpha+\widetilde\alpha}{2}
=N_{F/\mathbf Q}(\delta_F).
}
\]

Thus the two universal mixed directions of the fourfold are exactly the two conjugate copies of the single surface relation `P-qB`.

This suggests that the RM problem should be viewed as a **categorical norm/corestriction problem**, not as two unrelated obstruction cancellations.

## 5. Why this is not yet a construction on the RM fourfold

The eigenspaces corresponding to the two real embeddings are generally not rational sub-Hodge structures of a simple RM abelian fourfold. In particular, the individual classes

\[
\theta_1^2,\qquad\theta_2^2
\]

need not be rational algebraic cycle classes even though their symmetric combinations are rational.

Therefore one cannot simply place an ideal sheaf of `q` points on each "eigen-surface" inside `X`: those eigen-surfaces need not exist as algebraic subvarieties.

The factorization is a blueprint for descent, not a literal product decomposition on a simple fourfold.

## 6. Concrete descent targets

Three versions of the same problem are now available.

### A. K-theoretic norm

Construct an `F`-linear class `delta_F` in an appropriate extension of algebraic K-theory whose two embeddings have characters

\[
1-\frac q2\theta_1^2,
\qquad
1-\frac q2\theta_2^2,
\]

and whose multiplicative norm is represented by an actual perfect complex.

### B. Corestriction of a category/object

Find an RM-linear or noncommutative category in which the surface ideal object exists before taking the two real embeddings, then apply a tensor-induction/corestriction operation. The desired Chern character is already forced by the norm identity above.

### C. Special-point deformation

Find a point in the same Hodge locus where the norm object becomes an honest tensor product of surface ideal sheaves, prove semiregularity there, and use Perry's variational theorem to deform it to the desired RM point while the norm class remains Hodge.

The difficult part of Route C is not the surface object—its semiregularity is settled above—but proving that a suitable decomposable/split point lies in the relevant connected Hodge locus and that the rational norm class specializes correctly.

## 7. Immediate research question

The main geometric question is now:

> Does the Hodge locus of `alpha + tilde(alpha)` contain a decomposable abelian fourfold on which the norm factorization is realized by actual algebraic surface factors?

A positive answer would turn the two mixed obstruction directions from an object-construction problem into a variational-deformation problem, exactly the setting of Perry's theorem.