# A smooth-isogeny perfect-complex scaffold for the RM secant class

> **Status.** This note constructs an explicit perfect complex with no negative self-Exts and Chern character a nonzero integral multiple of Markman's real-multiplication secant class. It is deliberately a scaffold rather than a semiregularity proof: the two generalized infinitesimal directions isolated in `real-multiplication-infinitesimal-kernel.md` still do not cancel at the object level in the split model.

## 1. Target

Keep the notation of Markman's genus-4 real-multiplication example and set

\[
A=g^*\Theta,
\qquad
C=(g^{-1})^*\Theta,
\qquad
\beta'=A-\frac q6C^3.
\]

Corollary 11.2.6(3) of arXiv:2509.23079 shows that `beta'` belongs to the relevant secant space when `g` comes from a nontrivial norm-one real-multiplication unit.

The goal here is to realize an integral multiple of `beta'` by a perfect complex built only from smooth divisors, complete intersections, and natural bundles. Such ingredients have a much more transparent deformation theory than the Jacobian-specific `W_2` gluing model.

Perry's arXiv:2604.00511v2, Theorem 1.1, explicitly allows semiregular **perfect complexes** satisfying `Ext^{<0}=0`; coherence or simplicity is not required for that theorem. Theorem 1.2 gives the corresponding weakly equivariant statement for finite translation--tensorization groups.

## 2. A universal rank-12 bundle on a smooth divisor

Let `X` be any abelian fourfold, let `D subset X` be a smooth ample divisor, and write

\[
y=[D].
\]

Because `Omega_X` is trivial of rank four, the conormal sequence is

\[
0\to\mathcal O_D(-D)
\to\mathcal O_D^{\oplus4}
\to\Omega_D^1\to0.
\]

Adjunction gives

\[
K_D=\mathcal O_D(D).
\]

Define the rank-12 vector bundle

\[
\boxed{
V_D=
\mathcal O_D^{\oplus3}
\oplus\Omega_D^1
\oplus\Omega_D^2
\oplus K_D^{\oplus3}.
}
\]

From the conormal sequence,

\[
\operatorname{ch}(\Omega_D^1)
=3+y-\frac12y^2+\frac16y^3,
\]

and

\[
\operatorname{ch}(\Omega_D^2)
=3+2y-\frac23y^3.
\]

Together with `ch(K_D)=e^y`, this gives the exact dimension-three identity

\[
\boxed{
\operatorname{ch}(V_D)
=12+6y+y^2
=12\,\operatorname{td}(\mathcal O_D(D)).
}
\]

(the cubic Todd coefficient of a line bundle is zero).

Let `i:D -> X` be the inclusion. Since `td(X)=1`, Grothendieck--Riemann--Roch gives

\[
\operatorname{ch}(i_*V_D)
=i_*\left(
\operatorname{ch}(V_D)
\operatorname{td}(\mathcal O_D(D))^{-1}
\right).
\]

Hence

\[
\boxed{
\operatorname{ch}(i_*V_D)=12y.
}
\]

This is useful because it realizes a **pure divisor Chern character with no degree-four, degree-six, or degree-eight contamination by an honest coherent sheaf**.

## 3. A universal pure cubic curve block

Let `L` be an ample line bundle on an abelian fourfold with first Chern class `z`, and choose three transverse divisors in `|L|` with smooth complete-intersection curve

\[
Z=D_1\cap D_2\cap D_3.
\]

The Koszul resolution gives

\[
\operatorname{ch}(\mathcal O_Z)
=(1-e^{-z})^3.
\]

Define

\[
R_Z:=\mathcal O_Z\oplus\mathcal O_Z(3L).
\]

Then

\[
\operatorname{ch}(R_Z)
=(1+e^{3z})(1-e^{-z})^3.
\]

On a fourfold the expansion truncates after degree four, and the quartic term cancels:

\[
\boxed{
(1+e^{3z})(1-e^{-z})^3=2z^3
\quad\text{in }H^{\le8}(X).
}
\]

Therefore

\[
\boxed{
\operatorname{ch}(R_Z)=2z^3.
}
\]

Again this is an honest sheaf, now with a pure cubic Chern character.

## 4. Regularize by an isogeny

The principal theta divisors occurring on a Jacobian need not be smooth. Instead take the multiplication isogeny

\[
\pi=[m]:X\to X
\]

with `m` sufficiently large. Put

\[
\widetilde A=\pi^*A,
\qquad
\widetilde C=\pi^*C.
\]

High powers of ample line bundles have sufficiently mobile linear systems, so choose:

- a smooth divisor `D` of class `A_tilde`;
- three transverse smooth divisors of class `C_tilde`, with smooth complete-intersection curve `Z`;
- the choices generically enough that `Z` is not contained in `D`.

Set

\[
S=i_*V_D,
\qquad
R=j_*\left(
\mathcal O_Z\oplus\mathcal O_Z(3\widetilde C)
\right),
\]

and define

\[
\boxed{
E_m=S\oplus R^{\oplus q}[1].
}
\]

Its Chern character is

\[
\begin{aligned}
\operatorname{ch}(E_m)
&=12\widetilde A-2q\widetilde C^3\\
&=12\pi^*\left(A-\frac q6C^3\right).
\end{aligned}
\]

Thus

\[
\boxed{
\operatorname{ch}(E_m)=12\pi^*\beta'.
}
\]

## 5. Negative Ext groups vanish

Both `S` and `R` are coherent sheaves, so their self-Ext groups in negative degrees vanish. For

\[
E_m=S\oplus R^{\oplus q}[1],
\]

the only potentially nonzero negative cross term is

\[
\operatorname{Ext}^{-1}(S,R[1])
=\operatorname{Hom}(S,R).
\]

The support of `S` is the divisor `D`, while `R` is pure of dimension one on the smooth curve `Z`. Since `Z` is not contained in `D`, any image of a map `S -> R` would be supported on the finite set `D cap Z`. A pure one-dimensional sheaf has no nonzero zero-dimensional subsheaf. Hence

\[
\operatorname{Hom}(S,R)=0.
\]

Consequently

\[
\boxed{
\operatorname{Ext}^{<0}(E_m,E_m)=0.
}
\]

This is exactly the homological boundedness hypothesis appearing in Perry's perfect-complex semiregularity theorems.

## 6. Push back to the original fourfold

Define

\[
F_m:=\pi_*E_m.
\]

The isogeny is finite etale, so `F_m` is perfect and GRR gives

\[
\operatorname{ch}(F_m)
=\pi_*\operatorname{ch}(E_m)
=12\deg(\pi)\beta'.
\]

For multiplication by `m` on a fourfold,

\[
\deg([m])=m^8,
\]

hence

\[
\boxed{
\operatorname{ch}(F_m)=12m^8\beta'.
}
\]

For general choices of `D` and `Z`, the same purity argument can be imposed simultaneously against the finitely many deck translates of `Z`. Using

\[
\pi^*\pi_*E_m
\simeq
\bigoplus_{a\in\ker\pi}t_a^*E_m,
\]

adjunction then gives

\[
\boxed{
\operatorname{Ext}^{<0}(F_m,F_m)=0.
}
\]

## 7. A large tensor stabilizer appears automatically

Let

\[
G_m:=\ker\left(\pi^*:\operatorname{Pic}^0(X)\to\operatorname{Pic}^0(X)\right).
\]

For `P in G_m`, the projection formula gives

\[
F_m\otimes P
\simeq
\pi_*(E_m\otimes\pi^*P)
\simeq
F_m.
\]

Thus the isomorphism class of `F_m` has a tensorization stabilizer of order

\[
\boxed{|G_m|=m^8.}
\]

This is the first construction in these notes where the exact RM secant Chern character, `Ext^{<0}=0`, and a symmetry group of arbitrarily large order coexist naturally.

**Caution.** Perry's equivariant theorem requires an actual compatible `G_m`-equivariant structure, not merely pointwise isomorphisms `F_m tensor P ~= F_m`. The possible linearization/cocycle issue must be checked before this stabilizer can be used in Theorem 1.2.

## 8. The six ordinary RM directions are built in

The construction uses only the two RM divisor classes `A` and `C`, their high pullbacks, smooth members of their linear systems, cotangent/canonical bundles of a relative divisor, and a relative complete intersection.

Along the ordinary PEL deformation space preserving the real multiplication and polarization, `A` and `C` remain algebraic divisor classes. After replacing the base etale-locally and taking `m` large, the ingredients above can be chosen relatively. Consequently the six ordinary infinitesimal RM directions

\[
\operatorname{Sym}^2(U_1)\oplus\operatorname{Sym}^2(U_2)
\]

identified in `real-multiplication-infinitesimal-kernel.md` are geometrically compatible with this scaffold.

This is the main advantage over the Jacobian-specific `W_2` construction: the ordinary RM deformations are no longer something one has to hope the gluing data follows; they are part of the design.

## 9. Why the split scaffold still fails the final two directions

The total Chern character has the two generalized annihilators

\[
P_{01}-qB_{01},
\qquad
P_{23}-qB_{23},
\]

(up to HKR sign convention), because the `A` and `C^3` contributions cancel under the Clifford action.

But that cancellation occurs **between the two direct summands** of `E_m`. For example, the `B_{01}` part acts nontrivially on the pure divisor character `12A`, while the bivector action on the cubic block supplies the cancelling term only after the two Chern characters are added.

Since the Atiyah class of a direct sum is block diagonal, such a cancellation in total Chern character does not force cancellation of the two obstruction classes inside

\[
\operatorname{Ext}^2(S,S)
\oplus
\operatorname{Ext}^2(R^{\oplus q}[1],R^{\oplus q}[1]).
\]

Indeed, nonvanishing of the Clifford action on one summand already implies nonvanishing of its Atiyah obstruction via the semiregularity--Atiyah compatibility diagram.

Therefore the split complex is **not** expected to satisfy

\[
\ker(at)=\ker(\mu_{\beta'}).
\]

This is not a failure of the scaffold; it identifies the missing mechanism exactly:

> the divisor block and cubic curve block must be coupled by a nontrivial derived construction so that the two generalized `B/P` obstructions cancel at the object level, not merely after taking Chern characters.

## 10. New concrete target

The RM problem has now been reduced to a much smaller categorification problem.

Construct a perfect complex `E_m^coupled` with the same K-class as

\[
S\oplus R^{\oplus q}[1],
\]

such that:

1. `Ext^{<0}(E_m^coupled,E_m^coupled)=0`;
2. the six ordinary RM directions remain in `ker(at)`;
3. the two mixed classes `P_01-qB_01` and `P_23-qB_23` also enter `ker(at)`;
4. preferably the `m^8` tensor stabilizer survives with a genuine linearization.

The remaining problem is therefore no longer to guess the secant K-class. It is to build **two explicit obstruction-cancelling couplings**.