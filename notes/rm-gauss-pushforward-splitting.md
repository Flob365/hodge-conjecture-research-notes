# Gauss-map splitting behind the twisted `1,11,11,1` profile

> **Status.** For a smooth principal theta divisor in an abelian fourfold and a nontrivial degree-zero twist, this note proves that the pushforward of the twist by the canonical/Gauss map splits as `O(-1) + 11 O(-2) + 11 O(-3) + O(-4)`. This gives a concrete geometric origin for the twisted `1,11,11,1` module and identifies the two middle 11-dimensional Hodge groups as the multiplicity spaces of the `O(-2)` and `O(-3)` summands. It does not yet prove the rank-eight Milestone B.

## 1. The Gauss map is finite of degree 24

Let `(X,Theta)` be a principally polarized abelian fourfold with smooth theta divisor

\[
D=\Theta.
\]

By adjunction

\[
K_D=O_D(\Theta).
\]

The four translation derivatives of the theta section form a basis of `H^0(D,K_D)` and define the canonical map

\[
\gamma:D\longrightarrow \mathbf P^3,
\]

which is the Gauss map.

Because `K_D` is ample, a positive-dimensional fiber of `gamma` is impossible: `K_D=gamma^*O(1)` would have degree zero on every curve in such a fiber. Thus `gamma` is finite.

Moreover

\[
\deg\gamma=K_D^3=\Theta^4=4!=24.
\]

This agrees with the general Gauss-map degree formula in the smooth case.

## 2. Push forward a nontrivial flat twist

Let

\[
P\in Pic^0(X),\qquad P\neq O_X,
\]

and write again `P` for its restriction to `D`. Define

\[
\boxed{\mathcal F_P:=\gamma_*P.}
\]

Since `gamma` is finite, `D` is smooth Cohen--Macaulay, and `P^3` is regular of the same dimension, `gamma` is finite flat. Hence `F_P` is a vector bundle of rank

\[
24.
\]

Projection formula gives

\[
H^i(\mathbf P^3,\mathcal F_P(m))
=H^i(D,K_D^m\otimes P).
\]

## 3. There is no intermediate cohomology for any twist

For `m>=1`, use

\[
0\to O_X((m-1)\Theta)\otimes P
\to O_X(m\Theta)\otimes P
\to K_D^m\otimes P
\to0.
\]

For `m=1`, the first term is the nontrivial degree-zero line bundle `P`, whose cohomology vanishes in every degree, while `O_X(Theta) tensor P` satisfies IT(0). For `m>=2`, both ambient line bundles are ample twists and satisfy IT(0). Therefore

\[
H^i(D,K_D^m\otimes P)=0\qquad(i>0,m\ge1),
\]

and

\[
h^0(D,K_D^m\otimes P)
=m^4-(m-1)^4.
\]

For `m<=0`, Serre duality on the threefold `D` gives

\[
H^i(D,K_D^m\otimes P)^\vee
\cong
H^{3-i}(D,K_D^{1-m}\otimes P^{-1}).
\]

Since `1-m>=1`, the preceding positive-twist calculation applies. Hence for `m<=0` the only possible cohomology is `H^3`.

Thus

\[
\boxed{
H^1(\mathbf P^3,\mathcal F_P(m))
=H^2(\mathbf P^3,\mathcal F_P(m))=0
\quad\text{for every }m\in\mathbf Z.
}
\]

## 4. Horrocks forces complete splitting

By Horrocks' splitting criterion, a vector bundle on `P^3` with no intermediate cohomology in any twist is a direct sum of line bundles. Hence

\[
\mathcal F_P\cong\bigoplus_{j=1}^{24}O(a_j).
\]

The degrees are forced by the extreme cohomology.

First,

\[
H^0(\mathcal F_P)=H^0(D,P)=0,
\]

so every `a_j<0`.

Next,

\[
h^0(\mathcal F_P(1))
=h^0(D,K_D\otimes P)=1.
\]

Therefore exactly one summand is `O(-1)` and all remaining summands have degree at most `-2`.

Serre duality gives

\[
h^3(\mathcal F_P)
=h^3(D,P)
=h^0(D,K_D\otimes P^{-1})=1.
\]

Since `h^3(O(-4))=1` and `h^3(O(k))=0` for `k>-4`, while a summand of degree at most `-5` would contribute more than one dimension, there is exactly one `O(-4)` and no summand of lower degree.

Finally

\[
h^0(\mathcal F_P(2))
=2^4-1^4=15.
\]

The already known `O(-1)` contributes four sections to this group. Each `O(-2)` contributes one, while `O(-3)` and `O(-4)` contribute none. Hence there are exactly eleven copies of `O(-2)`. Rank 24 then forces eleven copies of `O(-3)`.

Therefore

\[
\boxed{
\mathcal F_P
\cong
O(-1)
\oplus O(-2)^{\oplus11}
\oplus O(-3)^{\oplus11}
\oplus O(-4).
}
\]

The Hilbert polynomial is correspondingly

\[
\chi(\mathcal F_P(m))
=4m^3-6m^2+4m-1
=m^4-(m-1)^4.
\]

## 5. The twisted Jacobian module is the generator space of the split Gauss module

Let

\[
S=\mathbf C[x_1,x_2,x_3,x_4]
\]

be the homogeneous coordinate ring of `P^3`. The four variables pull back to the four canonical theta-gradient sections of `K_D`.

The graded module

\[
M_P:=\bigoplus_{m\ge0}H^0(D,K_D^m\otimes P)
\]

is the graded module of global sections of `F_P`; the splitting above gives

\[
\boxed{
M_P\cong
S(-1)
\oplus S(-2)^{11}
\oplus S(-3)^{11}
\oplus S(-4).
}
\]

Consequently the minimal generator space

\[
M_P/(x_1,x_2,x_3,x_4)M_P
\]

has Hilbert profile

\[
\boxed{1,11,11,1.}
\]

This is exactly the twisted Jacobian/Koszul profile found earlier by direct theta-function calculations.

So the profile is not accidental: it is the splitting type of the finite Gauss cover.

## 6. The two middle Hodge groups are the two multiplicity spaces

The Gauss map also identifies the cotangent bundles with standard bundles on `P^3`.

The pulled-back Euler sequences give

\[
\boxed{
\Omega_D^1\cong\gamma^*T_{\mathbf P^3}(-1),
\qquad
T_D\cong\gamma^*\Omega_{\mathbf P^3}^1(1).
}
\]

Since `rank Omega_D^1=3`,

\[
\Omega_D^2
\cong\gamma^*\Omega_{\mathbf P^3}^1(2).
\]

By projection formula,

\[
H^1(D,\Omega_D^2\otimes P)
=H^1\bigl(\mathbf P^3,\Omega^1(2)\otimes\mathcal F_P\bigr).
\]

Substitute the splitting. The only summands contributing to `H^1` are

\[
\Omega^1(2)\otimes O(-2)=\Omega^1,
\]

and `h^1(P^3,Omega^1)=1`. Therefore

\[
\boxed{
H^1(D,\Omega_D^2\otimes P)
\cong\mathbf C^{11},
}
\]

canonically attached to the multiplicity space of the eleven `O(-2)` summands.

Similarly

\[
H^2(D,\Omega_D^1\otimes P)
=H^2\bigl(\mathbf P^3,T(-1)\otimes\mathcal F_P\bigr).
\]

The only contributing summands are

\[
T(-1)\otimes O(-3)=T(-4),
\]

and `h^2(P^3,T(-4))=1` by the Euler sequence/Serre duality. Hence

\[
\boxed{
H^2(D,\Omega_D^1\otimes P)
\cong\mathbf C^{11},
}
\]

coming exactly from the multiplicity space of the eleven `O(-3)` summands.

Thus the Milestone-B operator

\[
T_Q:
H^1(\Omega_D^2\otimes P)
\longrightarrow
H^2(\Omega_D^1\otimes P)
\]

is literally the middle `11 x 11` block of the infinitesimal variation of the finite Gauss-cover module.

## 7. Duality pairs the two eleven-dimensional blocks

Finite Grothendieck duality gives

\[
(\gamma_*P)^\vee
\cong
\gamma_*\bigl(P^{-1}\otimes\omega_D\otimes\gamma^*\omega_{\mathbf P^3}^{-1}\bigr).
\]

Since

\[
\omega_D=K_D=\gamma^*O(1),
\qquad
\omega_{\mathbf P^3}=O(-4),
\]

we obtain

\[
\boxed{
\mathcal F_P^\vee
\cong
\mathcal F_{P^{-1}}(5).
}
\]

On splitting types this exchanges

\[
O(-1)\leftrightarrow O(-4),
\qquad
O(-2)^{11}\leftrightarrow O(-3)^{11}.
\]

This is the geometric origin of the perfect duality between the two middle eleven-dimensional twisted Hodge spaces.

## 8. Consequence for Milestone B

The remaining problem can now be stated without the previous abstract Jacobian-module language.

Choose a deformation direction `Q`. Its twisted IVHS central block is a linear map between the two multiplicity spaces

\[
\boxed{
T_Q:\mathbf C^{11}_{(-2)}\longrightarrow\mathbf C^{11}_{(-3)}.
}
\]

For the proposed rank-one extension design `Q_0=v^2`, Milestone B asks for

\[
\boxed{rank(T_{Q_0})=8.}
\]

The three-dimensional kernel should be generated by the compatible mixed directions `v odot w_i` used to build the rank-six Kodaira--Spencer bundle.

Thus the next calculation is the infinitesimal deformation of the **splitting of the Gauss pushforward** and, in particular, the rank of its middle block. The finite-cover description gives a new route to this calculation through the Gauss map, its ramification divisor, and the induced variation of the two multiplicity spaces.

## References

- G. Codogni, S. Grushevsky, E. Sernesi, *The degree of the Gauss map of the theta divisor*, arXiv:1608.02686. For a smooth theta divisor the Gauss linear system is basepoint-free; in dimension four its degree is `Theta^4=24`.
- E. Izadi, J. Wang, *The primitive cohomology of theta divisors*, arXiv:1410.5868, for the gradient/canonical description and the associated Koszul cohomology of a smooth theta divisor.