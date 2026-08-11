# Riemann--Roch and bilinear structure of the final middle extension

> **Status.** This note analyzes the final extension space in `rm-kodaira-spencer-divisor-bundle.md`. The calculation shows that there is no Euler-characteristic or parity obstruction to a nondegenerate middle connecting map. It does **not** prove that an extension with nonzero determinant exists.

## 1. Setup

Let `D` be a smooth ample divisor in an abelian fourfold, put

\[
y=c_1(K_D)=c_1(\mathcal O_D(D)),
\]

and let

\[
0\to\mathcal O_D^{\oplus3}\to\mathcal E\to\Omega_D^1\to0
\]

be the rank-six Kodaira--Spencer bundle from `rm-kodaira-spencer-divisor-bundle.md`.

The final proposed bundle is an extension

\[
0\to\mathcal E\to W_D\to\mathcal E^\vee\otimes K_D\to0.
\]

Write

\[
A_D=\mathcal E^\vee\otimes K_D.
\]

Then

\[
\operatorname{Ext}^1(A_D,\mathcal E)
=H^1(D,\mathcal E\otimes\mathcal E\otimes K_D^{-1}).
\]

## 2. Chern character of `E`

The conormal sequence of the divisor is

\[
0\to K_D^{-1}\to\mathcal O_D^{\oplus4}\to\Omega_D^1\to0.
\]

Therefore, in dimension three,

\[
\operatorname{ch}(\Omega_D^1)
=4-e^{-y}
=3+y-\frac12y^2+\frac16y^3.
\]

Since `[E]=3[O_D]+[Omega_D^1]`,

\[
\boxed{
\operatorname{ch}(\mathcal E)
=6+y-\frac12y^2+\frac16y^3.
}
\]

The Todd class of `D` is

\[
\operatorname{td}(D)
=\operatorname{td}(K_D)^{-1}
=\frac{1-e^{-y}}{y}
=1-\frac12y+\frac16y^2-\frac1{24}y^3.
\]

## 3. Total extension space has Euler characteristic zero

Because

\[
A_D^\vee\otimes\mathcal E
=\mathcal E\otimes\mathcal E\otimes K_D^{-1},
\]

we compute

\[
\operatorname{ch}(\mathcal E^{\otimes2}\otimes K_D^{-1})
=36-24y+y^2+6y^3.
\]

Multiplying by `td(D)` gives

\[
\boxed{
\operatorname{ch}(\mathcal E^{\otimes2}\otimes K_D^{-1})\operatorname{td}(D)
=36-42y+19y^2,
}
\]

with **zero cubic coefficient**. Hence

\[
\boxed{
\chi(\mathcal E\otimes\mathcal E\otimes K_D^{-1})=0.
}
\]

Thus Riemann--Roch neither forces nor forbids the final `Ext^1`; the total extension problem is numerically self-balanced.

## 4. Symmetric and alternating sectors are not balanced individually

In characteristic zero,

\[
\mathcal E\otimes\mathcal E
=\operatorname{Sym}^2\mathcal E\oplus\Lambda^2\mathcal E.
\]

Using

\[
\operatorname{ch}(\operatorname{Sym}^2\mathcal E)
=\frac12\left(\operatorname{ch}(\mathcal E)^2+\operatorname{ch}(\psi^2\mathcal E)\right),
\]

and the analogous minus sign for `Lambda^2`, one obtains

\[
\operatorname{ch}(\operatorname{Sym}^2\mathcal E)
=21+7y-\frac72y^2+\frac76y^3,
\]

\[
\operatorname{ch}(\Lambda^2\mathcal E)
=15+5y-\frac32y^2-\frac16y^3.
\]

After twisting by `K_D^{-1}` and multiplying by `td(D)`, the cubic coefficients are respectively

\[
\frac{35}{24}
\quad\text{and}\quad
-\frac{35}{24}.
\]

If

\[
N=\chi(\mathcal O_X(D))
=\frac1{24}\int_X[D]^4,
\]

then

\[
\int_D y^3=24N.
\]

Consequently

\[
\boxed{
\chi(\operatorname{Sym}^2\mathcal E\otimes K_D^{-1})=35N,
}
\]

\[
\boxed{
\chi(\Lambda^2\mathcal E\otimes K_D^{-1})=-35N.
}
\]

The two sectors cancel in total, but each carries substantial cohomological content of order `N`.

This does not locate that cohomology in degree one; it only shows that the final extension problem is not numerically empty.

## 5. The middle determinant is a bilinear form at two-torsion twists

Assume the three Kodaira--Spencer classes have passed Milestone A, so for a suitable degree-zero twist `P`

\[
\dim H^1(A_D\otimes P)
=\dim H^2(\mathcal E\otimes P)=8N.
\]

For an extension class

\[
\varepsilon\in H^1(\mathcal E\otimes\mathcal E\otimes K_D^{-1}),
\]

the final connecting map is

\[
\partial_{\varepsilon,P}:
H^1(A_D\otimes P)
\to
H^2(\mathcal E\otimes P).
\]

Serre duality gives

\[
H^2(\mathcal E\otimes P)
\cong
H^1(A_D\otimes P^{-1})^\vee.
\]

If `P` is two-torsion, so `P=P^{-1}`, then `partial_{epsilon,P}` is equivalently a bilinear form

\[
\boxed{
B_{\varepsilon,P}:
V_P\otimes V_P\to\mathbf C,
\qquad
V_P=H^1(A_D\otimes P),
\quad\dim V_P=8N.
}
\]

## 6. Symmetry type of the form

The extension class decomposes as

\[
\varepsilon=\varepsilon_++\varepsilon_-
\]

with

\[
\varepsilon_+\in H^1(\operatorname{Sym}^2\mathcal E\otimes K_D^{-1}),
\qquad
\varepsilon_-\in H^1(\Lambda^2\mathcal E\otimes K_D^{-1}).
\]

When the two degree-one cohomology inputs in `V_P` are exchanged, their cup product contributes a minus sign. Therefore, up to the harmless global Serre-duality convention,

- a **symmetric** tensor extension `epsilon_+` induces an **alternating** form `B_epsilon`;
- an **alternating** tensor extension `epsilon_-` induces a **symmetric** form.

Thus the final determinant problem naturally splits into symplectic and orthogonal sectors.

## 7. There is no parity obstruction

The remaining vector space has dimension

\[
\boxed{\dim V_P=8N,}
\]

which is always even.

Therefore a nondegenerate alternating form is allowed. A nondegenerate symmetric form is of course also allowed.

Hence neither sector is ruled out by parity:

\[
\boxed{
\text{the `8N x 8N` determinant can in principle be nonzero in either symmetry sector.}
}
\]

This is a useful contrast with the local curve constructions, where the bivector obstruction forced an immediate rank contradiction.

## 8. Sharpened next target

Choose a nontrivial two-torsion point `P` lying in the open set where the outer Kodaira--Spencer maps have maximal rank. Then test the two linear maps

\[
H^1(\operatorname{Sym}^2\mathcal E\otimes K_D^{-1})
\longrightarrow
\Lambda^2V_P^\vee,
\]

and

\[
H^1(\Lambda^2\mathcal E\otimes K_D^{-1})
\longrightarrow
\operatorname{Sym}^2V_P^\vee.
\]

It is enough to show that the image of either map contains a nondegenerate form.

This is strictly sharper than searching an arbitrary extension class: the final problem is now a **linear family of symplectic/orthogonal forms followed by one determinant/Pfaffian test**.