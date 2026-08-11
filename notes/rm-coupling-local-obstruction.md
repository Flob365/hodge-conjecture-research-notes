# Local obstruction to coupling transverse RM divisor and curve blocks

> **Status.** This note proves a small but useful local no-go result for the coupling problem left by the smooth-isogeny RM scaffold. It shows that the obvious two-stage Postnikov coupling is impossible when the divisor and curve supports meet transversely.

## 1. Why a coupling is needed

The split scaffold

\[
E=S\oplus R[1]
\]

has the correct signed K-class

\[
[E]=[S]-[R]
\]

and `Ext^{<0}=0`, but the two mixed generalized directions

\[
P_{01}-qB_{01},
\qquad
P_{23}-qB_{23}
\]

cancel only after the Chern characters of `S` and `R[1]` are added. The Atiyah class of a direct sum is block diagonal, so this does not produce cancellation at the obstruction level.

The first natural repair is to replace the split object by a non-split object having

\[
\mathcal H^0(E)=S,
\qquad
\mathcal H^1(E)=R.
\]

Such a two-stage object is controlled by a Postnikov class

\[
\varepsilon\in\operatorname{Ext}^2(R,S).
\]

## 2. Transverse local model

At a transverse intersection point between a smooth divisor and a smooth complete-intersection curve, the completed local ring can be written

\[
R_0=k[[x_1,x_2,x_3,x_4]].
\]

Take

\[
S_0=R_0/(x_1),
\qquad
T_0=R_0/(x_2,x_3,x_4).
\]

The sequence

\[
x_2,x_3,x_4
\]

is a regular sequence on `S_0`. Resolve `T_0` by its length-three Koszul resolution and apply

\[
\operatorname{Hom}_{R_0}(-,S_0).
\]

The resulting dual Koszul complex is again the Koszul complex of the same regular sequence on `S_0`, shifted by three. Therefore

\[
\boxed{
\operatorname{Ext}^i_{R_0}(T_0,S_0)=0
\quad(i=0,1,2),
}
\]

while

\[
\boxed{
\operatorname{Ext}^3_{R_0}(T_0,S_0)
\cong
S_0/(x_2,x_3,x_4)
\cong k.
}
\]

Tensoring by local vector bundles on either support only adds matrix factors and does not create degree-two Ext.

## 3. Consequence for the RM scaffold

For the divisor block

\[
S=i_*V_D
\]

and cubic curve block

\[
R=j_*R_Z
\]

of `rm-smooth-isogeny-scaffold.md`, assume the supports meet transversely. Then the local contribution to

\[
\operatorname{Ext}^2(R,S)
\]

at every intersection point vanishes.

Hence the desired local Postnikov class cannot be supported at the transverse intersection points. In particular, the direct sum cannot be repaired merely by choosing generic nonzero two-extension parameters at those points: there are no such parameters.

This contrasts sharply with the `W_2` surface/surface model, where two codimension-two branches in a fourfold produce a nonzero local `Ext^2` Postnikov class.

## 4. Three surviving coupling mechanisms

The local calculation leaves three natural escape routes.

### A. Make the supports nontransverse or nested

If the cubic correction is represented by a curve lying inside the divisor support, the regular-sequence calculation changes and degree-two extensions can appear.

The geometric problem becomes: realize the required RM cubic class by a deformation-friendly curve or perfect curve class inside a divisor representing the `A` block.

### B. Insert a codimension-two mediator

Introduce an auxiliary surface block with net-zero K-theory contribution. A three-stage monad may carry nontrivial extension data even though the direct divisor--curve `Ext^2` vanishes.

The first test is purely local: classify minimal three-stage complexes over

\[
k[[x_1,x_2,x_3,x_4]]
\]

whose outer associated-graded pieces are `S_0` and `T_0`, whose total K-class is `[S_0]-[T_0]`, and whose negative self-Exts vanish.

### C. Apply a Fourier--Mukai transform before coupling

On an abelian fourfold, Fourier--Mukai transforms exchange cohomological degrees and can turn a cubic class into a divisor-type class. Coupling after such a transform may replace the transverse divisor/curve problem by a divisor/divisor or surface/surface problem with nonzero degree-two local Ext.

Because derived equivalences preserve perfectness and self-Ext groups, this route is especially attractive if the transformed Chern character remains inside the same secant-spin representation.

## 5. Immediate next calculation

The lowest-cost next experiment is Route B:

1. enumerate local codimension-two mediator modules;
2. compute the relevant `Ext^1` and `Ext^2` groups by Koszul resolutions;
3. search for a three-stage complex with K-class `[S_0]-[T_0]` and `Ext^{<0}=0`;
4. only after such a local model exists attempt a global geometric realization.

The transverse two-stage ansatz is now eliminated.