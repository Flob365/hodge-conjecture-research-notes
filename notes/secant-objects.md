# Secant objects and Chern-character constraints

## The rational secant class

Let ((X,\Theta)) be a principally polarized abelian fourfold and let (d>0) be odd. Put (x=\Theta) and (s^2=-d). Define

\[
\alpha=\frac{e^{sx}+e^{-sx}}2,
\qquad
\beta=\frac{e^{sx}-e^{-sx}}{2s}.
\]

Modulo (x^5),

\[
\alpha+\beta
=1+x-\frac d2x^2-\frac d6x^3+\frac{d^2}{24}x^4.
\]

Any class in the two-dimensional secant span having rank (1) and first Chern class (x) must equal \(\alpha+\beta\).

## Degree-four audit of the cyclic candidate

For surfaces (Z_i=D_i\cap D_{i+1}) formed from translates of (Theta), let (Z=\bigcup_{i=1}^nZ_i\). A finite partial normalization supported at points does not alter \(\operatorname{ch}_2\), so

\[
\operatorname{ch}_2(\nu_*\mathcal O_{\widetilde Z})=[Z]=n x^2.
\]

Consequently, up to an overall cohomological sign,

\[
\operatorname{ch}_{\le2}\left(
[\mathcal O_X\to\nu_*\mathcal O_{\widetilde Z}]\otimes\mathcal O_X(\Theta)
\right)
=1+x+\left(\frac12-n\right)x^2.
\]

Comparison with \(\alpha+\beta\) forces

\[
n=\frac{d+1}{2}.
\]

The value (n=(d+9)/2) printed in Markman's arXiv:2509.23403v2 differs by four surface classes. This is an audit of the formula as written; an omitted codimension-two correction could change the conclusion.

## Obstruction for every graph-type construction

Let \(\Gamma\) be a simple graph. Associate a theta translate (D_v) to each vertex and a surface \(D_u\cap D_v\) to each edge. Assume transverse intersections and modifications only at finitely many points. Let

\[
e=|E(\Gamma)|,
\qquad
w=\sum_v\binom{\deg(v)}2-\#\{\text{triangles}\}.
\]

The quantity (w\) is nonnegative. Inclusion–exclusion through codimension three yields

\[
\operatorname{ch}(\mathcal O_Z)
=e x^2-(e+w)x^3+O(x^4).
\]

For

\[
E=(\mathcal O_X-\nu_*\mathcal O_{\widetilde Z})e^x,
\]

we obtain

\[
\operatorname{ch}_2(E)=\left(\frac12-e\right)x^2,
\qquad
\operatorname{ch}_3(E)=\left(\frac16+w\right)x^3.
\]

The secant character would require

\[
e=\frac{d+1}{2},
\qquad
w=-\frac{d+1}{6},
\]

which is impossible. Point normalizations cannot fix a codimension-three discrepancy.

## Corrected virtual class

For a transverse codimension-(r) theta complete intersection, set

\[
B_r=e^x(1-e^{-x})^r.
\]

Modulo (x^5),

\[
B_2=x^2+\frac{x^4}{12},
\quad
B_3=x^3-\frac{x^4}{2},
\quad
B_4=x^4.
\]

Then

\[
V=e^x-\frac{d+1}{2}B_2-\frac{d+1}{6}B_3
+\frac{(d-2)(d+1)}{24}B_4
\]

satisfies

\[
\operatorname{ch}(V)=\alpha+\beta.
\]

The coefficient of (B_4) corresponds to total point length \((d-2)(d+1)\). This is a quadratic contribution and suggests that a viable equivariant object will need quadratic, rather than cyclic-linear, symmetry.

## Semiregularity filter

Perry's equivariant semiregularity theorem gives a sufficient deformation criterion through injectivity on an invariant obstruction space. For a hypothetical simple equivariant object (E), an Euler-characteristic estimate can be used as a preliminary filter, but only under additional hypotheses:

- the relevant translation–tensorization action must be genuinely linearized;
- its categorical Lefschetz traces must vanish away from the identity;
- the infinitesimal (X\times\widehat X)-stabilizer must be finite to obtain the full lower bound on invariant \(\operatorname{Ext}^1\).

These hypotheses do not hold automatically for the printed rank-one cyclic object. In particular, a pure nontrivial translation cannot preserve the determinant \(\mathcal O_X(\Theta)\) on a principally polarized abelian variety. Any dimension bound should therefore be treated as a design constraint, not as an unconditional theorem about that candidate.

