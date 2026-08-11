# Nested RM elementary transform: a genuinely coupled secant sheaf

> **Status.** This note constructs a single coherent sheaf with Chern character a nonzero integral multiple of the real-multiplication secant class. It evades the transverse parity obstruction in `rm-coupling-local-obstruction.md` by putting all cubic curve blocks inside the divisor block and replacing the split object by an elementary transform. This solves the **existence of a non-split categorical coupling with the correct K-class**. It does **not** yet prove that the two mixed generalized directions lie in the Atiyah kernel.

## 1. Setup

Use the notation of `real-multiplication-infinitesimal-kernel.md` and `rm-smooth-isogeny-scaffold.md`:

\[
A=g^*\Theta,
\qquad
C=(g^{-1})^*\Theta,
\qquad
\beta'=A-\frac q6C^3.
\]

Over `C`, write

\[
A=\rho\theta_1+\rho^{-1}\theta_2,
\qquad
C=\rho^{-1}\theta_1+\rho\theta_2,
\]

where `rho>0`, `rho != 1`, `theta_1^3=theta_2^3=0`, and

\[
\int_X\theta_1^2\theta_2^2=4.
\]

Put

\[
s:=\rho^2+\rho^{-2}\ge2.
\]

A direct intersection calculation gives

\[
A^4=C^4=24,
\qquad
A\,C^3=C\,A^3=12s.
\]

Let

\[
\pi=[m]:X\to X
\]

and set

\[
\widetilde A=\pi^*A,
\qquad
\widetilde C=\pi^*C.
\]

Then all fourfold intersection numbers scale by `m^8`.

## 2. Why enough cubic curves can be nested in one divisor

Fix a positive integer `M`. We will use a divisor

\[
D\in|M\widetilde A|
\]

and

\[
N=qM
\]

pairwise disjoint smooth curves

\[
Z_1,\ldots,Z_N,
\]

each a transverse complete intersection of three divisors in `|C_tilde|`.

For one such curve `Z`, adjunction gives

\[
K_Z=3\widetilde C|_Z,
\]

hence

\[
2g(Z)-2
=3\widetilde C^4
=72m^8,
\qquad
g(Z)=1+36m^8.
\]

The degree of `M A_tilde` on `Z` is

\[
\deg((M\widetilde A)|_Z)
=M\widetilde A\widetilde C^3
=12Ms\,m^8.
\]

If

\[
Ms>6,
\]

then this degree is larger than `2g-2`, so Riemann--Roch gives

\[
h^0\bigl(Z,\mathcal O_Z(M\widetilde A)\bigr)
=(12Ms-36)m^8.
\]

On the other hand, since `M A_tilde` is ample on the abelian fourfold,

\[
h^0\bigl(X,\mathcal O_X(M\widetilde A)\bigr)
=\frac{(M\widetilde A)^4}{24}
=M^4m^8.
\]

For a disjoint union

\[
U=Z_1\sqcup\cdots\sqcup Z_N,
\qquad N=qM,
\]

the restriction sequence gives the lower bound

\[
\begin{aligned}
h^0(I_U(M\widetilde A))
&\ge h^0(M\widetilde A)-h^0(U,M\widetilde A|_U)\\
&=m^8\left[M^4-qM(12Ms-36)\right].
\end{aligned}
\]

Thus a simple sufficient numerical condition for the existence of divisors containing all `qM` curves is

\[
\boxed{M^2>12qs}
\]

together with `Ms>6`.

This bound is deliberately stronger than necessary, but it has two useful features:

1. it is independent of the multiplication-isogeny parameter `m`;
2. the available number of divisor sections grows like `M^4`, whereas the conditions imposed by `qM` curves grow only like `M^2`.

Consequently the nested-support ansatz has abundant asymptotic room.

For fixed smooth disjoint curves `U`, Serre vanishing/global generation for `I_U tensor O_X(M A_tilde)` and Bertini with imposed smooth base locus show that, after increasing `M` if necessary, one can choose `D` smooth and containing `U`. The dimension estimate above explains why this requirement is numerically compatible with the RM scaling.

## 3. The pure divisor bundle still works for `D in |M A_tilde|`

On the smooth divisor `D`, define as before

\[
V_D
=\mathcal O_D^{\oplus3}
\oplus\Omega_D^1
\oplus\Omega_D^2
\oplus K_D^{\oplus3}.
\]

The universal GRR calculation in `rm-smooth-isogeny-scaffold.md` applies to every smooth divisor class. Therefore

\[
\boxed{
\operatorname{ch}(i_*V_D)=12[D]=12M\widetilde A.
}
\]

## 4. Quotient onto all cubic curve blocks

For every `Z_j`, put

\[
R_j
=\mathcal O_{Z_j}
\oplus\mathcal O_{Z_j}(3\widetilde C).
\]

As before,

\[
\boxed{
\operatorname{ch}(R_j)=2\widetilde C^3.
}
\]

For `m` sufficiently large, `O_X(3 C_tilde)` is globally generated. Hence its restriction to each smooth curve `Z_j` is basepoint free. Over an infinite field, two general sections of a basepoint-free line bundle on a curve have no common zero, so there is a surjection

\[
\mathcal O_{Z_j}^{\oplus2}	woheadrightarrow
\mathcal O_{Z_j}(3\widetilde C).
\]

Together with the identity map onto `O_{Z_j}`, this gives

\[
\mathcal O_{Z_j}^{\oplus3}	woheadrightarrow R_j.
\]

Because the curves are pairwise disjoint, these maps can be chosen independently. Restricting the three trivial summands inside `V_D` therefore produces a global surjection

\[
\boxed{
V_D\twoheadrightarrow
R_U:=\bigoplus_{j=1}^{qM}R_j.
}
\]

Define the elementary-transform kernel on `D`

\[
0\longrightarrow K_{M,m}
\longrightarrow V_D
\longrightarrow R_U
\longrightarrow0.
\]

Finally regard it as a sheaf on `X`:

\[
\boxed{
E_{M,m}:=i_*K_{M,m}.
}
\]

This is one coherent sheaf, not a direct sum of oppositely shifted blocks.

## 5. Exact secant Chern character

In `K_0(X)`,

\[
[E_{M,m}]=[i_*V_D]-[R_U].
\]

Therefore

\[
\begin{aligned}
\operatorname{ch}(E_{M,m})
&=12M\widetilde A
-(qM)\,2\widetilde C^3\\
&=12M\left(
\widetilde A-\frac q6\widetilde C^3
\right).
\end{aligned}
\]

Hence

\[
\boxed{
\operatorname{ch}(E_{M,m})
=12M\,\pi^*\beta'.
}
\]

This is exactly the same RM secant ray as the split smooth-isogeny scaffold.

## 6. The transverse parity obstruction has disappeared

Locally along one `Z_j subset D`, choose coordinates

\[
R_0=k[[x_1,x_2,x_3,x_4]],
\]

with

\[
D=(x_1=0),
\qquad
Z_j=(x_1,x_2,x_3=0).
\]

The elementary transform is an honest kernel inside the divisor module. Its K-class has the required sign

\[
[V_D]-[R_j]
\]

without introducing an odd shift.

This is precisely the nested-support mechanism predicted in `rm-coupling-local-obstruction.md`. The earlier parity argument does not apply because `x_1` vanishes on the curve: the cross-Ext algebra changes, and the coupling is supplied by the quotient map itself.

## 7. Homological boundedness is automatic

The sheaf `E_{M,m}` is coherent on the smooth fourfold `X`. Thus, viewed as an object of `D^b(X)`,

\[
\boxed{
\operatorname{Ext}^{k}(E_{M,m},E_{M,m})=0
\qquad(k<0).
}
\]

Since `X` is smooth, `E_{M,m}` is also perfect.

Therefore the coupled construction satisfies the basic perfect-complex hypothesis in Perry's semiregularity theorem without any cross-Ext purity argument.

## 8. Pushforward and large tensor stabilizer

Set

\[
F_{M,m}:=\pi_*E_{M,m}.
\]

Because `pi` is finite etale,

\[
\operatorname{ch}(F_{M,m})
=12M\,m^8\beta'.
\]

Moreover for

\[
G_m=\ker(\pi^*:\operatorname{Pic}^0(X)\to\operatorname{Pic}^0(X)),
\]

projection formula gives

\[
F_{M,m}\otimes P\simeq F_{M,m}
\qquad(P\in G_m),
\]

so the isomorphism class again has tensor stabilizer

\[
|G_m|=m^8.
\]

As before, a genuine compatible linearization/cocycle still has to be constructed before invoking Perry's equivariant theorem.

## 9. What this actually solves

The previous active target asked for a coupled object with the same signed K-class as the divisor-plus-curve scaffold. The elementary transform gives exactly that:

\[
\boxed{
\text{one coherent perfect sheaf}
\quad E_{M,m}=i_*K_{M,m}
\quad\text{with}\quad
\operatorname{ch}(E_{M,m})=12M\pi^*\beta'.
}
\]

Thus the problem is no longer **whether a coupling exists**. A coupling exists very explicitly once the supports are nested.

What remains is the decisive deformation calculation:

\[
\boxed{
(P_{01}-qB_{01})\cdot at_{E_{M,m}}=0,
\qquad
(P_{23}-qB_{23})\cdot at_{E_{M,m}}=0\ ?
}
\]

The total Chern character guarantees that both directions vanish after applying semiregularity, but injectivity on the Atiyah image is exactly what is still unknown.

## 10. New immediate experiment

The elementary-transform sequence gives a much more concrete way to attack those two classes than the split complex did.

The next calculation should write the Atiyah class of the kernel in terms of the Atiyah classes of

\[
V_D,
\qquad
R_U,
\qquad
\text{and the quotient }V_D\to R_U,
\]

and evaluate the two mixed generalized directions on this exact triangle.

A positive result for both directions would establish

\[
\ker(at_{E_{M,m}})=\ker(\mu_{\beta'}),
\]

because the six ordinary RM directions are already built geometrically into the relative construction and the reverse inclusion follows from the semiregularity--Atiyah compatibility diagram.