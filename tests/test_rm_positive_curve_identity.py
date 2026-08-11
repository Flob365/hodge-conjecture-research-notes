import pathlib
import sys
import unittest
from fractions import Fraction


ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from verify_rm_positive_curve_identity import coefficients, verify  # noqa: E402


class RMPositiveCurveIdentityTests(unittest.TestCase):
    def test_positive_identity(self) -> None:
        for rho in (
            Fraction(2),
            Fraction(3, 2),
            Fraction(5, 3),
            Fraction(7, 4),
        ):
            with self.subTest(rho=rho):
                self.assertTrue(verify(rho))
                T, delta, r, s = coefficients(rho)
                self.assertGreater(T, 2)
                self.assertGreater(delta, 0)
                self.assertGreater(r, 0)
                self.assertGreater(s, 0)

    def test_scalar_case_rejected(self) -> None:
        self.assertFalse(verify(Fraction(1)))


if __name__ == "__main__":
    unittest.main()
