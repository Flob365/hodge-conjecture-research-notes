# Real multiplication: the two missing directions are gluing-cancellation directions

> **Status.** This note refines the rank-20 calculation for Markman's real-multiplication class by separating the divisor-supported secant block from the correcting curve block used in Example 11.2.7. The result identifies exactly what the gluing must do: six kernel directions vanish componentwise, while two generalized directions require cancellation of equal and opposite obstruction contributions.

## 1. Split Markman's class according to the construction

Use the notation of [`rm-semiregularity-kernel.md`](rm-semiregularity-kernel.md). Put

\[
\Theta_A=A\Theta_++A^{-1}\Theta_-,
\qquad
\Theta_{A^{-1}}=A^{-1}\Theta_++A\Theta_-.
\]

In Example 11.2.7, the auxiliary secant sheaf `g^*F'` has Chern character proportional to

\[
\alpha_{A,d}
:=\Theta_A-\frac d6\Theta_A^3,
\]

while the curve `C'` is chosen with class proportional to

\[
\gamma_{A,d,q}
:=\frac d6\Theta_A^3
-\frac q6\Theta_{A^{-1}}^3.
\]

Their sum is precisely

\[
\alpha_{A,d}+\gamma_{A,d,q}
=\Theta_A-\frac q6\Theta_{A^{-1}}^3
=\beta'.
\]

Thus the cohomological decomposition exactly mirrors the geometric gluing construction.

## 2. Three exact ranks

Let `mu_alpha`, `mu_gamma`, and `mu_beta` denote the HKR Chern actions on `HT^2(X)`.

For `A != 0`, and for the non-exceptional auxiliary parameter values

\[
d\neq4q,
\qquad
4d\neq q,
\]

exact exterior-algebra row reduction gives

\[
\boxed{\operatorname{rank}(\mu_\alpha)=12,}
\]

\[
\boxed{\operatorname{rank}(\mu_\gamma)=12,}
\]

and

\[
\boxed{
\operatorname{rank}
\begin{pmatrix}
\mu_\alpha\\
\mu_\gamma
\end{pmatrix}
=22.
}
\]

Hence

\[
\boxed{
\dim(\ker\mu_\alpha\cap\ker\mu_\gamma)=6.
}
\]

On the other hand, for the genuine RM case `A>0`, `A!=1`,

\[
\boxed{\operatorname{rank}(\mu_{\alpha+\gamma})=20,}
\]

so

\[
\dim\ker\mu_{\alpha+\gamma}=8.
\]

A fixed `22 x 22` stacked minor has determinant, up to the nonzero basis normalization used by the verifier,

\[
-\frac{50625}{1024}
q^4(d-4q)(4d-q)^5.
\]

In Markman's construction `d` may be taken sufficiently large, so the exceptional equalities can be avoided.

## 3. The common six-dimensional kernel

The intersection

\[
\ker\mu_\alpha\cap\ker\mu_\gamma
\]

is exactly

\[
\boxed{
\operatorname{span}\{
D_{11},D_{22},D_{12}+D_{21},
D_{33},D_{44},D_{34}+D_{43}
\}.
}
\]

Thus the six ordinary RM-preserving deformation directions annihilate **both pieces separately**.

This is stronger than merely saying that they annihilate the total Chern character.

## 4. The remaining two directions cancel between the pieces

Define

\[
\xi_+=B_+-q^{-1}P_+,
\qquad
\xi_-=B_--q^{-1}P_-.
\]

These are in the kernel of the total class,

\[
\mu_{\alpha+\gamma}(\xi_\pm)=0,
\]

but generically they are **not** in the kernel of either summand.

With the contraction convention of the verifier,

\[
\boxed{
\mu_\alpha(\xi_+)
=-\frac{4d-q}{2q}\,B_+\wedge\Theta_-,
\qquad
\mu_\gamma(\xi_+)
=+\frac{4d-q}{2q}\,B_+\wedge\Theta_-.
}
\]

Likewise,

\[
\boxed{
\mu_\alpha(\xi_-)
=-\frac{d-4q}{2q}\,\Theta_+\wedge B_-,
\qquad
\mu_\gamma(\xi_-)
=+\frac{d-4q}{2q}\,\Theta_+\wedge B_-.
}
\]

The dependence on the RM eigenvalue `A` cancels completely in these two formulas.

Therefore the last two kernel directions are **not componentwise deformation directions**. Their vanishing for the total Chern character is an exact cancellation between the surface/divisor-supported secant block and the correcting curve block.

## 5. Consequence for any Atiyah-map proof

This eliminates one tempting but incorrect proof strategy.

If one proves that a deformation of the glued sheaf exists only when the secant components and the curve component deform separately, then one can obtain at most the six-dimensional common kernel above. That can never establish the desired eight-dimensional kernel.

A successful proof must use the gluing extension itself to cancel the two generalized obstruction classes.

Equivalently, for

\[
\xi_+,\xi_-,
\]

the Atiyah obstruction of the divisor-supported part and the Atiyah obstruction of the curve-supported correction must map to opposite classes in the obstruction theory of the glued sheaf.

This is now the sharp missing local-to-global statement.

## 6. Local model at a gluing point

Markman chooses the translates so that the correcting curve meets each support at points where the secant sheaf is a line bundle over its support. At a transverse such point, after trivializing the two line bundles, the expected completed local model is

\[
R=k[[x_1,x_2,x_3,x_4]],
\]

with divisor branch

\[
D:\ x_1=0
\]

and curve branch

\[
C:\ x_2=x_3=x_4=0.
\]

The glued rank-one module on `D union C` is the fiber product

\[
M=
R/(x_1)\times_k R/(x_2,x_3,x_4),
\]

fitting into

\[
0\to M
\to R/(x_1)\oplus R/(x_2,x_3,x_4)
\to k
\to0.
\]

Equivalently,

\[
M\cong R/(x_1x_2,x_1x_3,x_1x_4).
\]

This local module has a short explicit free resolution obtained by multiplying the Koszul resolution of `(x_2,x_3,x_4)` by `x_1`. It is therefore a tractable target for an explicit local Atiyah calculation.

The global `B`-field part of `xi_+` and `xi_-` means that the full cancellation cannot be proved from one affine stalk alone, but this local model should determine the local contribution of the bivector part and the compatibility condition imposed by the gluing morphism.

## 7. Revised attack

The next proof attempt should not compute all of `Ext^2(E',E')`. It should prove the following **Gluing Cancellation Lemma**.

> Let `E'` be Markman's glued sheaf. For each of the two generalized directions `xi_+` and `xi_-`, the evaluation of the Hochschild class on the divisor-supported secant summand and on the curve-supported summand maps to equal and opposite classes after passage to the deformation complex of the gluing. Hence `ob_E'(xi_+)=ob_E'(xi_-)=0`.

Together with deformation of the six RM-preserving ordinary directions, this lemma would give eight independent elements of `ker(ob_E')`. Since the Chern-action calculation already gives

\[
\ker(ob_{E'})\subseteq\ker(\mu_{\beta'})
\]

and the latter has dimension `8`, it would force equality and settle the missing semiregularity-on-the-obstruction-image condition.

## 8. Why this is a useful narrowing

The remaining problem has split into two qualitatively different pieces:

1. **six geometric directions:** construct ordinary first-order deformations of the glued object along the RM polarized locus;
2. **two generalized directions:** prove a specific cancellation across the divisor--curve gluing.

The second part is only two-dimensional and its cohomological cancellation is already known exactly, including the two scalar coefficients above. Any local-to-global Atiyah calculation now has a very concrete answer it must reproduce.
