import pathlib
import sys
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from verify_rm_smooth_isogeny_scaffold import (  # noqa: E402
    verify,
    verify_curve_block,
    verify_divisor_bundle,
    verify_grr_divisor_pushforward,
    verify_isogeny_scaling,
)


class RMSmoothIsogenyScaffoldTests(unittest.TestCase):
    def test_divisor_bundle(self) -> None:
        self.assertTrue(verify_divisor_bundle())
        self.assertTrue(verify_grr_divisor_pushforward())

    def test_curve_block(self) -> None:
        self.assertTrue(verify_curve_block())

    def test_isogeny_scaling(self) -> None:
        for m in (2, 3, 5, 7):
            for q in (1, 3, 5, 11):
                with self.subTest(m=m, q=q):
                    self.assertTrue(verify_isogeny_scaling(m, q))
                    self.assertTrue(verify(m, q))


if __name__ == "__main__":
    unittest.main()
