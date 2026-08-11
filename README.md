# Hodge Conjecture — Exploratory Research Notes

> **Status: not a proof.** These are AI-assisted exploratory notes, calculations, obstructions, and concrete research targets. They have not been peer reviewed, and no claim of novelty or priority is made.

This repository records a multi-track attempt to make measurable progress on the Hodge conjecture. The work concentrates on three interfaces:

1. formal deformation of algebraic (K)-classes on abelian schemes;
2. singular hyperplane sections and relations between vanishing cycles;
3. secant objects, equivariant semiregularity, and explicit Chern-character constraints.

The general Hodge conjecture remains open. The purpose of the repository is to separate statements that can be checked rigorously from speculative construction problems.

## Main findings

### 1. Formal rigidity for abelian schemes

For an abelian scheme over (k[[t]]), set

\[
D=\psi^{\ell^2}-[\ell]^*.
\]

In Adams weight (p), filtering absolute differential forms by the number (s) of base differentials gives the following eigenvalues:

| term | eigenvalue of (D) |
|---|---:|
| tangent, (q=p) | \(\ell^{2p-1-s}(\ell^{s+1}-1)\) |
| obstruction, (q=p+1) | \(\ell^{2p-s}(\ell^s-1)\) |

The tangent eigenvalue is always nonzero. The obstruction eigenvalue vanishes only for (s=0), which is precisely the Hodge/Kodaira–Spencer obstruction. Consequently, a (D)-fixed Hodge class has a unique (D)-fixed formal lift order by order.

For a constant abelian scheme, this formal lift equals the constant pullback and is therefore algebraizable. The remaining non-isotrivial problem is the continuity defect

\[
K_0(\mathcal A)_{\mathbf Q}\longrightarrow
\varprojlim_m K_0(\mathcal A_m)_{\mathbf Q}.
\]

The sharp target is to rule out a (D)-fixed class in its cokernel.

See [`notes/formal-k-theory.md`](notes/formal-k-theory.md).

### 2. A no-go result for simple normal-crossing degenerations

Let (X) be smooth projective of dimension (2n), (L) ample, and let

\[
\alpha\in H^{2n}(X,\mathbf Q)\cap H^{n,n}(X),
\qquad L\alpha=0.
\]

If (Y=\bigcup_iD_i) is a simple normal-crossing union of smooth divisors with (D_i\in|m_iL|), then

\[
\alpha|_Y=0.
\]

Indeed, each restriction to a component vanishes by Gysin injectivity and weak Lefschetz; the top weight of (H^{2n}(Y)) comes from the components, while a pure class cannot map nontrivially only into lower weights.

For a nodal hypersurface, the relevant datum is not the number of nodes but a global relation among their vanishing cycles. A single ordinary double point is generally rationally invisible. Dimension estimates show that the expected number of nodes in a moving linear system is far below the threshold that would force such a relation automatically.

See [`notes/singular-hypersurfaces.md`](notes/singular-hypersurfaces.md).

### 3. Chern-character obstruction for graph-type secant objects

Consider a principally polarized abelian fourfold ((X,\Theta)) and a union of surfaces

\[
Z=\bigcup_{uv\in E(\Gamma)}(D_u\cap D_v),
\]

where the (D_u) are transverse translates of (Theta). Let (e=|E(\Gamma)|) and

\[
w=\sum_v\binom{\deg(v)}2-\#\{\text{triangles of }\Gamma\}\ge0.
\]

For

\[
E=(\mathcal O_X-\nu_*\mathcal O_{\widetilde Z})\otimes\mathcal O_X(\Theta),
\]

where the modification is supported only at points, inclusion–exclusion gives

\[
\operatorname{ch}_2(E)=\left(\frac12-e\right)\Theta^2,
\qquad
\operatorname{ch}_3(E)=\left(\frac16+w\right)\Theta^3.
\]

Membership in

\[
\operatorname{span}\{e^{\sqrt{-d}\Theta},e^{-\sqrt{-d}\Theta}\}
\]

with rank (1) and first Chern class (Theta) would require

\[
e=\frac{d+1}{2},
\qquad
w=-\frac{d+1}{6},
\]

which is impossible for (d>0). Thus no effective graph of pairwise theta intersections, corrected only at points, can realize the desired secant character.

This also exposes an apparent inconsistency in the numerical candidate in Section 12 of Markman's arXiv:2509.23403v2: the printed value (n=(d+9)/2) is already incompatible with the degree-four Chern character, which instead forces (n=(d+1)/2). This statement concerns the preprint as written and should not be read as a rejection of its broader strategy.

See [`notes/secant-objects.md`](notes/secant-objects.md).

### 4. A corrected virtual class

Write (x=\Theta) and

\[
B_r=e^x(1-e^{-x})^r
=\operatorname{ch}(\mathcal O_{\Theta^r}(\Theta)).
\]

In dimension four,

\[
B_2=x^2+\frac{x^4}{12},\quad
B_3=x^3-\frac{x^4}{2},\quad
B_4=x^4.
\]

The virtual class

\[
V=
[\mathcal O(\Theta)]
-\frac{d+1}{2}[\mathcal O_{\Theta^2}(\Theta)]
-\frac{d+1}{6}[\mathcal O_{\Theta^3}(\Theta)]
+\frac{(d-2)(d+1)}{24}[\mathcal O_{\Theta^4}(\Theta)]
\]

satisfies exactly

\[
\operatorname{ch}(V)
=1+x-\frac d2x^2-\frac d6x^3+\frac{d^2}{24}x^4.
\]

This is the rational secant class forced by rank and first Chern class. The point contribution has total length

\[
(d-2)(d+1)=O(d^2),
\]

which introduces the quadratic scale absent from cyclic surface constructions.

The unresolved construction problem is to realize (V), not as a decomposable formal sum, but as a simple equivariant perfect complex or monad whose invariant obstruction space is controlled by the semiregularity map.

The identity can be checked with:

```bash
python scripts/verify_virtual_class.py --d 5
python -m unittest discover -s tests
```

## Concrete research targets

### Target A — continuity in formal (K)-theory

Prove

\[
\ker\left(D:\operatorname{coker}(K_0(\mathcal A)_{\mathbf Q}
\to\varprojlim K_0(\mathcal A_m)_{\mathbf Q})\to\operatorname{coker}(\cdots)\right)=0.
\]

### Target B — defect realization

For every nonzero primitive Hodge class (alpha), construct a singular hypersurface (Y) and a relation (eta) among its vanishing cycles such that

\[
\langle\alpha,\gamma_\beta\rangle\ne0.
\]

### Target C — a quadratic-symmetry monad

Construct a perfect complex (\mathcal E^\bullet) with

\[
[\mathcal E^\bullet]=V,
\qquad
\operatorname{Hom}(\mathcal E^\bullet,\mathcal E^\bullet)=\mathbf C,
\qquad
\operatorname{Ext}^{<0}(\mathcal E^\bullet,\mathcal E^\bullet)=0,
\]

carrying a translation–tensorization symmetry group of order (O(d^2)), and prove injectivity of the equivariant semiregularity map.

See [`notes/research-program.md`](notes/research-program.md).

## Repository map

- [`notes/formal-k-theory.md`](notes/formal-k-theory.md) — Adams eigenvalues and the formal algebraization gap.
- [`notes/singular-hypersurfaces.md`](notes/singular-hypersurfaces.md) — SNC no-go lemma, Gysin defect, and vanishing cycles.
- [`notes/secant-objects.md`](notes/secant-objects.md) — Chern-character audit and graph obstruction.
- [`notes/research-program.md`](notes/research-program.md) — surviving construction program and falsifiable milestones.
- [`scripts/verify_virtual_class.py`](scripts/verify_virtual_class.py) — symbolic verification.
- [`tests/test_virtual_class.py`](tests/test_virtual_class.py) — regression tests.

The verifier uses only the Python standard library.

## Primary references

- S. Bloch, H. Esnault, M. Kerz, [*Deformation of algebraic cycle classes in characteristic zero*](https://arxiv.org/abs/1310.1773).
- R. P. Thomas, [*Nodes and the Hodge conjecture*](https://arxiv.org/abs/math/0212216).
- M. Saito, [*Generalized Thomas hyperplane sections and relations between vanishing cycles*](https://arxiv.org/abs/0806.1461).
- M. A. de Cataldo, L. Migliorini, [*The decomposition theorem, perverse sheaves and the topology of algebraic maps*](https://arxiv.org/abs/0711.1307).
- E. Markman, [*Secant sheaves and Weil classes on abelian varieties*, v2](https://arxiv.org/abs/2509.23403).
- A. Perry, [*The semiregularity theorem for equivariant noncommutative varieties*](https://arxiv.org/abs/2604.00511).

## Citation and contribution policy

Please cite the primary papers above for established results. If using a calculation specific to this repository, link to the exact commit and independently verify it. Corrections, counterexamples, and references to prior occurrences are especially welcome.
