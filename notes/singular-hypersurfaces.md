# Singular hypersurfaces and vanishing-cycle relations

## Primitive setup

Let (X) be smooth projective of dimension (2n), let (L) be ample, and let

\[
\alpha\in H^{2n}(X,\mathbf Q)\cap H^{n,n}(X),
\qquad L\alpha=0.
\]

Thomas's strategy asks for a singular hypersurface (Y) such that \(\alpha|_Y\ne0\). After resolving (Y), induction on dimension can turn the detected class into an algebraic cycle pairing nontrivially with (alpha).

## SNC no-go lemma

Let (D\in|mL|) be smooth and let (i:D\hookrightarrow X). Then

\[
i_*i^*\alpha=mL\alpha=0.
\]

The Gysin map

\[
i_*:H^{2n}(D)\to H^{2n+2}(X)
\]

is injective, since it is dual to the weak-Lefschetz isomorphism

\[
H^{2n-2}(X)\xrightarrow{\sim}H^{2n-2}(D).
\]

Therefore (i^*\alpha=0\).

Now let (Y=\bigcup_iD_i) be a proper simple normal-crossing union with (D_i\in|m_iL|). In the weight spectral sequence, the weight-(2n) part of (H^{2n}(Y)) comes from the components. Multiple intersections contribute at lower weight. Since all component restrictions vanish, strict compatibility of mixed Hodge structures gives

\[
\alpha|_Y=0.
\]

The purity of the class coming from (H^{2n}(X)) is essential here.

## Resolution and the Gysin defect

For a resolution (f:\widetilde Y\to Y\hookrightarrow X), define

\[
K_Y=\ker\left(f_*:H^{2n}(\widetilde Y)\to H^{2n+2}(X)\right)
\]

and

\[
C_Y=\operatorname{coker}\left(
f^*:H^{2n-2}(X)\to H^{2n-2}(\widetilde Y)
\right).
\]

Poincaré duality identifies (K_Y\simeq C_Y^\vee\). The map

\[
\Gamma_Y:C_Y\to H^{2n}(X)_{\mathrm{prim}},
\qquad
[\eta]\mapsto\operatorname{pr}_{\mathrm{prim}}(f_*\eta)
\]

satisfies

\[
\langle\alpha,\Gamma_Y(\eta)\rangle_X
=\langle f^*\alpha,\eta\rangle_{\widetilde Y}.
\]

Thus

\[
Y\text{ detects }\alpha
\iff
\alpha\not\perp\Gamma_Y(C_Y).
\]

The required singularity must create a targeted failure of weak Lefschetz on the resolution; singular gluing alone is insufficient.

## Nodal hypersurfaces

Suppose (Y) has (delta) ordinary double points and (Y_t) is a smoothing. Let (v_i\in H_{2n-1}(Y_t)) be the vanishing cycles and set

\[
R_Y=\ker\left(
\mathbf Q^\delta\to H_{2n-1}(Y_t),
\ e_i\mapsto v_i
\right).
\]

The extra middle cohomology of (Y) is dual to (R_Y). The restriction of (alpha) defines a functional on (R_Y), and detection requires a relation \(\beta\in R_Y\) such that

\[
\langle\alpha,\gamma_\beta\rangle\ne0.
\]

A single node generally has a nonzero vanishing cycle and no rational relation. For an (A_k) singularity, the antisymmetric local intersection matrix has nullity zero for even (k) and at most one for odd (k). A large Milnor number therefore does not automatically provide many useful relations.

## Why counting nodes is insufficient

Let (M=\dim_{\mathbf C}X=2n), (h=c_1(L)), and (a=\int_Xh^M\). Riemann–Roch gives

\[
N_d:=\dim|L^d|
=\frac{a}{M!}d^M+O(d^{M-1}).
\]

For a smooth (Y_d\in|L^d|), its vanishing middle cohomology has dimension

\[
\dim V_d=a d^M+O(d^{M-1})=2g_d.
\]

The vanishing cycles of simultaneous nodes span an isotropic subspace, so a relation is forced by dimension only when \(\delta>g_d\). A nodal stratum of expected codimension satisfies \(\delta\le N_d\), while

\[
\frac{N_d}{g_d}\longrightarrow\frac{2}{M!}.
\]

In dimension four this limit is (1/12). Hence no argument based solely on the number of nodes in a stratum of expected dimension can force the required relation. The missing input is a special homological dependence with the correct pairing against (alpha).

