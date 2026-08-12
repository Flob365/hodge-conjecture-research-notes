# Milestone B: determinantal forcing in the two-torsion `7+4` decomposition

> **Status.** This note supersedes the older `P^9 in P^65` argument, which assumed rank ten for the first twisted Hodge block at two-torsion. The correct two-torsion geometry has a rigorous `7+4` parity decomposition. Conditional on three much sharper statements -- surjectivity of the first block onto the seven-dimensional parity piece, exclusion of visible rank at most three, and existence of one nonsingular normal form -- projective geometry forces exactly the rank-eight central operator required by Milestone B.

## 1. Two-torsion decomposition

Let `D=Theta` be a smooth principal theta divisor in an abelian fourfold and choose

\[
0\ne P\in Pic^0(X)[2].
\]

By `rm-two-torsion-parity-splitting.md`, inversion gives

\[
H_P:=H^1(D,\Omega_D^2\otimes P)
=H_7\oplus H_4,
\]

with

\[
\dim H_7=7,
\qquad
\dim H_4=4.
\]

The first ppav Hodge block

\[
\rho_P:V\to H_P,
\qquad
V=T_{[X,Theta]}A_4,
\quad \dim V=10,
\]
lands entirely in `H_7`.

Assume the expected generic two-torsion rank statement

\[
\boxed{Im(rho_P)=H_7.}
\]

Then

\[
\boxed{W:=ker(rho_P)\text{ has dimension }3,}
\]

and

\[
\overline V:=V/W\cong H_7
\]
has dimension seven.

## 2. The central operator is block diagonal

At two-torsion, Serre duality identifies the central twisted IVHS block with a symmetric bilinear form

\[
T_Q:H_P\to H_P^*.
\]

The deformation tensor `Q` is invariant under inversion, so `T_Q` preserves inversion eigenspaces. Thus

\[
\boxed{
T_Q=B_Q\oplus D_Q,
}
\]

where

\[
B_Q:H_7\to H_7^*,
\qquad
D_Q:H_4\to H_4^*
\]
are symmetric forms of sizes `7 x 7` and `4 x 4`.

Higgs integrability gives

\[
T_Q\rho_P(R)=T_R\rho_P(Q)
\]
for all `Q,R in V`.

If `w in W`, then `rho_P(w)=0`, hence

\[
T_w(H_7)=0.
\]

Therefore

\[
\boxed{
B_w=0\quad(w\in W).
}
\]

So the visible block factors through the seven-dimensional quotient:

\[
\boxed{
B:\overline V\longrightarrow Sym^2H_7^*.
}
\]

The normal block, on the other hand, can be varied by adding elements of `W` without changing `B_Q`.

## 3. The visible family is a system of polar quadrics of a cubic

Use `rho_P` to identify `overline V` with `H_7`. Integrability becomes

\[
B_q(r)=B_r(q),
\qquad q,r\in H_7.
\]

Together with symmetry of each `B_q`, this means there is a symmetric cubic tensor

\[
\boxed{
C\in Sym^3H_7^*
}
\]
such that

\[
\boxed{
B_q(r,s)=C(q,r,s).
}
\]

Thus the projective six-plane

\[
\mathbf P(B(H_7))\subset\mathbf P(Sym^2H_7^*)=\mathbf P^{27}
\]
is the family of polar quadrics of one cubic hypersurface in `P(H_7)=P^6`.

This is the precise sense in which a rank-four quadrics problem appears in the present construction.

## 4. Projective geometry forces a visible rank-at-most-four form

The symmetric determinantal variety

\[
Sigma_{\le4}^{(7)}
=\{[A]\in P(Sym^2C^7):rank(A)\le4\}
\]
has codimension

\[
\binom{7-4+1}{2}=\binom42=6
\]
in `P^27`, hence dimension

\[
21.
\]

Assume the visible linear map

\[
B:H_7\to Sym^2H_7^*
\]
is injective. Then

\[
L:=P(B(H_7))\cong P^6.
\]

Since

\[
\dim L+\dim Sigma_{\le4}^{(7)}=6+21=27,
\]
the projective dimension theorem gives

\[
\boxed{L\cap Sigma_{\le4}^{(7)}\ne\varnothing.}
\]

Therefore there is a nonzero visible direction `q_0` with

\[
\boxed{rank(B_{q_0})\le4.}
\]

This part is unconditional once `B` is injective.

## 5. Rank at most three is the only visible danger

The next symmetric determinantal locus

\[
Sigma_{\le3}^{(7)}
\]
has codimension

\[
\binom{7-3+1}{2}=\binom52=10
\]
in `P^27`.

A general `P^6` avoids it. Our `P^6` is not arbitrary -- it is the polar system of the geometric cubic `C` -- so avoidance must be proved.

The exact needed statement is:

> **Visible rank-four lemma.** The polar system of the two-torsion twisted-IVHS cubic contains no nonzero quadric of rank at most three.

Combined with Section 4, this forces a direction `q_0` satisfying

\[
\boxed{rank(B_{q_0})=4.}
\]

Hence

\[
\dim ker(B_{q_0})=3.
\]

## 6. The normal `4 x 4` block can be adjusted independently

Lift `q_0` to some `Q_0 in V`. Every other lift has the form

\[
Q_0+w,
\qquad w\in W.
\]

Because `B_w=0`, all these lifts have the same visible block:

\[
B_{Q_0+w}=B_{Q_0}.
\]

Their normal blocks form an affine three-parameter family

\[
D_{Q_0}+D(W)\subset Sym^2H_4^*.
\]

The second required statement is:

> **Normal nondegeneracy lemma.** The determinant polynomial
> \[
> w\longmapsto det(D_{Q_0+w})
> \]
> is not identically zero on the three-dimensional space `W`.

Then choose `w` for which

\[
\boxed{rank(D_{Q_0+w})=4.}
\]

The full central operator has rank

\[
rank(T_{Q_0+w})
=rank(B_{q_0})+rank(D_{Q_0+w})
=4+4=8.
\]

Its kernel is exactly the three-dimensional visible kernel:

\[
\boxed{ker(T_{Q_0+w})=ker(B_{q_0})\subset H_7.}
\]

## 7. Milestone B follows

Assume additionally the two-torsion rank lemma `Im(rho_P)=H_7`. Then every vector in the visible kernel has a unique lift modulo `W` to a ppav deformation direction. Choose independent

\[
Q_1,Q_2,Q_3\in V
\]
with

\[
rho_P(\langle Q_1,Q_2,Q_3\rangle)
=ker(B_{q_0}).
\]

Use these three classes to define the rank-six Kodaira--Spencer bundle

\[
0\to O_D^3\to E\to\Omega_D^1\to0.
\]

The lifted central class `Q_0+w` lies in the surviving extension space precisely because its central operator kills those three first-block images. Its middle map on the `(0,8,8,0)` cohomology is the quotient of `T_{Q_0+w}` by the three-dimensional kernel and cokernel. Since the full rank is eight, that quotient map is an isomorphism.

Therefore the final extension

\[
0\to E\to W_D\to E^\vee K_D\to0
\]
has generically acyclic twisted cohomology, and **Milestone B is solved**.

## 8. The three remaining lemmas

The current Milestone-B program has therefore been reduced to exactly three geometric statements:

1. **Two-torsion rank lemma**
   \[
   rank(rho_P)=7.
   \]

2. **Visible rank-four lemma**
   
   no nonzero polar quadric `B_q` has rank at most three.

3. **Normal nondegeneracy lemma**
   
   the three-dimensional invisible space `W` is not mapped entirely into the determinant hypersurface of singular `4 x 4` symmetric forms.

The first statement is constrained by inversion parity and strongly supported by theta-series calculations. The latter two are also satisfied numerically on an explicit real-multiplication period matrix for `Q(sqrt(5))`.

## 9. Generic cubic dimension check

The visible rank-four lemma is generically reasonable for a cubic in seven variables. For fixed nonzero `q`, contraction

\[
Sym^3H_7^*\to Sym^2H_7^*,
\qquad C\mapsto C(q,-,-),
\]
is surjective. The locus of rank-at-most-three quadrics has codimension ten in `P^27`. Allowing `q in P^6` lowers the expected codimension by six, so cubics admitting some rank-at-most-three polar form a proper subset of expected codimension four in `P(Sym^3H_7^*)`.

Thus a general cubic has a rank-four polar by Section 4 but no rank-at-most-three polar. What remains is to prove that the geometric cubic arising from the RM theta family is not trapped in this special codimension-four locus.

## 10. Numerical RM certificate to turn into a proof

On an explicit period matrix with real multiplication by `Q(sqrt(5))`, theta-series experiments show:

- `rank(rho_P)=7` at a nonzero two-torsion twist;
- `dim W=3`;
- each tested basis vector of `W` gives a central operator of rank exactly four, supported on the normal block;
- the visible `P^6` contains a form of rank exactly four;
- after adding an invisible direction, the normal block can be made invertible without changing the visible rank-four block;
- the resulting full central operator has rank eight and three-dimensional kernel contained in `H_7`.

These computations are evidence, not proof. They identify exactly which modular determinants/minors should be certified algebraically next.