# Two-torsion parity: the rigorous `7+4` splitting

> **Status.** This note proves the inversion-parity decomposition behind the current two-torsion Milestone-B strategy. For a nonzero two-torsion twist, `H^0(2Theta tensor P)` splits as `8+8` under inversion; after quotienting by the five gauge directions, the twisted Hodge group splits as `7+4`. The covariant ppav Kodaira--Spencer image lies in the seven-dimensional summand, so `rank(rho_P) <= 7`. Numerical experiments strongly indicate equality on a generic RM point, but surjectivity onto the seven-dimensional summand is not proved here.

## 1. Symmetric level-two line bundle

Let `(X,Theta)` be a principally polarized abelian fourfold, choose a symmetric theta line bundle

\[
L=O_X(Theta),
\]

and let

\[
0\ne P\in Pic^0(X)[2].
\]

Then

\[
M=L^{\otimes2}\otimes P
\]

is symmetric under inversion

\[
i=[-1]_X.
\]

Its space of sections has dimension

\[
h^0(X,M)=2^4=16.
\]

Fix the symmetric linearization induced from `L` and `P`.

## 2. Lefschetz trace of inversion is zero

The fixed points of `i` are the 256 points of `X[2]`. At every fixed point the differential of `i` is `-1` on the four-dimensional tangent space, so the local denominator in the holomorphic Lefschetz formula is

\[
det(1-di)=2^4=16.
\]

For `L^2`, the fiber sign of the symmetric linearization on a two-torsion point is the square of the sign for `L`, hence equals `+1`. Twisting by the nontrivial two-torsion line bundle `P` multiplies that fiber sign by the nontrivial Weil character

\[
\chi_P:X[2]\to\{\pm1\}.
\]

Therefore

\[
Tr\bigl(i|H^0(X,M)\bigr)
=\frac1{16}\sum_{x\in X[2]}\chi_P(x).
\]

Because `P` is nontrivial, `chi_P` is a nontrivial character of the finite group `X[2]`, and hence

\[
\sum_{x\in X[2]}\chi_P(x)=0.
\]

Thus

\[
\boxed{Tr(i|H^0(M))=0.}
\]

Since the total dimension is 16, the two inversion eigenspaces have equal dimensions:

\[
\boxed{
H^0(M)=H^0(M)^+\oplus H^0(M)^-,
\qquad
\dim H^0(M)^+=\dim H^0(M)^-=8.
}
\]

This is the level-two special case of the general symmetric theta-structure eigenspace formulas.

## 3. Parity of the five gauge directions

Take the theta section `theta` to be even; this is the standard zero-characteristic symmetric normalization. Let `theta_P` be the horizontal theta section representing `L tensor P`, with inversion parity

\[
theta_P(-z)=\varepsilon\,theta_P(z),
\qquad \varepsilon\in\{\pm1\}.
\]

The five-dimensional gauge space in the twisted Jacobian description of

\[
H^1(D,\Omega_D^2\otimes P),
\qquad D=Theta,
\]
is generated in `H^0(M)` by

\[
theta\,theta_P
\]
and the four first Wronskians

\[
W_i=theta\,(theta_P)_i-theta_P\,theta_i.
\]

Their parities are immediate:

\[
parity(theta\,theta_P)=\varepsilon,
\]

while differentiation reverses parity, so

\[
parity(W_i)=-\varepsilon.
\]

For smooth `D` and nontrivial `P`, these five gauge sections are independent: modulo `theta theta_P`, restriction to `D` sends

\[
W_i|_D=-theta_P\,theta_i|_D,
\]

and the four canonical derivative sections `theta_i|_D` are independent.

Hence quotienting the `8+8` section space by the gauge directions gives

\[
\boxed{
H^1(D,\Omega_D^2\otimes P)
=H_7\oplus H_4,
}

where

\[
\dim H_7=8-1=7
\]
is the quotient eigenspace of parity `epsilon`, while

\[
\dim H_4=8-4=4
\]
is the quotient eigenspace of parity `-epsilon`.

## 4. The correct period covariant has parity `epsilon`

For a polarized period deformation

\[
Q\in Sym^2\mathbf C^4,
\]
the covariant second transvectant representing the first twisted Hodge block is, up to the global heat-equation normalization,

\[
U_{Q,P}
=
\theta_P\,tr(Q\,Hess\,theta)
-2(\nabla theta)^tQ\nabla theta_P
+\theta\,tr(Q\,Hess\,theta_P).
\]

Each term has parity `epsilon`:

- `theta_P` has parity `epsilon` and `Hess(theta)` is even;
- `nabla theta` is odd and `nabla theta_P` has parity `-epsilon`, so their product has parity `epsilon`;
- `theta` is even and `Hess(theta_P)` again has parity `epsilon`.

Therefore the class of `U_QP` in the five-dimensional gauge quotient belongs entirely to `H_7`.

Consequently

\[
\boxed{
Im(rho_P)\subseteq H_7,
\qquad
rank(rho_P)\le7.
}

This upper bound is exact and representation-theoretic; it does not depend on numerical theta-series experiments.

## 5. The central IVHS preserves the `7+4` blocks

The middle twisted Hodge operator

\[
T_Q:
H^1(\Omega_D^2\otimes P)
\to
H^2(\Omega_D^1\otimes P)
\]
is induced by a ppav deformation tensor `Q`, which is invariant under inversion. Hence `T_Q` commutes with the inversion action.

At `P=P^{-1}`, Serre duality identifies the target with the dual of the source compatibly with inversion. Therefore

\[
\boxed{
T_Q=B_Q\oplus D_Q,
}

with

\[
B_Q:H_7\to H_7^*,
\qquad
D_Q:H_4\to H_4^*.
\]

The polarization makes both blocks symmetric after fixing the Serre-duality convention.

This is the rigorous origin of the current `7 x 7` visible block and `4 x 4` normal block.

## 6. Integrability and invisible deformation directions

The Higgs-field integrability relation gives

\[
\boxed{
T_Q\,rho_P(R)=T_R\,rho_P(Q)
}

for all polarized deformation directions `Q,R`.

Let

\[
W=ker(rho_P).
\]

For `w in W` and any `R`,

\[
T_w\,rho_P(R)=0.
\]

Thus `T_w` annihilates `Im(rho_P)`. If the expected generic equality

\[
Im(rho_P)=H_7
\]
holds, then every invisible direction acts only on the four-dimensional normal block:

\[
\boxed{
B_w=0,
\qquad
T_w=0\oplus D_w.
}
\]

Since the source deformation space has dimension ten and `H_7` dimension seven, equality would also give

\[
\boxed{dim W=3.}
\]

This is exactly the numerical `7+3` deformation splitting observed in the explicit real-multiplication experiment.

## 7. What remains to prove

The parity theorem reduces the first remaining statement to one clean surjectivity problem:

> **Two-torsion rank lemma.** On a general smooth RM principal theta fourfold and for a suitable nonzero two-torsion `P`, the covariant map
> \[
> rho_P:Sym^2\mathbf C^4\to H_7
> \]
> is surjective.

Equivalently,

\[
rank(rho_P)=7.
\]

Once this is proved, `W=ker rho_P` is exactly three-dimensional and the central Milestone-B problem splits canonically into a `7 x 7` visible family parametrized by `V/W` and a `4 x 4` normal net parametrized by `W`.

## References

- H. Lange, Ch. Birkenhake, *Symmetric Theta-Structures*, Manuscripta Math. 70 (1991), 67--92, for the general inversion-eigenspace formalism for symmetric line bundles and theta structures.
- The holomorphic Lefschetz calculation above is sufficient for the particular `8+8` statement needed here.