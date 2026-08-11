import sympy as sp
from itertools import combinations_with_replacement


N = 4
PAIRS = list(combinations_with_replacement(range(N), 2))


def kernel_matrix(diagonal):
    """Return the linear system for pi_(2,2)(A odot B)=0.

    A is diagonal with entries `diagonal`.  B is a general symmetric 4x4
    matrix.  Vanishing of the S_(2,2) component is equivalent to full
    symmetry of T_{ij,kl}=A_ij B_kl+B_ij A_kl.
    """
    A = sp.zeros(N)
    for i, value in enumerate(diagonal):
        A[i, i] = sp.Rational(value)

    variables = sp.symbols(f"b0:{len(PAIRS)}")
    B = sp.zeros(N)
    for var, (i, j) in zip(variables, PAIRS):
        B[i, j] = B[j, i] = var

    def tensor(i, j, k, l):
        return A[i, j] * B[k, l] + B[i, j] * A[k, l]

    equations = []
    for i in range(N):
        for j in range(N):
            for k in range(N):
                for l in range(N):
                    equations.append(
                        sp.expand(tensor(i, j, k, l) - tensor(i, k, j, l))
                    )

    matrix, _ = sp.linear_eq_to_matrix(equations, variables)
    return matrix, variables


def kernel_dimension(diagonal):
    matrix, variables = kernel_matrix(diagonal)
    return len(variables) - matrix.rank()


def main():
    expected = {
        1: 4,
        2: 2,
        3: 0,
        4: 0,
    }

    for rank in range(1, 5):
        diagonal = [1] * rank + [0] * (N - rank)
        dim = kernel_dimension(diagonal)
        print(f"rank(A)={rank}: dim ker = {dim}")
        assert dim == expected[rank]

    # Check that unequal nonzero eigenvalues in rank 2 do not change the result.
    assert kernel_dimension([1, 2, 0, 0]) == 2
    assert kernel_dimension([1, -1, 0, 0]) == 2

    print("Verified: three independent ambient annihilators force rank(A)=1.")


if __name__ == "__main__":
    main()
