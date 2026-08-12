# Retracted: the naive Fourier-kernel resolution

> **Status: RETRACTED.** The K-theory identity used in the previous version of this note is correct, but it was incorrectly promoted to a global locally free resolution by powers of the principal theta line bundle. The resulting rank-eight Fourier-kernel construction is therefore not valid and must not be used.

## 1. What remains correct

Let `D=Theta` be a smooth principal theta divisor, `L=O_X(Theta)`, and

\[
0\to O_D^{\oplus3}\to E\to\Omega_D^1\to0.
\]

In K-theory one does have

\[
[i_*\Omega_D^1]
=4[O_X]-5[L^{-1}]+[L^{-2}],
\]

and hence

\[
\boxed{
[i_*E]=7[O_X]-8[L^{-1}]+[L^{-2}].
}
\]

This is only a K-class identity.

## 2. Why the claimed resolution cannot exist

The previous note asserted a resolution

\[
0\to L^{-2}\to L^{-1\,\oplus8}\to O_X^{\oplus7}\to i_*E\to0.
\]

That assertion is false.

The conormal map on the theta divisor

\[
K_D^{-1}\longrightarrow O_D^{\oplus4}
\]

is given by the four translation derivatives

\[
\theta_1|_D,\ldots,\theta_4|_D\in H^0(D,K_D).
\]

These become honest canonical sections only **after restriction to `D`**: the inhomogeneous terms in the theta transformation law are multiples of `theta` and vanish on `D`.

They do not lift to four independent global sections of `L` on `X`, because for a principal polarization

\[
h^0(X,L)=1.
\]

Indeed every global morphism

\[
L^{-2}\to L^{-1}
\]

is multiplication by a scalar multiple of the single theta section. Therefore any map

\[
L^{-2}\to L^{-1\,\oplus8}
\]

has eight components proportional to the same section. Its Fourier transform cannot produce the rank-eight quotient asserted in the previous version.

This gives an internal contradiction and invalidates the proposed resolution.

## 3. Source of the mistake

A vector bundle on the hypersurface `D`, viewed as an `O_X`-module, is locally Cohen--Macaulay of codimension one and locally has projective dimension one. Globally it admits a two-term resolution by suitable vector bundles on `X`, but those vector bundles need not split as sums of powers of `L`.

The formal identity

\[
7[O_X]-8[L^{-1}]+[L^{-2}]
\]

therefore records the class in `K_0(X)` but does **not** determine a resolution or its differentials.

The horseshoe/mapping-cone argument failed precisely because the four conormal derivative sections do not lift to maps between the chosen line-bundle resolutions on `X`.

## 4. Consequence

The following claims from the previous version are withdrawn:

- the existence of a rank-sixteen-to-rank-eight Fourier map coming from that line-bundle complex;
- the rank-eight bundle `K` defined as its kernel;
- the reformulation of Milestone B as `(-1)^*K^vee -> K`;
- the proposed stability and theta-group routes based on that bundle.

The independent results remain unaffected:

1. Milestone A for a smooth principal theta divisor;
2. the K-theory/Chern-character identities for the divisor block;
3. the extension-space reduction
   \[
   H^1(Sym^2E\,K_D^{-1})=0,
   \qquad
   H^1(\Lambda^2E\,K_D^{-1})\hookrightarrow H^1(T_D);
   \]
4. the fact that Milestone B asks for one nondegenerate symmetric middle pairing arising from a surviving extension class.

## 5. Correct next target

Return to the intrinsic theta-divisor problem. For

\[
\kappa=(Q_1,Q_2,Q_3)
\]

defining `E`, determine explicitly

\[
Ext^1(E^\vee\otimes K_D,E)
=H^1(\Lambda^2E\,K_D^{-1})
\subset H^1(T_D),
\]

and compute, for a surviving class `Q_0`, the induced map

\[
H^1(E^\vee K_D\otimes P)
\longrightarrow
H^2(E\otimes P).
\]

The most concrete candidate remains the rank-one ambient pattern

\[
Q_0=v\odot v,
\qquad
Q_i=v\odot w_i,
\quad i=1,2,3,
\]

whose pairwise exterior products with `Q_0` vanish at the ambient Dolbeault-cochain level. The next task is to verify whether this yields a genuine surviving extension and whether its middle form is necessarily degenerate or can be made invertible.