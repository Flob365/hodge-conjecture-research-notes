# A semihomogeneous Fourier resolution of the principal-theta `11`-bundle

> **Status.** This note gives an exact ambient resolution of `i_* Omega_D^2` for a smooth principal theta divisor and transforms it into a three-term semihomogeneous complex on the punctured dual abelian variety. It supplies a second concrete route to the `10 -> 11` Milestone A rank problem, independent of the Hessian-symbol bridge.

## 1. Ambient resolution of `i_* Omega_D^2`

Let `(X,Theta)` be a principally polarized abelian fourfold, let

\[
i:D=Theta\hookrightarrow X
\]

be smooth, and abbreviate `O_X(-kTheta)` by `O(-k)`.

The conormal sequence on `D` is

\[
0\to O_D(-1)\to O_D^{\oplus4}\to Omega_D^1\to0.
\]

Taking the second exterior power gives

\[
0\to O_D(-1)\otimes Omega_D^1
\to O_D^{\oplus6}
\to Omega_D^2\to0.
\]

Tensoring the conormal sequence by `O_D(-1)` gives

\[
0\to O_D(-2)
\to O_D(-1)^{\oplus4}
\to O_D(-1)\otimes Omega_D^1
\to0.
\]

Resolve every `O_D(-k)` by

\[
0\to O_X(-(k+1))\to O_X(-k)\to O_D(-k)\to0
\]

and take the two mapping cones. One obtains the exact locally free resolution on `X`

\[
\boxed{
0\to O(-3)
\to O(-2)^{\oplus5}
\to O(-1)^{\oplus10}
\to O_X^{\oplus6}
\to i_*Omega_D^2
\to0.
}
\]

Its K-class is

\[
[i_*Omega_D^2]
=6[O]-10[O(-1)]+5[O(-2)]-[O(-3)],
\]

which reproduces the Chern-character calculation used elsewhere in the repository.

## 2. Fourier transforms of the negative theta powers

Identify `X` with its dual via the principal polarization and let `Phi` be the normalized Poincare Fourier--Mukai transform.

Each anti-ample line bundle `O(-kTheta)` is WIT in degree four. Write

\[
E_k:=R^4Phi(O(-kTheta)).
\]

Then `E_k` is a simple semihomogeneous vector bundle with

\[
\boxed{
rank(E_k)=k^4,
\qquad
ch(E_k)=k^4\exp(\widehat\Theta/k).
}
\]

Thus

\[
rank(E_1)=1,
\qquad
rank(E_2)=16,
\qquad
rank(E_3)=81.
\]

Also

\[
Phi(O_X)=O_{\widehat 0}[-4].
\]

## 3. Restrict to the punctured dual

Put

\[
U=\widehat X\setminus\{0\}.
\]

The Fourier transform of the `O_X^6` term disappears after restriction to `U`. The ambient resolution therefore gives the three-term complex

\[
\boxed{
E_3
\longrightarrow
E_2^{\oplus5}
\longrightarrow
E_1^{\oplus10}
}
\]

on `U`.

At a point `P in U`, this is the Fourier transform of the complex computing

\[
R\Gamma(D,Omega_D^2\otimes P).
\]

For nontrivial general `P`, the only cohomology is

\[
H^1(D,Omega_D^2\otimes P),
\qquad \dim=11.
\]

The fiber ranks of the transformed complex are

\[
81\longrightarrow80\longrightarrow10.
\]

Consequently the maps have generic ranks `70` and `10`, and the first kernel has rank `11`. If

\[
G=R^1Phi(i_*Omega_D^2)|_U,
\]

then, up to the harmless overall shift convention,

\[
\boxed{
0\to G
\to E_3
\to E_2^{\oplus5}
\to E_1^{\oplus10}
\to0
}
\]

is exact on a dense open subset, and after removing the determinantal loci one may regard it as an exact resolution of `G` on that open set.

Its K-class is

\[
[G]=[E_3]-5[E_2]+10[E_1],
\]

so

\[
ch(G)
=81e^{x/3}-80e^{x/2}+10e^x,
\]

which is the same formula as

\[
10e^x-80e^{x/2}+81e^{x/3}
\]

in `rm-principal-theta-fourier-rank.md`.

## 4. Relation to the Kodaira--Spencer map

The Fourier transform of `i_*K_D` restricts on `U` to the line bundle

\[
O_U(-\widehat\Theta).
\]

Cup/contraction by a deformation class therefore packages into a morphism

\[
\kappa:
H^1(T_D)\otimes O_U(-\widehat\Theta)
\longrightarrow G.
\]

Since the relevant ppav deformation space has dimension ten,

\[
\boxed{
\kappa:O_U(-\widehat\Theta)^{\oplus10}\to G,
\qquad rank(G)=11.
}
\]

The semihomogeneous resolution above gives a purely algebraic way to study these ten sections: lift them to `E_3`, impose the syzygy condition for the map

\[
E_3\to E_2^{\oplus5},
\]

and compute a `3 x 3` minor (or the full `10 x 10` wedge) there.

This avoids taking a second-order limit at the origin of `Pic^0`.

## 5. Two routes to Milestone A are now available

### Route A: Hessian symbol

Use the translated-theta expansion, the heat equation, and the twisted Jacobian quotient to identify the first nonzero symbol of `kappa` with the second fundamental form of the Gauss map. De Jong's theorem then supplies rank three away from the ramification divisor.

### Route B: semihomogeneous syzygies

Use the exact transformed complex

\[
E_3\to E_2^5\to E_1^{10}
\]

to compute `kappa` as a syzygy morphism. A single nonzero `3 x 3` minor proves Milestone A; a nonzero `10 x 10` wedge proves the strongest expected generic rank.

Route B is particularly suitable for a computer-assisted theta-function experiment because all three ambient bundles are semihomogeneous and their ranks and Chern characters are explicit.

## 6. Caveat at the origin

The omitted term `O_{0}^{\oplus6}` matters at the origin of the dual abelian variety and records the jump in the untwisted Hodge groups. Statements above are therefore made on the punctured dual or on a dense open subset.

Any attempt to extend the resolution globally across the origin must keep the origin-supported cohomology sheaves; dropping them would give incorrect fourth Chern classes and Euler characteristics.
