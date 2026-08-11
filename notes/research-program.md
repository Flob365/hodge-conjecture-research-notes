# A falsifiable research program

## Current state of the attack

The real-multiplication route is now concentrated on a **smooth principal theta divisor** and two finite-dimensional rank problems.

Established inside these notes:

1. the RM secant Chern character and its generalized Chern-action map are explicit;
2. that action has rank `20` and an `8`-dimensional kernel: six ordinary RM directions plus two mixed `B`/bivector directions;
3. scalar semihomogeneous monads fail the earlier large-symmetry target;
4. ordinary elementary transforms along curves cannot kill the two mixed directions simultaneously on a simple RM fourfold;
5. the generic divisor--curve gluing architecture of Markman's explicit `E'` has the same local obstruction;
6. for `q=1`, the RM secant class is Fourier-even while the two mixed directions are Fourier-odd;
7. a Kodaira--Spencer rank-six bundle on one divisor preserves the pure divisor Chern character and reduces the split `3,11,11,3` Fourier profile to a single middle determinant;
8. in the **principal theta case** (`N=1`), the first rank problem becomes a natural `10 -> 11` map and the second becomes an `8 x 8` bilinear-form problem;
9. the `10 -> 11` target is a twisted Jacobian module with Hilbert profile `1,11,11,1`;
10. bounded-rank matrix theorems reduce the final determinant to rank thresholds `29` (symmetric forms) or `22` (alternating forms).

The active frontier is therefore no longer a search over arbitrary secant sheaves. It is:

\[
\boxed{
\text{(A) prove a rank-3 Hessian/Jacobian bridge,}\qquad
\text{(B) prove one finite Petri map has sufficiently large rank.}
}
\]

---

## Problem 1 — exact RM infinitesimal kernel

For

\[
\beta'=g^*\Theta-\frac q6(g^{-1})^*(\Theta^3),
\]

the exact exterior-algebra computation in
[`rm-semiregularity-kernel.md`](rm-semiregularity-kernel.md) gives

\[
\operatorname{rank}(\mu_{\beta'})=20,
\qquad
\dim\ker(\mu_{\beta'})=8.
\]

Up to the chosen HKR convention,

\[
\ker(\mu_{\beta'})
=
Sym^2(U_+)\oplus Sym^2(U_-)
\oplus
\langle B_+-q^{-1}P_+,\ B_--q^{-1}P_-\rangle.
\]

For a candidate `E` with Chern character on this ray, semiregularity on the Atiyah image is equivalent to

\[
\ker(at_E)=\ker(\mu_{\beta'}).
\]

---

## Problem 2 — local coherent couplings already rejected

### Curve elementary transforms

The local calculation in
[`rm-elementary-transform-no-go.md`](rm-elementary-transform-no-go.md)
shows that the curve-supported `mathcal Ext^2` edge term detects the bivector obstruction before the global `B`-field can cancel it.

### Markman's ordinary divisor--curve gluing

The generic local model

\[
R/(ab,ac,ad)
\]

has the same issue: simultaneous Atiyah-vanishing for the two RM bivectors would force a three-dimensional curve conormal space to project to dimension at most one in each of two two-dimensional RM blocks, which is impossible.

See [`markman-eprime-local-gluing-obstruction.md`](markman-eprime-local-gluing-obstruction.md).

These are architectural no-go results, not a rejection of Markman's general question.

---

## Problem 3 — pure-divisor Kodaira--Spencer bundle

Let `D` be a smooth ample divisor and put `K_D=O_D(D)`. Choose three deformation classes and form

\[
0\to O_D^{\oplus3}\to E\to\Omega_D^1\to0.
\]

Since `rank(E)=6` and `det(E)=K_D`,

\[
\Lambda^5E\cong E^\vee\otimes K_D.
\]

Moreover

\[
[E]+[\Lambda^5E]
=3[O_D]+[\Omega_D^1]+[\Omega_D^2]+3[K_D],
\]

so

\[
ch\bigl(i_*(E\oplus\Lambda^5E)\bigr)=12[D].
\]

If the first three connecting maps have maximal rank, the generic twisted cohomology profile becomes

\[
(0,8,8,0)N.
\]

See [`rm-kodaira-spencer-divisor-bundle.md`](rm-kodaira-spencer-divisor-bundle.md).

---

## Problem 4 — principal theta specialization (`N=1`)

Now take `D=Theta` smooth on a principally polarized abelian fourfold. Then

\[
N=h^0(X,O_X(Theta))=1.
\]

For nontrivial `P in Pic^0(X)`, the first milestone becomes

\[
\rho_P:H^1(T_D)\longrightarrow H^1(\Omega_D^2\otimes P),
\]

with dimensions

\[
10\longrightarrow11.
\]

Only

\[
\boxed{rank(\rho_P)\ge3}
\]

is required: three deformation classes with independent images then produce the desired outer cancellation.

The family packages over `Pic^0(X) minus {0}` into

\[
\kappa:O(-\widehat\Theta)^{\oplus10}\to G,
\qquad rank(G)=11.
\]

The exact Fourier calculation gives

\[
c_1(G)=-3\widehat\Theta,
\qquad
c_2(G)=5\widehat\Theta^2.
\]

If `kappa` has generic rank ten, Thom--Porteous predicts its rank-nine locus to have class

\[
30\widehat\Theta^2.
\]

There is therefore no Chern-class obstruction to the strongest expected rank.

See [`rm-principal-theta-fourier-rank.md`](rm-principal-theta-fourier-rank.md).

---

## Problem 5 — twisted Jacobian module and the Hessian bridge

The four theta gradients generate `K_D`. For nontrivial `P`,

\[
H^1(\Omega_D^2\otimes P)^\vee
\cong
coker\left[
H^0(K_D^2P^{-1})^{\oplus4}
\to
H^0(K_D^3P^{-1})
\right].
\]

The dimensions are `60 -> 65`, with cokernel `11`. The complete twisted Koszul package has Hilbert profile

\[
\boxed{1,11,11,1.}
\]

Thus Milestone A is a variation problem for a finite twisted Jacobian module.

Near `P=O`, the first ambient variation dies in the derivative/Aomoto quotient. The first potentially nonzero symbol is second order. The heat equation converts ppav-period variation into second derivatives of theta, so this symbol is expected to be the second fundamental form of the theta divisor.

De Jong proves that, off the ramification divisor of the Gauss map, the Hessian restricted to the tangent three-plane is nondegenerate, hence has rank `3`.

### Immediate bridge lemma

Prove that the first nonzero symbol of `kappa` at the projectivized tangent cone of the origin in `Pic^0` is the Gauss-map second fundamental form.

If true,

\[
rank(kappa)\ge3
\]

on a dense open set and **Milestone A is solved**.

See [`rm-principal-theta-jacobian-module.md`](rm-principal-theta-jacobian-module.md).

---

## Problem 6 — the final middle extension

After A, seek

\[
0\to E\to W_D\to E^\vee\otimes K_D\to0.
\]

At a suitable two-torsion `P`, the remaining connecting map is a bilinear form on an eight-dimensional vector space `V_P`.

The extension class splits into two symmetry sectors:

\[
\lambda_P^+:
H^1(Sym^2E\,K_D^{-1})\to\Lambda^2V_P^*,
\]

\[
\lambda_P^-:
H^1(\Lambda^2E\,K_D^{-1})\to Sym^2V_P^*.
\]

Sharp bounded-rank matrix theorems give the sufficient criteria

\[
\boxed{rank(\lambda_P^+)\ge22}
\]

or

\[
\boxed{rank(\lambda_P^-)\ge29.}
\]

Either inequality forces the image to contain a nondegenerate form and therefore solves Milestone B.

By Serre duality these become Petri/cup-product rank computations with sources of dimensions at most `28` and `36`.

See [`rm-middle-extension-bounded-rank-criterion.md`](rm-middle-extension-bounded-rank-criterion.md).

---

## Problem 7 — `q=1` Fourier symmetry

For

\[
q=1,
\qquad
\beta=A-\frac16C^3,
\]

the cohomological Poincare Fourier transform fixes `beta`, while

\[
B_+-P_+,
\qquad
B_--P_-
\]

are Fourier-odd.

This remains the only surviving structural mechanism which separates the final two generalized deformation directions before semiregularity is applied.

See [`rm-q1-fourier-symmetry.md`](rm-q1-fourier-symmetry.md).

The general equivariant theorem still requires gluable-ness and geometric-origin control for the Fourier-generated finite action.

---

## Problem 8 — relation to Markman's general RM framework

Markman's construction of the secant space `B` applies to an abelian variety with real multiplication; his explicit coherent secant-sheaf examples are built on genus-four Jacobians. The present pure-divisor construction is deliberately aimed at producing a different `B`-secant representative on a smooth-theta RM ppav, thereby avoiding the local singular-support mechanism that obstructs the explicit Jacobian gluing model.

A successful object must still satisfy the open tensor-square criterion needed to produce a nonzero Weil component after Orlov's equivalence.

---

## Problem 9 — later stages

Only after A and B should we:

1. compute `Phi(i_*W_D)[2]` and negative cross-Exts;
2. impose the `q=1` Fourier symmetry;
3. investigate finite isogeny equivariance;
4. compare the resulting deformation with the formal K-theory lift;
5. return to the independent vanishing-cycle route if the global Fourier step fails.

---

# Immediate next experiments

1. **Bridge lemma:** compute the second-order symbol of `kappa` and identify it with the bordered-Hessian/Gauss differential.
2. **Petri ranks:** once three Kodaira--Spencer directions are fixed, compute the two finite maps `lambda_P^+` and `lambda_P^-` at `N=1`.
3. Reject the model immediately if A has rank `<3` or if every middle pairing is singular.

A proof of A and either rank criterion in B would move the RM program past the two currently identified global bottlenecks.