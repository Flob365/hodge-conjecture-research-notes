# Formal (K)-theory on abelian schemes

## Setup

Let (R=k[[t]]), let \(\mathcal A/R\) be an abelian scheme, let (A) be its special fibre, and let

\[
D=\psi^{\ell^2}-[\ell]^*,\qquad \ell>1.
\]

All statements below are rational. The deformation theory is considered in Adams weight (p).

## Tangent–obstruction calculation

The Bloch–Esnault–Kerz tangent–obstruction sequence contains

\[
T_p=H^p(A,\Omega^{p-1}_{A/\mathbf Q})
\longrightarrow CH^p(\mathcal A_m)_{\mathbf Q}
\longrightarrow CH^p(\mathcal A_{m-1})_{\mathbf Q}
\xrightarrow{\mathrm{Ob}}
O_p=H^{p+1}(A,\Omega^{p-1}_{A/\mathbf Q}).
\]

Filter absolute forms by the number (s) of differentials from (k/\mathbf Q). The graded terms are subquotients of

\[
H^q(A,\Omega^{p-1-s}_{A/k})\otimes_k\Omega^s_{k/\mathbf Q}.
\]

On an abelian variety,

\[
[\ell]^*=\ell^{q+p-1-s},
\qquad
\psi^{\ell^2}=\ell^{2p}.
\]

### Tangent space

For (q=p), the eigenvalue is

\[
\lambda_s=\ell^{2p}-\ell^{2p-1-s}
=\ell^{2p-1-s}(\ell^{s+1}-1),
\]

which is nonzero for every (s\ge0). Hence (D) is invertible on the filtered tangent space.

### Obstruction space

For (q=p+1), the eigenvalue is

\[
\mu_s=\ell^{2p}-\ell^{2p-s}
=\ell^{2p-s}(\ell^s-1).
\]

It vanishes only for (s=0). The quotient at (s=0) is

\[
H^{p+1}(A,\Omega^{p-1}_{A/k}),
\]

and the projection of the obstruction to this quotient is the Kodaira–Spencer obstruction to preserving (F^p). The Hodge condition kills that projection.

All remaining obstruction components lie at (s\ge1), where (D) is invertible. Naturality gives

\[
D\,\mathrm{Ob}(\xi)=\mathrm{Ob}(D\xi).
\]

If (D\xi=0), then (D\,\mathrm{Ob}(\xi)=0), hence \(\mathrm{Ob}(\xi)=0\). Any lift can then be corrected uniquely by a tangent vector to become (D)-fixed.

## Consequences

### Formal rigidity

A (D)-fixed class whose flat de Rham class remains in (F^p) has a unique (D)-fixed lift at each infinitesimal order, with fixed special fibre.

The pro-Chern character transfers this statement rationally to the relevant inverse system of (K_0)-groups.

### Constant families

If

\[
\mathcal A=A_0\times_k\operatorname{Spec}k[[t]],
\]

the pullback of the special-fibre class is a global (D)-fixed lift. Formal uniqueness implies that every (D)-fixed formal system with that special fibre is its restriction. It is therefore algebraizable.

The same trace argument works after a finite étale base extension that makes the family constant. Over a strictly henselian base such as \(\mathbf C[[t]]\), this variant is essentially trivial.

## Exact remaining gap

Formal GAGA gives an equivalence at the level of compatible perfect complexes, but algebraic (K)-theory need not commute with inverse limits:

\[
K_0\!\left(\varprojlim_m\operatorname{Perf}(\mathcal A_m)\right)
\longrightarrow
\varprojlim_mK_0(\operatorname{Perf}(\mathcal A_m)).
\]

A sufficient concrete condition is that, after multiplying by a common integer, the formal classes admit representatives (E_m) with actual compatibilities

\[
E_{m+1}\otimes^{\mathbf L}\mathcal O_{\mathcal A_m}\simeq E_m.
\]

The target problem is to exclude (D)-torsion in the cokernel of

\[
K_0(\mathcal A)_{\mathbf Q}\to\varprojlim_mK_0(\mathcal A_m)_{\mathbf Q}.
\]

## Caveats

- Uniqueness is uniqueness among (D)-fixed lifts with a prescribed special fibre.
- The argument is rational and pro-infinitesimal.
- Extending the trace argument from finite étale trivializations to arbitrary isogenies requires care with the choice of (ell) and the relevant pull–push square.

