# Principal-theta reduction of Milestone A to a Fourier rank problem

> **Status.** This note specializes the Kodaira--Spencer divisor-bundle construction to a smooth principal theta divisor. It reduces Milestone A to the generic rank of one natural `10 -> 11` Fourier-bundle morphism and computes the Chern/Porteous data of that morphism. The generic rank `10` is not yet proved.

## 1. Why the principal case is preferable

Let `(X,Theta)` be a principally polarized abelian fourfold and assume that a symmetric theta divisor

\[
D\in|\Theta|
\]

is smooth. Put

\[
K_D=\mathcal O_D(\Theta).
\]

Here

\[
N=h^0(X,\mathcal O_X(\Theta))=1.
\]

Thus the generic cohomology profile from `rm-kodaira-spencer-divisor-bundle.md`

\[
(3,11,11,3)N
\]

becomes simply

\[
(3,11,11,3).
\]

For a nontrivial `P in Pic^0(X)`, Kodaira vanishing on `X` and the standard restriction sequences give

\[
h^0(D,K_D\otimes P)=1,
\qquad
h^1(D,\Omega_D^2\otimes P)=11,
\]

with the other generic cohomology groups of these two sheaves vanishing in the relevant degrees.

The deformation space of a smooth principal theta divisor has the expected dimension

\[
h^1(D,T_D)=10.
\]

For the present note it is enough to use the natural ten-dimensional ppav deformation subspace; the rank calculation below concerns that subspace.

## 2. Milestone A becomes a twisted `10 -> 11` map

Fix a nontrivial `P` and let

\[
\alpha_P\in H^0(D,K_D\otimes P)
\]

be a nonzero section, unique up to scale.

Contraction with `alpha_P` gives a sheaf map

\[
T_D\longrightarrow \Omega_D^2\otimes P.
\]

On first cohomology this is

\[
\boxed{
\rho_P:
H^1(D,T_D)
\longrightarrow
H^1(D,\Omega_D^2\otimes P),
}
\]

of dimensions

\[
10\longrightarrow11.
\]

If `rank(rho_P)>=3`, choose three deformation classes whose images are independent. The dual connecting map in the Kodaira--Spencer bundle construction is then injective on the three one-dimensional copies of `H^0(K_D tensor P)`, which is exactly Milestone A for `N=1`.

So the former `11N -> 3N` problem has become the much smaller condition

\[
\boxed{\operatorname{rank}(\rho_P)\ge3.}
\]

Generic injectivity of `rho_P` would be much stronger than necessary.

## 3. A geometric description of the kernel

Let

\[
Z_P=(\alpha_P=0)\subset D.
\]

Because `alpha_P` is a section of `K_D tensor P`, the contraction map is simply multiplication by that section under the canonical identification

\[
T_D\otimes K_D\cong\Omega_D^2.
\]

Hence

\[
0\to T_D
\to \Omega_D^2\otimes P
\to (\Omega_D^2\otimes P)|_{Z_P}
\to0.
\]

For nontrivial general `P`, `H^0(D,Omega_D^2 tensor P)=0`, and therefore

\[
\boxed{
\ker(\rho_P)
\cong
H^0\bigl(Z_P,(\Omega_D^2\otimes P)|_{Z_P}\bigr).
}
\]

Equivalently, using the tangent sequence of `D` in `X` and writing

\[
N_P=(K_D\otimes P)|_{Z_P},
\]

the kernel is the kernel of the explicit gradient multiplication map

\[
\boxed{
H^0(Z_P,N_P)^{\oplus4}
\longrightarrow
H^0(Z_P,K_D\otimes N_P).
}
\]

In the principal case the two spaces have dimensions

\[
16\longrightarrow17.
\]

Thus generic injectivity of `rho_P` is equivalent to injectivity of one concrete `16 -> 17` gradient map on the theta--translate intersection surface `Z_P`.

For Milestone A one only needs its kernel to have dimension at most seven.

## 4. Fourier transform of the two sides

Identify `X` with `X^vee` using the principal polarization and write `x=[Theta]`.

The relevant K-class for the canonical bundle of the theta divisor is

\[
[i_*K_D]=[\mathcal O_X(\Theta)]-[\mathcal O_X],
\]

so

\[
\operatorname{ch}(i_*K_D)=e^x-1.
\]

Away from the origin of the dual abelian variety, its Fourier--Mukai transform is a line bundle whose Chern character is

\[
\boxed{e^{-x}.}
\]

Thus on

\[
U=X^vee\setminus\{0\}
\]

the source of the universal Kodaira--Spencer map is

\[
\boxed{
\mathcal S=\mathcal O_U(-\widehat\Theta)^{\oplus10}.
}
\]

For the second term, the conormal sequence gives in `K(D)`

\[
[\Omega_D^2]=6-4[K_D^{-1}]+[K_D^{-2}].
\]

Pushing to `X`,

\[
\operatorname{ch}(i_*\Omega_D^2)
=6-10e^{-x}+5e^{-2x}-e^{-3x}.
\]

For a ppav fourfold the cohomological Fourier transform satisfies

\[
\mathcal F(e^{a x})=a^4e^{-x/a}
\]

for nonzero `a`; terms supported at the origin may be discarded on `U`.

Since `Omega_D^2` is generically WIT in degree one, define

\[
\mathcal G=R^1\Phi(i_*\Omega_D^2)|_U.
\]

Then

\[
\boxed{
\operatorname{ch}(\mathcal G)
=10e^x-80e^{x/2}+81e^{x/3}
\quad\text{on }U.
}
\]

Expanding through codimension two gives

\[
\boxed{
\operatorname{rk}\mathcal G=11,
\qquad
c_1(\mathcal G)=-3x,
\qquad
c_2(\mathcal G)=5x^2.
}
\]

The family of maps `rho_P` therefore packages into a natural bundle morphism

\[
\boxed{
\kappa:
\mathcal O_U(-\widehat\Theta)^{\oplus10}
\longrightarrow
\mathcal G.
}
\]

Milestone A follows if the generic rank of `kappa` is at least three; the strongest expected statement is generic rank ten.

## 5. Porteous consistency test for rank ten

Assume provisionally that `kappa` has generic rank ten. Its virtual rank-one quotient

\[
\mathcal Q=\mathcal G-\mathcal S
\]

has

\[
c_1(\mathcal Q)=7x.
\]

From

\[
c(\mathcal G)=c(\mathcal S)c(\mathcal Q)
\]

one obtains

\[
\boxed{c_2(\mathcal Q)=30x^2.}
\]

For a map of ranks `10 -> 11`, the expected codimension of the locus where the rank drops to at most nine is two. Thom--Porteous therefore predicts

\[
\boxed{
[D_9(\kappa)]=30\,\widehat\Theta^2.
}
\]

This class is positive and nonzero. Thus the Chern data are perfectly consistent with the desired picture:

- generic rank `10`;
- a codimension-two surface where the rank drops by one;
- no numerical requirement that the generic rank be smaller.

The next lower degeneracy locus `rank <=8` has expected codimension six, larger than `dim X^vee=4`, so a sufficiently general morphism of these bundles would have no such locus.

This does not prove that the specific Kodaira--Spencer morphism `kappa` is sufficiently general, but it removes a possible global Chern obstruction and gives an exact geometric prediction to test.

## 6. Relation with infinitesimal Torelli

Bloß proves infinitesimal Torelli for sufficiently positive smooth hypersurfaces in simple abelian varieties by reducing the period map to multiplication maps of sections. In the present principal case the map `rho_P` is a twisted, single-top-form analogue of the same mechanism.

The Fourier formulation above suggests a sharper target than invoking ordinary infinitesimal Torelli:

> prove that the natural Kodaira--Spencer morphism `kappa` has generic rank ten (or merely at least three) on `Pic^0(X) minus {0}`.

Possible attacks are:

1. identify `kappa` analytically through the heat equation for theta functions and compute one nonzero `10 x 10` minor;
2. prove that the corresponding ten-dimensional space of morphisms `O(-Theta-hat) -> G` is generically generating in rank ten;
3. study the predicted Porteous surface of class `30 Theta-hat^2` and show that it is the full rank-nine degeneracy locus.

## 7. Immediate falsifiable target

For one smooth RM ppav fourfold and one nontrivial degree-zero twist `P`, compute the rank of

\[
\rho_P:H^1(T_D)\to H^1(\Omega_D^2\otimes P).
\]

- rank `<3` rejects the present three-Kodaira--Spencer construction;
- rank `>=3` settles Milestone A for that point and hence on an open set;
- rank `10` establishes the strongest expected principal-theta version and predicts the degeneracy class `30 Theta-hat^2` globally.
