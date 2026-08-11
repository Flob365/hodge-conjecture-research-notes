# A genus-4 Jacobian realization of the corrected secant class

> **Status.** This note gives an explicit perfect complex with the corrected secant Chern character on a genus-4 Jacobian. Under the stated transverse genericity hypotheses, the same construction is simple and has no negative self-Exts. This does **not** prove semiregularity and therefore is not a proof of the Hodge conjecture.

## 1. The surface `W_2(C)` has exactly the needed degree-six term

Let `C` be a smooth non-hyperelliptic curve of genus `4`, let

\[
X=J(C),\qquad x=c_1(\Theta),
\]

and let

\[
W=W_2(C)\subset X
\]

be the Abel-Jacobi image of `C^(2)`. For a non-hyperelliptic curve the Abel-Jacobi map on `C^(2)` is an embedding, so `W` is a smooth surface.

The standard Poincare and symmetric-product formulas give

\[
[W]=\frac{x^2}{2},\qquad
K_W=x|_W+X_p,
\qquad
(i_W)_*[X_p]=[C]=\frac{x^3}{6},
\]

where `X_p` is the divisor `p+C` on `C^(2)`. Hence

\[
(i_W)_*K_W
=x[W]+[C]
=\frac{x^3}{2}+\frac{x^3}{6}
=\frac{2x^3}{3}.
\]

Moreover

\[
\chi(\mathcal O_W)=1-4+\binom42=3.
\]

Since `td(X)=1`, Grothendieck-Riemann-Roch gives

\[
\operatorname{ch}(\mathcal O_W)
=(i_W)_*\operatorname{td}(W).
\]

Consequently

\[
\boxed{
\operatorname{ch}(\mathcal O_W)
=\frac{x^2}{2}-\frac{x^3}{3}+\frac{x^4}{8}
}
\]

because `x^4/24` is the class of a point on a principally polarized abelian fourfold.

This is the key numerical improvement over the theta-complete-intersection ansatz: the ratio between the codimension-two and codimension-three terms is already the secant ratio.

## 2. Partial gluing of `d+1` translates

Set

\[
n=d+1.
\]

Choose general translates

\[
W_1,\ldots,W_n
\]

of `W`. Since

\[
[W]^2=\frac{x^4}{4},
\]

every pair of general translates meets transversely in

\[
\int_X\frac{x^4}{4}=6
\]

reduced points. General translates can also be chosen with no triple intersections.

For every unordered pair `{i,j}`, choose exactly two of the six points of `W_i cap W_j`. Let `S` be the set of all selected points. Then

\[
|S|=2\binom n2=n(n-1)=d(d+1).
\]

Put

\[
N=\bigoplus_{i=1}^n\mathcal O_{W_i}.
\]

Define an evaluation-difference map

\[
\delta:N\longrightarrow
Q:=\bigoplus_{p\in S}\mathcal O_p
\]

by sending a local tuple of functions to the difference of the two branch values at every selected intersection point. Set

\[
G:=\ker(\delta).
\]

Thus `G` is a finite partial normalization of the full union: at two points per pair the branches are glued, while at the remaining four points they stay separated.

The exact sequence

\[
0\to G\to N\to Q\to0
\]

gives

\[
\operatorname{ch}(G)
=n\operatorname{ch}(\mathcal O_W)-n(n-1)\frac{x^4}{24}.
\]

Using the boxed formula above,

\[
\boxed{
\operatorname{ch}(G)
=\frac n2x^2-\frac n3x^3+\frac{n(4-n)}{24}x^4
}
\]

or, with `n=d+1`,

\[
\operatorname{ch}(G)
=\frac{d+1}{2}x^2
-\frac{d+1}{3}x^3
-\frac{(d-3)(d+1)}{24}x^4.
\]

## 3. The explicit perfect complex

The restriction map

\[
\mathcal O_X\longrightarrow N
\]

lands in `G`, because a single ambient function has the same value on both branches at every selected intersection point. Define the two-term complex

\[
F_d=[\mathcal O_X\longrightarrow G]
\]

with `O_X` in degree `0` and `G` in degree `1`, and finally set

\[
E_d:=F_d\otimes\mathcal O_X(\Theta).
\]

Since `X` is smooth, every coherent sheaf has a finite locally free resolution, hence `E_d` is perfect.

Its K-class is

\[
[F_d]=[\mathcal O_X]-[G],
\]

so

\[
\operatorname{ch}(E_d)
=e^x(1-\operatorname{ch}(G)).
\]

Substitution yields the exact identity

\[
\boxed{
\operatorname{ch}(E_d)
=1+x-\frac d2x^2-\frac d6x^3+\frac{d^2}{24}x^4.
}
\]

Thus the corrected rational secant character is realized by a single integral perfect complex on a special principally polarized abelian fourfold.

### Small cases

For `d=3`, `n=4`. There are six pairs of surfaces and `36` transverse intersection points. We glue `12` of them and leave `24` normalized.

For `d=5`, `n=6`. There are fifteen pairs and `90` transverse intersection points. We glue `30` and leave `60` normalized.

The point-gluing length is exactly

\[
d(d+1),
\]

the quadratic scale that appeared independently in the Euler-characteristic filter.

## 4. Cohomology sheaves and a local model

Let

\[
Z=\bigcup_iW_i.
\]

The image of `O_X -> G` is the ordinary structure sheaf `O_Z`. Therefore

\[
\mathcal H^0(F_d)=I_Z,
\qquad
\mathcal H^1(F_d)=T:=G/\mathcal O_Z.
\]

At each pair `W_i,W_j`, the full union glues all six intersection points while `G` glues only two. Hence

\[
\operatorname{length}(T)
=4\binom n2
=2n(n-1)
=2d(d+1).
\]

At an unglued transverse point the completed local model is

\[
R=k[[x_1,x_2,x_3,x_4]],
\quad
A=R/(x_1,x_2),
\quad
B=R/(x_3,x_4),
\]

and

\[
F_{d,p}\simeq[R\to A\oplus B].
\]

Writing

\[
I=(x_1,x_2)\cap(x_3,x_4)
=(x_1,x_2)(x_3,x_4),
\]

there is an exact sequence

\[
0\to I\to R\to A\oplus B\to k\to0.
\]

Thus the local Postnikov class is a two-extension

\[
\varepsilon_p\in\operatorname{Ext}^2_R(k,I).
\]

It is nonzero. Indeed, if `S=R/I`, the sequence

\[
0\to S\to A\oplus B\to k\to0
\]

does not split because `A\oplus B` has zero socle. Since `R` is regular of dimension four,

\[
\operatorname{Ext}^i_R(k,R)=0\qquad(i<4),
\]

so the connecting map identifies this nonsplit class with `epsilon_p` in `Ext^2_R(k,I)`.

The same two exact sequences give

\[
\operatorname{depth}(S)=1,
\qquad
\operatorname{depth}(I)=2.
\]

Therefore

\[
\operatorname{Hom}_R(k,I)=0,
\qquad
\operatorname{Ext}^1_R(k,I)=0.
\]

## 5. Simplicity and vanishing of negative Exts

Assume all unglued points are distinct, as guaranteed by the no-triple-intersection hypothesis. Then

\[
T=\bigoplus_{p\in U}k_p.
\]

Globally,

\[
\operatorname{Hom}(T,I_Z)=0,
\qquad
\operatorname{Ext}^1(T,I_Z)=0.
\]

Also

\[
\operatorname{End}(I_Z)=\mathbf C.
\]

Indeed `I_Z` is rank-one torsion-free with reflexive hull `O_X`; an endomorphism is multiplication by a rational function regular in codimension one, hence regular on the smooth variety `X`, and `H^0(O_X)=C`.

The hyper-Ext spectral sequence for an object with only `H^0=I_Z` and `H^1=T` now gives

\[
\operatorname{Ext}^{<0}(F_d,F_d)=0.
\]

For degree zero it gives the kernel of

\[
\operatorname{End}(I_Z)\oplus\operatorname{End}(T)
\longrightarrow
\operatorname{Ext}^2(T,I_Z),
\]

where a pair of scalars acts on the Postnikov class. Since every local component `epsilon_p` is nonzero, compatibility forces the scalar on every skyscraper summand to equal the scalar on `I_Z`. Hence

\[
\boxed{
\operatorname{Hom}(E_d,E_d)=\mathbf C,
\qquad
\operatorname{Ext}^{<0}(E_d,E_d)=0.
}
\]

This completes the first construction milestone from `research-program.md` on a genus-4 Jacobian.

## 6. A symmetry obstruction for this particular ansatz

The construction does **not** automatically solve the equivariant semiregularity problem.

Suppose the translates `W_i` have trivial translation stabilizer, as happens for a general genus-4 Jacobian choice. Any translation-tensorization symmetry of `E_d` is determined by its translation part: comparing the double dual of `H^0(E_d)=I_Z tensor O(Theta)` forces the tensor factor to compensate the translated determinant. Hence the translation projection is injective.

The translation part must preserve the union of the `n=d+1` irreducible components. Because no nontrivial translation fixes an individual `W_i`, the induced action on the set of components is free. Therefore every such finite symmetry group `H` satisfies

\[
|H|\le n=d+1
\]

(and in fact `|H|` divides `n`).

So this `W_2` partial-normalization model cannot carry the target symmetry of order `d(d+1)` when the component stabilizers are trivial.

For `d=3`, the maximal possible component-permuting translation symmetry has order `4`. Under the standard fixed-point/Lefschetz trace vanishing assumption for nonidentity translations,

\[
\chi(E_3,E_3)^H=\frac{8\cdot3\cdot4}{4}=24.
\]

If the infinitesimal `(X times X-hat)` stabilizer is finite, the usual eight-dimensional translation-tensorization orbit contributes at least eight invariant first-order deformations. Serre duality would then force

\[
\dim\operatorname{Ext}^2(E_3,E_3)^H
\ge 24-2+2\cdot8=38,
\]

which is larger than

\[
\dim HH_{-2}(X)=28.
\]

Thus, under those standard trace and stabilizer hypotheses, the present `W_2` model cannot be equivariantly semiregular. This is useful: it isolates the next design requirement. A successful object must keep the exact `W_2`-type numerical correction while admitting genuinely larger symmetry, for example through full-support monad terms or building blocks with nontrivial finite translation stabilizers.

## 7. What has actually advanced

This construction changes the research program in two concrete ways.

1. The corrected secant K-class is no longer merely a virtual rational combination of complete intersections: it is realized by one explicit integral perfect complex.
2. Simplicity and negative-Ext vanishing can be checked locally and hold in the transverse model.
3. The obstruction has moved to the genuinely hard step: obtaining enough finite symmetry to make equivariant semiregularity numerically possible.

The next target should therefore be **an isogeny-stabilized or full-support variant of this complex**, not another attempt to repair the Chern character.