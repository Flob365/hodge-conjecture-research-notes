from fractions import Fraction
from math import factorial


def exp_series(a, degree=4):
    a = Fraction(a)
    return [a**k / factorial(k) for k in range(degree + 1)]


def add(*polys):
    n = max(len(p) for p in polys)
    out = [Fraction(0) for _ in range(n)]
    for p in polys:
        for i, c in enumerate(p):
            out[i] += c
    return out


def scale(c, p):
    c = Fraction(c)
    return [c * x for x in p]


def ch_G_open():
    # G = R^1 Phi(i_* Omega_D^2) away from the origin.
    # ch(G) = 10 e^x - 80 e^(x/2) + 81 e^(x/3).
    return add(
        scale(10, exp_series(1)),
        scale(-80, exp_series(Fraction(1, 2))),
        scale(81, exp_series(Fraction(1, 3))),
    )


def c1_c2_from_ch(ch):
    rank = ch[0]
    c1 = ch[1]
    # ch_2 = (c1^2 - 2 c2)/2
    c2 = (c1 * c1 - 2 * ch[2]) / 2
    return rank, c1, c2


def virtual_rank_one_quotient():
    g = ch_G_open()
    rank_g, c1_g, c2_g = c1_c2_from_ch(g)

    # S = O(-Theta)^10.
    rank_s = Fraction(10)
    c1_s = Fraction(-10)
    c2_s = Fraction(45)  # binomial(10,2)

    rank_q = rank_g - rank_s
    c1_q = c1_g - c1_s
    # c(G)=c(S)c(Q), hence c2(Q)=c2(G)-c2(S)-c1(S)c1(Q)
    c2_q = c2_g - c2_s - c1_s * c1_q
    return rank_q, c1_q, c2_q


def main():
    ch = ch_G_open()
    print("ch(G) coefficients in 1,x,x^2,x^3,x^4:")
    print(ch)

    rank, c1, c2 = c1_c2_from_ch(ch)
    print("rank(G), c1/x, c2/x^2 =", rank, c1, c2)
    assert (rank, c1, c2) == (11, -3, 5)

    rq, q1, q2 = virtual_rank_one_quotient()
    print("virtual quotient rank, c1/x, c2/x^2 =", rq, q1, q2)
    assert (rq, q1, q2) == (1, 7, 30)

    print("Expected Thom-Porteous class for rank <= 9: 30 * Theta_hat^2")
    print("Expected codimension for rank <= 8: (10-8)(11-8)=6 > 4")


if __name__ == "__main__":
    main()
