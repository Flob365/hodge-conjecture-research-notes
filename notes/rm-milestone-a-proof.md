# Milestone A: rank-10 injectivity for a smooth principal theta divisor

> **Status.** Under the standard local universal-family description of a smooth principal theta divisor, the twisted Kodaira--Spencer map used in `rm-kodaira-spencer-divisor-bundle.md` is injective on the ten-dimensional ppav deformation space. Hence the rank is `10`, in particular at least the `3` needed for Milestone A. The proof is a deformation-theoretic Wronskian argument using the heat equation. The remaining milestones B and C are unchanged.

## 1. Setup

Let `(X,Theta)` be a principally polarized complex abelian fourfold with **smooth** theta divisor

\[
D=\Theta.
\]

Let `P in Pic^0(X)` be nontrivial and chosen in the open locus for which the translated theta divisor meets `D` transversely. Write

\[
L=O_X(\Theta).
\]

The unique section of `L tensor P^{-1}` restricts to a nonzero section

\[
s_P\in H^0(D,K_D\otimes P^{-1}),
\]

because `K_D=L|_D` by adjunction.

For a first-order deformation class

\[
e\in H^1(T_D),
\]

contraction with `s_P` gives

\[
\rho_P(e)=e\lrcorner s_P
\in H^1(\Omega_D^2\otimes P^{-1}).
\]

We restrict this map to the ten-dimensional space of polarized deformations of `(X,Theta)`, canonically identified with

\[
T_{[X,\Theta]}\mathcal A_4\cong \operatorname{Sym}^2 H^1(O_X).
\]

The claim is

\[
\boxed{\rho_P|_{T\mathcal A_4}\text{ is injective}.}
\]

Therefore its rank is `10`.

## 2. Theta-function model and the heat equation

Choose a period matrix `tau in H_4` and write the Riemann theta function as

\[
\theta(z,\tau)
=\sum_{m\in\mathbf Z^4}
\exp\bigl(\pi i\,m^t\tau m+2\pi i\,m^tz\bigr).
\]

A tangent vector to `A_4` is a symmetric matrix

\[
Q=(q_{ij})\in\operatorname{Sym}^2\mathbf C^4.
\]

Differentiating the Fourier series directly gives the heat equation, up to a fixed nonzero normalization depending only on the convention for symmetric coordinates on Siegel space:

\[
\delta_Q\theta
\sim
\sum_{i,j}q_{ij}\,\theta_{ij},
\qquad
\theta_{ij}=\frac{\partial^2\theta}{\partial z_i\partial z_j}.
\]

Let `theta_P` denote a theta function representing the translated line bundle `L tensor P^{-1}`. Horizontal transport of the flat line bundle `P` can change `delta_Q theta_P` by first-derivative and scalar gauge terms; these will be exactly the terms quotiented out below.

## 3. The five-dimensional gauge subspace

Set

\[
Z_P=D\cap D_P,
\qquad D_P=(\theta_P=0).
\]

The twisted Koszul sequence of the complete intersection is

\[
0\to O_X
\to (L\otimes P^{-1})\oplus L
\to L^2\otimes P^{-1}
\to K_{Z_P}\to0.
\]

The intermediate cokernel has a five-dimensional space of global sections. Analytically, a convenient spanning set of its image in

\[
H^0(X,L^2\otimes P^{-1})
\]

is

\[
\theta\theta_P
\]

and the four Wronskians

\[
\boxed{
W_i
=\theta\,(\theta_P)_i-\theta_P\,\theta_i,
\qquad i=1,\ldots,4.
}
\]

The inhomogeneous terms in the theta transformation law cancel in each `W_i`, so these are genuine global sections of `L^2 tensor P^{-1}`.

On `D`, one has

\[
W_i|_D=-\theta_P\theta_i|_D.
\]

Since `D` is smooth, the four canonical sections `theta_i|_D` span `H^0(K_D)`, and since `theta_P|_D` is not identically zero, the four `W_i` are independent modulo `theta theta_P`. Thus the gauge subspace has dimension exactly five.

Equivalently,

\[
H^1(\Omega_D^2\otimes P^{-1})
\cong
H^0(X,L^2\otimes P^{-1})
/\langle\theta\theta_P,W_1,\ldots,W_4\rangle,
\]

and the dimensions are `16-5=11`.

## 4. The variation Wronskian represents the twisted period map

Define

\[
\boxed{
F_Q
:=
\theta\,\delta_Q\theta_P
-\theta_P\,\delta_Q\theta.
}
\]

This is the numerator of the first-order variation of the meromorphic `P^{-1}`-valued ratio

\[
f=\frac{\theta_P}{\theta}.
\]

Indeed

\[
\delta_Q f
=\frac{F_Q}{\theta^2}.
\]

The same cancellation that makes the `W_i` global shows that the class of `F_Q` modulo

\[
\langle\theta\theta_P,W_1,\ldots,W_4\rangle
\]

is independent of the chosen flat trivialization of `P`: changing that trivialization only adds a scalar multiple of `theta theta_P` and a linear combination of the `W_i`.

The standard Griffiths--Green description of infinitesimal variation for a hypersurface, together with the heat equation for the universal theta divisor, identifies precisely this class with contraction of the Kodaira--Spencer class by `s_P`:

\[
\boxed{
\rho_P(Q)=[F_Q].
}
\]

This is the only place where the universal-family/heat-equation description enters.

## 5. Vanishing of `rho_P(Q)` means only translation plus rescaling

Assume

\[
\rho_P(Q)=0.
\]

Then there exist constants `c,a_1,...,a_4` such that

\[
F_Q
=c\,\theta\theta_P
+\sum_i a_iW_i.
\]

Divide by `theta^2`. Since

\[
\frac{\theta\theta_P}{\theta^2}=f
\]

and

\[
\frac{W_i}{\theta^2}=\partial_i f,
\]

we obtain the meromorphic identity

\[
\boxed{
\delta_Q f
=c f+\sum_i a_i\partial_i f.
}
\]

The right hand side is exactly the infinitesimal action on `f` of

1. a scalar change of trivialization of the flat line bundle, and
2. the translation-invariant vector field
   \[
   a=\sum_i a_i\partial_{z_i}.
   \]

Hence the zero and pole divisors of `f` deform only by the same infinitesimal translation. In particular the pole divisor

\[
D=(\theta=0)
\]

has **trivial abstract first-order deformation**: an infinitesimal translation is induced by an ambient vector field and therefore maps to zero in `H^1(T_D)`.

## 6. A nonzero ppav deformation cannot induce a trivial theta-divisor deformation

For a smooth ample divisor of dimension at least two in an abelian variety, weak Lefschetz identifies

\[
H^1(D,\mathbf Z)\cong H^1(X,\mathbf Z),
\]

so the Albanese variety of `D` is canonically `X` (up to translation of the Albanese map).

Consequently an abstract first-order deformation of `D` induces the corresponding first-order deformation of its Albanese variety. If the deformation of `D` is trivial, then its Albanese deformation is trivial.

But `Q` is precisely a tangent vector to the moduli of principally polarized abelian fourfolds. A trivial infinitesimal deformation of the underlying abelian variety forces

\[
Q=0.
\]

Thus

\[
\rho_P(Q)=0\Longrightarrow Q=0.
\]

Therefore

\[
\boxed{
\rho_P:\operatorname{Sym}^2\mathbf C^4
\hookrightarrow
H^1(\Omega_D^2\otimes P^{-1})
}
\]

is injective.

Since the source has dimension `10`,

\[
\boxed{\operatorname{rank}(\rho_P)=10.}
\]

## 7. Milestone A follows

Choose any three independent polarized deformation directions

\[
Q_1,Q_2,Q_3\in\operatorname{Sym}^2\mathbf C^4.
\]

Their images under `rho_P` are independent. By Serre duality, the dual combined connecting map

\[
H^2(\Omega_D^1\otimes P)
\longrightarrow
H^3(O_D^{\oplus3}\otimes P)
\]

is therefore surjective.

Hence the Kodaira--Spencer bundle

\[
0\to O_D^{\oplus3}\to\mathcal E\to\Omega_D^1\to0
\]

constructed from `Q_1,Q_2,Q_3` has the generic cohomology cancellation required in `rm-kodaira-spencer-divisor-bundle.md`:

\[
(3,11,11,3)\longrightarrow(0,8,8,0).
\]

So **Milestone A is proved in the smooth-principal-theta case**.

## 8. What is not proved

This argument does not solve the Hodge conjecture and does not yet finish the RM construction.

The active obstacles are now:

1. **Milestone B:** find an extension
   \[
   0\to\mathcal E\to W_D\to\mathcal E^\vee\otimes K_D\to0
   \]
   whose induced `8 x 8` middle pairing is nondegenerate for a suitable degree-zero twist;
2. **Milestone C:** prove the Fourier orbit object is gluable and that the finite Fourier action satisfies the hypotheses needed for the equivariant semiregularity theorem;
3. connect the resulting RM object to the broader Hodge-conjecture deformation argument.

## References

- R. de Jong, *Theta functions on the theta divisor*, arXiv:math/0611810v3. The Hessian restricted to the tangent space is the differential of the Gauss map, and the gradient/Hessian combination detects its ramification.
- P. Bloß, *The Infinitesimal Torelli Theorem for hypersurfaces in abelian varieties*, arXiv:1911.08311, for the Green/Griffiths multiplication-map description of infinitesimal variation for hypersurfaces in abelian varieties.
- R. Smith and R. Varley, *Deformations of theta divisors and the rank 4 quadrics problem*, Compositio Math. 76 (1990), for deformation theory of theta divisors and the heat-equation framework.
- O. Debarre and E. Izadi, *Ampleness of intersections of translates of theta divisors in an abelian fourfold*, arXiv:math/0506374v2, especially the identification of the canonical sections of a smooth theta divisor with translation derivatives of the theta function.
