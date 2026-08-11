import pathlib
import sys
import unittest
from fractions import Fraction


ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from verify_virtual_class import evaluate_character, verify, virtual_character  # noqa: E402


class VirtualCharacterTests(unittest.TestCase):
    def test_symbolic_identity(self) -> None:
        self.assertTrue(verify())

    def test_small_odd_values(self) -> None:
        for d in (1, 3, 5, 7, 11, 101):
            with self.subTest(d=d):
                self.assertTrue(verify(d))

    def test_d_five_coefficients(self) -> None:
        computed, target = virtual_character()
        expected = (
            Fraction(1),
            Fraction(1),
            Fraction(-5, 2),
            Fraction(-5, 6),
            Fraction(25, 24),
        )
        self.assertEqual(evaluate_character(computed, 5), expected)
        self.assertEqual(evaluate_character(target, 5), expected)


if __name__ == "__main__":
    unittest.main()
