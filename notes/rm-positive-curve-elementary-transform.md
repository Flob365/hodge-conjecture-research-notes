# A coupled coherent RM secant sheaf from positive curve classes

> **Status.** This note upgrades the split RM perfect-complex scaffold to a genuinely coupled coherent sheaf. The key new ingredient is a positive codimension-three identity in the real-multiplication plane. After passing to a multiplication isogeny so that the relevant linear systems are mobile, the correcting cubic class can be represented by smooth curves contained in one smooth divisor. An elementary transform then produces a coherent sheaf with Chern character an explicit integral multiple of Markman's RM secant class. The two generalized Atiyah directions are still not proved to vanish.

## 1. RM notation

Let

\[
A=g^*\Theta,
\qquad
C=(g^{-1})^*\Theta
\]

on a principally polarized abelian fourfold with real multiplication as in Markman's genus-4 example. Over `R`, diagonalize the real multiplication and write

\[
A=\rho u+\rho^{-1}v,
\qquad
C=\rho^{-1}u+\rho v,
\]

where

\[
u^3=v^3=0,
\qquad
\rho>1.
\]

Replacing the two real embeddings if necessary achieves `rho>1`. The nontriviality assumption `f^2 != 1` is exactly what excludes `rho=1`.

Define a third ample RM divisor class

\[
H=(g^{-2})^*\Theta
=\rho^{-2}u+\rho^2v.
\]

Finally put

\[
T=\rho^2+\rho^{-2}.
\]

This is invariant under exchange of the two real embeddings and hence belongs to `Q`. If the RM unit lies in the relevant endomorphism order, then `T` is an integer trace; rationality is enough for the construction after clearing denominators.

Since `rho != 1`,

\[
T>2.
\]

## 2. The positive cubic identity

In the basis

\[
\{u^2v,uv^2\}
\]

of the RM-generated cubic plane, direct expansion gives

\[
C^3=3\rho^{-1}u^2v+3\rho uv^2,
\]

\[
AC^2=(2\rho+\rho^{-3})u^2v
+(\rho^3+2\rho^{-1})uv^2,
\]

and

\[
AH^2=(2\rho+\rho^{-5})u^2v
+(\rho^5+2\rho^{-1})uv^2.
\]

Solving the resulting two-by-two linear system yields

\[
\boxed{
C^3
=\frac{3(T-2)}{\Delta}\,AC^2
+\frac{3}{\Delta}\,AH^2,
}
\]

where

\[
\boxed{\Delta=2T^2-2T-1.}
\]

Equivalently,

\[
\boxed{
\Delta C^3
=3(T-2)AC^2+3AH^2.
}
\]

Every coefficient is positive because `T>2`, and `Delta>0`.

This positivity is the crucial point. The earlier identity

\[
C^3=\frac{1}{T}(3AC^2-A^3)
\]

has a negative coefficient and therefore cannot directly be realized by a quotient supported on effective curves. Passing one step further along the RM orbit, from `C=g^{-1*}Theta` to `H=g^{-2*}Theta`, moves the second effective ray past `C^3` and removes the negative sign.

## 3. Geometric realization after an isogeny

To avoid basepoint and singular-theta issues, pass to a multiplication isogeny

\[
\pi=[m]:X\to X
\]

with `m` large enough that the pullbacks of `A,C,H` have mobile, sufficiently positive linear systems. The cubic identity is preserved by pullback, so we suppress tildes below.

Choose a smooth divisor

\[
D\in|A|.
\]

Choose general smooth divisors in the classes `C` and `H`. Their intersections with `D` give smooth complete-intersection curves of the two types

\[
Z_C=D\cap C_1\cap C_2,
\qquad
[Z_C]=AC^2,
\]

and

\[
Z_H=D\cap H_1\cap H_2,
\qquad
[Z_H]=AH^2.
\]

General choices can be made pairwise disjoint because two curves in the threefold `D` have negative expected intersection dimension; only finitely many curves are needed.

If `T` and `Delta` are merely rational, multiply the entire identity by a common positive denominator. For readability assume from now on that the displayed multiplicities are integral; this is automatic in the usual integral-unit situation after one global scaling.

## 4. Pure curve sheaves

For any smooth curve `j:Z -> X`,

\[
\operatorname{ch}(j_*\mathcal O_Z)
=[Z]+\chi(\mathcal O_Z)[pt],
\]

while

\[
\operatorname{ch}(j_*K_Z)
=[Z]+\chi(K_Z)[pt].
\]

Serre duality gives

\[
\chi(K_Z)=-\chi(\mathcal O_Z).
\]

Therefore

\[
\boxed{
R_Z:=j_*(\mathcal O_Z\oplus K_Z)
\quad\text{satisfies}\quad
\operatorname{ch}(R_Z)=2[Z].
}
\]

There is no point-class contamination.

Take

- `3q(T-2)` pairwise general curves of type `Z_C`;
- `3q` pairwise general curves of type `Z_H`.

Let `Q` be the direct sum of their corresponding `R_Z`. The positive cubic identity gives

\[
\boxed{
\operatorname{ch}(Q)
=2q\Delta C^3.
}
\]

## 5. The divisor block

For the smooth divisor `i:D -> X`, use the rank-12 bundle from
[`rm-smooth-isogeny-scaffold.md`](rm-smooth-isogeny-scaffold.md):

\[
V_D=
\mathcal O_D^{\oplus3}
\oplus\Omega_D^1
\oplus\Omega_D^2
\oplus K_D^{\oplus3}.
\]

Grothendieck--Riemann--Roch gives

\[
\operatorname{ch}(i_*V_D)=12A.
\]

Set

\[
S=(i_*V_D)^{\oplus\Delta}.
\]

Then

\[
\boxed{
\operatorname{ch}(S)=12\Delta A.
}
\]

## 6. A surjection onto every correcting curve

Because each correcting curve is contained in `D`, a sheaf map from `i_*V_D` to `R_Z` is the same as the corresponding map on `D`.

For a complete-intersection curve

\[
Z=D\cap L_1\cap L_2,
\]

adjunction gives

\[
K_Z=K_D|_Z\otimes L_1|_Z\otimes L_2|_Z.
\]

The three trivial summands in `V_D` give an immediate quotient

\[
\mathcal O_D^{\oplus3}|_Z\twoheadrightarrow\mathcal O_Z.
\]

The three `K_D` summands give a quotient onto `K_Z` as soon as the line bundle

\[
L_1|_Z\otimes L_2|_Z
\]

is globally generated. After the multiplication-isogeny regularization this can be arranged; on a curve, two suitably chosen sections of a globally generated line bundle already suffice to have no common zero.

Hence one can choose a surjection

\[
V_D|_Z\twoheadrightarrow
\mathcal O_Z\oplus K_Z.
\]

Since the finitely many correcting curves can be chosen disjoint, these quotient maps combine without local rank competition into a global surjection

\[
\boxed{
S\twoheadrightarrow Q.
}
\]

## 7. The coupled coherent sheaf

Define

\[
\boxed{
E:=\ker(S\twoheadrightarrow Q).
}
\]

Then `E` is a coherent sheaf on `X`, supported on `D`. In particular

\[
\operatorname{Ext}^{<0}(E,E)=0
\]

automatically.

Its Chern character is

\[
\begin{aligned}
\operatorname{ch}(E)
&=12\Delta A-2q\Delta C^3\\
&=12\Delta\left(A-\frac q6C^3\right).
\end{aligned}
\]

Thus

\[
\boxed{
\operatorname{ch}(E)=12\Delta\beta'.
}
\]

This is a genuine **coupled coherent representative** of Markman's real-multiplication secant ray. Unlike the split scaffold `S direct-sum Q[1]`, the divisor and cubic correction now interact through one elementary-transform exact sequence.

## 8. Why this improves the deformation problem

The construction uses only divisor classes in the RM orbit

\[
A=g^*\Theta,
\quad
C=g^{-1*}\Theta,
\quad
H=g^{-2*}\Theta,
\]

together with smooth relative divisors, complete intersections, natural canonical/cotangent bundles, and quotient maps.

These ingredients are available over the RM PEL deformation locus after the same isogeny regularization. Consequently there is a direct geometric route to deforming `E` along the six ordinary RM tangent directions

\[
\operatorname{Sym}^2(U_1)\oplus\operatorname{Sym}^2(U_2).
\]

Making this relative construction fully formal should put those six directions in `ker(at_E)`.

Combining this with the already proved rank-20 Chern-action calculation would constrain the Atiyah rank to

\[
20\le\operatorname{rank}(at_E)\le22.
\]

Thus only the two mixed generalized directions remain undecided.

## 9. Local elementary-transform model

At a smooth point of one correcting curve, work inside the smooth threefold `D` with

\[
A_{loc}=k[[x,y,z]],
\qquad
Z:(y,z).
\]

A local surjection from a free divisor bundle to a rank-one curve summand can be reduced to

\[
A_{loc}\twoheadrightarrow A_{loc}/(y,z),
\]

whose kernel is the ideal `(y,z)`.

Thus locally the elementary transform is built from copies of the codimension-two ideal

\[
I_Z=(y,z)
\]

plus free summands. This gives a very small explicit resolution

\[
0\to A_{loc}
\xrightarrow{(-z,y)}
A_{loc}^{\oplus2}
\to I_Z\to0.
\]

This is the correct local algebra for the next Atiyah calculation. In particular the remaining generalized obstruction problem has been reduced from Markman's large global gluing sheaf to the behavior of an elementary transform along smooth codimension-two complete intersections inside one divisor.

## 10. Next falsifiable milestone

Prove, for the elementary-transform sheaf `E`, that the two vectors

\[
B_+-q^{-1}P_+,
\qquad
B_--q^{-1}P_-
\]

lie in `ker(at_E)`.

A direct local-to-global calculation can now use:

1. the two-term resolution of `I_Z` above;
2. the conormal sequences of `D` and the correcting curves;
3. the exact sequence `0 -> E -> S -> Q -> 0`;
4. the known fact that the Chern images of the two component obstructions cancel exactly.

If both classes vanish, then `ker(at_E)` has dimension at least eight. Since it is already contained in the eight-dimensional Chern-action kernel, equality follows and Markman's requested injectivity of semiregularity on `im(at_E)` is obtained for this new `F_2` candidate.
