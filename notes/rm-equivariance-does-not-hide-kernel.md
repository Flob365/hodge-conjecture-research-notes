# Why translation--tensorization equivariance does not hide the two RM kernel directions

> **Status.** This note rules out one tempting use of a large isogeny stabilizer: for the translation--tensorization groups appearing in Perry's clean abelian equivariant theorem, the two mixed RM deformation directions cannot simply be made non-invariant. A separate Fourier--Mukai idea survives only as a more technical speculative variant.

## 1. Perry's clean abelian theorem

Perry's Theorem 1.2 in arXiv:2604.00511v2 considers a finite group

\[
G\subset X\times X^\vee
\]

acting on `Dperf(X)` through translations and tensoring by degree-zero line bundles. If a perfect complex is weakly `G`-semiregular, has no negative self-Exts, and its twisted Chern character remains Hodge, then it deforms as a twisted perfect complex and the class remains algebraic.

This theorem is exactly why the `m^8` tensor stabilizer in `rm-smooth-isogeny-scaffold.md` is potentially useful.

However, it does **not** automatically remove the two generalized kernel directions from the semiregularity problem.

## 2. Connected autoequivalences act trivially on the generalized tangent cohomology

Translations act trivially on the cohomology of an abelian variety. Tensorization by a line bundle `P in Pic^0(X)` has

\[
ch(P)=1
\]

in rational cohomology, and its induced cohomological/Hochschild action is likewise trivial on the generalized deformation space

\[
HT^2(X)=H^2(O_X)\oplus H^1(T_X)\oplus H^0(\wedge^2T_X).
\]

Thus a finite subgroup of the identity component

\[
X\times X^\vee
\]

acts trivially on `HT^2(X)`.

## 3. Naturality forces Atiyah images to be invariant

Let `E` carry a genuine `G`-equivariant structure. The Hochschild/Atiyah action

\[
at_E:HT^2(X)\longrightarrow Ext^2(E,E)
\]

is natural with respect to autoequivalences. Hence it is `G`-equivariant.

Since `G` acts trivially on the source, its image lies in the invariant obstruction space:

\[
\boxed{
im(at_E)\subseteq Ext^2(E,E)^G.}
\]

In particular, if one of the two RM classes

\[
\xi_+=B_+-q^{-1}P_+,
\qquad
\xi_-=B_--q^{-1}P_-
\]

has nonzero Atiyah image, that image is itself `G`-invariant.

Therefore ordinary `G`-semiregularity cannot evade the issue: injectivity of semiregularity on `Ext^2(E,E)^G` would still force

\[
at_E(\xi_+)=at_E(\xi_-)=0
\]

because their Chern action vanishes.

This does not prove that **weak** `G`-semiregularity is impossible without killing them, because weak semiregularity is formulated in the invariant category and is genuinely weaker. But there is no simple representation-theoretic argument that the two directions disappear merely because the tensor stabilizer is large.

## 4. A special `q=1` Fourier--Mukai possibility

Markman's genus-4 real-quadratic example allows `q` to be a positive integer. The specialization

\[
q=1,
\qquad
K=F(i)
\]

is therefore allowed at the level of the secant construction.

Then the two generalized Chern-kernel vectors become

\[
\xi_+=B_+-P_+,
\qquad
\xi_-=B_--P_-.
\]

Under the standard cohomological action of a Fourier transform on a principally polarized abelian variety, `B`-field and bivector directions are exchanged (up to HKR/sign conventions). Thus these differences are natural candidates for anti-invariant directions under a Fourier-type involution.

This observation is potentially useful because Perry's **general** equivariant theorem is formulated for suitable finite group actions on categories, not only the translation--tensorization special case.

However, this route has two extra obligations:

1. construct a finite Fourier--Mukai group action preserving the candidate object, with all categorical coherence data;
2. verify that the invariant category is of the geometric origin required by Perry's general theorem and that the relevant weak semiregularity condition really discards the anti-invariant directions.

Until those points are checked, the `q=1` Fourier idea is a secondary speculative route, not a solution of the two-direction problem.

## 5. Design consequence

For the main line of attack, keep the isogeny stabilizer for what it genuinely provides:

- a large finite symmetry useful for reducing invariant Ext dimensions;
- possible access to Perry's weak equivariant semiregularity theorem.

But do **not** count it as a mechanism that automatically kills the two mixed Atiyah obstructions.

The primary target remains a coupled object in which those two obstructions vanish at the object level. The `q=1` Fourier symmetry should be developed in parallel only if the coupling approach stalls.
