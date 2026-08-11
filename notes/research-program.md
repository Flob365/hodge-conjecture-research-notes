# A falsifiable research program

## Current state of the attack

The real-multiplication route has now become much more sharply constrained.

Established inside these notes:

1. the target RM secant Chern character is explicit;
2. its infinitesimal Chern-action map on `HT^2` has rank exactly `20` and kernel exactly `8` dimensional;
3. six kernel directions are ordinary RM deformations;
4. the remaining two are mixed `B`-field/bivector directions;
5. scalar semihomogeneous monads cannot provide the previously targeted large common torsion symmetry;
6. ordinary curve elementary transforms cannot kill both mixed directions locally;
7. ordinary divisor--curve point gluing of the type used in Markman's explicit `E'` candidate also cannot kill both mixed directions in the generic smooth/reduced local model;
8. the `q=1` specialization has an exact Fourier symmetry: the secant class is Fourier-even while the two mixed directions are Fourier-odd;
9. a new Kodaira--Spencer vector-bundle construction keeps the pure divisor Chern character while reducing the generic Fourier cohomology profile from `3,11,11,3` to one square `8N x 8N` determinant.

The active frontier is therefore no longer the Chern character or a local curve correction. It is a **global vector-bundle/Fourier coupling problem on one smooth divisor**.

---

## Problem 1 — the exact RM infinitesimal kernel

Let

\[
\beta'=g^*\Theta-\frac q6(g^{-1})^*(\Theta^3).
\]

For nontrivial real multiplication, the exact exterior-algebra computation in
[`rm-semiregularity-kernel.md`](rm-semiregularity-kernel.md) gives

\[
\boxed{
\operatorname{rank}(\mu_{\beta'})=20,
\qquad
\dim\ker(\mu_{\beta'})=8.
}
\]

Up to the chosen HKR normalization,

\[
\ker(\mu_{\beta'})
=
\operatorname{Sym}^2(U_+)\oplus\operatorname{Sym}^2(U_-)
\oplus
\langle B_+-q^{-1}P_+,\ B_--q^{-1}P_-\rangle.
\]

For any candidate `E` with `ch(E)` a nonzero multiple of `beta'`, semiregularity on the Atiyah image is equivalent to

\[
\boxed{
\ker(at_E)=\ker(\mu_{\beta'}).
}
\]

Thus the target remains: put all eight displayed directions into the Atiyah kernel.

---

## Problem 2 — rejected local coherent couplings

### A. Elementary transforms along curves

The local model

\[
I=(y,z)\subset k[[w,x,y,z]]/(w)
\]

has

\[
\mathcal Ext^2(I,I)\cong I/I^2.
\]

The degree-two Atiyah square detects the bivector component before the global `B`-field can cancel it. On a simple RM fourfold, both `P_+` and `P_-` cannot vanish along one transverse correcting curve.

See [`rm-elementary-transform-no-go.md`](rm-elementary-transform-no-go.md).

### B. Markman's divisor--curve fiber gluing

At an ordinary gluing point of a smooth divisor and a smooth curve,

\[
M=R/(ab,ac,ad).
\]

Its minimal resolution has Betti numbers `1,3,3,1`. The local Atiyah square shows that Atiyah-vanishing for a bivector `P` forces the three-dimensional curve conormal space to be isotropic for `P`.

A three-plane cannot be simultaneously isotropic for both rank-two RM bivectors `P_+` and `P_-` in

\[
U_+^*\oplus U_-^*,
\qquad \dim U_+^*=\dim U_-^*=2.
\]

Therefore the generic smooth/reduced fiber-gluing architecture of Markman's Example 11.2.7 cannot satisfy the remaining semiregularity condition.

See [`markman-eprime-local-gluing-obstruction.md`](markman-eprime-local-gluing-obstruction.md).

**Important:** this rejects a local architecture, not Question 11.2.2 itself.

---

## Problem 3 — the surviving pure-divisor strategy

Let `D` be a smooth sufficiently positive divisor on the abelian fourfold and put

\[
K_D=\mathcal O_D(D).
\]

The old split bundle

\[
V_D=3\mathcal O_D\oplus\Omega_D^1\oplus\Omega_D^2\oplus3K_D
\]

satisfies

\[
\operatorname{ch}(i_*V_D)=12[D],
\]

but its generic degree-zero-twist cohomology profile is

\[
(3,11,11,3)N.
\]

### Kodaira--Spencer replacement

Choose three first-order deformation classes and form

\[
0\to\mathcal O_D^{\oplus3}\to\mathcal E\to\Omega_D^1\to0.
\]

Then

\[
0\to\Omega_D^2\to\Lambda^5\mathcal E\to K_D^{\oplus3}\to0
\]

and

\[
\boxed{
[\mathcal E]+[\Lambda^5\mathcal E]=[V_D].
}
\]

If the three Kodaira--Spencer maps have maximal generic rank, then

\[
(h^0,h^1,h^2,h^3)
\bigl((\mathcal E\oplus\Lambda^5\mathcal E)\otimes P\bigr)
=(0,8,8,0)N
\]

for general `P in Pic^0(X)`.

See [`rm-kodaira-spencer-divisor-bundle.md`](rm-kodaira-spencer-divisor-bundle.md).

---

## Problem 4 — one final determinant

Seek an extension

\[
0\to\mathcal E\to W_D\to\mathcal E^\vee\otimes K_D\to0.
\]

Its K-class remains `[V_D]`, so

\[
\operatorname{ch}(i_*W_D)=12[D].
\]

After the outer Kodaira--Spencer cancellation, the only remaining generic map is

\[
\partial_{\varepsilon,P}:
H^1(\mathcal E^\vee\otimes K_D\otimes P)
\longrightarrow
H^2(\mathcal E\otimes P),
\]

between two spaces of dimension `8N`.

The immediate target is therefore

\[
\boxed{
\det(\partial_{\varepsilon,P})\not\equiv0.
}
\]

This is currently the smallest surviving construction problem.

### Why this target is structurally promising

The two `8N` spaces are Serre-dual after `P <-> P^{-1}`. The final extension can therefore be searched for in a self-dual/symplectic or orthogonal subspace of

\[
H^1(\mathcal E\otimes\mathcal E\otimes K_D^{-1}).
\]

A single nonzero determinant at one generic `P` proves generic acyclicity of `W_D` under degree-zero twists.

---

## Problem 5 — multiplication-map / infinitesimal-Torelli input

The first maximal-rank requirement is not an isolated phenomenon. For smooth sufficiently positive hypersurfaces in simple abelian varieties, Green's method reduces infinitesimal Torelli to multiplication maps of sections; effective bounds are known.

The next technical task is to express the three Kodaira--Spencer maps in the same Jacobian-ring/multiplication formalism and prove that a general three-dimensional deformation subspace gives the required rank `3N`.

### Falsifiable milestone

Produce one smooth sufficiently positive `D` and three deformation classes for which

\[
H^2(\Omega_D^1\otimes P)
\to
H^3(\mathcal O_D^{\oplus3}\otimes P)
\]

is generically surjective.

If this fails, abandon the `3 -> 8` reduction.

---

## Problem 6 — the `q=1` Fourier symmetry

Specialize to

\[
q=1,
\qquad
\beta=A-\frac16C^3,
\]

with

\[
A=g^*\Theta,
\qquad
C=(g^{-1})^*\Theta.
\]

The cohomological Poincare Fourier transform satisfies

\[
\Phi^H(A)=-\frac16C^3,
\qquad
\Phi^H\left(\frac16C^3\right)=-A,
\]

hence

\[
\boxed{\Phi^H(\beta)=\beta.}
\]

Meanwhile the two unresolved directions

\[
B_+-P_+,
\qquad
B_--P_-
\]

are Fourier-odd.

See [`rm-q1-fourier-symmetry.md`](rm-q1-fourier-symmetry.md).

This remains the only mechanism found so far which separates the two mixed directions *before* the semiregularity map.

### Caveat

A Fourier-generated finite categorical action is outside the clean translation--tensorization special case of Perry's abelian theorem. The general equivariant theorem requires additional categorical/geometric-origin input.

---

## Problem 7 — symmetry by isogeny remains auxiliary

The smooth-isogeny scaffold still provides arbitrarily large tensor stabilizers after pushforward, but translation/tensorization actions are cohomologically trivial on the two mixed generalized directions. They cannot simply project those directions away.

Use isogenies for:

- positivity and smoothness of divisor constructions;
- finite symmetry after a successful local/global coupling;

not as a substitute for solving the mixed Atiyah problem.

---

## Problem 8 — connection to formal K-theory

If a coupled RM object is shown semiregular, compare its compatible infinitesimal K-classes with the unique `D`-fixed formal lift from
[`formal-k-theory.md`](formal-k-theory.md).

A match would connect the explicit geometric route to the formal-rigidity route.

---

## Problem 9 — independent hypersurface route

The vanishing-cycle/defect route remains logically independent and should be retained as a fallback if the RM secant construction ultimately encounters a global obstruction.

---

# Immediate next experiments

In order:

1. **prove or disprove maximal rank for three Kodaira--Spencer classes;**
2. compute the space
   \[
   H^1(\mathcal E\otimes\mathcal E\otimes K_D^{-1})
   \]
   and search for an extension with nonzero `8N x 8N` determinant;
3. compute `Phi(i_*W_D)[2]` once such a bundle is found;
4. only then reintroduce the `q=1` Fourier symmetry and finite-isogeny equivariance.

A failure at step 1 or 2 is immediately falsifiable. A success at both would remove the last known local obstruction mechanism from the RM program.