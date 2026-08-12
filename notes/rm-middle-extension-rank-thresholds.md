# Exact matrix-space thresholds for the final middle extension

> **Status.** This note turns Milestone B into a finite-dimensional rank problem. It uses sharp dimension bounds for linear spaces of symmetric or alternating matrices with bounded rank. The missing input is the rank of the geometric cup-product map.

## 1. Eight-dimensional middle cohomology in the principal case

Assume the principal theta-divisor specialization `N=1` and that Milestone A has been achieved. Then the two middle groups in the final extension

\[
0\to\mathcal E\to W_D\to\mathcal E^\vee\otimes K_D\to0
\]

have dimension

\[
\dim V_P=8
\]

at a two-torsion twist `P=P^{-1}`.

An extension class

\[
\varepsilon\in H^1(\mathcal E\otimes\mathcal E\otimes K_D^{-1})
\]

therefore induces a bilinear form on `V_P`.

The decomposition

\[
\mathcal E\otimes\mathcal E
=\operatorname{Sym}^2\mathcal E\oplus\Lambda^2\mathcal E
\]

produces two linear maps

\[
\lambda_{+,P}:
H^1(\operatorname{Sym}^2\mathcal E\otimes K_D^{-1})
\to\Lambda^2V_P^*,
\]

and

\[
\lambda_{-,P}:
H^1(\Lambda^2\mathcal E\otimes K_D^{-1})
\to\operatorname{Sym}^2V_P^*.
\]

The switch of symmetry is the usual Koszul sign from cup-product in degree one.

## 2. Alternating branch

An alternating `8 x 8` form is singular precisely when its rank is at most `6`.

The sharp bounded-rank theorem for alternating matrices says that a linear subspace of alternating `8 x 8` matrices all of rank at most `6` has dimension at most

\[
\boxed{21.}
\]

Therefore

\[
\boxed{
\dim\operatorname{Im}(\lambda_{+,P})\ge22
\Longrightarrow
\text{some induced alternating form is nondegenerate.}
}
\]

Such a class solves Milestone B.

## 3. Symmetric branch

A symmetric `8 x 8` form is singular precisely when its rank is at most `7`.

The sharp bounded-rank theorem for symmetric matrices gives maximum dimension

\[
\boxed{28}
\]

for a linear subspace all of whose matrices have rank at most `7`.

Therefore

\[
\boxed{
\dim\operatorname{Im}(\lambda_{-,P})\ge29
\Longrightarrow
\text{some induced symmetric form is nondegenerate.}
}
\]

Again this settles Milestone B.

## 4. Why this is useful

The target spaces have dimensions

\[
\dim\Lambda^2V_P^*=28,
\qquad
\dim\operatorname{Sym}^2V_P^*=36.
\]

Thus:

- the alternating branch only needs image codimension at most `6`;
- the symmetric branch only needs image dimension at least `29`.

One no longer needs to exhibit an extension with nonzero determinant directly. It suffices to establish one of these image-rank bounds for the corresponding geometric cup-product map.

## 5. Current target

Compute, for a principal theta divisor and a Milestone-A Kodaira--Spencer bundle `E`, the ranks of

\[
\lambda_{+,P},\qquad\lambda_{-,P}
\]

at one two-torsion point `P` where the middle cohomology has the expected dimension eight.

A rank `22` result for the alternating branch or a rank `29` result for the symmetric branch completes Milestone B without evaluating a determinant.

## Reference

- C. de Seguins Pazzis, *Large spaces of symmetric or alternating matrices with bounded rank*, arXiv:1603.08560, especially the sharp maximal-dimension theorems for symmetric and alternating bounded-rank spaces.
