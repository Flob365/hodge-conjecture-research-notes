# Principal-theta Milestone A as a full Fourier evaluation and a Massey product

> **Status.** This note gives two exact reformulations of the principal-theta `10 -> 11` map. First, it identifies the target with an explicit `15/4` quotient. Second, it shows that the ten Kodaira--Spencer classes are all global sections of the Fourier bundle `G(Theta-hat)`. The cohomological map is intrinsically a secondary/Massey operation, explaining why a Hessian rather than a first-order gradient is expected in its leading symbol. The remaining problem is to prove that its complete evaluation has generic rank at least three.

## 1. Setup

Let `(X,Theta)` be a principally polarized abelian fourfold and let

\[
i:D=Theta\hookrightarrow X
\]

be smooth. Put

\[
K=K_D=O_D(Theta),
\qquad
V=H^0(X,T_X),
\qquad \dim V=4.
\]

The tangent-normal sequence is

\[
\boxed{
0\to T_D\to V\otimes O_D\xrightarrow{s}K\to0,
}
\]

where `s` is given by the four translation derivatives of a theta equation. These four sections form the canonical linear system of `D`.

Fix a nontrivial

\[
P\in Pic^0(X).
\]

Then

\[
h^0(D,K\otimes P)=1.
\]

Choose its nonzero section

\[
\alpha_P\in H^0(D,K\otimes P),
\]

unique up to scalar.

## 2. An exact `15/4` model of the eleven-dimensional target

Tensor the tangent-normal sequence by `K tensor P`. Since

\[
T_D\otimes K\cong\Omega_D^2,
\]

we obtain

\[
0\to\Omega_D^2\otimes P
\to V\otimes K\otimes P
\to K^2\otimes P
\to0.
\]

For nontrivial `P`, the ample line bundle `K tensor P` on `D` satisfies

\[
h^0(KP)=1,
\qquad
H^{>0}(KP)=0,
\]

and

\[
h^0(K^2P)=15.
\]

The map on global sections is

\[
V\longrightarrow H^0(K^2P),
\qquad
v\longmapsto s_v\alpha_P.
\]

It is injective: the `s_v` are linearly independent and `alpha_P` is a nonzero section on the integral variety `D`.

Therefore

\[
H^0(\Omega_D^2P)=0
\]

and the long exact sequence gives the canonical quotient

\[
\boxed{
H^1(D,\Omega_D^2\otimes P)
\cong
\frac{H^0(D,K^2\otimes P)}
{\alpha_P\,H^0(D,K)}.
}
\]

Its dimension is

\[
15-4=11.
\]

This is the most economical model of the target found so far.

## 3. The Kodaira--Spencer map is secondary

Multiplication by `alpha_P` gives a morphism of tangent-normal sequences

\[
\begin{array}{ccccccccc}
0&\to&T_D&\to&V\otimes O_D&\to&K&\to&0\\
&&\downarrow\alpha_P&&\downarrow\alpha_P&&\downarrow\alpha_P\\
0&\to&T_DKP&\to&V\otimes KP&\to&K^2P&\to&0.
\end{array}
\]

The desired map is

\[
\rho_P:
H^1(T_D)\to H^1(T_DKP)=H^1(\Omega_D^2P).
\]

But

\[
H^1(V\otimes KP)=0.
\]

Thus the ambient first-order class dies. The map `rho_P` is recovered only after choosing a primitive in the middle term and applying the normal map. In other words it is a secondary operation.

### Cech description

Represent

\[
\xi\in H^1(T_D)
\]

by a Cech cocycle `t_ij`. View it through the inclusion `T_D -> V tensor O_D`. Then

\[
\alpha_Pt_{ij}
\]

is a Cech cocycle with values in `V tensor KP`. Since its first cohomology vanishes, choose local sections `b_i` with

\[
\boxed{
b_j-b_i=\alpha_Pt_{ij}.}
\]

Apply the normal map

\[
s:V\otimes KP\to K^2P.
\]

Because `s(t_ij)=0`, the sections `s(b_i)` agree on overlaps and define a global section

\[
\beta_\xi\in H^0(K^2P).
\]

Changing the primitive `b_i` by a global section of `V tensor KP` changes `beta_xi` by an element of

\[
\alpha_PH^0(K).
\]

Hence

\[
\boxed{
\rho_P(\xi)=[\beta_\xi]
\in
H^0(K^2P)/(\alpha_PH^0(K)).
}
\]

This formula is independent of all choices.

### Dolbeault description

If `t` is a Dolbeault representative of `xi`, choose a smooth `V tensor KP`-valued section `b` solving

\[
\bar\partial b=\alpha_Pt.
\]

Then

\[
\boxed{
\rho_P(\xi)=[s(b)]
\mod \alpha_PH^0(K).
}
\]

The quotient kills the ambiguity in `b`.

This is precisely the shape of a Massey/Toda-type secondary product.

## 4. Why this explains the Hessian bridge

The section `alpha_P` is obtained by restricting the theta section of the translated principal polarization to `D`. If `P=P_{tv}` tends to the origin along a tangent vector `v`, then after the natural first-order normalization

\[
\alpha_{P_{tv}}
\sim
 t\,\partial_v\theta|_D
+\frac{t^2}{2}\partial_v^2\theta|_D+\cdots.
\]

The first term is in the canonical gradient system. But Section 3 shows that the ambient first-order contribution is annihilated by the vanishing of `H^1(KP)` and then quotienting by

\[
\alpha_PH^0(K).
\]

Thus the first potentially visible symbol of `rho_P` is secondary. The next theta term is a second derivative. Period-matrix deformation is also converted into second `z`-derivatives by the heat equation.

So the earlier Hessian prediction is not merely dimensional: it is forced by the exact cohomological architecture of `rho_P`.

What is still missing is the comparison theorem identifying this secondary symbol with the second fundamental form of the Gauss map.

## 5. All ten Fourier sections come from Kodaira--Spencer classes

Set

\[
F=i_*\Omega_D^2
\]

and let

\[
\Phi:D^b(X)\to D^b(\widehat X)
\]

be the Poincare Fourier--Mukai equivalence. On

\[
U=\widehat X\setminus\{0\},
\]

put

\[
G=R^1\Phi(F)|_U.
\]

For every nontrivial `P`, Section 2 shows

\[
H^0(D,\Omega_D^2\otimes P)=0.
\]

Hence

\[
R^0\Phi(F)
\]

is supported at the origin.

For a principal polarization,

\[
\Phi(O_X(Theta))\cong O_{\widehat X}(-\widehat\Theta)
\]

up to the standard normalization. Fourier equivalence therefore gives

\[
\operatorname{Ext}^1_{\widehat X}
\bigl(O(-\widehat\Theta),\Phi(F)\bigr)
\cong
\operatorname{Ext}^1_X(O(Theta),F).
\]

The right hand side is

\[
H^1(D,\Omega_D^2\otimes K^{-1})
=H^1(D,T_D).
\]

Since the first Fourier cohomology below `G` is zero-dimensional, the hyper-Ext spectral sequence has no higher cohomology contribution from it against a line bundle. Hence the edge map gives

\[
\boxed{
H^0\bigl(U,G(\widehat\Theta)\bigr)
\cong H^1(D,T_D).
}
\]

For a smooth principal theta divisor

\[
h^1(D,T_D)=10.
\]

Therefore

\[
\boxed{
h^0(G(\widehat\Theta))=10}
\]

in the reflexive/punctured-dual sense relevant here.

## 6. Milestone A is the complete evaluation map

Under the identification above, the universal family of maps `rho_P` is exactly the evaluation of all sections of `G(Theta-hat)`:

\[
\boxed{
\mathrm{ev}:
H^0(G(\widehat\Theta))\otimes O_U
\longrightarrow
G(\widehat\Theta),
}
\]

with

\[
10\longrightarrow11
\]

on every fiber.

Equivalently, before twisting,

\[
O_U(-\widehat\Theta)^{\oplus10}\to G.
\]

Thus Milestone A has become a standard generation-rank question for one Fourier bundle:

\[
\boxed{
\text{prove that the complete evaluation of }G(\widehat\Theta)
\text{ has generic rank at least }3.
}
\]

The natural expectation is generic rank `10`.

## 7. Two concrete ways forward

### A. Secondary-symbol/Hessian route

Use the explicit Massey formula of Section 3, pass to the tangent cone at the origin of `Pic^0`, and prove that its first nonzero symbol is the second fundamental form of the theta Gauss map. De Jong's non-ramification theorem then gives the required rank `3` at a suitable point.

### B. Evaluation-bundle route

Use the semihomogeneous resolution of `G` from
[`principal-theta-semihomogeneous-resolution.md`](principal-theta-semihomogeneous-resolution.md)
and prove directly that its ten global sections span at least a three-dimensional subspace at the generic point.

Because these are all global sections, there is no longer an unspecified choice of Kodaira--Spencer directions: any generic three-dimensional subspace works once the evaluation rank is at least three.

## References

- R. Lazarsfeld and M. Popa, *Derivative complex, BGG correspondence, and numerical inequalities for compact Kahler manifolds*, arXiv:0907.0651.
- L. Lombardi, *Inequalities for the Hodge numbers of irregular compact Kaehler manifolds*, arXiv:1103.1704.
- G. Pareschi, *Gaussian maps and generic vanishing I: subvarieties of abelian varieties*, arXiv:1401.7442.
- R. de Jong, *Theta functions on the theta divisor*, arXiv:math/0611810.
