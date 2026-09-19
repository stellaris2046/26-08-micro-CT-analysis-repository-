#!/usr/bin/env python3
"""Compute CEJ-ABC distances projected onto a calibrated MPR axis."""

from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path


def _pair(value, name):
    if not isinstance(value, list) or len(value) != 2:
        raise ValueError(f"{name} must be a two-number JSON list")
    pair = tuple(float(v) for v in value)
    if not all(math.isfinite(v) for v in pair):
        raise ValueError(f"{name} contains a non-finite value")
    return pair


def calculate(payload):
    sx, sy = _pair(payload["pixel_spacing_mm"], "pixel_spacing_mm")
    if sx <= 0 or sy <= 0:
        raise ValueError("pixel spacing must be positive")
    ux, uy = _pair(payload.get("axis_unit_xy", [0.0, 1.0]), "axis_unit_xy")
    norm = math.hypot(ux, uy)
    if norm == 0:
        raise ValueError("axis_unit_xy must be non-zero")
    ux, uy = ux / norm, uy / norm
    rows = []
    for item in payload.get("measurements", []):
        cx, cy = _pair(item["cej_xy"], "cej_xy")
        ax, ay = _pair(item["abc_xy"], "abc_xy")
        dx_mm, dy_mm = (ax - cx) * sx, (ay - cy) * sy
        projected = abs(dx_mm * ux + dy_mm * uy)
        rows.append(
            {
                "id": str(item["id"]),
                "cej_x_px": cx,
                "cej_y_px": cy,
                "abc_x_px": ax,
                "abc_y_px": ay,
                "distance_mm": projected,
            }
        )
    if not rows:
        raise ValueError("measurements must contain at least one item")
    return {
        "pixel_spacing_mm": [sx, sy],
        "axis_unit_xy": [ux, uy],
        "measurements": rows,
    }


def self_test():
    result = calculate(
        {
            "pixel_spacing_mm": [0.01, 0.02],
            "axis_unit_xy": [0, 1],
            "measurements": [
                {"id": "vertical", "cej_xy": [5, 10], "abc_xy": [99, 13]}
            ],
        }
    )
    assert math.isclose(result["measurements"][0]["distance_mm"], 0.06)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_json", nargs="?")
    parser.add_argument("--output-json")
    parser.add_argument("--output-csv")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        print("SELF_TEST=PASS")
        return
    if not args.input_json or not args.output_json or not args.output_csv:
        parser.error("input_json, --output-json, and --output-csv are required")
    payload = json.loads(Path(args.input_json).read_text(encoding="utf-8"))
    result = calculate(payload)
    Path(args.output_json).write_text(
        json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    with Path(args.output_csv).open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(result["measurements"][0]))
        writer.writeheader()
        writer.writerows(result["measurements"])


if __name__ == "__main__":
    main()
