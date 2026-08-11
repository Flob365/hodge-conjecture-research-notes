# The five-dimensional quartic correction to ambient deformation products

> **Status.** This note isolates the exact place where intrinsic products of polarized deformations of a smooth principal theta divisor differ from their ambient products. The ambient product detects a universal `20`-dimensional Schur component. The remaining geometry is a canonical map from `Sym^4 W` to a five-dimensional bicanonical quotient. This makes the corrected common-factor ansatz a finite `4 -> 5` rank problem. The identification of this quartic correction map with an explicit theta-Hessian/Gaussian map remains open.

## 1. Setup

Let `(X,Theta)` be a principally polarized abelian fourfold and let

\[
D=Theta\subset X
\]

be smooth. Put

\[
K=K_D=O_D(Theta),
\qquad
V=H^0(X,T_X),
\qquad \dim V=4.
\]

The tangent-normal sequence is

\[
0\to T_D\to V\otimes O_D\xrightarrow{s}K\to0,
\]

where `s` is the four-dimensional canonical gradient system.

The principal polarization identifies the ten-dimensional polarized deformation space with

\[
\boxed{
H^1(T_D)\cong Sym^2 W
}
\]

for a four-dimensional vector space `W` (after the standard identification of the tangent and Hodge factors supplied by the polarization).

## 2. The exterior-square Koszul resolution

Because the normal quotient has rank one, taking the exterior square of the tangent-normal sequence gives the exact length-three complex

\[
\boxed{
0\to\Lambda^2T_D
\to\Lambda^2V\otimes O_D
\to V\otimes K
\to K^2
\to0.
}
\]

Equivalently,

\[
\Lambda^2T_D\cong\Omega_D^1\otimes K^{-1}.
\]

The conormal sequence twisted by `K^{-1}` is

\[
0\to K^{-2}
\to K^{-1\,\oplus4}
\to\Lambda^2T_D
\to0.
\]

Kodaira vanishing plus Serre duality shows

\[
H^0(\Lambda^2T_D)=H^1(\Lambda^2T_D)=0.
\]

The remaining groups are controlled by the degree-three multiplication map of the four gradient sections.

## 3. Cohomology dimensions

For a smooth principal theta divisor,

\[
(h^0,h^1,h^2,h^3)(O_D)=(1,4,6,4)
\]

and by Serre duality

\[
(h^0,h^1,h^2,h^3)(K)=(4,6,4,1).
\]

Moreover

\[
h^0(K^2)=15,
\qquad
H^{>0}(K^2)=0.
\]

The multiplication map

\[
H^0(K)\otimes H^0(K)
\to H^0(K^2)
\]

has image `Sym^2 H^0(K)` of dimension ten. Injectivity of

\[
Sym^2H^0(K)\to H^0(K^2)
\]

follows because the canonical system is the Gauss map and its image is dense in `P^3`; a quadratic polynomial vanishing after pullback therefore vanishes identically.

Define the five-dimensional quotient

\[
\boxed{
Q_D=
H^0(K^2)/Sym^2H^0(K),
\qquad \dim Q_D=5.
}
\]

Let

\[
B=T_D\otimes K\cong\Omega_D^2.
\]

From

\[
0\to B\to V\otimes K\to K^2\to0
\]

one gets

\[
0\to Q_D
\to H^1(B)
\to V\otimes H^1(K)
\to0,
\]

so

\[
h^1(B)=5+24=29.
\]

The cohomology map induced by

\[
\Lambda^2V\otimes O_D\to B
\]

identifies the `24`-dimensional group

\[
H^1(\Lambda^2V\otimes O_D)
\]

with the `24`-dimensional quotient

\[
V\otimes H^1(K).
\]

This is the degree-one linear-algebra map in the Koszul complex of the four canonical gradient sections; under the standard Hodge identifications it is the canonical `4`-dimensional Koszul isomorphism.

Consequently the long exact sequence of

\[
0\to\Lambda^2T_D
\to\Lambda^2V\otimes O_D
\to B\to0
\]

contains a canonical injection

\[
\boxed{
Q_D\hookrightarrow H^2(\Lambda^2T_D)
}
\]

whose image is exactly the kernel of the ambient map

\[
H^2(\Lambda^2T_D)
\to H^2(\Lambda^2V\otimes O_D).
\]

The next Koszul map

\[
H^2(\Lambda^2V\otimes O_D)
\to H^2(B)
\]

is surjective with a `20`-dimensional kernel. Hence

\[
\boxed{
h^2(\Lambda^2T_D)=5+20=25.}
\]

Thus the intrinsic degree-two polyvector cohomology has a canonical five-dimensional nonambient piece.

## 4. Ambient products of polarized deformations

Under

\[
H^1(T_D)\cong Sym^2W,
\]

the cup-wedge product is symmetric: swapping two degree-one classes gives one minus sign from the Dolbeault degree and another from the wedge of tangent vectors.

The ambient product is therefore a map

\[
Sym^2(Sym^2W)
\longrightarrow
H^2(\Lambda^2V\otimes O_D).
\]

The standard Schur decomposition is

\[
\boxed{
Sym^2(Sym^2W)
\cong
Sym^4W\oplus S_{(2,2)}W,
}
\]

with dimensions

\[
35+20=55.
\]

The ambient double-antisymmetrization kills `Sym^4 W` and identifies the `S_(2,2) W` summand with the `20`-dimensional kernel of

\[
H^2(\Lambda^2V\otimes O_D)
\to H^2(B).
\]

Hence the universal/ambient part of the intrinsic product is completely understood.

## 5. Definition of the quartic correction map

Let

\[
\omega_D:
Sym^2H^1(T_D)
\to H^2(\Lambda^2T_D)
\]

be the intrinsic cup-wedge product.

On the `Sym^4W` summand, the ambient product is zero. Therefore `omega_D` lands in the five-dimensional kernel `Q_D` from Section 3.

This defines the canonical geometry-dependent map

\[
\boxed{
\tau_D:
Sym^4W
\longrightarrow
Q_D.
}

All of the difference between intrinsic and ambient products on the common-factor sector is encoded in `tau_D`.

The `S_(2,2)` component is universal and detected ambiently; `tau_D` is the only new theta-divisor geometry needed for products that vanish ambiently.

## 6. The corrected common-factor test

Fix `0 != v in W` and let

\[
L_v=vW\subset Sym^2W,
\qquad \dim L_v=4,
\]

and

\[
\xi=v^2.
\]

For `e=v\odot w in L_v`, the product of the two symmetric tensors belongs to the `Sym^4 W` component and is, up to the standard scalar normalization,

\[
v^3w.
\]

Thus

\[
\boxed{
\xi\wedge e
=\tau_D(v^3w)
\in Q_D.
}
\]

Define

\[
\boxed{
\tau_{D,v}:W\to Q_D,
\qquad
w\mapsto\tau_D(v^3w).
}
\]

To choose three independent classes

\[
e_1,e_2,e_3\in L_v
\]

with

\[
e_a\wedge\xi=0
\]

for all `a`, it is necessary and sufficient that

\[
\boxed{\dim\ker(\tau_{D,v})\ge3}
\]

or equivalently

\[
\boxed{rank(\tau_{D,v})\le1.}
\]

This is the rigorous replacement for the false ambient argument that every common-factor product vanishes intrinsically.

## 7. A five-dimensional linear system of quartics

Dualizing `tau_D` gives

\[
\boxed{
\tau_D^*:Q_D^*\to Sym^4W^*.
}
\]

Thus the theta divisor determines a five-dimensional linear system of quartic forms on `P(W)`.

For `q in Q_D^*`, let `F_q` be the associated quartic. Then

\[
dF_q|_v(w)
=4\,F_q(v,v,v,w),
\]

so the dual of `tau_{D,v}` is, up to the scalar `4`, the simultaneous differential at `v` of this five-dimensional quartic system.

Consequently the common-factor survival condition

\[
rank(\tau_{D,v})\le1
\]

is a concrete ramification condition for a quartic map

\[
P(W)\dashrightarrow P(Q_D).
\]

This turns the extension-survival question into explicit projective geometry.

## 8. Relation to Hessians and Gaussian maps

The target

\[
Q_D=H^0(K^2)/Sym^2H^0(K)
\]

is exactly the non-canonical-product part of the bicanonical system. Secondary products arising from the tangent-normal sequence are the natural habitat of Gaussian/co-Gaussian maps.

Pareschi's Gaussian-map approach to generic vanishing gives a general framework in which normal extension classes are tested by differentiation maps, while de Jong identifies the theta gradient/Hessian combination controlling the ramification of the Gauss map.

This strongly suggests that `tau_D` admits a direct expression in theta Hessians or a higher Gaussian map. That identification is **not** proved here.

The next falsifiable calculation is therefore:

1. compute `tau_D` in theta coordinates;
2. evaluate the rank of `tau_{D,v}`;
3. if `rank(tau_{D,v})>=2` for every `v`, reject the common-factor survival architecture;
4. if some `v` has rank at most one, combine its three-dimensional kernel with the twisted map `rho_P` and test Milestone A on that kernel.

## References

- G. Pareschi, *Gaussian maps and generic vanishing I: subvarieties of abelian varieties*, arXiv:1401.7442.
- R. de Jong, *Theta functions on the theta divisor*, arXiv:math/0611810.
