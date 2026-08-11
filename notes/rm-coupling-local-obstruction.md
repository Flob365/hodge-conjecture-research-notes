# Local obstruction to coupling transverse RM divisor and curve blocks

> **Status.** This note proves a local no-go result for the coupling problem left by the smooth-isogeny RM scaffold. It shows that **any two-block filtered object with the required opposite K-theory signs is locally split** when the divisor and curve supports meet transversely.

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

The first natural repair is a non-split filtered object whose associated graded pieces are a divisor sheaf and an odd shift of a curve sheaf. The odd relative shift is forced by the sign

\[
[S]-[R].
\]

## 2. Transverse local model

At a transverse intersection point between a smooth divisor and a smooth complete-intersection curve, write

\[
R_0=k[[x_1,x_2,x_3,x_4]],
\]

\[
S_0=R_0/(x_1),
\qquad
T_0=R_0/(x_2,x_3,x_4).
\]

### Ext from the curve to the divisor

The sequence `x_2,x_3,x_4` is regular on `S_0`. Resolving `T_0` by its length-three Koszul resolution and applying `Hom(-,S_0)` gives

\[
\boxed{
\operatorname{Ext}^i_{R_0}(T_0,S_0)=0
\quad(i=0,1,2),
}
\]

and

\[
\boxed{
\operatorname{Ext}^3_{R_0}(T_0,S_0)\cong k.
}
\]

### Ext from the divisor to the curve

Resolve `S_0` by

\[
0\to R_0\xrightarrow{x_1}R_0\to S_0\to0.
\]

The element `x_1` is a nonzerodivisor on

\[
T_0\cong k[[x_1]].
\]

Hence

\[
\boxed{
\operatorname{Ext}^0_{R_0}(S_0,T_0)=0,
\qquad
\operatorname{Ext}^1_{R_0}(S_0,T_0)\cong k,
}
\]

and

\[
\operatorname{Ext}^i_{R_0}(S_0,T_0)=0
\quad(i\ge2).
\]

Thus the only local cross-Ext degrees are **odd**: degree `1` in one direction and degree `3` in the other.

Tensoring by local vector bundles only adds matrix factors and does not change this parity statement.

## 3. The parity obstruction

Take an odd integer `n`. The object `T_0[n]` has the opposite K-theory sign from `T_0`:

\[
[T_0[n]]=-[T_0].
\]

A nontrivial extension between `S_0` and `T_0[n]` would require one of

\[
\operatorname{Ext}^1(S_0,T_0[n])
=\operatorname{Ext}^{1+n}(S_0,T_0)
\]

or

\[
\operatorname{Ext}^1(T_0[n],S_0)
=\operatorname{Ext}^{1-n}(T_0,S_0)
\]

to be nonzero.

But `n` is odd, so both `1+n` and `1-n` are even. The cross-Ext groups above are supported only in the odd degrees `1` and `3`. Therefore

\[
\boxed{
\operatorname{Ext}^1(S_0,T_0[n])
=\operatorname{Ext}^1(T_0[n],S_0)=0
\qquad(n\text{ odd}).
}
\]

This proves:

> **Transverse two-block parity no-go.** A filtered local object whose associated graded pieces are `S_0` and an odd shift of `T_0` cannot be a nontrivial extension. In particular, no two-block construction with K-class `[S_0]-[T_0]` can couple the transverse divisor and curve pieces.

The previously considered Postnikov object with cohomology in degrees `0` and `1` is the special case `n=1`, where the missing parameter is

\[
\operatorname{Ext}^2(T_0,S_0)=0.
\]

## 4. Consequence for the RM scaffold

For the divisor block

\[
S=i_*V_D
\]

and cubic curve block

\[
R=j_*R_Z
\]

of `rm-smooth-isogeny-scaffold.md`, transverse intersection therefore rules out **every two-associated-graded coupling with the required signed K-class**, not just the simplest two-extension ansatz.

This contrasts with the `W_2` surface/surface model, where codimension-two branches in a fourfold do support a degree-two local Postnikov class.

## 5. Three surviving mechanisms

### A. Nested or nontransverse support

If the curve lies inside the divisor, the local model becomes

\[
S_0=R_0/(x_1),
\qquad
T_0=R_0/(x_1,x_2,x_3).
\]

Now degree-two Ext can occur. Equivalently, the elementary-transform sheaf

\[
I_{T_0/S_0}
\]

already has K-class

\[
[S_0]-[T_0].
\]

The global problem is therefore to realize the required RM cubic correction on a curve or perfect curve class lying inside an appropriate divisor support.

### B. A codimension-two mediator with net-zero K-class

Insert surface terms in opposite parities so that their total K-class cancels while their extension data connects the divisor and curve blocks. This is the minimal way to evade the two-block parity obstruction without forcing nested support.

A candidate should be rejected locally unless its differential really uses the surface Ext algebra and its total negative self-Exts vanish.

### C. Fourier--Mukai / Spin transport

Apply a derived equivalence before coupling. Derived equivalences preserve perfectness and self-Ext groups, while changing support dimensions and the HKR realization of the two mixed generalized directions. A useful transform would turn the divisor/curve pair into associated graded pieces whose required sign and available Ext parity are compatible.

## 6. Immediate next calculation

The local decision tree is now sharp:

1. test whether a deformation-friendly multiple of the cubic RM class can be represented by a curve nested in a divisor block;
2. if not, enumerate minimal codimension-two mediator complexes;
3. in parallel, search for a Fourier--Mukai/Spin transform making the two mixed `B/P` directions ordinary or making the relevant cross-Ext degree even.

The entire transverse two-block family is eliminated.