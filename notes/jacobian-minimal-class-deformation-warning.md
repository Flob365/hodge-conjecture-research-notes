# Why the Jacobian `W_2` block should not be expected to follow every RM deformation

> **Status.** This note records a deformation-theoretic warning from known results on minimal cohomology classes. It does not prove that Markman's secant sheaf itself fails to deform outside the Jacobian locus; a sheaf can in principle deform while losing the visible `W_2` presentation.

## 1. The relevant theorem

For a smooth non-hyperelliptic curve `C`, Lombardi--Tirabassi prove that the infinitesimal deformations of the Brill--Noether locus

\[
W_d(C)\subset J(C)
\]

are in one-to-one correspondence with the deformations of `C`.

They further show that if a Jacobian deforms together with a minimal cohomology class out of the Jacobian locus, then the Jacobian must be hyperelliptic.

Reference:

- L. Lombardi, S. Tirabassi, *Deformations of minimal cohomology classes on abelian varieties*, arXiv:1410.7986.

This fits the older global rigidity theorem of Debarre: on a Jacobian, effective cycles of minimal class are translates of the expected Brill--Noether loci, and the Jacobian locus is an irreducible component of the locus of ppavs carrying such effective minimal classes.

Reference:

- O. Debarre, *Minimal Cohomology Classes and Jacobians*, arXiv:alg-geom/9301002.

## 2. Consequence for the present RM program

The ordinary Chern-action kernel of the real-multiplication secant class contains a six-dimensional subspace

\[
\operatorname{Sym}^2(U_1)\oplus\operatorname{Sym}^2(U_2).
\]

It is tempting to try to put these six directions in the Atiyah kernel of Markman's Jacobian-specific sheaf simply by deforming every ingredient of its `W_2` construction.

The minimal-class deformation theorem shows why this is not automatic. If an ordinary RM tangent direction leaves the Jacobian locus, one cannot expect the embedded `W_2(C)` itself to deform along that direction in the same geometric form.

Therefore the implication

\[
\text{RM direction preserves the Hodge class of }W_2
\Longrightarrow
\text{the geometric }W_2\text{ construction deforms}
\]

is false in general as a proof principle.

## 3. Important limitation

This does **not** imply

\[
at_{F'}(\xi)\ne0
\]

for Markman's sheaf `F'` in a direction `xi` transverse to the Jacobian locus.

The sheaf may have deformations which do not preserve a presentation in terms of a visible minimal-class surface. Thus Lombardi--Tirabassi obstruct the naive **presentation-preserving** argument, not the existence of a more subtle deformation of the secant sheaf.

A direct calculation of the Atiyah map could still show a larger kernel.

## 4. Why the universal RM class helps

The construction in [`rm-universal-integral-perfect-class.md`](rm-universal-integral-perfect-class.md) uses only:

- the RM divisor classes `g^*Theta` and `(g^{-1})^*Theta`;
- line bundles with those first Chern classes;
- generic translates of ample divisors;
- Koszul complete intersections.

Those ingredients are not tied to the Jacobian locus. Consequently they provide a cleaner starting point for trying to realize all six ordinary RM infinitesimal directions by actual relative perfect complexes.

The cost is that the obvious representative is decomposable. The remaining research problem is therefore categorical rather than Hodge-theoretic: couple the universal blocks without destroying their family-wise deformation behavior.

## 5. Revised design principle

A robust RM candidate should satisfy two independent portability tests:

1. **ordinary portability:** its geometric ingredients exist relatively over the full six-dimensional RM polarized infinitesimal locus, not merely over the Jacobian sublocus;
2. **generalized cancellation:** the two mixed `B`-field/bivector directions must vanish under the Atiyah map at the coupled-object level.

The Jacobian `W_2` construction is still valuable as an existence model for simple secant sheaves, but it should no longer be the only geometric scaffold used for the deformation argument.
