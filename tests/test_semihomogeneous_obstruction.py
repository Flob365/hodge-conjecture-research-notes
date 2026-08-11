import pathlib
import sys
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from verify_semihomogeneous_obstruction import (  # noqa: E402
    central_moments,
    choose_h,
    quadratic_target_exceeds_common_torsion,
    symmetry_divisor,
    verify_even_certificate_box,
    verify_symbolic_identities,
)


class SemihomogeneousObstructionTests(unittest.TestCase):
    def test_central_moments(self) -> None:
        self.assertEqual(central_moments(5), (1, 0, -6, 12, 12))
        self.assertEqual(central_moments(23), (1, 0, -24, 48, 480))

    def test_symbolic_certificate_identities(self) -> None:
        self.assertTrue(verify_symbolic_identities())

    def test_even_certificate_boxes(self) -> None:
        for N in (2, 4, 6, 8, 10, 12):
            with self.subTest(N=N):
                self.assertEqual(choose_h(N) % 2, 1)
                self.assertTrue(verify_even_certificate_box(N, radius=12))

    def test_proved_divisors(self) -> None:
        self.assertEqual(symmetry_divisor(2), 24)
        self.assertEqual(symmetry_divisor(3), 162)
        self.assertEqual(symmetry_divisor(4), 1536)
        self.assertEqual(symmetry_divisor(5), 1250)
        self.assertEqual(symmetry_divisor(6), 1944)
        self.assertEqual(symmetry_divisor(8), 24576)

    def test_common_scalar_torsion_is_too_small(self) -> None:
        for N in range(2, 20):
            with self.subTest(N=N):
                self.assertTrue(quadratic_target_exceeds_common_torsion(N))


if __name__ == "__main__":
    unittest.main()
