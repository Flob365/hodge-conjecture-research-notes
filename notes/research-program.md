# A falsifiable research program

## Current state of the attack

The exploratory program has progressively eliminated several broad ansatzes and reduced the real-multiplication route to a much smaller obstruction problem.

What is now available:

1. the target secant Chern character is understood exactly;
2. Markman's `W_2` partial-normalization construction already realizes the genus-4 Jacobian secant K-class (arXiv:2502.03415v2, Example 8.2.3);
3. the local Postnikov calculation in this repository records simplicity and `Ext^{<0}=0` for that transverse model;
4. scalar-slope semihomogeneous monads cannot supply the previously targeted quadratic common symmetry;
5. in the non-scalar real-multiplication model, the HKR/Clifford annihilator of Markman's class has dimension exactly eight;
6. six of those eight directions are ordinary RM deformations;
7. a smooth-isogeny construction realizes an integral multiple of the RM secant class by a perfect complex with `Ext^{<0}=0` using only deformation-friendly divisor and complete-intersection blocks.

The active frontier is therefore **not** the Chern character. It is the cancellation of two explicit generalized deformation obstructions.

---

## Problem 1 — the exact RM infinitesimal kernel

Let

\[
\beta'=g^*\Theta-\frac q6(g^{-1})^*(\Theta^3)
\]

be Markman's real-multiplication secant class for a genus-4 example with a nontrivial norm-one real quadratic unit.

Split

\[
H^1(\mathcal O_X)=U_1\oplus U_2,
\qquad
\dim U_i=2.
\]

The exact exterior-algebra calculation in
[`real-multiplication-infinitesimal-kernel.md`](real-multiplication-infinitesimal-kernel.md)
proves

\[
\operatorname{rank}(\mu_{\beta'})=20,
\qquad
\dim\ker(\mu_{\beta'})=8.
\]

Up to the sign convention for the bivector HKR action,

\[
\boxed{
\ker(\mu_{\beta'})
=
\operatorname{Sym}^2(U_1)
\oplus
\operatorname{Sym}^2(U_2)
\oplus
\langle P_{01}-qB_{01},\ P_{23}-qB_{23}\rangle.
}
\]

A `20 x 20` minor provides the uniform rank certificate

\[
q^8\frac{(\rho-1)^8(\rho+1)^8(\rho^2+1)^8}{\rho^{16}},
\]

which is nonzero for the nontrivial real-multiplication situation `rho>0`, `rho != 1`.

### Falsifiable target

For a candidate perfect complex `E` with `ch(E)` a nonzero multiple of `beta'`, prove

\[
\ker(at_E)=\ker(\mu_{\beta'}).
\]

The general Atiyah--semiregularity compatibility already gives

\[
\ker(at_E)\subseteq\ker(\mu_{\beta'}).
\]

So the problem is to force exactly the eight displayed directions into `ker(at_E)`.

---

## Problem 2 — six ordinary RM directions

The first six annihilators are

\[
\operatorname{Sym}^2(U_1)\oplus\operatorname{Sym}^2(U_2).
\]

They are the natural ordinary first-order deformations preserving the two real-multiplication blocks and the polarization.

The smooth-isogeny scaffold in
[`rm-smooth-isogeny-scaffold.md`](rm-smooth-isogeny-scaffold.md)
is designed from divisor classes which remain algebraic on this RM PEL locus. It therefore turns these six directions from an accidental hoped-for property of Jacobian gluing data into a geometric design constraint.

### Concrete scaffold

After a sufficiently large multiplication isogeny, take

\[
\widetilde A=[m]^*g^*\Theta,
\qquad
\widetilde C=[m]^*(g^{-1})^*\Theta.
\]

For a smooth divisor `D` of class `A_tilde`, define

\[
V_D=
\mathcal O_D^{\oplus3}
\oplus\Omega_D^1
\oplus\Omega_D^2
\oplus K_D^{\oplus3}.
\]

Then

\[
\operatorname{ch}(i_*V_D)=12\widetilde A.
\]

For a smooth complete-intersection curve `Z` of three divisors of class `C_tilde`, define

\[
R_Z=\mathcal O_Z\oplus\mathcal O_Z(3\widetilde C).
\]

Then

\[
\operatorname{ch}(R_Z)=2\widetilde C^3.
\]

Hence

\[
E_m=i_*V_D\oplus R_Z^{\oplus q}[1]
\]

satisfies

\[
\operatorname{ch}(E_m)=12[m]^*\beta'
\]

and, for transverse choices,

\[
\operatorname{Ext}^{<0}(E_m,E_m)=0.
\]

Pushing through `[m]` produces a perfect complex with

\[
\operatorname{ch}([m]_*E_m)=12m^8\beta'
\]

and an isomorphism-class tensor stabilizer of order `m^8`.

### Falsifiable milestone

Write the construction relatively over the six-dimensional RM infinitesimal base and verify explicitly that the six classes in

\[
\operatorname{Sym}^2(U_1)\oplus\operatorname{Sym}^2(U_2)
\]

map to zero under the Atiyah obstruction map.

---

## Problem 3 — the two generalized directions

The only remaining annihilators are

\[
\boxed{
P_{01}-qB_{01},
\qquad
P_{23}-qB_{23}.
}
\]

These mix bivector and `B`-field deformations.

The split smooth-isogeny scaffold does **not** solve them. The cancellation occurs only after adding the divisor and cubic Chern characters. The Atiyah class of a direct sum is block diagonal, so a cancellation at the level of

\[
\mu_{12A-2qC^3}
\]

does not imply cancellation of the two individual obstruction classes.

This is now the central construction problem.

### Falsifiable milestone

Construct a coupled perfect complex with the same K-class as

\[
i_*V_D\oplus R_Z^{\oplus q}[1]
\]

such that both mixed generalized directions lie in its Atiyah kernel.

Possible mechanisms to test, in order:

1. a non-split Postnikov object whose extension data links the divisor and cubic blocks;
2. a Fourier--Mukai transform which turns the two blocks into supports admitting nontrivial coupling;
3. an equivariantization under the isogeny tensor stabilizer;
4. a modification on a common support where the two mixed Atiyah classes can cancel locally.

Every candidate should be rejected immediately if either mixed direction has a nonzero local obstruction.

---

## Problem 4 — genuine equivariant structure

For

\[
F_m=[m]_*E_m,
\]

the kernel

\[
G_m=\ker([m]^*:\operatorname{Pic}^0(X)\to\operatorname{Pic}^0(X))
\]

has order `m^8`, and projection formula gives isomorphisms

\[
F_m\otimes P\simeq F_m,
\qquad P\in G_m.
\]

This is only an isomorphism-class stabilizer until the compatibility cocycle is checked.

Perry's 2026 theorem applies directly to perfect complexes with `Ext^{<0}=0`, and its equivariant form permits weak `G`-semiregularity for finite translation--tensorization actions. Thus a genuine linearization here could be valuable even if full ordinary semiregularity is hard.

### Falsifiable milestone

Compute the projective cocycle of the `G_m` action on `F_m`.

- If it is trivial, construct the linearization and compute invariant Ext groups.
- If it is nontrivial, determine whether a central extension or twisted equivariant category is the correct Perry-compatible replacement.

---

## Problem 5 — discarded or downgraded ansatzes

### `W_2` partial normalization

The K-theory construction is prior art: Markman, arXiv:2502.03415v2, Example 8.2.3. The local derived analysis remains useful, but this model has too little obvious translation symmetry for the earlier large-symmetry design.

### Scalar semihomogeneous monads

The Chern-character problem becomes the binary quartic identity

\[
s^4+4s^3t-6d s^2t^2-4d st^3+d^2t^4
=\sum_i c_i(b_i s+a_i t)^4.
\]

The common scalar torsion congruences force its common stabilizer to remain below the previous target `d(d+1)`. See
[`semihomogeneous-monad-obstruction.md`](semihomogeneous-monad-obstruction.md).

This does not eliminate non-scalar real multiplication; indeed the current program is precisely exploiting the directions that survive that obstruction.

---

## Problem 6 — connection to formal K-theory

If a coupled RM object is shown semiregular (or weakly equivariantly semiregular in the sense needed by Perry), deform it along the Hodge locus.

Its compatible infinitesimal K-classes should then be compared with the unique `D`-fixed formal lift from the Bloch--Esnault--Kerz calculation in
[`formal-k-theory.md`](formal-k-theory.md).

A match would connect the explicit geometric object to the formal rigidity route.

---

## Problem 7 — independent hypersurface route

For a primitive Hodge class `alpha`, define

\[
\mathcal D_L
=\operatorname{span}\{\Gamma_Y(C_Y):Y\in|L^d|,\ d\ge1\}.
\]

The decisive statement remains

\[
H^{2n}(X,\mathbf Q)_{\mathrm{prim}}\cap H^{n,n}
\subseteq\mathcal D_L.
\]

For nodal `Y`, this is the construction of a relation among vanishing cycles whose defect class pairs nontrivially with `alpha`.

This route is logically independent of the RM secant-object program and remains available if the final two generalized Atiyah directions prove impossible to cancel.

---

# Immediate next experiment

The highest-value next calculation is now extremely specific:

\[
\boxed{
\text{construct a local/derived coupling which kills }
P_{01}-qB_{01}
\text{ and }
P_{23}-qB_{23}.
}
\]

A candidate which fails either one is discarded. A candidate which kills both, preserves `Ext^{<0}=0`, and retains a usable finite symmetry would cross the main remaining infinitesimal barrier in the real-multiplication route.