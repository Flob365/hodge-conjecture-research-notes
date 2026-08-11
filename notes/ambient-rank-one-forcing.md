# Rank-one forcing for three compatible Kodaira--Spencer directions

> **Status.** This note gives an exact linear-algebra classification of the kernel of the ambient `S_(2,2)` product. It proves that any nonzero class capable of annihilating three independent polarized deformation directions must have rank one. Thus the common-factor ansatz `xi=v^2`, `e_a in vW` is not merely convenient; it is forced before the five-dimensional theta correction is considered.

## 1. The ambient product

Let `W` be a four-dimensional complex vector space and put

\[
T=Sym^2W.
\]

The symmetric square decomposes as

\[
Sym^2T
=Sym^4W\oplus S_{(2,2)}W.
\]

The ambient cup-wedge product of polarized deformation tensors is, up to a nonzero scalar, the projection

\[
\pi_{22}:Sym^2(Sym^2W)\to S_{(2,2)}W.
\]

For a fixed nonzero

\[
A\in Sym^2W,
\]

define

\[
m_A:T\to S_{(2,2)}W,
\qquad
B\mapsto\pi_{22}(A\odot B).
\]

The question is the dimension of `ker(m_A)` as a function of the rank of the symmetric matrix `A`.

## 2. Tensor criterion

Choose a basis and write symmetric matrices `A=(A_ij)` and `B=(B_ij)`.

The tensor `A odot B` has components

\[
T_{ij,kl}=A_{ij}B_{kl}+B_{ij}A_{kl}.
\]

Its `S_(2,2)` projection vanishes exactly when this tensor is fully symmetric in all four indices. It is enough to impose

\[
\boxed{
A_{ij}B_{kl}+B_{ij}A_{kl}
=
A_{ik}B_{jl}+B_{ik}A_{jl}
}
\]

for all `i,j,k,l`.

Since the problem is invariant under `GL(W)` congruence, over `C` we may put a rank-`r` form in the normal form

\[
A=diag(1,\ldots,1,0,\ldots,0).
\]

## 3. Rank one

Take

\[
A=e_1^2.
\]

The equations force

\[
B_{ij}=0
\qquad(i,j>1),
\]

while the four coefficients

\[
B_{11},B_{12},B_{13},B_{14}
\]

are arbitrary.

Hence

\[
\boxed{
\ker(m_A)=e_1W,
\qquad \dim\ker(m_A)=4.
}
\]

Equivalently, if `A=v^2`,

\[
\ker(m_A)=vW.
\]

This is exactly the common-factor subspace used in the theta construction.

## 4. Rank two

Take

\[
A=e_1^2+e_2^2.
\]

Solving the symmetry equations gives

\[
B=
\lambda(e_1e_2)
+\mu(e_2^2-e_1^2)
\]

(up to the scalar convention for symmetric products).

Therefore

\[
\boxed{
\dim\ker(m_A)=2
\qquad(rank(A)=2).
}
\]

The same dimension holds for every rank-two symmetric form by congruence invariance.

## 5. Ranks three and four

For

\[
A=e_1^2+e_2^2+e_3^2
\]

or a nondegenerate rank-four form, the symmetry equations force every entry of `B` to vanish.

Thus

\[
\boxed{
\dim\ker(m_A)=0
\qquad(rank(A)=3,4).
}
\]

## 6. Classification

For every nonzero `A in Sym^2 W`,

\[
\boxed{
\dim\ker(m_A)=
\begin{cases}
4,&rank(A)=1,\\
2,&rank(A)=2,\\
0,&rank(A)=3,4.
\end{cases}
}
\]

This can also be checked by the exact symbolic verifier `scripts/verify_ambient_rank_one_forcing.py`.

## 7. Consequence for the middle-extension construction

Let

\[
\xi\in H^1(T_D)\cong Sym^2W
\]

be a candidate surviving class for the final extension. If three independent defining Kodaira--Spencer classes

\[
e_1,e_2,e_3
\]

are to satisfy the **intrinsic** vanishings

\[
\xi\wedge e_a=0,
\]

then their ambient projections must also vanish. Hence

\[
e_a\in\ker(m_\xi).
\]

Three independent such classes require

\[
\dim\ker(m_\xi)\ge3.
\]

The classification above immediately gives

\[
\boxed{rank(\xi)=1.}
\]

Therefore

\[
\boxed{
\xi=v^2,
\qquad
e_a\in vW.
}
\]

The only remaining issue is the five-dimensional nonambient correction

\[
\tau_{D,v}:W\to Q_D.
\]

Three independent intrinsic annihilators exist if and only if

\[
\boxed{rank(\tau_{D,v})\le1.}
\]

Thus the quartic ramification test from `principal-theta-quartic-correction-map.md` is not one ansatz among many: it is forced by ambient representation theory for this final-extension architecture.
