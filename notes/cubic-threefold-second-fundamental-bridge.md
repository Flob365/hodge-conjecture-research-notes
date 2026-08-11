# The cubic-threefold second-fundamental-form bridge

> **Status.** This note identifies the exact cubic-threefold object having the same source and target as the five-dimensional nonambient correction map of a smooth genus-4 theta divisor. The established facts strongly suggest that the theta correction is the pullback of the dual second fundamental form of the cubic intermediate-Jacobian locus. The final comparison is not yet proved here.

## 1. The two five-dimensional spaces on the theta side

Let `(A,Theta)` be a principally polarized abelian fourfold with smooth theta divisor

\[
D=\Theta.
\]

The primitive middle Hodge structure

\[
K_D^{\rm prim}\subset H^3(D)
\]

has Hodge numbers

\[
h^{2,1}_{\rm prim}=h^{1,2}_{\rm prim}=5.
\]

The residue/Koszul description gives the concrete realization

\[
\boxed{
Q_D=
H^0(D,2K_D)/\operatorname{Sym}^2H^0(D,K_D),
\qquad \dim Q_D=5.
}
\]

Thus `Q_D` is the `K^{2,1}` piece of the primitive theta Hodge structure.

The intrinsic cup-wedge product of polarized deformations is

\[
\omega_D:\operatorname{Sym}^2H^1(T_D)
\longrightarrow H^2(\Lambda^2T_D).
\]

Its ambient projection has rank `20`; its nonambient part lands in the canonical five-dimensional kernel `Q_D`. Since

\[
H^1(T_D)\cong\operatorname{Sym}^2W,
\qquad \dim W=4,
\]

and

\[
\operatorname{Sym}^2(\operatorname{Sym}^2W)
=S_{(2,2)}W\oplus\operatorname{Sym}^4W,
\]

the nonambient part is exactly the map

\[
\boxed{
\tau_D:\operatorname{Sym}^4W\to Q_D
}
\]

introduced in `principal-theta-quartic-correction-map.md`.

## 2. Donagi's cubic and the primitive Hodge structure

For `(A,Theta)` in a dense open subset of `A_4`, Donagi associates a smooth cubic threefold

\[
T=T(A,\Theta)\subset\mathbf P^4
\]

together with a two-torsion point of its intermediate Jacobian.

The construction is generically finite and dominant onto the locus `C` of intermediate Jacobians of smooth cubic threefolds.

Kramer--Weissauer and the work they cite identify the ten-dimensional primitive theta Hodge structure with the Hodge structure of the cubic intermediate Jacobian, up to the standard Tate twist:

\[
H^1(B_D,\mathbf Q)
\cong
H^1(JT,\mathbf Q)(-1).
\]

Izadi--Wang describe the same primitive theta structure by an Abel--Jacobi family of Prym-embedded curves inside `Theta`.

Consequently, on the dense locus where the constructions are simultaneously available,

\[
\boxed{
Q_D\cong H^{2,1}(T).
}
\]

The identification is meant at the level of the naturally associated variation of Hodge structure; normalizations and dual/Tate conventions should be fixed when writing a comparison formula.

## 3. Jacobian ring of a cubic threefold

Let

\[
T=V(F)\subset\mathbf P^4
\]

be smooth and put

\[
R_F=\mathbf C[x_0,\ldots,x_4]/J_F,
\qquad
J_F=(\partial_0F,\ldots,\partial_4F).
\]

The five partial derivatives form a regular sequence of quadrics, so

\[
\operatorname{Hilb}(R_F,t)=(1+t)^5.
\]

Hence the graded dimensions are

\[
\boxed{1,5,10,10,5,1.}
\]

Macaulay duality has socle degree `5`:

\[
R_F^i\cong (R_F^{5-i})^*.
\]

Griffiths' residue description gives

\[
\boxed{
H^{2,1}(T)\cong R_F^1,
\qquad
H^{1,2}(T)\cong R_F^4,
}
\]

and infinitesimal cubic deformations are

\[
\boxed{T_{[T]}\mathcal C\cong R_F^3.}
\]

Since `dim R_F^3=10`, this matches `dim A_4=10`.

The infinitesimal period map is multiplication

\[
R_F^3\otimes R_F^1\to R_F^4.
\]

Equivalently, after Macaulay duality, a tangent class `q in R_F^3` gives the symmetric bilinear form

\[
(a,b)\longmapsto \langle qab\rangle_{R_F^5}
\]

on `R_F^1`.

## 4. The cubic locus inside `A_5`

The intermediate Jacobian locus

\[
\mathcal C\subset\mathcal A_5
\]

has dimension `10` and codimension `5`.

Colombo--Frediani--Naranjo--Pirola give at `JT` the exact cotangent description

\[
\Omega^1_{\mathcal A_5}|_{JT}
\cong\operatorname{Sym}^2R_F^1,
\]

\[
\Omega^1_{\mathcal C}|_{JT}
\cong R_F^2,
\]

and the restriction map is multiplication

\[
f:\operatorname{Sym}^2R_F^1\to R_F^2.
\]

Since `R_F^1` is the space of linear forms and the Jacobian ideal first appears in degree two,

\[
\ker(f)=J_F^2,
\qquad \dim J_F^2=5.
\]

Thus

\[
\boxed{
N^*_{\mathcal C/\mathcal A_5,JT}\cong J_F^2.
}
\]

The five elements of `J_F^2` are the polar quadrics

\[
\Gamma_p(T)=
\sum_{i=0}^4a_i\,\partial_iF,
\qquad p=[a_0:\cdots:a_4]\in\mathbf P^4.
\]

The gradient map identifies

\[
J_F^2\cong (R_F^1)^*
\]

up to the standard coordinate duality, so

\[
N_{\mathcal C/\mathcal A_5,JT}
\cong R_F^1
\cong H^{2,1}(T).
\]

This is the same five-dimensional Hodge space as `Q_D`.

## 5. The second fundamental form has exactly our type

The second fundamental form of the cubic locus is

\[
II_{\mathcal C/\mathcal A_5}:
J_F^2\to\operatorname{Sym}^2R_F^2.
\]

Using Macaulay duality

\[
R_F^2\cong(R_F^3)^*,
\qquad
(J_F^2)^*\cong R_F^1,
\]

dualizing gives

\[
\boxed{
II^\vee_{\mathcal C/\mathcal A_5}:
\operatorname{Sym}^2R_F^3\to R_F^1.
}
\]

Therefore the source and target dimensions are

\[
55\longrightarrow5,
\]

identical to the full nonambient quadratic correction on the theta side.

Colombo et al. prove the strong identity

\[
\boxed{
\operatorname{Im}(II_{\mathcal C/\mathcal A_5})
\subseteq
\ker\left[
\operatorname{Sym}^2R_F^2\xrightarrow{m_F}R_F^4
\right].
}
\]

They also show that `II` is nonzero and relate it to Hodge-Gaussian maps, Prym theory, Jacobian ideals, and polar quadrics. For a nonempty open set of cubic threefolds there exist points whose polar quadrics have rank three.

## 6. The comparison conjecture

Let

\[
\phi:\mathcal A_4\dashrightarrow\mathcal C
\]

be the Donagi correspondence on the dense open where it is defined. Its differential is an isomorphism at a generic point because `phi` is generically finite and dominant:

\[
d\phi:H^1(T_D)\xrightarrow{\sim}R_F^3.
\]

The primitive theta variation and the intermediate-Jacobian variation are identified by the Abel--Jacobi correspondence reviewed above.

This leads to the precise bridge to prove:

> **Cubic second-fundamental-form bridge.** Under the identifications
> \[
> H^1(T_D)\cong R_F^3,
> \qquad
> Q_D\cong R_F^1,
> \]
> the nonambient projection of the intrinsic theta cup-wedge product
> \[
> \operatorname{Sym}^2H^1(T_D)\to Q_D
> \]
> equals, up to a nonzero universal scalar and the Hodge-duality convention, the pullback of
> \[
> II^\vee_{\mathcal C/\mathcal A_5}.
> \]

Equivalently,

\[
\boxed{
\pi_{Q_D}\circ\omega_D
\stackrel{?}{=}
(d\phi)^*II^\vee.
}
\]

The equality is not claimed as proved in this note.

## 7. Why the bridge is structurally plausible

Both sides are secondary deformation operations:

1. `omega_D` differs from the ambient double-antisymmetrization only by the five-dimensional correction `Q_D`;
2. the second fundamental form measures the failure of the first derivative of the primitive period map to remain tangent to the cubic locus;
3. the primitive theta VHS is the cubic intermediate-Jacobian VHS on the Donagi open set;
4. Karpishpan's higher-period-map formalism shows in general that second fundamental forms of a VHS depend only on first Kodaira--Spencer data, exactly as the cup-wedge correction does.

What remains is to compare normalizations at the chain level (residue/Koszul on the theta side versus Gauss--Manin/Hodge-Gaussian on the cubic side).

## 8. The five quartics become restricted second-fundamental quadrics

Assume the bridge. Write

\[
T=H^1(T_D)\cong\operatorname{Sym}^2W,
\qquad \dim W=4.
\]

The dual second fundamental form is a five-dimensional linear system of quadrics on

\[
\mathbf P(T)=\mathbf P^9.
\]

Restrict it to the rank-one Veronese locus

\[
\nu_2:\mathbf P(W)=\mathbf P^3\hookrightarrow\mathbf P(T),
\qquad [v]\mapsto[v^2].
\]

Each quadratic equation on `T` restricts to a quartic on `W`. These are exactly the five quartics encoded by

\[
\tau_D^*:Q_D^*\to\operatorname{Sym}^4W^*.
\]

For fixed `v`, the map

\[
\tau_{D,v}:W\to Q_D,
\qquad w\mapsto\tau_D(v^3w)
\]

is the differential at `[v]` of this restricted five-quartic map.

Thus the common-factor survival condition

\[
\operatorname{rank}(\tau_{D,v})\le1
\]

becomes a severe ramification condition for the second-fundamental-form linear system restricted to the Veronese `P^3`.

This gives a concrete computational target on the cubic side.

## 9. Immediate next calculations

1. Prove the bridge by comparing the second derivative of the primitive theta period map with the cup-wedge correction `omega_D`.
2. Once the bridge is established, compute the differential rank of the five second-fundamental quadrics on the Veronese rank-one locus.
3. Test the Klein cubic and a generic cubic with a rank-three polar quadric, where explicit equations are available in Colombo et al.
4. If the restricted differential has rank at least two at every point, reject the Kodaira--Spencer middle-extension architecture.
5. If a point with rank at most one exists, its three-dimensional kernel supplies exactly the three Kodaira--Spencer classes required by the construction.

## References

- T. Kramer and R. Weissauer, *The symmetric Square of the Theta Divisor in Genus 4*, arXiv:1109.2249.
- E. Izadi and J. Wang, *The primitive cohomology of theta divisors*, arXiv:1410.5868.
- E. Colombo, P. Frediani, J. C. Naranjo, G. P. Pirola, *The second fundamental form of the moduli space of cubic threefolds in A_5*, arXiv:2207.13432.
- Y. Karpishpan, *Higher-order differentials of the period map and higher Kodaira-Spencer classes*, arXiv:alg-geom/9405005.
