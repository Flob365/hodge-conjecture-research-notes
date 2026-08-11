import pathlib
import sys
import unittest
from fractions import Fraction


ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from verify_rm_universal_integral_class import (  # noqa: E402
    add,
    complete_intersection_twist,
    poly,
    rm_moments,
    verify,
    verify_one_variable_identities,
)


class RMUniversalIntegralClassTests(unittest.TestCase):
    def test_complete_intersection_pair(self) -> None:
        self.assertTrue(verify_one_variable_identities())
        self.assertEqual(
            add(complete_intersection_twist(1), complete_intersection_twist(2)),
            poly(0, 0, 0, 2, 0),
        )

    def test_rm_identity(self) -> None:
        for q in (1, 2, 3, 5, 7, 11, Fraction(5, 2)):
            with self.subTest(q=q):
                self.assertTrue(verify(q))
                x_total, y_total = rm_moments(q)
                self.assertEqual(x_total, poly(0, 12, 0, 0, 0))
                self.assertEqual(y_total, poly(0, 0, 0, -2 * Fraction(q), 0))


if __name__ == "__main__":
    unittest.main()
