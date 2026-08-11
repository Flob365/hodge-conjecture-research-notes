# A falsifiable research program

## Problem 1 — realize the corrected class by a simple object

Construct a perfect complex or monad (E_d\) on a principally polarized abelian fourfold such that

\[
[E_d]=V_d
\]

for the corrected virtual class in the main README, and such that

\[
\operatorname{Hom}(E_d,E_d)=\mathbf C,
\qquad
\operatorname{Ext}^{<0}(E_d,E_d)=0.
\]

The naive direct sum of shifted structure sheaves is not acceptable: it has many idempotents and a large obstruction space. The differentials must genuinely couple the codimension-two, codimension-three, and codimension-four terms.

### Falsifiable milestone

For a fixed small odd value such as (d=3\) or (d=5\), write an explicit quiver/monad and compute its derived endomorphism algebra. Failure of simplicity or the presence of negative Ext groups eliminates the model before any deformation argument.

## Problem 2 — introduce quadratic symmetry

Seek a finite group

\[
G\subset X\times\widehat X
\]

acting by translation and tensorization, of order on the scale (d^2\), and a (G)-linearization of (E_d\).

A numerically convenient target is

\[
|G|=d(d+1),
\]

because the expected Euler characteristic

\[
\chi(E_d,E_d)=8d(d+1)
\]

then has quotient (8\). This merely passes a dimension filter; it does not prove that such a group action or object exists.

### Falsifiable milestone

Compute the categorical trace of every nonidentity group element on (R\!\operatorname{End}(E_d)\). If the invariant Euler characteristic is not the desired quotient or is nonintegral, reject the action.

## Problem 3 — test equivariant semiregularity

Compute

\[
\sigma_{E_d}:\operatorname{Ext}^2(E_d,E_d)^G
\longrightarrow HH_{-2}(X)^G.
\]

For an abelian fourfold,

\[
\dim HH_{-2}(X)=6+16+6=28.
\]

The first necessary check is therefore

\[
\dim\operatorname{Ext}^2(E_d,E_d)^G\le28.
\]

The actual requirement is injectivity of the semiregularity map, not merely the dimension inequality.

### Falsifiable milestone

Produce the matrix of \(\sigma_{E_d}\) under HKR and verify its rank exactly for one small (d\).

## Problem 4 — connect the object to formal (K)-theory

If (E_d\) is equivariantly semiregular, deform it along the relevant Hodge locus. Its compatible infinitesimal (K_0\)-classes must coincide with the unique (D)-fixed formal lift from the Bloch–Esnault–Kerz calculation.

This would supply precisely the compatible perfect object that formal (K)-theory alone does not produce.

## Problem 5 — the general hypersurface route

For a primitive Hodge class \(\alpha\), define the span of all defect classes

\[
\mathcal D_L=
\operatorname{span}\{\Gamma_Y(C_Y):Y\in|L^d|, d\ge1\}.
\]

The decisive statement would be

\[
H^{2n}(X,\mathbf Q)_{\mathrm{prim}}\cap H^{n,n}
\subseteq \mathcal D_L.
\]

For nodal (Y\), this becomes the construction of a relation among vanishing cycles whose associated defect class pairs nontrivially with \(\alpha\).

This target is deliberately stated as a concrete spanning problem. It should not be mistaken for a shortcut: proving it may encode most of the original conjecture.

