import pathlib
import sys
import unittest
from fractions import Fraction


ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from verify_rm_infinitesimal_kernel import (  # noqa: E402
    action_matrix,
    certificate_minor,
    explicit_kernel_vectors,
    expected_minor,
    mat_vec,
    matrix_rank,
    verify,
)


class RMInfinitesimalKernelTests(unittest.TestCase):
    def test_nontrivial_rm_rank_twenty(self) -> None:
        for t, q in (
            (Fraction(2), Fraction(3)),
            (Fraction(3, 2), Fraction(5)),
            (Fraction(5, 3), Fraction(1)),
            (Fraction(7, 4), Fraction(11)),
        ):
            with self.subTest(t=t, q=q):
                labels, basis, matrix = action_matrix(t, q)
                self.assertEqual(len(labels), 28)
                self.assertEqual(len(basis), 24)
                self.assertEqual(matrix_rank(matrix), 20)
                self.assertTrue(verify(t, q))

    def test_eight_explicit_kernel_vectors(self) -> None:
        t = Fraction(3, 2)
        q = Fraction(5)
        labels, _, matrix = action_matrix(t, q)
        kernel = explicit_kernel_vectors(labels, q)
        self.assertEqual(len(kernel), 8)
        self.assertEqual(matrix_rank(kernel), 8)
        for vector in kernel:
            self.assertTrue(all(entry == 0 for entry in mat_vec(matrix, vector)))

    def test_certificate_minor(self) -> None:
        for t, q in (
            (Fraction(2), Fraction(3)),
            (Fraction(3, 2), Fraction(5)),
            (Fraction(5, 3), Fraction(1)),
        ):
            with self.subTest(t=t, q=q):
                labels, basis, matrix = action_matrix(t, q)
                self.assertEqual(
                    certificate_minor(labels, basis, matrix),
                    expected_minor(t, q),
                )

    def test_scalar_limit_rank_drop(self) -> None:
        for t in (Fraction(1), Fraction(-1)):
            with self.subTest(t=t):
                labels, _, matrix = action_matrix(t, Fraction(3))
                self.assertEqual(len(labels) - matrix_rank(matrix), 16)
                self.assertEqual(matrix_rank(matrix), 12)
                self.assertTrue(verify(t, Fraction(3)))


if __name__ == "__main__":
    unittest.main()
