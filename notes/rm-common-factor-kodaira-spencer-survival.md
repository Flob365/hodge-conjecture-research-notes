# Common-factor Kodaira--Spencer tensors: an ambient cancellation and its tangent correction

> **Status.** This note records a useful common-factor cancellation in the ambient polarized deformation space, but corrects an earlier overstatement: the cancellation does **not** by itself prove that the corresponding class survives in `H^1(Lambda^2 E tensor K_D^{-1})`. The reason is that a polarized deformation tensor is represented naturally in `H^1(T_X|_D)`; lifting it to an actual `T_D`-valued Dolbeault representative requires a normal correction governed by the theta gradient/Hessian. Controlling that correction is now the key bridge problem.

## 1. Polarized deformation tensors

Let `D=Theta` be a smooth principal theta divisor in a principally polarized abelian fourfold `X`.

Via the polarization, the ten-dimensional infinitesimal ppav deformation space is

\[
H^1(T_D)\cong Sym^2W,
\qquad \dim W=4.
\]

More precisely, the tangent-normal sequence

\[
0\to T_D\to T_X|_D\to K_D\to0
\]

induces an injection

\[
H^1(T_D)\hookrightarrow H^1(T_X|_D)
\cong H^1(O_D)\otimes H^0(T_X),
\]

whose image is the symmetric-tensor subspace.

Choose ambient coordinates and write

\[
D_{ij}=\bar z_j\otimes\partial_{z_i}
\]

for the corresponding constant `(0,1)`-forms with values in `T_X|_D`.

Fix `0 != v in W` and set

\[
\xi=v^2,
\qquad
L_v=v\cdot W\subset Sym^2W,
\qquad \dim L_v=4.
\]

## 2. Exact ambient common-factor cancellation

Choose coordinates with `v=partial_1`. Then the ambient representative of

\[
\xi=v^2
\]

is

\[
D_{11}=\bar z_1\otimes\partial_1.
\]

For `w=partial_j`, the ambient representative of `v odot w` is

\[
D_{1j}+D_{j1}
=
\bar z_j\otimes\partial_1
+
\bar z_1\otimes\partial_j.
\]

In the ambient Dolbeault polyvector algebra one has pointwise

\[
\boxed{
D_{11}\wedge(D_{1j}+D_{j1})=0.
}
\]

Indeed the first term has repeated holomorphic vector `partial_1`, while the second has repeated antiholomorphic form `bar z_1`.

Similarly, for any `e,f in L_v`,

\[
\boxed{
\xi_{amb}\wedge e_{amb}\wedge f_{amb}=0.
}
\]

Thus the common-factor subspace is genuinely isotropic **after passage to the ambient bundle** `T_X|_D`.

## 3. Why this does not yet prove tangent-bundle vanishing

The crucial subtlety is that the constant tensors above are not pointwise sections of `T_D`.

A class

\[
q\in H^1(T_D)
\]

maps to its symmetric constant tensor in `H^1(T_X|_D)`, but an actual Dolbeault representative with values in `T_D` must have its normal component cancelled.

From

\[
0\to T_D\to T_X|_D\xrightarrow{d\theta}K_D\to0,
\]

the normal part of a constant ambient tensor is measured by the theta gradient. Solving it away introduces a correction depending on derivatives of the gradient, hence on the Hessian/second fundamental form of the theta divisor.

Consequently

\[
\xi_{amb}\wedge e_{amb}=0
\]

does **not** imply without further work that

\[
\xi\wedge e=0
\quad\text{in }H^2(\Lambda^2T_D).
\]

The difference lies precisely in the kernel of the map from tangent polyvectors to ambient polyvectors.

This is the point missed in the earlier version of this note.

## 4. The filtration differential remains correct abstractly

Let

\[
0\to U\otimes O_D\to E\to\Omega_D^1\to0
\]

be defined by three classes

\[
e_1,e_2,e_3\in H^1(T_D).
\]

The filtration of `Lambda^2 E tensor K_D^{-1}` has top graded term

\[
\Lambda^2\Omega_D^1\otimes K_D^{-1}\cong T_D.
\]

Its first spectral-sequence differential is canonically

\[
\boxed{
d_1(\eta)
=
(e_1\wedge\eta,
 e_2\wedge\eta,
 e_3\wedge\eta)
}
\]

with values in

\[
H^2(\Lambda^2T_D)^{\oplus3}.
\]

This formula is intrinsic. What remains unknown is whether, for the **tangent-corrected** representatives of

\[
\eta=\xi=v^2,
\qquad e_a\in L_v,
\]

the three classes `e_a wedge xi` actually vanish.

## 5. The normal correction is another Hessian problem

The tangent correction can be described through the same normal sequence that produced the Massey formula for

\[
\rho_P:H^1(T_D)\to H^1(\Omega_D^2\otimes P).
\]

For a symmetric ambient tensor `q`, choose a local primitive cancelling its theta-gradient normal component. Differentiating the gradient produces the Hessian of `theta`.

Thus there are now two appearances of the same second fundamental form:

1. the secondary map `rho_P` from `principal-theta-massey-evaluation.md`;
2. the correction to the ambient common-factor wedge needed to decide whether `v^2` survives in the middle extension space.

This is useful: Milestone A and extension survival are not unrelated constraints. They are controlled by the same normal geometry of the theta divisor.

## 6. Corrected unified target

Fix `v in W` and let

\[
L_v=vW.
\]

The promising architecture is still to choose the three defining classes of `E` inside `L_v`, because the ambient common-factor algebra is maximally degenerate there.

But two statements must now be proved simultaneously:

### A. Outer cancellation

Find `P` and three classes in `L_v` such that

\[
\boxed{
rank(\rho_P|_{L_v})\ge3.
}
\]

### B. Tangent corrected common-factor survival

Show that for

\[
\xi=v^2
\]

the Hessian correction does not destroy the ambient cancellation, i.e. that the intrinsic classes

\[
e_a\wedge\xi
\in H^2(\Lambda^2T_D)
\]

vanish for the chosen three `e_a`.

If both hold, then `xi` survives the first filtration differential. One must then check the remaining higher filtration obstruction, although the ambient triple-wedge identity strongly suggests that its principal symbol also vanishes.

## 7. Why the correction is productive rather than fatal

The failure of the naive pointwise argument identifies exactly what needs to be computed: the **second fundamental form of the theta embedding** applied to the common-factor tensors.

De Jong's bordered-Hessian invariant detects where that second fundamental form has full rank three, while Pareschi's Gaussian/Fourier formalism controls precisely the passage from the normal sequence to the relative Fourier transform.

Therefore the next calculation is no longer an abstract extension-space search. It is a concrete comparison of two Hessian corrections:

\[
\boxed{
\text{the Hessian term in }\rho_P|_{L_v}
\quad\text{versus}\quad
\text{the Hessian term in }d_1(v^2).
}
\]

A cancellation identity between them would restore the common-factor construction rigorously; a nonzero correction would reject it immediately.
