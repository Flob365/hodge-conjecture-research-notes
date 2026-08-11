import pathlib
import sys
import unittest
from fractions import Fraction


ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from verify_rm_nested_elementary_transform import (  # noqa: E402
    check_intersections,
    containment_margin,
    sufficient_conditions,
)


class NestedRMTests(unittest.TestCase):
    def test_intersection_identities(self) -> None:
        for rho in (Fraction(2), Fraction(3, 2), Fraction(5, 3)):
            with self.subTest(rho=rho):
                A4, C4, AC3 = check_intersections(rho)
                s = rho * rho + 1 / (rho * rho)
                self.assertEqual(A4, 24)
                self.assertEqual(C4, 24)
                self.assertEqual(AC3, 12 * s)

    def test_sufficient_bound_implies_positive_margin(self) -> None:
        rho = Fraction(2)
        q = 3
        for M in range(1, 50):
            if sufficient_conditions(rho, q, M):
                self.assertGreater(containment_margin(rho, q, M), 0)

    def test_large_M_eventually_works(self) -> None:
        for rho, q in ((Fraction(2), 1), (Fraction(3, 2), 5), (Fraction(5, 3), 11)):
            self.assertTrue(any(sufficient_conditions(rho, q, M) for M in range(1, 200)))


if __name__ == "__main__":
    unittest.main()
