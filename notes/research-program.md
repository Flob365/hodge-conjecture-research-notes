# A falsifiable research program

## Problem 1 — realize the corrected class by a simple object

Construct a perfect complex or monad `E_d` on a principally polarized abelian fourfold such that

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

### Current status

The genus-4 Jacobian `W_2` partial-normalization construction in [`jacobian-w2-construction.md`](jacobian-w2-construction.md) realizes the corrected Chern character by one explicit integral perfect complex. Under the transverse no-triple-intersection hypotheses, the local Postnikov calculation gives

\[
\operatorname{Hom}(E_d,E_d)=\mathbf C,
\qquad
\operatorname{Ext}^{<0}(E_d,E_d)=0.
\]

Thus the original first construction milestone is achieved on this special Jacobian model. Its defect is symmetry, not K-theory realization.

## Problem 2 — introduce quadratic symmetry

Seek a finite group

\[
G\subset X\times\widehat X
\]

acting by translation and tensorization, of order on the scale `d^2`, and a `G`-linearization of `E_d`.

A numerically convenient target is

\[
|G|=d(d+1),
\]

because the expected Euler characteristic

\[
\chi(E_d,E_d)=8d(d+1)
\]

then has quotient `8`. This merely passes a dimension filter; it does not prove that such a group action or object exists.

### Eliminated sub-ansatz: scalar semihomogeneous monads

A natural attempt is to replace the support-permuting `W_2` object by a full-support monad whose terms are simple semihomogeneous bundles of scalar rational slopes `a_i/b_i`.

This entire termwise-equivariant scalar ansatz fails the quadratic symmetry target. The Chern-character condition is equivalent to the integral binary-quartic identity

\[
s^4+4s^3t-6d s^2t^2-4d st^3+d^2t^4
=\sum_i c_i(b_i s+a_i t)^4.
\]

If the common finite intersection of the Mukai stabilizer graphs is `X[N]`, then the first two moments force all slopes to be congruent to slope `1` modulo `N`. The resulting quartic congruences imply a lower bound on `d+1` of at least `(3/2)N^4` in the weakest case, while

\[
|X[N]|=N^8.
\]

Consequently

\[
|X[N]|<d(d+1).
\]

See [`semihomogeneous-monad-obstruction.md`](semihomogeneous-monad-obstruction.md) and the accompanying verifier.

This is a no-go for the **design target**, not a theorem that smaller symmetry groups can never be semiregular.

### Surviving symmetry target: non-scalar endomorphisms

The next serious construction should exploit real multiplication. Replace scalar integer pairs `(a,b)` by endomorphism pairs in an order `O_F` of a real quadratic field. The common stabilizer is then controlled by kernels and norms of non-scalar endomorphisms rather than by one integer torsion level `N`; the scalar quartic congruence obstruction does not apply verbatim.

This is aligned with Markman's genus-4 real-multiplication secant examples, where the appropriate semiregularity remains open.

### Falsifiable milestone

For one real quadratic order, preferably the smallest discriminants first:

1. write the analogue of the five Chern moments over `O_F`;
2. construct a signed semihomogeneous decomposition of the secant class;
3. compute the common finite stabilizer exactly as a kernel of endomorphisms;
4. compare its order with `d(d+1)`;
5. reject the model immediately if the symmetry/Euler quotient remains too large.

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

Perry's 2026 equivariant semiregularity theorem is important here because it applies directly to equivariant perfect complexes; a successful construction need not first be converted into a coherent secant sheaf.

### Falsifiable milestone

Produce the matrix of `sigma_{E_d}` under HKR and verify its rank exactly for one small arithmetic model.

## Problem 4 — connect the object to formal K-theory

If `E_d` is equivariantly semiregular, deform it along the relevant Hodge locus. Its compatible infinitesimal `K_0`-classes must coincide with the unique `D`-fixed formal lift from the Bloch--Esnault--Kerz calculation.

This would supply precisely the compatible perfect object that formal K-theory alone does not produce.

## Problem 5 — the general hypersurface route

For a primitive Hodge class `alpha`, define the span of all defect classes

\[
\mathcal D_L=
\operatorname{span}\{\Gamma_Y(C_Y):Y\in|L^d|, d\ge1\}.
\]

The decisive statement would be

\[
H^{2n}(X,\mathbf Q)_{\mathrm{prim}}\cap H^{n,n}
\subseteq \mathcal D_L.
\]

For nodal `Y`, this becomes the construction of a relation among vanishing cycles whose associated defect class pairs nontrivially with `alpha`.

This target is deliberately stated as a concrete spanning problem. It should not be mistaken for a shortcut: proving it may encode most of the original conjecture.
