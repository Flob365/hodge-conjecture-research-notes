# Determinantal forcing for Milestone B

> **Status.** This note isolates a purely projective-geometric mechanism which would force Milestone B once one lower-rank exclusion is proved. It is rigorous as a conditional statement. The missing input is the **Rank-8 lemma**: every nonzero central twisted-IVHS operator `T_Q` must have rank at least eight.

## 1. Linear system of central operators

Let `D=Theta` be a smooth principal theta divisor in an abelian fourfold and choose a nontrivial two-torsion twist `P` in the Milestone-A open set.

Put

\[
H_P:=H^1(D,\Omega_D^2\otimes P),
\qquad \dim H_P=11.
\]

Serre duality and `P=P^{-1}` identify

\[
H^2(D,\Omega_D^1\otimes P)\cong H_P^*.
\]

For a polarized deformation

\[
Q\in V:=T_{[X,\Theta]}\mathcal A_4,
\qquad \dim V=10,
\]

the central block of the twisted IVHS is a symmetric map

\[
T_Q:H_P\longrightarrow H_P^*.
\]

Thus there is a linear map

\[
\boxed{
T:V\longrightarrow Sym^2H_P^*.
}
\]

Milestone A gives an injective first Hodge block

\[
\rho_P:V\hookrightarrow H_P.
\]

Write

\[
H:=\rho_P(V)\subset H_P,
\qquad \dim H=10.
\]

So `H` is a hyperplane.

## 2. The incidence variety with a three-plane in the kernel

Let `n=11`. In

\[
\mathbf P(Sym^2H_P^*)\cong\mathbf P^{65}
\]
consider the incidence variety

\[
Y_H=
\left\{
[A]:\exists K\in Gr(3,H)\text{ with }K\subseteq\ker A
\right\}.
\]

For a fixed `K`, a symmetric form vanishing on `K` is a symmetric form on the eight-dimensional quotient `H_P/K`. Hence the fiber over `K` is

\[
\mathbf P(Sym^2(H_P/K)^*)\cong\mathbf P^{35}.
\]

Since

\[
\dim Gr(3,H)=3(10-3)=21,
\]
we obtain

\[
\boxed{
\dim Y_H=21+35=56.
}
\]

Therefore

\[
\boxed{
codim_{\mathbf P^{65}}Y_H=9.}
\]

The map from the projective bundle over `Gr(3,H)` is proper, so `Y_H` is closed.

## 3. Every projective `P^9` meets `Y_H`

Assume the central map `T` is injective. Then

\[
L:=\mathbf P(T(V))\cong\mathbf P^9
\subset\mathbf P^{65}.
\]

The projective dimension theorem gives

\[
\dim L+\dim Y_H=9+56=65.
\]

Hence

\[
\boxed{L\cap Y_H\neq\varnothing.}
\]

Thus there is a nonzero deformation direction `Q` such that

\[
T_Q
\]
has a three-dimensional kernel subspace contained in `H=im(rho_P)`.

Since the existence of such a `K` forces

\[
rank(T_Q)\le8,
\]
projective geometry alone gives a rank-at-most-eight candidate.

## 4. Why rank seven is the only remaining danger

The projective symmetric determinantal variety

\[
\Sigma_{\le r}
=\{[A]:rank(A)\le r\}
\subset\mathbf P(Sym^2\mathbf C^{11})
\]
has codimension

\[
\binom{11-r+1}{2}.
\]

For `r=7`,

\[
\boxed{codim\Sigma_{\le7}=\binom52=10,}
\]
so

\[
\dim\Sigma_{\le7}=55.
\]

Notice that `Sigma_{<=7}` is contained in `Y_H`: a kernel of dimension at least four meets any hyperplane `H` in dimension at least three.

Therefore the boundary

\[
Y_H\setminus\{rank=8,\ ker\subset H\}
\]
contains the full rank-at-most-seven locus.

A **general** projective `P^9` in `P^65` avoids `Sigma_{<=7}` because

\[
9+55=64<65.
\]

For our geometric `P^9`, however, this avoidance must be proved rather than assumed.

## 5. Conditional solution of Milestone B

Suppose the following two statements hold:

1. the central map
   \[
   T:V\to Sym^2H_P^*
   \]
   is injective;
2. every nonzero `Q` satisfies
   \[
   \boxed{rank(T_Q)\ge8.}
   \]

Then Section 3 produces a nonzero `Q_0` with `rank(T_Q0)<=8` and with a three-plane

\[
K\subset H\cap ker(T_{Q_0}).
\]

The lower bound forces

\[
rank(T_{Q_0})=8,
\qquad \dim ker(T_{Q_0})=3.
\]

Hence necessarily

\[
ker(T_{Q_0})=K\subset H.
\]

Since `rho_P:V -> H` is an isomorphism onto `H`, choose unique independent

\[
Q_1,Q_2,Q_3\in V
\]
with

\[
rho_P(\langle Q_1,Q_2,Q_3\rangle)=K.
\]

By symmetry of `T_Q0`, its image is the annihilator of `K`, so the complex

\[
\boxed{
\mathbf C^3
\xrightarrow{\rho_P}
H_P
\xrightarrow{T_{Q_0}}
H_P^*
\xrightarrow{\rho_P^*}
(\mathbf C^3)^*
}
\]

is exact.

This is precisely the cohomological exactness required for the final extension bundle `W_D`. Therefore **Milestone B follows**.

## 6. The new decisive lemma

The remaining target is now exceptionally sharp:

> **Rank-8 lemma.** For a smooth principal theta divisor `D` and a suitable nontrivial two-torsion `P`, every nonzero polarized deformation `Q` has
> \[
> rank(T_Q)\ge8.
> \]

This lemma also implies injectivity of `T`, so it subsumes both missing assumptions in Section 5.

## 7. Gauss-cover form of the Rank-8 lemma

By `rm-gauss-pushforward-splitting.md`, the finite Gauss map

\[
\gamma:D\to P^3
\]
satisfies

\[
\gamma_*P
\cong
O(-1)\oplus O(-2)^{11}\oplus O(-3)^{11}\oplus O(-4).
\]

The source and target of `T_Q` are exactly the multiplicity spaces of the eleven `O(-2)` and eleven `O(-3)` summands.

Thus the Rank-8 lemma can be attacked as a statement about the infinitesimal variation of the middle two summands of this finite Gorenstein Gauss-cover module. The rank-one candidate `Q=v^2` remains particularly important: proving

\[
rank(T_{v^2})=8
\]
for one generic `v` would already supply the desired point if its kernel lies in `H`; the uniform Rank-8 lemma would give the clean projective-forcing proof above.