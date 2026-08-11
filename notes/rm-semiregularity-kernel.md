# Real multiplication: an explicit 8-dimensional Chern-action kernel

> **Status.** This note computes the infinitesimal Chern-character action for the real-multiplication secant class appearing in Markman's Example 11.2.7. The computation reduces Markman's remaining semiregularity condition to an exact rank statement for the Atiyah obstruction map. It does **not** prove that rank statement.

## 1. The exact open condition

Markman's Question 11.2.2 asks, for a genus-4 Jacobian `X`, for a sheaf `F_2` whose Chern character lies in the real-multiplication secant space `B` and for which the semiregularity map is injective on

\[
\operatorname{im}\bigl(at_{F_2}:HT^2(X)\to\operatorname{Ext}^2(F_2,F_2)\bigr).
\]

Example 11.2.7 constructs a simple coherent sheaf `E'` with Chern character an integer multiple of

\[
\beta'=g^*\Theta-\frac q6(g^{-1})^*(\Theta^3),
\]

where `X` has real multiplication by a real quadratic field `F`, `f in F` has norm one, `f^2 != 1`, and the Hodge endomorphism associated to `f` is induced by an automorphism `g` of `X`.

The missing issue is therefore the Atiyah/semiregularity condition for this explicit `E'`.

## 2. Diagonalizing the real multiplication

Over `C`, write

\[
H^{1,0}(X)=U_+\oplus U_-,
\qquad \dim U_+=\dim U_-=2,
\]

for the two real embeddings of `F`. Choose coordinates `z_1,z_2` on `U_+` and `z_3,z_4` on `U_-`, and write

\[
\Theta_+=z_1\bar z_1+z_2\bar z_2,
\qquad
\Theta_-=z_3\bar z_3+z_4\bar z_4,
\qquad
\Theta=\Theta_++\Theta_-.
\]

Markman's formula `g^*Theta=f^2 . Theta`, together with `Nm(f)=1`, gives

\[
g^*\Theta=A\Theta_++A^{-1}\Theta_-,
\]

and

\[
(g^{-1})^*\Theta=A^{-1}\Theta_++A\Theta_-,
\]

where

\[
A=\hat\sigma_1(f)^2>0.
\]

The assumption `f^2 != 1` implies `A != 1`.

Since `Theta_+^3=Theta_-^3=0`,

\[
\boxed{
\beta'
=A\Theta_++A^{-1}\Theta_-
-\frac q2\left(
A^{-1}\Theta_+^2\Theta_-
+A\Theta_+\Theta_-^2
\right).
}
\]

Multiplying `beta'` by the positive integer used to obtain `ch(E')` does not change the kernel of the infinitesimal Chern action.

## 3. The 28-dimensional generalized deformation space

For an abelian fourfold,

\[
HT^2(X)
=H^2(\mathcal O_X)
\oplus H^1(T_X)
\oplus H^0(\wedge^2T_X),
\]

with dimensions

\[
6+16+6=28.
\]

Under HKR, the Chern-character action associated to `beta'` is the map

\[
\mu_{\beta'}:HT^2(X)\longrightarrow H\Omega_{-2}(X)
\]

with

\[
H\Omega_{-2}(X)
=H^2(\mathcal O_X)
\oplus H^3(\Omega_X^1)
\oplus H^4(\Omega_X^2),
\]

also of dimension `28`.

The action is wedge product on the `H^2(O_X)` summand, contraction followed by wedge product on `H^1(T_X)`, and double contraction on `H^0(wedge^2 T_X)`. Up to the conventional HKR signs, Buchweitz--Flenner's Atiyah-Chern formalism gives

\[
\boxed{
\mu_{ch(E')}=\sigma_{E'}\circ at_{E'}.
}
\]

Thus

\[
\ker(at_{E'})\subseteq\ker(\mu_{\beta'}).
\]

## 4. Exact rank: 20

Let

\[
D_{ij}=\bar z_j\otimes\partial_{z_i}\in H^1(T_X).
\]

Let

\[
P_+=\partial_{z_1}\wedge\partial_{z_2},
\quad
P_-=\partial_{z_3}\wedge\partial_{z_4},
\]

and

\[
B_+=\bar z_1\wedge\bar z_2,
\quad
B_-=\bar z_3\wedge\bar z_4.
\]

A direct exterior-algebra calculation gives eight independent vectors in the kernel:

\[
\boxed{
\begin{aligned}
&D_{11},\quad D_{22},\quad D_{12}+D_{21},\\
&D_{33},\quad D_{44},\quad D_{34}+D_{43},\\
&B_+-q^{-1}P_+,\quad B_--q^{-1}P_-.
\end{aligned}
}
\]

The first six lie in `H^1(T_X)`. The last two mix ordinary `B`-field directions with bivector/Poisson directions.

To show that these are the whole kernel, use the ordered exterior bases implemented in `scripts/verify_rm_semiregularity_kernel.py`. A fixed `20 x 20` minor of the resulting `24 x 28` matrix has determinant

\[
\boxed{
-\frac{q^8}{A^{16}}
(A-1)^8(A+1)^8(A^2+1)^8.
}
\]

For the real-multiplication case `q != 0`, `A>0`, and `A != 1`, this determinant is nonzero. Hence the map has rank at least `20`. The eight displayed kernel vectors give rank at most `20`. Therefore

\[
\boxed{
\operatorname{rank}(\mu_{\beta'})=20,
\qquad
\dim\ker(\mu_{\beta'})=8.
}
\]

The excluded scalar case is genuinely different: at `A=1` the rank drops to `12`.

## 5. Structure of the six ordinary deformation directions

Write a class in `H^1(T_X)` as

\[
M=\sum_{i,j}m_{ij}D_{ij}.
\]

The `H^2(O_X)` and `H^4(Omega_X^2)` components of `mu_beta'(M)` imply, for `A != 1`, that all cross-block coefficients vanish and each `2 x 2` diagonal block is symmetric. Thus

\[
\ker(\mu_{\beta'}|_{H^1(T_X)})
=\operatorname{Sym}^2(U_+^\vee)
\oplus\operatorname{Sym}^2(U_-^\vee),
\]

of dimension `3+3=6`.

This is exactly the linear-algebra shape expected for infinitesimal polarized deformations preserving the real-multiplication splitting. This identification is a geometric interpretation of the kernel calculation; it does not by itself prove that `E'` deforms along those directions.

## 6. The semiregularity question is now an Atiyah-rank question

Because

\[
\mu_{\beta'}=\sigma_{E'}\circ at_{E'},
\]

we always have

\[
\ker(at_{E'})\subseteq\ker(\mu_{\beta'}).
\]

Markman's desired injectivity of `sigma_E'` on `im(at_E')` is equivalent to the reverse inclusion. Hence it is equivalent to any of the following statements:

\[
\boxed{
\ker(at_{E'})=\ker(\mu_{\beta'}),
}
\]

\[
\boxed{
\dim\ker(at_{E'})=8,
}
\]

or

\[
\boxed{
\operatorname{rank}(at_{E'})=20.
}
\]

There is an even sharper sufficient target:

> **It is enough to prove that the eight explicit vectors displayed in Section 4 lie in `ker(at_E')`.**

Since `ker(at_E')` is already contained in their eight-dimensional span, eight independent Atiyah-zero directions would force equality and prove the requested semiregularity-on-the-Atiyah-image condition.

## 7. Two possible attacks on the remaining rank bound

### A. Deform the explicit glued sheaf

The six `H^1(T_X)` kernel vectors are the RM-preserving polarized directions. If the glued sheaf in Example 11.2.7 can be constructed relatively along these first-order deformations, then those six vectors lie in `ker(at_E')`.

This route needs a relative version of all ingredients in the gluing construction: the secant sheaf, the curve `C'`, the generic translates, and the fiber identifications. Hodge-theoretic preservation of `beta'` alone is not sufficient; an actual first-order deformation of the object is needed.

The remaining two directions

\[
B_+-q^{-1}P_+,
\qquad
B_--q^{-1}P_-
\]

are genuinely generalized directions and likely require a Fourier--Mukai/noncommutative interpretation rather than an ordinary family of varieties.

### B. Prove the upper bound `rank(at_E') <= 20`

The Chern-action computation already gives

\[
\operatorname{rank}(at_{E'})\ge20.
\]

Therefore any independent argument showing

\[
\operatorname{rank}(at_{E'})\le20
\]

would immediately force equality and settle the missing condition.

This suggests computing the Atiyah action through the explicit local-to-global Ext algebra of Markman's glued sheaf. A factorization of the Atiyah map through a `20`-dimensional quotient is enough; one does not need the full `Ext^2(E',E')` algebra.

## 8. Falsifiable next milestone

For the sheaf `E'` of Example 11.2.7:

1. write the local-to-global Ext spectral sequence for the gluing of the `N` translated surface sheaves to the curve sheaf;
2. isolate the image of `HT^2(X)` under the Atiyah action;
3. prove that this image has dimension at most `20`, or directly annihilate the eight kernel vectors above;
4. if the image has dimension greater than `20`, reject the proposed reduction or locate the mismatch in the HKR/semiregularity convention.

This is now a concrete finite-dimensional target rather than an undifferentiated semiregularity problem.

## References

- E. Markman, *Secant sheaves on abelian n-folds with real multiplication and Weil classes on abelian 2n-folds with complex multiplication*, arXiv:2509.23079, especially Question 11.2.2, Corollary 11.2.6, and Example 11.2.7.
- R.-O. Buchweitz and H. Flenner, *The Atiyah-Chern Character yields the Semiregularity Map as well as the Infinitesimal Abel-Jacobi Map*, arXiv:math/9907004.
- R.-O. Buchweitz and H. Flenner, *A Semiregularity Map for Modules and Applications to Deformations*, arXiv:math/9912245.
