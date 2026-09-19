"""Tests use invented coordinates, never specimen-derived data."""

import importlib.util
import json
import math
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "mimics-mouse-jaw-analysis/scripts/calibrated_cej_abc_distance.py"
spec = importlib.util.spec_from_file_location("distance", SCRIPT)
distance = importlib.util.module_from_spec(spec)
spec.loader.exec_module(distance)


class DistanceTests(unittest.TestCase):
    def payload(self):
        return {
            "pixel_spacing_mm": [0.01, 0.02],
            "axis_unit_xy": [0, 1],
            "measurements": [{"id": "synthetic", "cej_xy": [0, 0], "abc_xy": [3, 4]}],
        }

    def test_anisotropic_vertical_projection_not_diagonal(self):
        result = distance.calculate(self.payload())
        self.assertAlmostEqual(result["measurements"][0]["distance_mm"], 0.08)
        self.assertNotAlmostEqual(result["measurements"][0]["distance_mm"], math.hypot(0.03, 0.08))

    def test_oblique_physical_axis_is_normalized(self):
        payload = self.payload()
        payload["axis_unit_xy"] = [3, 4]
        self.assertAlmostEqual(distance.calculate(payload)["measurements"][0]["distance_mm"], 0.082)

    def test_reversed_axis_has_same_unsigned_distance(self):
        payload = self.payload()
        payload["axis_unit_xy"] = [0, -2]
        self.assertAlmostEqual(distance.calculate(payload)["measurements"][0]["distance_mm"], 0.08)

    def test_invalid_calibration_rejected(self):
        for spacing in ([0, 1], [-1, 1], [float("nan"), 1], [1, float("inf")]):
            with self.subTest(spacing=spacing), self.assertRaises(ValueError):
                payload = self.payload()
                payload["pixel_spacing_mm"] = spacing
                distance.calculate(payload)

    def test_zero_axis_and_missing_measurements_rejected(self):
        payload = self.payload()
        payload["axis_unit_xy"] = [0, 0]
        with self.assertRaises(ValueError):
            distance.calculate(payload)
        payload = self.payload()
        payload["measurements"] = []
        with self.assertRaises(ValueError):
            distance.calculate(payload)

    def test_nonfinite_landmark_rejected(self):
        payload = self.payload()
        payload["measurements"][0]["abc_xy"] = [0, float("nan")]
        with self.assertRaises(ValueError):
            distance.calculate(payload)

    def test_synthetic_example_cli(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            subprocess.run([sys.executable, str(SCRIPT), str(ROOT / "examples/synthetic-landmarks.json"),
                            "--output-json", str(output / "result.json"),
                            "--output-csv", str(output / "result.csv")], check=True)
            rows = json.loads((output / "result.json").read_text())["measurements"]
            self.assertAlmostEqual(rows[0]["distance_mm"], 0.06)
            self.assertAlmostEqual(rows[1]["distance_mm"], 0.04)
            self.assertEqual(len((output / "result.csv").read_text(encoding="utf-8-sig").splitlines()), 3)


if __name__ == "__main__":
    unittest.main()
