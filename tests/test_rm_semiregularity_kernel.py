import pathlib
import sys
import unittest
from fractions import Fraction


ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from verify_rm_semiregularity_kernel import (  # noqa: E402
    build_matrix,
    certificate_minor,
    claimed_kernel_vectors,
    expected_minor,
    matvec,
    rank,
    verify,
)


class RMSemiregularityKernelTests(unittest.TestCase):
    def test_generic_rank_and_certificate(self) -> None:
        for A, q in (
            (Fraction(2), Fraction(3)),
            (Fraction(3), Fraction(5)),
            (Fraction(5, 2), Fraction(7)),
        ):
            with self.subTest(A=A, q=q):
                matrix, labels, _ = build_matrix(A, q)
                self.assertEqual(rank(matrix), 20)
                self.assertEqual(certificate_minor(matrix), expected_minor(A, q))
                self.assertTrue(verify(A, q))
                for vector in claimed_kernel_vectors(labels, q):
                    self.assertTrue(all(value == 0 for value in matvec(matrix, vector)))

    def test_scalar_rank_drop(self) -> None:
        matrix, _, _ = build_matrix(Fraction(1), Fraction(3))
        self.assertEqual(rank(matrix), 12)


if __name__ == "__main__":
    unittest.main()
