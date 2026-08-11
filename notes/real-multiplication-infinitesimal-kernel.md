# Real multiplication: an explicit 8-dimensional infinitesimal kernel

> **Status.** This is an exact linear-algebra calculation for the real-multiplication secant class appearing in Markman's arXiv:2509.23079. It reduces Markman's semiregularity question to eight explicit generalized deformation directions. It does **not** prove that those directions are unobstructed for the sheaf constructed by Markman.

## 1. The open condition to attack

In Question 11.2.2 of Markman's *Secant sheaves on abelian n-folds with real multiplication and Weil classes on abelian 2n-folds with complex multiplication*, one seeks a coherent sheaf `F_2` on a genus-4 Jacobian such that the semiregularity map is injective on the image of

\[
at_{F_2}:HT^2(X)\longrightarrow \operatorname{Ext}^2(F_2,F_2).
\]

Markman's Example 11.2.7 constructs a simple coherent sheaf `E'` whose Chern character is a positive integral multiple of

\[
\beta'
=g^*\Theta-\frac q6(g^{-1})^*(\Theta^3),
\]

where `X` has real multiplication by a real quadratic field, `f` is a norm-one unit with `f^2 != 1`, and `g^*` realizes `f` on `H^1(X,Q)`.

The semiregularity/Atiyah diagram gives

\[
\sigma_{F_2}\circ at_{F_2}
=\mu_{\operatorname{ch}(F_2)},
\]

where `mu` is the HKR/Clifford action on Hodge cohomology. Consequently

\[
\sigma_{F_2}|_{\operatorname{im}at_{F_2}}
\text{ is injective}
\iff
\ker(at_{F_2})=\ker(\mu_{\operatorname{ch}(F_2)}).
\]

Since multiplying the Chern character by a nonzero integer does not change its annihilator, it is enough to compute `ker(mu_beta')`.

Primary sources:

- E. Markman, arXiv:2509.23079, Question 11.2.2, Corollary 11.2.6, Example 11.2.7, Lemma 11.2.8.
- E. Markman, arXiv:2502.03415v2, Diagram (8.3.4), Lemma 8.3.4 and Remark 8.3.5 for the kernel criterion.

## 2. Split the genus-4 tangent space by the two real embeddings

Over `C`, write

\[
H^1(\mathcal O_X)=U_1\oplus U_2,
\qquad
\dim U_1=\dim U_2=2,
\]

for the two real embeddings of the quadratic field. Choose bases

\[
u_0,u_1\in U_1,
\qquad
u_2,u_3\in U_2,
\]

and dual holomorphic one-forms `x_i`. Put

\[
\theta_1=u_0x_0+u_1x_1,
\qquad
\theta_2=u_2x_2+u_3x_3,
\qquad
\Theta=\theta_1+\theta_2.
\]

Let the two real values of the norm-one unit `f` be `lambda` and `lambda^{-1}` and set

\[
\rho=\lambda^2>0.
\]

The nontriviality assumption `f^2 != 1` gives `rho != 1`. Then

\[
g^*\Theta=\rho\theta_1+\rho^{-1}\theta_2,
\qquad
(g^{-1})^*\Theta=\rho^{-1}\theta_1+\rho\theta_2.
\]

Since `theta_1^3=theta_2^3=0`, the secant class becomes

\[
\boxed{
\beta'
=\rho\theta_1+\rho^{-1}\theta_2
-\frac q2\left(
\rho^{-1}\theta_1^2\theta_2
+\rho\theta_1\theta_2^2
\right).
}
\]

## 3. The 28-dimensional HKR source

For an abelian fourfold,

\[
HT^2(X)
=H^2(\mathcal O_X)
\oplus H^1(T_X)
\oplus H^0(\wedge^2T_X),
\]

of dimensions `6 + 16 + 6 = 28`.

Use the following generators:

\[
B_{ij}=u_i\wedge u_j\wedge(-),
\]

\[
M_{ij}=u_i\wedge\iota_{e_j},
\]

and

\[
P_{ij}=\iota_{e_j}\iota_{e_i},
\]

where `e_i` is dual to `x_i`. These respectively represent the `B`-field, ordinary commutative, and bivector parts of `HT^2`.

Define

\[
\mu_{\beta'}:HT^2(X)\to H\Omega_*(X),
\qquad
\xi\mapsto\xi\cdot\beta'.
\]

## 4. Eight explicit annihilators

A direct exterior-algebra calculation gives the following eight independent classes in `ker(mu_beta')`:

\[
M_{00},\quad
M_{01}+M_{10},\quad
M_{11},
\]

\[
M_{22},\quad
M_{23}+M_{32},\quad
M_{33},
\]

and

\[
P_{01}-qB_{01},
\qquad
P_{23}-qB_{23}.
\]

The sign of the last two expressions changes if the opposite convention for the bivector part of the HKR/Clifford action is used; their span and the rank calculation are convention-independent.

The first six classes are

\[
\boxed{
\operatorname{Sym}^2(U_1)\oplus\operatorname{Sym}^2(U_2),
}
\]

inside `H^1(T_X)`. This is exactly the expected six-dimensional ordinary tangent space obtained by preserving the two real-multiplication blocks and the polarization.

The remaining two directions are genuinely generalized deformations mixing a `B`-field and a bivector.

## 5. Rank certificate

Order the domain basis by the six `B_ij`, then the sixteen `M_ij`, then the six `P_ij`. In the exterior-monomial basis of the image, one explicit `20 x 20` minor has determinant

\[
\boxed{
q^8\frac{(\rho-1)^8(\rho+1)^8(\rho^2+1)^8}{\rho^{16}}.
}
\]

For the real-multiplication situation under consideration,

\[
q>0,
\qquad
\rho>0,
\qquad
\rho\neq1,
\]

so this determinant is nonzero. Hence

\[
\operatorname{rank}(\mu_{\beta'})\ge20.
\]

The eight explicit independent annihilators give the reverse inequality. Therefore

\[
\boxed{
\operatorname{rank}(\mu_{\beta'})=20,
\qquad
\dim\ker(\mu_{\beta'})=8.
}
\]

The exact rational verifier in `scripts/verify_rm_infinitesimal_kernel.py` reconstructs the exterior algebra, verifies the eight kernel vectors, computes the rank, and checks the determinant certificate for arbitrary rational specializations of `rho` and `q`.

## 6. Reformulation of Markman's Question 11.2.2

For the sheaf `E'` of Example 11.2.7, `ch(E')=N beta'` with `N != 0`, so

\[
\ker\mu_{\operatorname{ch}(E')}
=\ker\mu_{\beta'}.
\]

Thus the remaining semiregularity-on-the-image condition is equivalent to the concrete statement

\[
\boxed{
\ker(at_{E'})
=
\operatorname{Sym}^2(U_1)
\oplus
\operatorname{Sym}^2(U_2)
\oplus
\langle P_{01}-qB_{01},\ P_{23}-qB_{23}\rangle.
}
\]

The general semiregularity diagram always gives

\[
\ker(at_{E'})\subseteq\ker(\mu_{\beta'}).
\]

Therefore it is enough to prove that **all eight displayed directions are unobstructed for `E'`**.

This is a much smaller target than computing the whole map into a potentially very large `Ext^2(E',E')`.

## 7. What can and cannot yet be claimed

### Six commutative directions

The six classes in

\[
\operatorname{Sym}^2(U_1)\oplus\operatorname{Sym}^2(U_2)
\]

are precisely the natural first-order polarized deformations preserving the real-multiplication splitting. This makes them geometrically plausible candidates for `ker(at_E')`.

However, Markman's concrete construction of `E'` uses a genus-4 Jacobian, a curve class, and gluing data. It is **not yet proved here** that this sheaf deforms along the full six-dimensional RM PEL tangent space. Hodge-theoretic annihilation alone is not enough.

### Two generalized directions

If the six ordinary RM directions can be shown to lie in `ker(at_E')`, the unresolved infinitesimal problem collapses to the two explicit classes

\[
P_{01}-qB_{01},
\qquad
P_{23}-qB_{23}.
\]

These are natural targets for an equivariant/perfect-complex construction, especially in view of Perry's 2026 semiregularity theorem for equivariant perfect complexes.

## 8. Next falsifiable milestones

1. **Ordinary RM deformation test.** Construct a first-order family of the gluing data in Example 11.2.7 along each of the six `Sym^2(U_i)` directions, or find a counter-obstruction.
2. **Generalized two-direction test.** Compute `at_E'` on `P_01-qB_01` and `P_23-qB_23` directly from the local gluing model.
3. **Perfect-complex fallback.** If the coherent sheaf fails one of those two directions, replace it by a quasi-isomorphic or modified equivariant perfect complex with the same secant Chern character and force the two generalized directions into its deformation kernel.

The calculation above therefore turns the real-multiplication route into an explicit rank-8 obstruction problem rather than an unconstrained semiregularity search.