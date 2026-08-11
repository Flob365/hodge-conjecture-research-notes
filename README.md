# Hodge Conjecture — Exploratory Research Notes

> **Status: not a proof.** These are AI-assisted exploratory notes, calculations, obstructions, rediscoveries, and concrete research targets. They have not been peer reviewed. No claim of novelty or priority is made unless independently established.

This repository records a multi-track attempt to make measurable progress around the Hodge conjecture, with a current emphasis on abelian fourfolds, secant objects, real multiplication, and semiregularity.

The working rule is simple: separate exact calculations and falsifiable lemmas from speculative construction ideas, and record prior art whenever a construction is rediscovered.

## Current strongest findings

### 1. Formal rigidity for abelian schemes

For an abelian scheme over `k[[t]]`, set

\[
D=\psi^{\ell^2}-[\ell]^*.
\]

Filtering absolute differential forms by the number of base differentials gives explicit eigenvalues for `D`. The tangent eigenvalue is nonzero, while the obstruction eigenvalue vanishes only in the Hodge/Kodaira--Spencer direction. Thus a `D`-fixed Hodge class has a unique `D`-fixed formal lift order by order.

The remaining non-isotrivial gap is the continuity defect

\[
K_0(\mathcal A)_{\mathbf Q}
\longrightarrow
\varprojlim_m K_0(\mathcal A_m)_{\mathbf Q}.
\]

See [`notes/formal-k-theory.md`](notes/formal-k-theory.md).

### 2. Singular-hypersurface no-go / defect formulation

A primitive middle Hodge class restricts trivially to a simple normal-crossing union of ample divisors in the basic setup considered here. For nodal hypersurfaces, the important datum is not merely the number of nodes but a global relation among vanishing cycles.

This isolates a concrete alternative target: construct a defect relation pairing nontrivially with a prescribed primitive Hodge class.

See [`notes/singular-hypersurfaces.md`](notes/singular-hypersurfaces.md).

### 3. Graph-type theta secant constructions are numerically obstructed

For unions of pairwise intersections of theta translates indexed by a graph, inclusion--exclusion forces incompatible degree-four and degree-six Chern-character coefficients. Point corrections cannot repair the codimension-three discrepancy.

A corrected virtual class is

\[
\operatorname{ch}(V)
=1+\Theta-\frac d2\Theta^2
-\frac d6\Theta^3
+\frac{d^2}{24}\Theta^4.
\]

See [`notes/secant-objects.md`](notes/secant-objects.md) and [`scripts/verify_virtual_class.py`](scripts/verify_virtual_class.py).

### 4. `W_2` realization: prior art plus local derived analysis

A partial-normalization construction using `d+1` translates of `W_2(C)` on a genus-4 Jacobian realizes the corrected secant character. This construction is essentially **Markman's Example 8.2.3 in arXiv:2502.03415v2**; the repository has been corrected to state this explicitly.

The useful additional calculation retained here is a local Postnikov model showing, under transverse no-triple-intersection hypotheses,

\[
\operatorname{Hom}(E_d,E_d)=\mathbf C,
\qquad
\operatorname{Ext}^{<0}(E_d,E_d)=0.
\]

See [`notes/jacobian-w2-construction.md`](notes/jacobian-w2-construction.md).

### 5. Scalar semihomogeneous monads: arithmetic no-go

For a simple semihomogeneous bundle of scalar slope `a/b` on a principally polarized abelian fourfold,

\[
\operatorname{ch}(E_{a/b})
=b^4\exp\left(\frac ab\Theta\right).
\]

The secant K-class condition becomes the integral binary-quartic identity

\[
s^4+4s^3t-6d s^2t^2-4d st^3+d^2t^4
=\sum_i c_i(b_i s+a_i t)^4.
\]

Common scalar torsion symmetry then satisfies strong divisibility constraints which keep it below the previously targeted quadratic symmetry scale.

See [`notes/semihomogeneous-monad-obstruction.md`](notes/semihomogeneous-monad-obstruction.md).

### 6. Real multiplication: exact rank-20 / kernel-8 calculation

For Markman's real-multiplication secant class

\[
\beta'
=g^*\Theta-rac q6(g^{-1})^*(\Theta^3),
\]

split

\[
H^1(\mathcal O_X)=U_1\oplus U_2,
\qquad \dim U_1=\dim U_2=2.
\]

The exact HKR/Clifford action

\[
\mu_{\beta'}:HT^2(X)\to H\Omega_*(X)
\]

has

\[
\boxed{
\operatorname{rank}(\mu_{\beta'})=20,
\qquad
\dim\ker(\mu_{\beta'})=8.
}
\]

Up to the bivector sign convention,

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

A `20 x 20` minor gives the uniform certificate

\[
q^8\frac{(\rho-1)^8(\rho+1)^8(\rho^2+1)^8}{\rho^{16}},
\]

nonzero in the nontrivial real-multiplication case.

This turns the open semiregularity-on-the-Atiyah-image condition into an explicit **eight-direction problem**, six ordinary and two generalized.

See [`notes/real-multiplication-infinitesimal-kernel.md`](notes/real-multiplication-infinitesimal-kernel.md) and [`scripts/verify_rm_infinitesimal_kernel.py`](scripts/verify_rm_infinitesimal_kernel.py).

### 7. Smooth-isogeny RM scaffold: exact class + no negative Exts

Let `D` be a smooth ample divisor on an abelian fourfold. The natural rank-12 bundle

\[
V_D=
\mathcal O_D^{\oplus3}
\oplus\Omega_D^1
\oplus\Omega_D^2
\oplus K_D^{\oplus3}
\]

satisfies

\[
\boxed{\operatorname{ch}(i_*V_D)=12[D].}
\]

If `Z` is a smooth complete intersection of three divisors of class `C`, then

\[
\boxed{
\operatorname{ch}
\left(\mathcal O_Z\oplus\mathcal O_Z(3C)\right)
=2C^3.
}
\]

After a sufficiently large multiplication isogeny `[m]`, these blocks give a perfect complex `E_m` with

\[
\operatorname{ch}(E_m)=12[m]^*\beta',
\qquad
\operatorname{Ext}^{<0}(E_m,E_m)=0.
\]

Pushing down gives

\[
\operatorname{ch}([m]_*E_m)=12m^8\beta'.
\]

The construction is deliberately deformation-friendly in the six ordinary RM directions. The remaining problem is to **couple** the divisor and cubic blocks so that the two mixed directions

\[
P_{01}-qB_{01},
\qquad
P_{23}-qB_{23}
\]

also vanish under the Atiyah obstruction map.

See [`notes/rm-smooth-isogeny-scaffold.md`](notes/rm-smooth-isogeny-scaffold.md) and [`scripts/verify_rm_smooth_isogeny_scaffold.py`](scripts/verify_rm_smooth_isogeny_scaffold.py).

## Current main target

The highest-value next step is now sharply defined:

\[
\boxed{
\text{construct a coupled RM perfect complex killing the two mixed }B/P\text{ directions.}
}
\]

A successful candidate should simultaneously satisfy:

\[
\operatorname{Ext}^{<0}(E,E)=0,
\qquad
\ker(at_E)=\ker(\mu_{\beta'}),
\]

and preferably retain a usable finite translation--tensorization symmetry.

See [`notes/research-program.md`](notes/research-program.md).

## Repository map

- [`notes/formal-k-theory.md`](notes/formal-k-theory.md) — Adams eigenvalues and the formal algebraization gap.
- [`notes/singular-hypersurfaces.md`](notes/singular-hypersurfaces.md) — SNC no-go lemma, Gysin defect, and vanishing cycles.
- [`notes/secant-objects.md`](notes/secant-objects.md) — Chern-character audit and graph obstruction.
- [`notes/jacobian-w2-construction.md`](notes/jacobian-w2-construction.md) — Markman prior art plus local Postnikov/Ext analysis.
- [`notes/semihomogeneous-monad-obstruction.md`](notes/semihomogeneous-monad-obstruction.md) — scalar semihomogeneous arithmetic obstruction.
- [`notes/real-multiplication-infinitesimal-kernel.md`](notes/real-multiplication-infinitesimal-kernel.md) — exact rank-20/kernel-8 RM calculation.
- [`notes/rm-smooth-isogeny-scaffold.md`](notes/rm-smooth-isogeny-scaffold.md) — deformation-friendly RM perfect-complex scaffold.
- [`notes/research-program.md`](notes/research-program.md) — current falsifiable milestones.
- [`scripts/`](scripts/) — exact symbolic verifiers using the Python standard library.
- [`tests/`](tests/) — regression tests for the symbolic identities.

Run:

```bash
python -m unittest discover -s tests
```

## Primary references

- S. Bloch, H. Esnault, M. Kerz, [*Deformation of algebraic cycle classes in characteristic zero*](https://arxiv.org/abs/1310.1773).
- R. P. Thomas, [*Nodes and the Hodge conjecture*](https://arxiv.org/abs/math/0212216).
- M. Saito, [*Generalized Thomas hyperplane sections and relations between vanishing cycles*](https://arxiv.org/abs/0806.1461).
- E. Markman, [*The Hodge conjecture for abelian fourfolds*, v2](https://arxiv.org/abs/2502.03415).
- E. Markman, [*Secant sheaves on abelian n-folds with real multiplication and Weil classes on abelian 2n-folds with complex multiplication*](https://arxiv.org/abs/2509.23079).
- A. Perry, [*The semiregularity theorem for equivariant noncommutative varieties*](https://arxiv.org/abs/2604.00511).

## Citation and contribution policy

Please cite primary papers for established results. If using a calculation specific to this repository, link to the exact commit and independently verify it. Corrections, counterexamples, and references to prior occurrences are especially welcome.