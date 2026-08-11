# Scalar semihomogeneous monads: an arithmetic obstruction

> **Status.** This note gives a rigorous obstruction to one natural way of repairing the symmetry defect of the `W_2` construction. It does not rule out semihomogeneous methods with non-scalar endomorphisms, non-termwise group actions, or more general Fourier--Mukai constructions.

## 1. Why perfect semihomogeneous monads are worth testing

Perry's equivariant semiregularity theorem applies directly to equivariant perfect complexes on families of abelian varieties. Thus one does not need to force a speculative secant class into a single coherent sheaf before testing semiregularity.

This makes the following ansatz natural. On a principally polarized abelian fourfold `(X,Theta)`, try to realize the corrected secant class by a bounded complex whose terms are sums of simple semihomogeneous bundles of rational slope with respect to `Theta`.

For a simple semihomogeneous bundle of slope

\[
\lambda=\frac ab,
\qquad \gcd(a,b)=1,\quad b>0,
\]

Mukai's formulas, recalled by Alvarado--Pareschi, give on a principally polarized fourfold

\[
\operatorname{rk}E_{a/b}=b^4,
\qquad
\Phi(E_{a/b})=\operatorname{Im}(b_X,a\varphi_\Theta)
\subset X\times\widehat X.
\]

Moreover

\[
[b]^*E_{a/b}\cong
\mathcal O_X(ab\Theta)^{\oplus b^4}.
\]

Comparing Chern characters under `[b]^*` gives

\[
\boxed{
\operatorname{ch}(E_{a/b})
=b^4\exp\left(\frac ab\Theta\right).
}
\]

Primary reference: N. Alvarado and G. Pareschi, *Semihomogeneous vector bundles, Q-twisted sheaves, duality, and linear systems on abelian varieties*, arXiv:2407.20646v2, especially (1.9), (1.10), and Proposition 2.1.1.

Perry reference: A. Perry, *The semiregularity theorem for equivariant noncommutative varieties*, arXiv:2604.00511.

## 2. The secant class becomes an integral binary-quartic problem

Write `x=Theta`. The target character is

\[
1+x-\frac d2x^2-\frac d6x^3+\frac{d^2}{24}x^4.
\]

Multiply the coefficient of `x^j` by `j!`. Its moment vector is

\[
M_d=(1,1,-d,-d,d^2).
\]

A semihomogeneous term of slope `a/b` has moment vector

\[
v(a,b)=
(b^4,ab^3,a^2b^2,a^3b,a^4).
\]

Hence a signed integral K-theory decomposition

\[
[E_d]=\sum_i c_i[E_{a_i/b_i}],
\qquad c_i\in\mathbf Z,
\]

has the desired Chern character if and only if

\[
\sum_i c_i v(a_i,b_i)=M_d.
\]

Equivalently, define the binary quartic

\[
\boxed{
P_d(s,t)=
 s^4+4s^3t-6d s^2t^2-4d st^3+d^2t^4.
}
\]

Then the K-class condition is exactly

\[
\boxed{
P_d(s,t)=\sum_i c_i(b_i s+a_i t)^4.
}
\]

Thus the scalar semihomogeneous construction problem is an **integral Waring problem for one explicit binary quartic**.

## 3. Common stabilizers of scalar slopes

The stabilizer of the slope `a/b` is the embedded copy

\[
\Gamma_{a,b}=\operatorname{Im}(b_X,a\varphi_\Theta).
\]

For primitive pairs `(a_i,b_i)`, the common finite intersection of several distinct scalar graphs is another full torsion group. More precisely, after choosing one pair `(a_0,b_0)`, set

\[
N=\gcd_i|a_i b_0-b_i a_0|.
\]

The common finite intersection is isomorphic to `X[N]`, hence has order

\[
|X[N]|=N^8
\]

because `dim X=4`.

Modulo `N`, all vectors `(b_i,a_i)` are projectively proportional. The first two target moments are both `1`. Reducing the two moment identities modulo `N` therefore forces the common projective slope to be `1`. Consequently

\[
a_i\equiv b_i\pmod N
\]

for every term after the harmless projective normalization. Equivalently, the common torsion subgroup is the diagonal graph

\[
\{(z,\varphi_\Theta(z)):z\in X[N]\}.
\]

So write

\[
a_i=b_i+Nk_i.
\]

Since `gcd(a_i,b_i)=1`, we also have `gcd(b_i,N)=1`.

## 4. Universal central-moment congruences

Put

\[
q=d+1.
\]

Changing variables from `(s,t)` to `(u-v,v)` in the quartic identity, or simply taking central moments around slope `1`, gives

\[
N\sum_i c_i k_i b_i^3=0,
\]

\[
N^2\sum_i c_i k_i^2b_i^2=-q,
\]

\[
N^3\sum_i c_i k_i^3b_i=2q,
\]

and

\[
N^4\sum_i c_i k_i^4=q(q-4).
\]

Therefore

\[
N^2\mid q,
\qquad
N^3\mid2q,
\qquad
N^4\mid q(q-4).
\]

There is a stronger cubic divisibility. For all integers `b,k`,

\[
kb^3-k^3b=kb(b-k)(b+k)
\]

is divisible by `6`. Since the first central moment vanishes,

\[
\sum_i c_i k_i^3b_i\equiv0\pmod6.
\]

Hence

\[
\boxed{3N^3\mid q.}
\]

This already severely constrains any common torsion symmetry.

## 5. Odd levels are impossible for the quadratic symmetry target

Assume `N` is odd. Since `N|q`,

\[
\gcd(N,q-4)=1.
\]

The divisibility `N^4|q(q-4)` therefore forces

\[
N^4\mid q.
\]

The parameter `d` is odd, so `q=d+1` is even. Thus

\[
\boxed{2N^4\mid d+1}
\]

for every odd `N`.

In particular

\[
d(d+1)=q(q-1)>N^8=|X[N]|.
\]

So **no odd scalar torsion level can supply a common symmetry group as large as the numerical target `d(d+1)`**.

## 6. Even levels: a quartic congruence certificate

Now assume `N` is even. Choose an odd integer `h` coprime to `N` as follows:

- if `3` does not divide `N`, require `h congruent -N (mod 3)`;
- if `3` divides `N`, require `3` not to divide `h`.

Define

\[
R_{N,h}(a,b)=
(a-b)((N-1)a+b)((N+1)a-b)
(ha+(2N-h)b).
\]

If `a=b+Nk`, then

\[
R_{N,h}(a,b)=N^4 k
(b+(N-1)k)(b+(N+1)k)(2b+hk).
\]

Because `N` is even and `gcd(b,N)=1`, `b` is odd. The product after `N^4` is always divisible by `24`:

- divisibility by `8`: if `k` is odd, the two middle factors are even and one is divisible by `4`; if `k` is even, the factor `k` together with `2b+hk` contributes at least three powers of `2`;
- divisibility by `3`: if `3|k` it is immediate. Otherwise reduce by `k` modulo `3`. If `3` does not divide `N`, the roots furnished by the last three linear factors cover all residues by the choice of `h`. If `3|N`, `b` cannot be divisible by `3` and the two middle factors already cover the two allowed nonzero residues.

Therefore

\[
\boxed{24N^4\mid R_{N,h}(a,b)}
\]

for every primitive slope containing the common level-`N` diagonal torsion.

Expanding `R_{N,h}` as a linear functional of the five quartic moments and applying it to `M_d` gives

\[
\sum_i c_i R_{N,h}(a_i,b_i)
=(d+1)\bigl(h(N^2-1)d-4N+3h\bigr).
\]

Consequently

\[
\boxed{
24N^4\mid
(d+1)\bigl(h(N^2-1)d-4N+3h\bigr).
}
\]

Together with `3N^3|d+1`, this determines enough prime-power divisibility to obtain:

\[
\boxed{
\begin{array}{ll}
\dfrac32N^4\mid d+1,& N\equiv2\pmod4,\\[4pt]
6N^4\mid d+1,& 4\mid N.
\end{array}}
\]

Here is the short valuation argument. Write `N=2^r m`, with `m` odd. For every odd prime `p|N`, the second factor in the boxed congruence is nonzero modulo `p` because `gcd(h,N)=1`; hence the full odd part `m^4`, together with the extra factor `3` coming from `24`, must occur in `d+1`. If `r=1`, `3N^3|d+1` already supplies exactly the needed `2^3`, giving `(3/2)N^4`. If `r>=2`, the second factor has exactly `2`-adic valuation `2`, while `24N^4` has valuation `4r+3`; hence `d+1` has valuation at least `4r+1`, giving `6N^4`.

Therefore for **every even `N>=2`**,

\[
d+1\ge\frac32N^4.
\]

It follows again that

\[
\boxed{d(d+1)>N^8=|X[N]|.}
\]

## 7. The scalar-semihomogeneous no-go theorem

Combining the odd and even cases gives:

### Proposition

Let `d>0` be odd. Suppose the corrected rank-one secant K-class on a principally polarized abelian fourfold is represented as a signed integral sum of simple semihomogeneous bundles of scalar rational slopes `a_i/b_i`. Suppose further that a finite translation--tensorization group acts termwise through the common intersection of the Mukai stabilizer graphs of all distinct slope blocks.

If that common finite intersection is `G`, then

\[
\boxed{|G|<d(d+1).}
\]

Thus the convenient quadratic symmetry target from `research-program.md` can **never** be achieved by a termwise-equivariant monad built only from scalar semihomogeneous slope blocks.

This does not say that the semiregularity map cannot be injective for a smaller group; `|G|=d(d+1)` was a strong numerical design target, not a necessary theorem. It does say that the most obvious way of generating the desired `O(d^2)` symmetry from large scalar semihomogeneous stabilizers is arithmetically self-defeating.

## 8. Concrete small-level checks

The general proof contains the following useful landmarks.

- `N=2`: `24 | d+1`; the first admissible odd value is `d=23`, but `2^8=256 < 23*24=552`.
- `N=3`: the general odd-level bound gives `2*3^4 | d+1`; a sharper quartic certificate gives `486 | d+1`.
- `N=4`: a sharper certificate gives `1536 | d+1`; hence `4^8=65536` is already far below `1535*1536`.
- `N=5`: a sharper certificate gives `3750 | d+1`.
- `N=6`: the even-level certificate gives `(3/2)6^4=1944 | d+1`.
- `N=8`: it gives `6*8^4=24576 | d+1`.

The accompanying standard-library verifier checks the binary-quartic identities, the certificate expansion, and exhaustive residue tests for the divisibility lemma.

## 9. What survives

This obstruction points away from **scalar** slope symmetry and toward the feature already present in Markman's more general construction: **real multiplication**.

For scalar slopes, intersections of stabilizer graphs are kernels of integer multiplication and therefore full groups `X[N]`; the same integer `N` then enters the quartic congruences above and causes the symmetry/class-size cancellation.

With real multiplication, the analogues of `(a,b)` are endomorphisms rather than integers. Intersections are kernels of non-scalar endomorphisms, whose degrees are governed by field norms. The scalar divisibility argument above no longer applies verbatim. This suggests the next concrete target:

> Replace the scalar binary quartic by an `O_F`-valued quartic for a real quadratic field `F`, and search for a signed semihomogeneous decomposition whose common stabilizer kernel has sufficiently large norm while the rational trace of the Chern character remains the corrected secant class.

This direction is also aligned with Markman's genus-4 real-multiplication examples, where secant sheaves are constructed but semiregularity is still left open.

Reference: E. Markman, *Secant sheaves on abelian n-folds with real multiplication and Weil classes on abelian 2n-folds with complex multiplication*, arXiv:2509.23079 (version dated March 22, 2026).