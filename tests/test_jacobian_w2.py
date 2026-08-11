import pathlib
import sys
import unittest
from fractions import Fraction


ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from verify_jacobian_w2 import character, verify  # noqa: E402


class JacobianW2Tests(unittest.TestCase):
    def test_small_odd_values(self) -> None:
        for d in (1, 3, 5, 7, 11, 101):
            with self.subTest(d=d):
                self.assertTrue(verify(d))

    def test_d_three_character(self) -> None:
        self.assertEqual(
            character(3),
            (
                Fraction(1),
                Fraction(1),
                Fraction(-3, 2),
                Fraction(-1, 2),
                Fraction(3, 8),
            ),
        )

    def test_d_five_character(self) -> None:
        self.assertEqual(
            character(5),
            (
                Fraction(1),
                Fraction(1),
                Fraction(-5, 2),
                Fraction(-5, 6),
                Fraction(25, 24),
            ),
        )


if __name__ == "__main__":
    unittest.main()
