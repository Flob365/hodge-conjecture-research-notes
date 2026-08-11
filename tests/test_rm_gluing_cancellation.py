import pathlib
import sys
import unittest
from fractions import Fraction


ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from verify_rm_gluing_cancellation import (  # noqa: E402
    action_matrix,
    alpha_form,
    gamma_form,
    six_common_vectors,
    stacked_rank,
    two_cancellation_vectors,
    verify,
)
from verify_rm_semiregularity_kernel import add, matvec, rank  # noqa: E402


class RMGluingCancellationTests(unittest.TestCase):
    def test_generic_decomposition(self) -> None:
        for A, d, q in (
            (Fraction(2), Fraction(5), Fraction(3)),
            (Fraction(3), Fraction(11), Fraction(2)),
            (Fraction(5, 2), Fraction(13), Fraction(3)),
        ):
            with self.subTest(A=A, d=d, q=q):
                alpha = alpha_form(A, d)
                gamma = gamma_form(A, d, q)
                total = add(alpha, gamma)
                ma, labels, _ = action_matrix(alpha)
                mg, _, _ = action_matrix(gamma)
                mt, _, _ = action_matrix(total)

                self.assertEqual(rank(ma), 12)
                self.assertEqual(rank(mg), 12)
                self.assertEqual(stacked_rank(ma, mg), 22)
                self.assertEqual(rank(mt), 20)
                self.assertTrue(verify(A, d, q))

                for vector in six_common_vectors(labels):
                    self.assertTrue(all(x == 0 for x in matvec(ma, vector)))
                    self.assertTrue(all(x == 0 for x in matvec(mg, vector)))

                for vector in two_cancellation_vectors(labels, q):
                    self.assertTrue(all(x == 0 for x in matvec(mt, vector)))


if __name__ == "__main__":
    unittest.main()
