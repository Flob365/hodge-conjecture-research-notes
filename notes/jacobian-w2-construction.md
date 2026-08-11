# Genus-4 Jacobian `W_2` model: prior art and local Ext analysis

> **Status and attribution.** The partial-normalization construction below is **not new**: it is essentially Markman's Example 8.2.3 in arXiv:2502.03415v2. Markman takes `d+1` translates of `W_2(C)`, notes that every pair meets in six points, and resolves four of those six points; equivalently, two points per pair remain glued. The independently derived calculation in this repository recovers the same K-class. What is retained here as useful additional bookkeeping is the explicit local Postnikov model used to test simplicity and negative self-Exts. No novelty claim is made for the K-theoretic construction.

## 1. Numerical input from `W_2(C)`

Let `C` be a smooth non-hyperelliptic curve of genus `4`,

\[
X=J(C),\qquad x=c_1(\Theta),
\]

and let

\[
W=W_2(C)\subset X.
\]

The standard Poincare and symmetric-product formulas give

\[
[W]=\frac{x^2}{2},
\qquad
(i_W)_*K_W=\frac{2x^3}{3},
\qquad
\chi(\mathcal O_W)=3.
\]

Since `td(X)=1`, GRR gives

\[
\boxed{
\operatorname{ch}(\mathcal O_W)
=\frac{x^2}{2}-\frac{x^3}{3}+\frac{x^4}{8}.
}
\]

This is the useful numerical feature of `W_2`: the codimension-two and codimension-three coefficients already occur in the ratio required by the secant class.

## 2. Markman's partial-normalization construction

Set

\[
n=d+1.
\]

Choose general translates

\[
W_1,\ldots,W_n
\]

with no triple intersections. Since

\[
[W]^2=\frac{x^4}{4},
\]

each pair meets transversely in six reduced points.

Markman's Example 8.2.3 partially normalizes the union by resolving four of the six points for every pair. Equivalently, one can describe the resulting sheaf by keeping exactly two points per pair glued.

Let

\[
N=\bigoplus_{i=1}^n\mathcal O_{W_i},
\]

choose two intersection points for every unordered pair, and let

\[
\delta:N\longrightarrow
Q:=\bigoplus_{p\in S}\mathcal O_p
\]

be the difference-of-branch-values map at the chosen points. Put

\[
G:=\ker(\delta).
\]

Then

\[
|S|=2\binom n2=n(n-1)=d(d+1)
\]

and

\[
\operatorname{ch}(G)
=n\operatorname{ch}(\mathcal O_W)
-n(n-1)\frac{x^4}{24}.
\]

Hence

\[
\operatorname{ch}(G)
=\frac n2x^2-\frac n3x^3+rac{n(4-n)}{24}x^4.
\]

Define

\[
F_d=[\mathcal O_X\to G],
\qquad
E_d=F_d\otimes\mathcal O_X(\Theta).
\]

The exact Chern-character calculation is

\[
\boxed{
\operatorname{ch}(E_d)
=1+x-\frac d2x^2-\frac d6x^3+\frac{d^2}{24}x^4.
}
\]

This is the same corrected secant character already realized in Markman's Example 8.2.3.

Primary reference: E. Markman, *The Hodge conjecture for abelian fourfolds*, arXiv:2502.03415v2, Example 8.2.3.

## 3. Cohomology sheaves

Let

\[
Z=\bigcup_iW_i.
\]

The image of `O_X -> G` is `O_Z`. Therefore

\[
\mathcal H^0(F_d)=I_Z,
\qquad
\mathcal H^1(F_d)=T:=G/\mathcal O_Z.
\]

At every pair of surfaces, four of the six intersection points are normalized. Thus

\[
\operatorname{length}(T)
=4\binom n2
=2n(n-1)
=2d(d+1).
\]

Under the no-triple-intersection hypothesis,

\[
T=\bigoplus_{p\in U}k_p.
\]

## 4. Local Postnikov model

At one normalized transverse point the completed local model is

\[
R=k[[x_1,x_2,x_3,x_4]],
\quad
A=R/(x_1,x_2),
\quad
B=R/(x_3,x_4),
\]

with

\[
F_{d,p}\simeq[R\to A\oplus B].
\]

Write

\[
I=(x_1,x_2)\cap(x_3,x_4)
=(x_1,x_2)(x_3,x_4).
\]

There is an exact sequence

\[
0\to I\to R\to A\oplus B\to k\to0.
\]

Thus the local object has a two-extension class

\[
\varepsilon_p\in\operatorname{Ext}^2_R(k,I).
\]

It is nonzero: the induced short exact sequence

\[
0\to R/I\to A\oplus B\to k\to0
\]

does not split, while regularity of `R` identifies this class with the corresponding element of `Ext^2_R(k,I)`.

The same sequences give

\[
\operatorname{depth}(I)=2,
\]

hence

\[
\operatorname{Hom}_R(k,I)=0,
\qquad
\operatorname{Ext}^1_R(k,I)=0.
\]

## 5. Simplicity / negative-Ext check

Globally the preceding local calculation gives

\[
\operatorname{Hom}(T,I_Z)=0,
\qquad
\operatorname{Ext}^1(T,I_Z)=0.
\]

Moreover

\[
\operatorname{End}(I_Z)=\mathbf C
\]

because `I_Z` is rank-one torsion-free with reflexive hull `O_X`.

The hyper-Ext spectral sequence for the two cohomology sheaves then yields

\[
\operatorname{Ext}^{<0}(F_d,F_d)=0.
\]

For degree zero, compatibility with the nonzero local Postnikov classes forces the scalar acting on each skyscraper summand of `T` to equal the scalar acting on `I_Z`. Consequently, under the stated transverse hypotheses,

\[
\boxed{
\operatorname{Hom}(E_d,E_d)=\mathbf C,
\qquad
\operatorname{Ext}^{<0}(E_d,E_d)=0.
}
\]

This local derived-endomorphism check is the part of the note that remains useful independently of the already-known Chern-character construction.

## 6. Why this model is not the final RM solution

If the individual `W_2` translates have trivial translation stabilizer, a finite translation group preserving the union must act freely on the `d+1` irreducible components. Its order is therefore at most `d+1`.

So the construction is excellent for realizing the K-class but does not naturally provide the much larger symmetry sought in the earlier equivariant-semiregularity design.

The current research program has therefore moved to the real-multiplication scaffold in:

- [`real-multiplication-infinitesimal-kernel.md`](real-multiplication-infinitesimal-kernel.md);
- [`rm-smooth-isogeny-scaffold.md`](rm-smooth-isogeny-scaffold.md).

Those notes isolate an eight-dimensional infinitesimal kernel and construct a deformation-friendly perfect complex with the exact RM secant character and no negative self-Exts.