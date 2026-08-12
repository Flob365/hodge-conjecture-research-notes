# Milestone A on a smooth theta divisor: a twisted Hessian rank problem

> **Status.** This note sharpens the first Kodaira--Spencer milestone for the non-split divisor bundle in the special principally polarized case `N=h^0(Theta)=1`. The main output is an explicit quotient description of the target and a concrete Hessian/Jacobian-ideal formulation. The final injectivity/rank-10 statement is not yet proved.

## 1. Setup

Let `(X,Theta)` be a principally polarized abelian fourfold with smooth theta divisor

\[
D=(\theta=0)\subset X.
\]

Put

\[
K_D=\mathcal O_D(\Theta).
\]

For a nontrivial `P in Pic^0(X)`, the basic exact sequences give

\[
h^0(D,K_D\otimes P^{-1})=1,
\qquad
h^0(D,K_D^2\otimes P^{-1})=15.
\]

Tensoring the tangent sequence

\[
0\to T_D\to \mathcal O_D^{\oplus4}\to K_D\to0
\]

by `K_D` gives

\[
0\to \Omega_D^2\to K_D^{\oplus4}\to K_D^2\to0.
\]

For nontrivial `P`, the relevant higher cohomology of `K_D\otimes P^{-1}` vanishes, so

\[
H^1(D,\Omega_D^2\otimes P^{-1})
\cong
\operatorname{coker}
\left[
H^0(K_D\otimes P^{-1})^{\oplus4}
\to
H^0(K_D^2\otimes P^{-1})
\right].
\]

Hence

\[
\boxed{\dim H^1(D,\Omega_D^2\otimes P^{-1})=15-4=11.}
\]

## 2. The Kodaira--Spencer source

The normal sequence

\[
0\to T_D\to \mathcal O_D^{\oplus4}\to K_D\to0
\]

and Lefschetz identify

\[
H^1(T_D)
\simeq
\ker\left(V\otimes V\to\Lambda^2V\right)
\simeq
\operatorname{Sym}^2V,
\qquad \dim V=4.
\]

Thus

\[
\boxed{\dim H^1(T_D)=10.}
\]

For

\[
e\in H^1(T_D)=\operatorname{Ext}^1(K_D,\Omega_D^2),
\]

the associated connecting map after twisting by `P^{-1}` is

\[
\rho_P(e):
H^0(K_D\otimes P^{-1})
\to
H^1(\Omega_D^2\otimes P^{-1}).
\]

Since the source is one-dimensional, varying `e` gives a linear map

\[
\boxed{
\rho_P:H^1(T_D)\simeq\operatorname{Sym}^2V
\longrightarrow
H^1(\Omega_D^2\otimes P^{-1})\simeq\mathbf C^{11}.
}
\]

Milestone A only needs three classes whose images are independent, so it is enough to prove

\[
\operatorname{rank}(\rho_P)\ge3
\]

for general `P`. The natural stronger target is generic injectivity, i.e. rank `10`.

## 3. Explicit quotient by theta and its first derivatives

Let `theta_P` denote the unique section of `O_X(Theta) tensor P^{-1}`. The exact sequence

\[
0\to O_X(Theta)\otimes P^{-1}
\xrightarrow{\cdot\theta}
O_X(2\Theta)\otimes P^{-1}
\to
K_D^2\otimes P^{-1}\to0
\]

identifies

\[
H^0(K_D^2\otimes P^{-1})
\cong
\frac{H^0(O_X(2\Theta)\otimes P^{-1})}
{\langle\theta\theta_P\rangle}.
\]

The four components of the map

\[
H^0(K_D\otimes P^{-1})^{\oplus4}
\to H^0(K_D^2\otimes P^{-1})
\]

are multiplication by the four Gauss sections `partial_i theta|_D`. Therefore, provided the five displayed sections are independent for general `P`,

\[
\boxed{
H^1(\Omega_D^2\otimes P^{-1})
\cong
\frac{H^0(O_X(2\Theta)\otimes P^{-1})}
{\langle
\theta\theta_P,
(\partial_1\theta)\theta_P,\ldots,
(\partial_4\theta)\theta_P
\rangle}.
}
\]

The numerator has dimension `16`, giving again `16-5=11`.

## 4. Heat equation and the ten second derivatives

Infinitesimal variations of the period matrix of a ppav are symmetric, hence parametrized by

\[
\operatorname{Sym}^2V.
\]

The heat equation for the Riemann theta function identifies differentiation in the period-matrix direction `(i,j)` with a scalar multiple of the second derivative

\[
\partial_i\partial_j\theta.
\]

Consequently the expected analytic representative of `rho_P` is the class of the ten products

\[
(\partial_i\partial_j\theta)\theta_P
\]

in the quotient of Section 3, after the standard correction terms required by the automorphy of theta derivatives.

Thus the sharp analytic target is:

\[
\boxed{
\text{for general }P,
\text{ the ten second-order theta variations have rank }10
\text{ modulo }\theta\text{ and }\nabla\theta.
}
\]

A weaker rank-three statement already proves Milestone A.

## 5. Relation with the Gauss map and Hessian

The canonical/Gauss map of a smooth theta divisor is

\[
\gamma:D\to\mathbf P^3,
\qquad
x\mapsto[\partial_1\theta(x):\cdots:\partial_4\theta(x)].
\]

Its differential is controlled by the Hessian of `theta` restricted to the tangent hyperplane of `D`.

Robin de Jong constructs an invariant from the gradient and Hessian whose zero locus is precisely the ramification locus of the Gauss map. Hence away from ramification the restricted second fundamental form has maximal rank `3`.

This number is exactly the minimum rank required by Milestone A. What remains to be proved is the precise identification between the rank-three second fundamental form at a point and the rank of the global twisted cup-product map `rho_P`.

So the current implication is only a **strong geometric hint**, not yet a theorem:

\[
\text{Gauss unramified}\quad\rightsquigarrow\quad
\operatorname{rank}(\rho_P)\ge3.
\]

The missing arrow is the key local-to-global comparison.

## 6. Fourier--Mukai reformulation

The class `e in H^1(T_D)` is a derived morphism

\[
e:K_D\to\Omega_D^2[1].
\]

After pushing forward to `X` and applying the Poincare Fourier--Mukai transform, its restriction over

\[
\widehat X\setminus\{0\}
\]

is exactly the family of maps `rho_P(e)`.

Therefore, if `rho_P(e)=0` for general `P`, the transformed morphism is supported at the origin of `widehat X`.

This gives another route to Milestone A:

> bound the subspace of `H^1(T_D)` whose Fourier transform is supported only at the origin.

A bound of dimension at most `7` already yields rank at least `3`; proving that this subspace is zero gives generic rank `10`.

## 7. Current falsifiable target

Prove one of the following, in increasing strength:

1. `rank(rho_P) >= 3` for general nontrivial `P`;
2. the Fourier-origin-supported kernel has dimension at most `7`;
3. `rho_P` is generically injective;
4. identify a `3 x 3` minor of `rho_P` with a nonzero Hessian/Gauss invariant.

Any of these settles the first Kodaira--Spencer cancellation needed for the non-split divisor bundle.

## References

- R. de Jong, *Theta functions on the theta divisor*, arXiv:math/0611810.
- P. Bloss, *The Infinitesimal Torelli Theorem for hypersurfaces in abelian varieties*, arXiv:1911.08311 (revised 2026).
