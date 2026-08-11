# The universal infinitesimal annihilator of the RM secant four-plane

> **Status.** Exact exterior-algebra calculation. It shows that the two mixed `B`/bivector directions found for Markman's rank-zero example are intrinsic to the entire four-dimensional real-multiplication secant space `B`; changing the Chern character inside `B` cannot remove them.

## 1. Markman's four-plane

For a genus-4 real-multiplication fourfold, write

\[
H^1(\mathcal O_X)=U_1\oplus U_2,
\qquad \dim U_i=2,
\]

and

\[
\Theta=\theta_1+\theta_2,
\qquad
\widetilde\Theta=\theta_1-\theta_2.
\]

Markman (arXiv:2509.23079, Section 11.2.1) sets

\[
\alpha=1-\frac q2\Theta^2+\frac{q^2}{24}\Theta^4,
\qquad
\beta=\Theta-\frac q6\Theta^3,
\]

and defines `tilde alpha`, `tilde beta` in the same way using `tilde Theta`. His rational secant space is

\[
B=\operatorname{span}_{\mathbf Q}
\{\alpha,\beta,\widetilde\alpha,\sqrt t\,\widetilde\beta\}.
\]

The scalar `sqrt(t)` on the fourth basis vector is irrelevant for the annihilator calculation.

## 2. HKR generators

Use the same conventions as in `real-multiplication-infinitesimal-kernel.md`:

\[
B_{ij}=u_i\wedge u_j\wedge(-),
\qquad
M_{ij}=u_i\wedge\iota_{e_j},
\qquad
P_{ij}=\iota_{e_j}\iota_{e_i}.
\]

These form the 28-dimensional space

\[
HT^2(X)=H^2(\mathcal O_X)\oplus H^1(T_X)\oplus H^0(\wedge^2T_X).
\]

## 3. Eight directions kill every class in `B`

Direct calculation shows that each of the following annihilates all four basis vectors of `B`:

\[
M_{00},\quad M_{01}+M_{10},\quad M_{11},
\]

\[
M_{22},\quad M_{23}+M_{32},\quad M_{33},
\]

and, up to the sign convention for the bivector part of HKR,

\[
P_{01}-qB_{01},
\qquad
P_{23}-qB_{23}.
\]

Equivalently,

\[
\mathfrak a_B:=
\operatorname{Sym}^2(U_1)
\oplus
\operatorname{Sym}^2(U_2)
\oplus
\langle P_{01}-qB_{01},\ P_{23}-qB_{23}\rangle
\]

is contained in the common annihilator

\[
\bigcap_{\gamma\in B}\ker(\mu_\gamma).
\]

## 4. The common annihilator is exactly eight-dimensional

Stack the four action matrices for

\[
\alpha,\ \beta,\ \widetilde\alpha,\ \widetilde\beta.
\]

The resulting linear map from the common 28-dimensional source has rank `20`. One explicit `20 x 20` minor has determinant

\[
\boxed{-256\,q^{14}}.
\]

Since `q>0`, this is nonzero. Therefore

\[
\boxed{
\bigcap_{\gamma\in B}\ker(\mu_\gamma)
=
\mathfrak a_B,
\qquad
\dim\mathfrak a_B=8.
}
\]

Thus the two generalized classes

\[
P_{01}-qB_{01},
\qquad
P_{23}-qB_{23}
\]

are **intrinsic to the whole secant four-plane**. They are not artifacts of Markman's special rank-zero class `beta'`.

## 5. Generic classes in `B`

For a generic rational class

\[
\gamma=a\alpha+b\beta+c\widetilde\alpha+d\sqrt t\,\widetilde\beta,
\]

the single action map `mu_gamma` already has rank `20`, hence

\[
\ker(\mu_\gamma)=\mathfrak a_B.
\]

Special choices can have a larger annihilator. For example,

\[
\gamma_+=\alpha+\widetilde\alpha
\]

has rank `18` and a ten-dimensional annihilator: the six symmetric ordinary directions enlarge to

\[
\operatorname{End}(U_1)\oplus\operatorname{End}(U_2),
\]

while the same two mixed `B/P` directions remain.

Hence switching to a positive-rank class can make the geometric realization easier, but it does **not** remove the mixed generalized-deformation problem.

## 6. A useful positive-rank candidate

The class

\[
\gamma_+=\alpha+\widetilde\alpha
\]

has

\[
\operatorname{rk}(\gamma_+)=2,
\qquad
c_1(\gamma_+)=0,
\]

and factorizes over the two real embeddings as

\[
\boxed{
\gamma_+
=2\left(1-\frac q2\theta_1^2\right)
 \left(1-\frac q2\theta_2^2\right).
}
\]

It has nonzero components in both secant planes `P_{K_0}` and `P_{K_1}`, so it is outside their union. If the first secant object is chosen with Chern character `alpha+beta` (Markman's Example 8.2.3 type), the top-degree coefficient of `alpha^2` is `q^2/3`; on a principally polarized fourfold

\[
\int_X\Theta^4=24,
\]

so the corresponding scalar pairing is `8q^2`, nonzero. Thus this rank-two class is a plausible alternative input for Markman's genericity criterion, subject to matching the precise normalization of the `check(phi)` pairing.

The main unresolved issue is now categorical realization with the universal two mixed directions in the Atiyah kernel.

## 7. Consequence for the research program

Changing `beta` inside `B` is not a way around the generalized directions. Any successful strategy must actually **categorify the universal eight-dimensional infinitesimal stabilizer of `B`**, in particular

\[
P_{01}-qB_{01},\qquad P_{23}-qB_{23}.
\]

The positive-rank route remains useful because stable/torsion-free objects may have better deformation theory than the rank-zero divisor/curve scaffold, but the target kernel is structurally fixed.