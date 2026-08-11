# Cohomological filtering of the final RM middle extension

> **Status.** This note corrects an overly optimistic dimension argument for Milestone B. For the Kodaira--Spencer bundle `E`, the symmetric tensor sector contributes no extension classes at all, while the alternating tensor sector injects into `H^1(T_D)` and therefore has dimension at most ten. Thus a dimension-only bounded-rank argument cannot settle the final determinant. The surviving extension, if any, is necessarily orthogonal/symmetric at a two-torsion twist. It remains to prove that the surviving `H^1` is nonzero for a choice of three Kodaira--Spencer directions satisfying Milestone A.

## 1. Setup

Let `D` be a smooth principal theta divisor in a principally polarized abelian fourfold and write

\[
K=K_D=O_D(D).
\]

Choose three Kodaira--Spencer classes and form

\[
0\to U\otimes O_D\to E\to\Omega_D^1\to0,
\qquad \dim U=3.
\]

The proposed final extension is

\[
0\to E\to W_D\to E^\vee\otimes K\to0.
\]

Its extension space is

\[
Ext^1(E^\vee K,E)
=H^1(E\otimes E\otimes K^{-1})
\]

and decomposes in characteristic zero as

\[
H^1(Sym^2E\,K^{-1})
\oplus
H^1(\Lambda^2E\,K^{-1}).
\]

## 2. Elementary anti-ample vanishings

For every `m>=1`, Serre duality gives

\[
H^i(D,K^{-m})^\vee
\cong
H^{3-i}(D,K^{m+1}).
\]

Since `K^{m+1}=K_D tensor K^m` and `K^m` is ample, Kodaira vanishing gives

\[
\boxed{H^i(D,K^{-m})=0\quad(i<3).}
\]

The conormal sequence

\[
0\to K^{-1}\to O_D^{\oplus4}\to\Omega_D^1\to0
\]

twisted by `K^{-1}` gives

\[
0\to K^{-2}\to K^{-1\,\oplus4}
\to\Omega_D^1K^{-1}\to0.
\]

Therefore

\[
\boxed{
H^0(\Omega_D^1K^{-1})
=H^1(\Omega_D^1K^{-1})=0.
}
\]

Similarly, because the quotient of a rank-four trivial bundle by a line has the symmetric-square resolution

\[
0\to K^{-1\,\oplus4}
\to O_D^{\oplus10}
\to Sym^2\Omega_D^1\to0,
\]

after twisting by `K^{-1}` we obtain

\[
0\to K^{-2\,\oplus4}
\to K^{-1\,\oplus10}
\to Sym^2\Omega_D^1K^{-1}\to0.
\]

Hence

\[
\boxed{
H^0(Sym^2\Omega_D^1K^{-1})
=H^1(Sym^2\Omega_D^1K^{-1})=0.
}
\]

No rank assumption on the multiplication maps is needed for these vanishings.

## 3. The symmetric tensor sector vanishes in degree one

The extension `0 -> U O -> E -> Omega^1 -> 0` induces the standard filtration of `Sym^2 E`. After twisting by `K^{-1}`, its associated graded pieces are

\[
Sym^2U\otimes K^{-1},
\qquad
U\otimes\Omega_D^1K^{-1},
\qquad
Sym^2\Omega_D^1K^{-1}.
\]

Every graded piece has zero `H^0` and zero `H^1` by Section 2. Applying the long exact cohomology sequences successively through the filtration gives

\[
\boxed{
H^1(Sym^2E\,K^{-1})=0.
}
\]

Thus the entire tensor-symmetric sector of the final extension space disappears.

In particular, the branch in `rm-middle-extension-bounded-rank-criterion.md` that aimed to produce an alternating/symplectic form from a `Sym^2 E` extension cannot occur for this `E`.

## 4. The alternating tensor sector has dimension at most ten

The standard filtration of `Lambda^2 E`, twisted by `K^{-1}`, has associated graded pieces

\[
\Lambda^2U\otimes K^{-1},
\qquad
U\otimes\Omega_D^1K^{-1},
\qquad
\Lambda^2\Omega_D^1K^{-1}.
\]

Because `dim D=3`,

\[
\Lambda^2\Omega_D^1\otimes K^{-1}
\cong T_D.
\]

Let `F_1` denote the first two filtration steps. Section 2 gives

\[
H^0(F_1)=H^1(F_1)=0.
\]

The final short exact sequence is

\[
0\to F_1
\to \Lambda^2E\,K^{-1}
\to T_D
\to0.
\]

Therefore the long exact sequence begins

\[
0\to
H^1(\Lambda^2E\,K^{-1})
\to H^1(T_D)
\xrightarrow{\delta_E} H^2(F_1).
\]

Hence

\[
\boxed{
H^1(\Lambda^2E\,K^{-1})
\cong\ker(\delta_E)
\subseteq H^1(T_D).
}
\]

For a smooth principal theta divisor,

\[
h^1(T_D)=10,
\]

so

\[
\boxed{
h^1(\Lambda^2E\,K^{-1})\le10.}
\]

The actual dimension depends on the three Kodaira--Spencer classes defining `E`.

## 5. Consequence for the bilinear middle pairing

At a suitable two-torsion twist `P`, Milestone A is designed to leave an eight-dimensional space

\[
V_P=H^1(E^\vee K\otimes P).
\]

An extension class in

\[
H^1(\Lambda^2E\,K^{-1})
\]

induces a **symmetric** bilinear form on `V_P` (the tensor antisymmetry is reversed by the odd cohomological degree).

Since the `Sym^2E` sector is zero, every possible final extension is of this orthogonal type.

Thus Milestone B is no longer

> make a large linear space of matrices and use a dimension theorem.

It is the sharper problem

\[
\boxed{
\text{find a single }\varepsilon\in\ker(\delta_E)
\text{ whose induced symmetric }8\times8\text{ form is nonsingular.}
}
\]

A one-dimensional extension space would already be enough if its generator has nonzero determinant.

## 6. New critical falsification test

Before computing any determinant, one must determine

\[
\ker(\delta_E)
\subset H^1(T_D).
\]

There are only two possibilities relevant to the program:

1. `ker(delta_E)=0` for every triple satisfying Milestone A. Then the final non-split bundle `W_D` does not exist and this entire Kodaira--Spencer divisor-bundle route must be rejected.
2. `ker(delta_E) != 0` for some triple satisfying Milestone A. Then choose a surviving class and compute its induced `8 x 8` symmetric pairing.

This kernel calculation now takes priority over the old bounded-rank thresholds.

## 7. Geometric interpretation to test

The map `delta_E` is induced functorially by the three-dimensional extension class

\[
e\in U\otimes H^1(T_D).
\]

Its leading component is a Yoneda/cup-product operation between a test deformation `xi in H^1(T_D)` and the three chosen Kodaira--Spencer classes. Therefore `ker(delta_E)` should admit a deformation-theoretic interpretation as directions compatible with the three-parameter cotangent extension.

In the RM situation the six ordinary directions split as

\[
Sym^2(U_+^*)\oplus Sym^2(U_-^*).
\]

A particularly important experiment is to choose the three defining classes inside one three-dimensional RM block and test whether the opposite block survives in `ker(delta_E)`. If it does, the RM splitting itself supplies the final extension classes.
