# Milestone B: the extension space collapses to at most ten symmetric forms

> **Status.** This note corrects the earlier bounded-rank strategy. For the Kodaira--Spencer bundle `E` on a smooth principal theta divisor, the degree-one extension space relevant to Milestone B has no symmetric-tensor contribution and injects into `H^1(T_D)`, hence has dimension at most ten. Thus the previous sufficient thresholds `22` and `29` cannot be reached geometrically in this model. Milestone B is instead the existence of one nonsingular form in a linear system of at most ten symmetric `8 x 8` forms.

## 1. Setup

Let `D=Theta` be a smooth principal theta divisor in a principally polarized abelian fourfold and put

\[
K=K_D=O_D(Theta).
\]

Choose three Kodaira--Spencer classes satisfying Milestone A and form

\[
0\to U\otimes O_D\to E\to\Omega_D^1\to0,
\qquad \dim U=3.
\]

Set

\[
A_D=E^\vee\otimes K=\Lambda^5E.
\]

The final extension classes are

\[
Ext^1(A_D,E)
=H^1(D,E\otimes E\otimes K^{-1}).
\]

Decompose

\[
E\otimes E=Sym^2E\oplus\Lambda^2E.
\]

## 2. The symmetric-tensor sector has no `H^1`

The filtration of `Sym^2E` induced by `0 -> U -> E -> Omega^1 -> 0` has associated graded terms

\[
Sym^2U\otimes O_D,
\qquad
U\otimes\Omega_D^1,
\qquad
Sym^2\Omega_D^1.
\]

After twisting by `K^{-1}` these are sums of

\[
K^{-1},
\qquad
\Omega_D^1K^{-1},
\qquad
Sym^2\Omega_D^1K^{-1}.
\]

Because `K` is ample on the threefold `D`, Serre duality plus Kodaira vanishing gives

\[
H^i(K^{-m})=0\qquad(i<3,\ m>0).
\]

The conormal sequence

\[
0\to K^{-1}\to O_D^{\oplus4}\to\Omega_D^1\to0
\]

twisted by `K^{-1}` gives

\[
H^0(\Omega_D^1K^{-1})=H^1(\Omega_D^1K^{-1})=0.
\]

For the symmetric square, since the kernel in `Sym^2(O_D^{\oplus4}) -> Sym^2(Omega_D^1)` is `K^{-1}\otimes O_D^{\oplus4}`, one has

\[
0\to K^{-2\,\oplus4}
\to K^{-1\,\oplus10}
\to Sym^2\Omega_D^1K^{-1}
\to0.
\]

Hence

\[
H^0(Sym^2\Omega_D^1K^{-1})
=H^1(Sym^2\Omega_D^1K^{-1})=0.
\]

Passing through the filtration therefore yields

\[
\boxed{
H^1(Sym^2E\,K^{-1})=0.
}
\]

So the former alternating-form branch of Milestone B is absent.

## 3. The alternating-tensor sector injects into `H^1(T_D)`

The filtration of `Lambda^2E` has a first stage `F` with

\[
0\to\Lambda^2U\otimes O_D
\to F
\to U\otimes\Omega_D^1
\to0,
\]

and then

\[
0\to F
\to\Lambda^2E
\to\Lambda^2\Omega_D^1
\to0.
\]

After twisting by `K^{-1}`, the first stage has

\[
H^0(FK^{-1})=H^1(FK^{-1})=0.
\]

On a threefold,

\[
\Lambda^2\Omega_D^1\otimes K^{-1}
\cong T_D.
\]

Since `K_D` is ample, `Aut(D)` is finite and therefore

\[
H^0(T_D)=0.
\]

The long exact sequence gives a canonical injection

\[
\boxed{
H^1(\Lambda^2E\,K^{-1})
\hookrightarrow H^1(T_D).
}
\]

For a smooth principal theta divisor,

\[
h^1(T_D)=10.
\]

Consequently

\[
\boxed{
\dim Ext^1(A_D,E)\le10.
}
\]

Moreover every surviving extension class lies in the alternating tensor sector, so after the odd cohomological sign it induces a **symmetric** bilinear form on the eight-dimensional middle space.

## 4. Correct form of Milestone B

At a degree-zero twist `P` where Milestone A gives the profile `(0,8,8,0)`, put

\[
V_P=H^1(A_D\otimes P),
\qquad \dim V_P=8.
\]

Every extension class

\[
\varepsilon\in Ext^1(A_D,E)
\]
induces a symmetric bilinear form

\[
B_{\varepsilon,P}:V_P\times V_{P^{-1}}\to\mathbf C,
\]

and for `P=P^{-1}` this is a symmetric `8 x 8` matrix.

Thus the old dimension criterion

\[
rank(\lambda_P^-)\ge29
\]

is not available here: the geometric source has dimension at most ten.

The actual target is simply

\[
\boxed{
\exists\,\varepsilon\in Ext^1(A_D,E)
\text{ such that }B_{\varepsilon,P}\text{ is nondegenerate.}
}
\]

So Milestone B is a determinant problem for a linear system of at most ten symmetric forms, not a large-image problem.

## 5. The remaining boundary map

Writing the three Kodaira--Spencer classes as

\[
\kappa=(Q_1,Q_2,Q_3)\in U\otimes H^1(T_D),
\]

the second exterior-power sequence shows more precisely that

\[
H^1(\Lambda^2E K^{-1})
=\ker\left[
H^1(T_D)\xrightarrow{\delta_\kappa}
H^2(FK^{-1})
\right].
\]

The leading symbol of `delta_kappa` is the cup--wedge product with the three classes `Q_i`. Hence a useful sufficient design condition for a candidate fourth direction `Q_0` is

\[
Q_i\wedge Q_0=0
\qquad(i=1,2,3)
\]

in the vector-valued Dolbeault model.

For ambient ppav deformation tensors, a concrete rank-one pattern is

\[
Q_0=v\odot v,
\qquad
Q_i=v\odot w_i
\quad(i=1,2,3),
\]

with `v,w_1,w_2,w_3` independent. Termwise, every wedge `Q_i wedge Q_0` vanishes because one factor repeats in either the holomorphic-vector or antiholomorphic-form slot.

This gives the next concrete candidate for a nonzero middle extension. The remaining task is to verify the comparison with the theta-divisor Kodaira--Spencer representatives and then test whether the resulting symmetric `8 x 8` form is nonsingular.

## 6. Immediate next target

1. verify that the rank-one pattern above survives the ambient-to-theta Kodaira--Spencer comparison;
2. compute the induced middle form for `Q_0=v^2`;
3. identify that form with the corresponding Hessian/Jacobian multiplication operator;
4. prove its determinant is nonzero for one choice of `v` and one general degree-zero twist `P`.

A success in step 4 settles Milestone B for the present divisor-bundle model.