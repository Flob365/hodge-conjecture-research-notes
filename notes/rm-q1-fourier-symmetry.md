# The `q=1` Fourier-symmetry route

> **Status.** This note isolates a special feature of Markman's real-multiplication construction when `q=1`: the RM secant class is fixed by the cohomological Fourier transform, while the two unresolved generalized deformation directions are exchanged with opposite parity. This gives a plausible equivariant route around the local elementary-transform no-go. The main unresolved issues are gluing/negative Exts and the geometric-origin hypothesis for a Fourier-generated invariant category.

## 1. Specialize to `q=1`

Markman's genus-4 real-quadratic setup allows `q` to be any positive integer. We therefore specialize to

\[
q=1.
\]

Put

\[
A=g^*\Theta,
\qquad
C=(g^{-1})^*\Theta.
\]

The target secant class becomes

\[
\boxed{
\beta=A-\frac16C^3.
}
\]

Both `A` and `C` are principal polarization classes because `g` is an automorphism.

## 2. Fourier exchanges the divisor and cubic terms

Identify `X` with its dual using the principal polarization and let

\[
\Phi=\Phi_{\mathcal P}:D^b(X)\to D^b(X)
\]

be the normalized Poincare Fourier--Mukai transform.

For a principal polarization class `A` whose dual inverse class is `C`, the cohomological Fourier transform satisfies

\[
\Phi^H(e^A)=e^{-C}.
\]

Comparing graded pieces gives

\[
\boxed{
\Phi^H(A)=-\frac16C^3,
\qquad
\Phi^H\!\left(\frac16C^3\right)=-A.
}
\]

Hence

\[
\boxed{
\Phi^H(\beta)=\beta.
}
\]

This is the first exact symmetry found in these notes which preserves the RM secant direction while exchanging its degree-two and degree-six pieces.

## 3. A finite categorical Fourier symmetry

For an abelian fourfold, Mukai duality gives

\[
\Phi^2\simeq(-1_X)^*[-4].
\]

Define

\[
\boxed{\Psi:=\Phi[2].}
\]

Then

\[
\Psi^2\simeq(-1_X)^*,
\qquad
\Psi^4\simeq id.
\]

Thus `Psi` generates a finite categorical symmetry of order dividing four.

The even shift `[2]` does not change the Chern character, so `Psi` has the same cohomological action as `Phi` on the secant class.

## 4. The two mixed RM directions are Fourier-odd

Under the standard generalized-cohomology action of the Poincare Fourier transform, the two summands

\[
H^2(O_X)
\quad\text{and}\quad
H^0(\wedge^2T_X)
\]

are exchanged. In each RM two-dimensional block, after fixing the HKR sign convention, one may normalize so that

\[
B_+\longleftrightarrow P_+,
\qquad
B_-\longleftrightarrow P_-.
\]

For `q=1`, the two generalized Chern-kernel directions are

\[
\xi_+=B_+-P_+,
\qquad
\xi_-=B_--P_-.
\]

Therefore

\[
\boxed{
\Psi(\xi_+)=-\xi_+,
\qquad
\Psi(\xi_-)=-\xi_-.
}
\]

In contrast, the total Chern character `beta` is Fourier-even.

This is exactly the representation-theoretic separation that was unavailable for finite translation--tensorization subgroups, which act trivially on the generalized tangent cohomology.

## 5. Orbit induction automatically gives the right Chern character

Let `S` be any perfect complex with

\[
ch(S)=12nA
\]

for some positive integer `n`. The pure-divisor block from `rm-smooth-isogeny-scaffold.md` supplies such an object: if `D in |nA|` is smooth,

\[
S=i_*V_D,
\qquad
ch(S)=12[D]=12nA.
\]

Then

\[
ch(\Psi S)
=\Phi^H(ch(S))
=-2nC^3.
\]

Consequently

\[
\boxed{
ch(S\oplus\Psi S)
=12nA-2nC^3
=12n\beta.
}
\]

If `D` and the natural bundle `V_D` are chosen `(-1_X)`-symmetric, then

\[
\Psi^2S\simeq S.
\]

In that case `S direct-sum Psi S` carries the expected two-cycle Fourier equivariance by exchanging the two summands. Equivalently, induction around the full four-element `Psi` orbit gives a canonical finite equivariant object with Chern character `24n beta`.

Thus **the Chern character and the finite categorical symmetry are simultaneously solved at the formal orbit level**.

## 6. The real obstruction is gluable-ness

Perry's equivariant deformation theorem applies to gluable objects, i.e. objects satisfying

\[
Ext^{<0}(E,E)=0.
\]

Self-Exts cause no problem:

\[
Ext^{<0}(S,S)=0
\]

for the divisor sheaf, and an autoequivalence preserves these groups, so

\[
Ext^{<0}(\Psi S,\Psi S)=0.
\]

The only issue is the cross terms

\[
Ext^{<0}(S,\Psi S),
\qquad
Ext^{<0}(\Psi S,S).
\]

Hence the Fourier route has a sharp first milestone:

\[
\boxed{
\text{construct a pure-divisor block }S
\text{ for which the two Fourier cross-Ext families vanish in negative degree.}
}
\]

If `S` and `Psi S` lie in one common heart of a bounded t-structure, this vanishing is automatic.

## 7. Why the split bundle `V_D` is not WIT

The direct-sum bundle used in the smooth-divisor scaffold is

\[
V_D=
O_D^{\oplus3}
\oplus\Omega_D^1
\oplus\Omega_D^2
\oplus K_D^{\oplus3}.
\]

Its Chern character is exactly right,

\[
ch(V_D)=12\,td(O_D(D)),
\]

but its Fourier behavior is too split.

Let

\[
N=h^0(X,O_X(D)).
\]

For a general nontrivial `P in Pic^0(X)`, Kodaira/Serre duality and the conormal sequence give

\[
H^i(D,O_D\otimes P)=0
\quad(i\neq3),
\qquad
h^3(D,O_D\otimes P)=N,
\]

and

\[
H^i(D,K_D\otimes P)=0
\quad(i\neq0),
\qquad
h^0(D,K_D\otimes P)=N.
\]

For the cotangent terms, the same conormal calculation gives generically

\[
H^i(D,\Omega_D^1\otimes P)=0
\quad(i\neq2),
\qquad
h^2(D,\Omega_D^1\otimes P)=11N,
\]

while Serre duality gives

\[
H^i(D,\Omega_D^2\otimes P)=0
\quad(i\neq1),
\qquad
h^1(D,\Omega_D^2\otimes P)=11N.
\]

Therefore

\[
\boxed{
\bigl(h^0,h^1,h^2,h^3\bigr)
(D,V_D\otimes P)
=(3N,11N,11N,3N)
}
\]

for general `P`.

So the direct-sum `V_D` is not WIT in a single degree. Its Fourier transform has four generic cohomological layers whose alternating ranks cancel.

## 8. This suggests a non-split `V_D` replacement

The symmetric profile

\[
3,11,11,3
\]

has Euler characteristic zero and admits a rank-exact pattern

\[
3\to11\to11\to3.
\]

This suggests replacing the direct sum

\[
3O_D\oplus\Omega_D^1\oplus\Omega_D^2\oplus3K_D
\]

by a genuinely non-split vector bundle `W_D` with the **same Chern character**, obtained by successive extensions among these four blocks, so that the connecting maps in cohomology make

\[
R\Gamma(D,W_D\otimes P)
\]

generically acyclic.

If the resulting Fourier transform is perverse/WIT in the appropriate shifted heart, then

\[
S_D=i_*W_D
\quad\text{and}\quad
\Psi S_D
\]

can plausibly lie in a common heart, solving the negative-Ext obstruction without introducing codimension-three singular support.

This is now a concrete moduli/extension problem rather than a Chern-character problem.

## 9. Exact K-theory identity for the divisor block

For reference, the scaffold divisor sheaf has the exact line-bundle K-class

\[
\boxed{
[i_*V_D]
=3[O_X(D)]+10[O_X]-18[O_X(-D)]
+6[O_X(-2D)]-[O_X(-3D)].
}
\]

The first four moments beyond the linear one cancel:

\[
\sum c_k=0,
\quad
\sum kc_k=12,
\quad
\sum k^jc_k=0
\quad(j=2,3,4).
\]

This identity can be used to compute the Fourier transform termwise and to search for non-split resolutions with the same K-class.

## 10. Perry's theorem: the remaining categorical caveat

The clean abelian equivariant theorem in Perry's 2026 paper treats finite groups in the identity component, acting by translations and degree-zero tensorizations. A Fourier transform is outside that special case.

Perry's general equivariant semiregularity theorem does allow a finite group acting on a smooth proper category, but additionally requires the invariant category to be smooth/proper **of geometric origin** and requires the equivariant K-class to extend in the invariant-category local system.

Perry explicitly notes that geometric origin of an invariant category can be subtle for a general finite action. The paper proves it for many actions coming from automorphisms/tensorizations after gerbe constructions, not automatically for a Fourier-generated action.

Therefore the `q=1` Fourier route has two independent remaining hurdles:

1. construct a gluable `Psi`-equivariant object of class a multiple of `beta`;
2. geometrize the finite Fourier action strongly enough to invoke the general equivariant semiregularity theorem.

Neither is solved here.

## 11. Why this route remains valuable

The elementary-transform no-go showed that an ordinary curve modification cannot annihilate both mixed directions locally on a simple RM fourfold.

The Fourier route avoids that obstruction for a structural reason: it does not ask the two mixed directions to vanish locally. Instead, for `q=1`, they lie in the Fourier-odd representation while the secant class lies in the Fourier-even representation.

This is the first surviving mechanism in the current program that separates the final two generalized directions **before** taking the semiregularity map.

The highest-value next experiment is therefore:

> build a non-split pure-divisor bundle `W_D` with `ch(W_D)=ch(V_D)` whose Fourier transform lies in a compatible shifted heart, and test `Ext^{<0}(i_*W_D, Psi(i_*W_D))` directly.
