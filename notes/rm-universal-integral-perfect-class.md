# A universal integral perfect realization of the RM secant class

> **Status.** This note gives an exact integral K-theory realization of a fixed multiple of Markman's real-multiplication secant class using only line bundles and codimension-three complete intersections. It works on any principally polarized abelian fourfold carrying the relevant automorphism `g`; it does not use a Jacobian, `W_2`, or an auxiliary effective correcting curve. The resulting obvious complex is decomposable, so this is not yet a semiregular/simple-object construction.

## 1. Setup

Let `(X,Theta)` be a principally polarized abelian fourfold and let `g` be an automorphism as in Markman's real-multiplication example. Put

\[
x=g^*\Theta,
\qquad
y=(g^{-1})^*\Theta,
\]

and let `q` be the positive integer occurring in

\[
\beta'=x-\frac q6y^3.
\]

Choose line bundles `L,M` with

\[
c_1(L)=x,
\qquad c_1(M)=y.
\]

Because `dim X=4`, all power-series identities below are truncated after cohomological degree eight, i.e. after fourth powers of divisor classes.

## 2. A cancellation identity for a codimension-three complete intersection

Let `Z_x` be a transverse intersection of three general translates of a divisor in the polarization class `x`. Its Koszul class gives

\[
\operatorname{ch}(\mathcal O_{Z_x})=(1-e^{-x})^3.
\]

For an integer `k`, set

\[
B^{(k)}_{3,x}
:=\operatorname{ch}(\mathcal O_{Z_x}\otimes L^k)
=e^{kx}(1-e^{-x})^3.
\]

Modulo `x^5`,

\[
(1-e^{-x})^3=x^3-\frac32x^4,
\]

so

\[
B^{(1)}_{3,x}=x^3-\frac12x^4,
\qquad
B^{(2)}_{3,x}=x^3+\frac12x^4.
\]

Therefore

\[
\boxed{B^{(1)}_{3,x}+B^{(2)}_{3,x}=2x^3.}
\]

The identical statement holds with `x,L,Z_x` replaced by `y,M,Z_y`.

This symmetric pair of twists is useful because its point-class contribution cancels exactly.

## 3. The exact integral RM identity

The odd part of the exponential satisfies

\[
e^x-e^{-x}=2x+\frac13x^3.
\]

Hence

\[
6(e^x-e^{-x})=12x+2x^3.
\]

Subtract the symmetric `x` complete-intersection pair and `q` copies of the analogous `y` pair:

\[
\begin{aligned}
&6(e^x-e^{-x})
-\bigl(B^{(1)}_{3,x}+B^{(2)}_{3,x}\bigr)
-q\bigl(B^{(1)}_{3,y}+B^{(2)}_{3,y}\bigr)\\
&=12x+2x^3-2x^3-2qy^3\\
&=12x-2qy^3\\
&=12\left(x-\frac q6y^3\right).
\end{aligned}
\]

Thus

\[
\boxed{
12\beta'
=6\bigl(\operatorname{ch}(L)-\operatorname{ch}(L^{-1})\bigr)
-\sum_{k=1}^{2}\operatorname{ch}(\mathcal O_{Z_x}\otimes L^k)
-q\sum_{k=1}^{2}\operatorname{ch}(\mathcal O_{Z_y}\otimes M^k).
}
\]

Equivalently, the integral K-class

\[
\boxed{
\begin{aligned}
V_{RM}:={}&6([L]-[L^{-1}])\\
&-[\mathcal O_{Z_x}\otimes L]
-[\mathcal O_{Z_x}\otimes L^2]\\
&-q[\mathcal O_{Z_y}\otimes M]
-q[\mathcal O_{Z_y}\otimes M^2]
\end{aligned}
}
\]

satisfies

\[
\operatorname{ch}(V_{RM})=12\beta'.
\]

Every term is represented by a perfect complex because `X` is smooth. Therefore `12 beta'` has an explicit integral perfect representative on any such RM fourfold.

## 4. Why this is different from the Jacobian construction

Markman's Example 11.2.7 realizes an integral multiple of `beta'` by gluing translated copies of a Jacobian-specific secant sheaf to a specially chosen correcting curve. That is substantially stronger because the result is a simple coherent sheaf.

The identity above is weaker at the object level but stronger in portability:

- it does not require `X` to be a Jacobian;
- it does not require a minimal class surface `W_2(C)`;
- it does not require the existence of one effective curve representing a mixed class such as `d x^3-q y^3`;
- all ingredients are line bundles, translates of ample divisors, Koszul complexes, and direct sums/shifts.

Thus K-theoretic realization of the RM secant direction is not the bottleneck. **Coupling and semiregularity are the bottleneck.**

## 5. The obvious perfect complex is not enough

One may realize the signed K-class by the direct sum of the positive terms in even degree and the negative terms in odd degree. This gives a bounded perfect complex with the desired Chern character, but it is highly decomposable and has many idempotents.

Consequently it is not a candidate for the simplicity hypotheses used in deformation arguments.

The correct next question is whether the same K-class can be represented by a genuinely coupled monad whose differentials mix the `x`-line-bundle block with the `x^3` and `y^3` Koszul blocks.

## 6. A more economical determinantal candidate

There is a second identity suggesting such a coupling.

Take a generically injective map

\[
S:L^{-1\,\oplus3}\longrightarrow L^{\oplus3}
\]

and let

\[
F_0=\operatorname{coker}(S).
\]

In K-theory,

\[
[F_0]=3([L]-[L^{-1}]),
\]

so

\[
\operatorname{ch}(F_0)=6x+x^3.
\]

If one can construct a pure one-dimensional quotient

\[
F_0\twoheadrightarrow Q
\]

with

\[
\operatorname{ch}(Q)=x^3+qy^3
\]

and no degree-eight contribution, then its kernel `E` satisfies

\[
\boxed{
\operatorname{ch}(E)=6x-qy^3=6\beta'.
}
\]

This would cut the scaling factor from `12` to `6` and, more importantly, would put the cancellation into an exact sequence rather than a formal signed direct sum.

The determinant of `S` is a section of `L^6`; thus the support of `F_0` is a determinantal divisor in `|6x|`. The unresolved geometric condition is to choose `S` so that its determinantal divisor contains suitable complete-intersection curves carrying the quotient `Q`, while retaining simplicity/genericity of the rank-one torsion sheaf `F_0`.

This is a falsifiable construction problem, not an existence claim.

## 7. Relation to the rank-20 kernel calculation

Any object with Chern character a nonzero multiple of `beta'` has the same Chern-action kernel computed in [`rm-semiregularity-kernel.md`](rm-semiregularity-kernel.md): an eight-dimensional subspace of `HT^2(X)`.

The universal K-class therefore does not solve the Atiyah problem by itself. Its value is that the six ordinary RM directions are no longer obstructed by the need to deform a Jacobian-specific `W_2` construction at the level of ingredients. Line bundles and relative Koszul complete intersections are available in families as soon as the relevant polarization classes remain algebraic.

The remaining hard target is still to build the differentials so that the two mixed `B`-field/Poisson directions are killed by the Atiyah map rather than merely by the Chern action.

## 8. Concrete next milestones

1. **Coupled monad test.** Build a finite quiver/monad with K-class `V_RM` and calculate `Hom` and negative `Ext` for one explicit RM fourfold model.
2. **Determinantal quotient test.** For the `3 x 3` map `S`, determine whether a determinantal divisor in `|6x|` can be forced to contain the required `x^3` and `y^3` curves while remaining integral.
3. **Atiyah cancellation test.** Compute the image of the two mixed directions in the deformation complex of either coupled construction. Reject the model unless the two classes vanish before applying semiregularity.

The verifier [`scripts/verify_rm_universal_integral_class.py`](../scripts/verify_rm_universal_integral_class.py) checks all truncated Chern-character identities exactly over the rationals.
