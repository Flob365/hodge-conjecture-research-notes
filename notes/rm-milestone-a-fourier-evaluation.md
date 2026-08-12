# Milestone A as a Fourier evaluation-rank problem

> **Status.** This note packages the twisted Kodaira--Spencer map on a smooth principal theta divisor into a rank-11 Fourier sheaf carrying ten natural global sections. Milestone A becomes the generic rank of their evaluation map. The generic-rank lower bound is still open.

## 1. Principal theta data

Let `D=Theta` be a smooth theta divisor in a principally polarized abelian fourfold `X`, and let `P` vary in `Pic^0(X)` away from the origin.

As in `rm-theta-milestone-a-hessian.md`, the family

\[
\rho_P:H^1(T_D)\to H^1(\Omega_D^2\otimes P^{-1})
\]

has source dimension `10` and target dimension `11`.

Let

\[
\mathcal G:=R^1\Phi_{\mathcal P}(i_*\Omega_D^2)
\]

on the open set where cohomology and base change hold. Its fiber at `P` is

\[
\mathcal G|_P\simeq H^1(D,\Omega_D^2\otimes P^{-1}).
\]

Thus `rank(G)=11`.

## 2. Ten natural sections

Each Kodaira--Spencer class

\[
e\in H^1(T_D)=\operatorname{Ext}^1(K_D,\Omega_D^2)
\]

is a morphism

\[
K_D\to\Omega_D^2[1].
\]

After push-forward to `X` and Fourier--Mukai transform, this produces, over the nonzero Picard locus, the family of vectors

\[
P\mapsto\rho_P(e).
\]

After twisting `G` by the inverse of the rank-one Fourier transform of `O_X(Theta)`, the ten basis vectors of `H^1(T_D)` become ten global sections of a rank-11 sheaf `G'`.

Hence the universal Milestone-A morphism can be written as

\[
\boxed{
\mathrm{ev}:\mathcal O_{\widehat X}^{\oplus10}\longrightarrow\mathcal G'.
}
\]

Its fiber rank at a general `P` is exactly `rank(rho_P)`.

## 3. What Milestone A requires

The Kodaira--Spencer divisor bundle only needs three independent deformation classes. Therefore it is enough to prove

\[
\boxed{\operatorname{rk}_{gen}(\mathrm{ev})\ge3.}
\]

The strongest natural target is

\[
\boxed{\operatorname{rk}_{gen}(\mathrm{ev})=10.}
\]

In that case the ten sections generate a rank-ten subsheaf of `G'`, leaving a rank-one quotient away from a codimension-two degeneracy locus.

## 4. Chern-class consistency check

The Fourier--Mukai calculation gives, after the normalization above,

\[
\operatorname{rk}(\mathcal G')=11,
\qquad
c_1(\mathcal G')=8\widehat\Theta,
\]

and the corresponding second Chern data imply that, if the evaluation map has generic rank ten, the expected Thom--Porteous class of the rank-drop locus is

\[
\boxed{30\,\widehat\Theta^2.}
\]

Thus there is no numerical Chern-class obstruction to generic rank ten. Instead the model predicts a concrete codimension-two degeneracy cycle.

## 5. Fourier-faithfulness interpretation of the kernel

Suppose

\[
e\in H^1(T_D)
\]

satisfies `rho_P(e)=0` for general `P`. Then the Fourier transform of the corresponding derived morphism

\[
i_*K_D\to i_*\Omega_D^2[1]
\]

vanishes away from the origin of `widehat X`. Hence it is supported at the origin.

Therefore

\[
\ker(\rho_{gen})
\]

is precisely the part of the Kodaira--Spencer space whose Fourier image is invisible off the origin.

This is a useful dichotomy:

- if the origin-supported subspace has dimension at most `7`, Milestone A follows;
- if it is zero, the generic rank is `10`.

## 6. Relation with the Gauss/Hessian picture

The same ten sections are represented analytically, via the heat equation, by second-order theta variations modulo the theta section and its four first derivatives.

Thus the two reformulations agree:

1. Fourier side: generic rank of ten global sections of `G'`;
2. theta-function side: rank of the ten Hessian variations modulo the Jacobian ideal.

Robin de Jong's gradient--Hessian invariant shows that the Hessian restricted to the tangent hyperplane has rank three away from the ramification divisor of the Gauss map. The remaining missing step is to identify a rank-three minor of `ev` with a nonzero local Gauss/Hessian minor.

## 7. Immediate next target

Prove one of:

\[
\operatorname{rk}_{gen}(\mathrm{ev})\ge3,
\]

or the stronger

\[
\operatorname{rk}_{gen}(\mathrm{ev})=10.
\]

Two plausible proofs remain:

- a local-to-global Hessian comparison using the heat equation and the Gauss map;
- a Fourier-local calculation showing that fewer than eight independent Kodaira--Spencer morphisms can be supported entirely at the origin.
