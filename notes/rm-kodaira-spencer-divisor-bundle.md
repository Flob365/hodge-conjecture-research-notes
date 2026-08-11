# A Kodaira--Spencer divisor bundle reducing `3,11,11,3` to one determinant

> **Status.** This note gives a concrete non-split vector-bundle replacement for the split divisor block `V_D`. It has exactly the same K-class and Chern character, but three Kodaira--Spencer extension directions can cancel the three outer generic cohomology dimensions on each side. A final self-dual extension reduces the remaining Fourier problem to a single square determinant. The existence of an extension with nonzero determinant is the unresolved step.

## 1. The split divisor block and its generic cohomology

Let `D` be a smooth ample divisor in an abelian fourfold `X`, put

\[
L=\mathcal O_D(D),
\qquad K_D=L,
\]

and write

\[
N=h^0(X,\mathcal O_X(D)).
\]

The split rank-12 bundle used in `rm-smooth-isogeny-scaffold.md` is

\[
V_D=
\mathcal O_D^{\oplus3}
\oplus\Omega_D^1
\oplus\Omega_D^2
\oplus K_D^{\oplus3}.
\]

For a general `P in Pic^0(X)`, its four graded pieces have generic cohomology

\[
\begin{array}{c|c}
\text{piece}&\text{only nonzero generic cohomology}\\
\hline
K_D^{\oplus3}&H^0\text{ of dimension }3N\\
\Omega_D^2&H^1\text{ of dimension }11N\\
\Omega_D^1&H^2\text{ of dimension }11N\\
\mathcal O_D^{\oplus3}&H^3\text{ of dimension }3N.
\end{array}
\]

Hence

\[
(h^0,h^1,h^2,h^3)(V_D\otimes P)
=(3,11,11,3)N.
\]

The goal is to keep the same K-class while coupling these four layers.

## 2. Three first-order deformations of `D`

Choose three independent first-order deformation directions of the threefold `D`. Equivalently, choose a three-dimensional subspace of Kodaira--Spencer classes in

\[
H^1(T_D)=\operatorname{Ext}^1(\Omega_D^1,\mathcal O_D).
\]

The relative cotangent sequence of the corresponding first-order three-parameter deformation restricts to a rank-six vector bundle `E` on `D` fitting into

\[
\boxed{
0\to\mathcal O_D^{\oplus3}
\to\mathcal E
\to\Omega_D^1
\to0.
}
\]

Thus

\[
[\mathcal E]=3[\mathcal O_D]+[\Omega_D^1].
\]

Since `rank(E)=6` and `det(E)=K_D`, there is a canonical identity

\[
\Lambda^5\mathcal E\cong\mathcal E^\vee\otimes K_D.
\]

Taking the fifth exterior power of the extension gives

\[
\boxed{
0\to\Omega_D^2
\to\Lambda^5\mathcal E
\to K_D^{\oplus3}
\to0.
}
\]

Hence

\[
[\Lambda^5\mathcal E]
=[\Omega_D^2]+3[K_D].
\]

Adding the two bundles gives the exact K-theory identity

\[
\boxed{
[\mathcal E]+[\Lambda^5\mathcal E]
=3[\mathcal O_D]+[\Omega_D^1]+[\Omega_D^2]+3[K_D]
=[V_D].
}
\]

Therefore every such Kodaira--Spencer choice preserves the crucial GRR identity

\[
\boxed{
\operatorname{ch}\bigl(i_*(\mathcal E\oplus\Lambda^5\mathcal E)\bigr)
=12[D].
}
\]

## 3. The first cancellation: `3,11,11,3 -> 0,8,8,0`

Twist the first exact sequence by a general `P in Pic^0(X)`.

The only relevant connecting map is

\[
\delta_P:
H^2(D,\Omega_D^1\otimes P)
\longrightarrow
H^3(D,\mathcal O_D^{\oplus3}\otimes P).
\]

Its source has dimension `11N` and its target dimension `3N`.

If the three Kodaira--Spencer classes are chosen so that `delta_P` is generically surjective, then

\[
H^3(D,\mathcal E\otimes P)=0,
\qquad
\dim H^2(D,\mathcal E\otimes P)=8N.
\]

By Serre duality and

\[
\Lambda^5\mathcal E=\mathcal E^\vee\otimes K_D,
\]

the dual connecting map for the second exact sequence is generically injective. Consequently

\[
H^0(D,\Lambda^5\mathcal E\otimes P)=0,
\qquad
\dim H^1(D,\Lambda^5\mathcal E\otimes P)=8N.
\]

Thus the non-split direct sum

\[
W_D^{(0)}:=\mathcal E\oplus\Lambda^5\mathcal E
\]

has generic cohomology profile

\[
\boxed{
(h^0,h^1,h^2,h^3)(W_D^{(0)}\otimes P)
=(0,8,8,0)N.
}
\]

The three Kodaira--Spencer directions have therefore removed exactly the three outer dimensions on both sides.

## 4. One final extension remains

Now use

\[
\Lambda^5\mathcal E=\mathcal E^\vee\otimes K_D.
\]

Consider an extension

\[
\boxed{
0\to\mathcal E
\to W_D
\to\mathcal E^\vee\otimes K_D
\to0
}
\]

with class

\[
\varepsilon\in
\operatorname{Ext}^1(\mathcal E^\vee\otimes K_D,\mathcal E)
=H^1(D,\mathcal E\otimes\mathcal E\otimes K_D^{-1}).
\]

Its K-class is still exactly `[V_D]`, so

\[
\boxed{
\operatorname{ch}(i_*W_D)=12[D].
}
\]

For a general `P`, the only remaining connecting map is

\[
\boxed{
\partial_{\varepsilon,P}:
H^1(D,\mathcal E^\vee\otimes K_D\otimes P)
\longrightarrow
H^2(D,\mathcal E\otimes P).
}
\]

Under the maximal-rank Kodaira--Spencer hypothesis, both sides have dimension exactly `8N`.

Therefore

\[
R\Gamma(D,W_D\otimes P)=0
\]

for general `P` if and only if

\[
\boxed{
\det(\partial_{\varepsilon,P})\neq0
}
\]

for one (equivalently general) `P` in a dense open subset.

This reduces the generic-Fourier problem from four independent cohomological layers to **one square determinant**.

## 5. Self-duality of the final problem

Serre duality identifies

\[
H^1(D,\mathcal E^\vee\otimes K_D\otimes P)
\cong
H^2(D,\mathcal E\otimes P^{-1})^\vee.
\]

Thus the family of matrices `partial_{epsilon,P}` naturally pairs the `P` and `P^{-1}` fibers.

A self-dual choice of extension class `epsilon` is therefore especially natural. One should search in the symmetric or alternating summand of

\[
H^1(\mathcal E\otimes\mathcal E\otimes K_D^{-1})
\]

for a class whose induced determinant is not identically zero on `Pic^0(X)`.

This is a much smaller and more structured problem than constructing an arbitrary rank-12 bundle with the required Chern character.

## 6. Relation to the `q=1` Fourier route

For the special real-multiplication case `q=1`, let

\[
A=g^*\Theta,
\qquad
C=(g^{-1})^*\Theta,
\qquad
\beta=A-\frac16C^3.
\]

The Poincare Fourier transform fixes `beta` and exchanges the two mixed deformation directions with sign.

Take `D` in a sufficiently positive multiple of `A` (for example after the same multiplication-isogeny regularization used elsewhere in the notes) and construct `W_D` as above.

Then

\[
S=i_*W_D
\]

is a coherent sheaf with pure divisor Chern character, no negative self-Exts, and a Fourier transform controlled by a single determinantal degeneracy problem rather than by the split profile `3,11,11,3`.

This is currently the most concrete surviving path toward a Fourier-compatible gluable object.

## 7. Falsifiable milestones

The construction now has three precise tests.

### Milestone A — maximal Kodaira--Spencer rank

Find three deformation classes for which

\[
H^2(\Omega_D^1\otimes P)
\to
H^3(\mathcal O_D^{\oplus3}\otimes P)
\]

is generically surjective.

Failure eliminates this model immediately.

### Milestone B — the middle determinant

Find

\[
\varepsilon\in H^1(\mathcal E\otimes\mathcal E\otimes K_D^{-1})
\]

such that

\[
\det(\partial_{\varepsilon,P})\not\equiv0.
\]

This would make `W_D` generically acyclic under degree-zero twists.

### Milestone C — Fourier gluable-ness

Compute the cohomology sheaves of

\[
\Phi(i_*W_D)[2]
\]

and test the negative cross-Exts with `i_*W_D`.

The local curve-edge obstruction from `rm-elementary-transform-no-go.md` and `markman-eprime-local-gluing-obstruction.md` is absent here because `W_D` is locally free on the divisor and no codimension-two curve modification is used.

## 8. Why this candidate is structurally different

The two previously rejected coherent couplings created a local `mathcal Ext^2` edge term supported on curves or gluing points. The bivector component was detected there before the global `B`-field could cancel it.

The present construction keeps the entire correction inside a locally free rank-12 bundle on one smooth divisor. Its complexity is encoded in deformation extensions of vector bundles, not in singular lower-dimensional support.

So the next obstruction, if one exists, must be genuinely global/Fourier-theoretic rather than the already-understood local conormal obstruction.