# The twisted Jacobian module behind principal-theta Milestone A

> **Status.** This note rewrites the `10 -> 11` principal-theta Kodaira--Spencer problem as a variation problem for a finite twisted Jacobian module of the theta equation. It also explains why the first nontrivial symbol near the origin of `Pic^0` is expected to involve the Hessian/second fundamental form rather than the gradient alone. The final identification of that second-order symbol with the Gauss-map differential is the remaining step before one can claim Milestone A.

## 1. Setup

Let `(X,Theta)` be an indecomposable principally polarized abelian fourfold and let

\[
D=\Theta
\]

be smooth. Write

\[
K=K_D=O_D(Theta).
\]

The four translation-invariant derivatives of a theta equation define four sections

\[
s_1,\ldots,s_4\in H^0(D,K).
\]

Because `D` is smooth, these sections have no common zero. They are the canonical linear system and define the Gauss map

\[
\gamma:D\to P^3.
\]

Fix a nontrivial degree-zero line bundle `P`.

## 2. Cohomology of powers of `K` with a nontrivial twist

For `m>=1`, the exact sequence on `X`

\[
0\to O_X((m-1)Theta)\otimes P
\to O_X(mTheta)\otimes P
\to K^m\otimes P
\to0
\]

and IT0 for positive line bundles on an abelian variety give

\[
h^0(D,K^m\otimes P)
=m^4-(m-1)^4.
\]

Thus, for `m=1,2,3,4`,

\[
\boxed{1,15,65,175.}
\]

All higher cohomology of `K^m tensor P` vanishes.

## 3. The degree-three Jacobian quotient is the 11-dimensional target

The conormal sequence of `D` is

\[
0\to K^{-1}\to O_D^{\oplus4}\to Omega_D^1\to0,
\]

where the first map is given by the four sections `s_i`.

Taking the second exterior power gives

\[
0\to K^{-1}\otimes Omega_D^1
\to O_D^{\oplus6}\to Omega_D^2\to0.
\]

Twist by `P`. Since a nontrivial degree-zero line bundle on `D` has only the top generic cohomology appearing in the relevant sequence, one obtains

\[
H^1(D,Omega_D^2\otimes P)
\cong
H^2(D,K^{-1}\otimes Omega_D^1\otimes P).
\]

Dualizing the conormal sequence twisted by `K^{-1}P` gives the exact finite-dimensional description

\[
\boxed{
H^1(D,Omega_D^2\otimes P)^\vee
\cong
\operatorname{coker}\left[
H^0(D,K^2\otimes P^{-1})^{\oplus4}
\xrightarrow{\sum s_i(-)}
H^0(D,K^3\otimes P^{-1})
\right].
}
\]

The dimensions are

\[
4\cdot15=60
\longrightarrow
65,
\]

and the cokernel has dimension `11`.

So the target of principal-theta Milestone A is literally a Jacobian quotient by the gradient ideal.

## 4. A twisted Jacobian module with Hilbert profile `1,11,11,1`

Define, whenever the relevant multiplication map is interpreted through the full Koszul complex of the basepoint-free gradient system,

\[
J_P^m
=
\text{the degree-}m\text{ hypercohomological Jacobian quotient for }
(s_1,\ldots,s_4)
\text{ with twist }P.
\]

The exact Koszul complex of the four gradient sections, together with the vanishings above, gives the four nonzero dimensions

\[
\boxed{
\dim J_P^1=1,
\quad
\dim J_P^2=11,
\quad
\dim J_P^3=11,
\quad
\dim J_P^4=1.
}
\]

The middle `11` in degree three is the group from Section 3.

This symmetric profile is the twisted analogue of the finite Jacobian-ring packages appearing in Green-type descriptions of infinitesimal variation of Hodge structure.

## 5. Why the Hessian, rather than the gradient, is the first useful symbol

Write the principal theta function analytically as

\[
theta(z,tau).
\]

A nontrivial `P` is represented by translating the theta section. Along a small one-parameter translation `a=tv`, the restricted section has expansion on `D`

\[
theta(z+tv)|_D
=
t\,partial_v theta(z)
+\frac{t^2}{2}\,partial_v^2theta(z)
+O(t^3),
\]

because `theta|_D=0`.

The first term is a gradient section. In the derivative/Aomoto complex controlling the degeneration of twisted cohomology as `P -> O`, the ambient first-order variation lies in the exact gradient part. Thus it disappears in the `11`-dimensional Jacobian quotient.

The next possible symbol involves second derivatives of `theta`. Simultaneously, the heat equation identifies derivatives with respect to the period matrix `tau` with second derivatives in `z`. Hence the first potentially nonzero symbol of the universal Kodaira--Spencer morphism is a gradient--Hessian expression.

This explains structurally why the principal-theta rank problem is tied to the second fundamental form of the theta divisor.

## 6. de Jong's invariant gives the exact rank-three local geometry

Robin de Jong defines on the theta divisor

\[
eta
=(nabla theta)^t\,cof(Hess(theta))\,(nabla theta).
\]

For a smooth point of the theta divisor, de Jong proves that `eta=0` exactly when the Gauss map is ramified. Equivalently, away from this divisor the Hessian restricted to the three-dimensional tangent hyperplane is nondegenerate.

For a fourfold theta divisor this means that at an unramified point

\[
\boxed{
rank\bigl(Hess(theta)|_{T_xD}\bigr)=3.
}
\]

An indecomposable ppav has generically finite dominant Gauss map, so the ramification divisor is proper and such points exist.

This rank `3` is exactly the threshold required by Milestone A.

## 7. The remaining bridge lemma

The following statement would settle Milestone A in the principal-theta model.

> **Bridge lemma.** On the projectivized tangent cone to `Pic^0(X)` at the origin, the first nonzero symbol of the universal morphism
> \[
> kappa:O(-Theta_hat)^{10}\to G
> \]
> from `rm-principal-theta-fourier-rank.md` identifies, under the heat equation and the twisted Jacobian quotient above, with the second fundamental form
> \[
> dgamma_x:T_xD\to T_xD^*.
> \]

If the bridge lemma holds, de Jong's theorem immediately supplies a point at which the symbol has rank three. Semicontinuity then gives

\[
\boxed{generic\ rank(kappa)>=3,}
\]

which is precisely Milestone A.

The stronger expected generic rank `10` is not needed for the construction.

## 8. Why the bridge is plausible but not yet claimed

There are three exact compatibilities pointing to it:

1. the translated theta section has first derivative equal to the Gauss-map gradient;
2. period-matrix deformation is converted to the theta Hessian by the heat equation;
3. the first ambient contribution dies in the twisted Jacobian/Aomoto quotient, so the first surviving term is second order.

However, a proof must track the comparison between:

- the Dolbeault derivative complex near `P=O`;
- the Koszul model of the gradient ideal;
- the Kodaira--Spencer extension class of the moving theta divisor;
- and the normalization constants/signs in the heat equation.

Until that comparison is written down, the rank-three conclusion remains a sharply formulated target rather than a theorem.

## References

- R. de Jong, *Theta functions on the theta divisor*, arXiv:math/0611810, especially Definition 1.1 and Theorem 3.1.
- P. Bloß, *The Infinitesimal Torelli Theorem for hypersurfaces in abelian varieties*, arXiv:1911.08311, for the reduction of infinitesimal Torelli questions on abelian hypersurfaces to multiplication maps.
