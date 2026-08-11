import pathlib
import sys
import unittest
from fractions import Fraction


ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from verify_rm_universal_b_annihilator import verify  # noqa: E402


class RMUniversalBAnnihilatorTests(unittest.TestCase):
    def test_positive_q_values(self) -> None:
        for q in (1, 2, 3, 5, 7, 11):
            with self.subTest(q=q):
                self.assertTrue(verify(Fraction(q)))

    def test_nonzero_rational_q_values(self) -> None:
        for q in (Fraction(1, 2), Fraction(3, 2), Fraction(5, 3)):
            with self.subTest(q=q):
                self.assertTrue(verify(q))

    def test_zero_rejected(self) -> None:
        self.assertFalse(verify(Fraction(0)))


if __name__ == "__main__":
    unittest.main()
