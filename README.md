# Mouse-jaw micro-CT analysis skill

[简体中文](README.zh-CN.md) · [MIT license](LICENSE)

A reusable, human-supervised skill for mouse maxilla and mandible micro-CT analysis. It guides calibrated multiplanar reconstruction (MPR), second-molar (M2) localization, cemento-enamel junction to alveolar bone crest (CEJ–ABC) measurements, and review of a furcation-centered bone volume fraction (BV/TV) region.

This distribution contains instructions and a small coordinate-based distance calculator. It is **not an end-to-end segmentation pipeline**. Image loading, reconstruction, segmentation, and anatomical review require your own calibrated imaging tools and dataset. No experimental images, specimen records, manual annotations, credentials, or laboratory results are distributed.

## What is included

- [`mimics-mouse-jaw-analysis/SKILL.md`](mimics-mouse-jaw-analysis/SKILL.md): the skill entry point and review gates.
- [`references/`](mimics-mouse-jaw-analysis/references/): source geometry, CEJ–ABC, BV/TV, and measurement-tool instructions.
- [`calibrated_cej_abc_distance.py`](mimics-mouse-jaw-analysis/scripts/calibrated_cej_abc_distance.py): projected distances from calibrated, already reviewed landmarks; Python standard library only.
- [`examples/synthetic-landmarks.json`](examples/synthetic-landmarks.json): invented coordinates for an executable smoke test, not biological reference data.

## Requirements and installation

Use an agent that can load `SKILL.md`, or read the workflow manually. To install in Codex, copy the `mimics-mouse-jaw-analysis` folder into your user skills directory (normally `~/.codex/skills/`). If a skill with the same name already exists, compare it first and keep only one active version; do not overwrite a study-specific protocol without reviewing the differences.

Python 3.10 or later runs the bundled calculator and tests. Image analysis additionally requires software that preserves physical image geometry, supports calibrated MPR and mask inspection, and can export coordinates and masks. Mimics is one possible environment and requires its own license; it is not included, and no Mimics automation bridge is bundled. An alternative imaging tool is acceptable when it preserves the same coordinate and review requirements.

Example request:

> Use $mimics-mouse-jaw-analysis to plan CEJ–ABC measurements for my mouse mandible DICOM series. Check source calibration and M2 orientation before proposing landmarks. Keep my images and results outside this repository.

The skill does not upload data or install services. If no suitable image interface is available, it provides a protocol and identifies the missing input; it must not claim to have inspected images.

## Try the calculator with synthetic data

From the repository root:

```sh
python mimics-mouse-jaw-analysis/scripts/calibrated_cej_abc_distance.py --self-test
mkdir results
python mimics-mouse-jaw-analysis/scripts/calibrated_cej_abc_distance.py examples/synthetic-landmarks.json --output-json results/distances.json --output-csv results/distances.csv
python -m unittest discover -s tests -v
```

The example returns **0.06 mm** for a vertical projection and **0.04 mm** for the second invented point pair. These values check arithmetic only. Read the [calculator contract](mimics-mouse-jaw-analysis/references/measurement-tool.md) before using real coordinates: spacing is **column/x then row/y**, and the axis is defined in the physical MPR plane. DICOM `PixelSpacing` has the opposite row/column order.

## Before analyzing a study

1. Verify the source series, voxel spacing, orientation, slice positions and full anatomical coverage.
2. Predefine the endpoint, tooth, side, plane selection, measurement axis, and exclusion rules. Record a study-specific parameter profile outside this repository.
3. Review anatomy on original grayscale MPR and neighboring planes. Accept source, plane, landmark and segmentation stages separately.
4. Preserve physical coordinates and review decisions with the local study records. Keep display resizing separate from measurement geometry.
5. Establish repeatability and acquisition-specific segmentation settings before reporting quantitative comparisons.

The CEJ–ABC section fractions in this skill describe one reproducible protocol option, not a universal biological standard. BV/TV region size, tooth exclusion/buffer, preprocessing and intensity thresholds must be specified and validated for the study. No scanner-independent grayscale cutoff, automated anatomical accuracy, or inter-observer agreement is claimed. BMD/TMD and trabecular microarchitecture metrics need separate calibration and validated methods.

## Contributing and data handling

See [CONTRIBUTING.md](CONTRIBUTING.md). Share minimal synthetic reproductions. Keep scans, image metadata, sample mappings, review screenshots, derived measurements, local paths and credentials out of commits, issues and attachments. `.gitignore` reduces accidental tracking; it does not anonymize files or erase Git history. Report accidental exposure through [SECURITY.md](SECURITY.md).

This public distribution replaces a study-specific archive. Its cohort processing scripts, release certificates, case histories and annotated teaching examples are not part of the reusable package. Do not restore an older archive into a public checkout or rely on this repository to restore private experimental evidence.

## License

Original code and documentation in this distribution are released under the [MIT License](LICENSE), copyright 2026 stellaris2046. Use, modification and redistribution, including commercial use, are permitted under its terms. Keep the copyright and license notice in redistributed copies or substantial portions. Third-party applications, datasets and services remain subject to their own licenses. This repository does not grant rights to another party's material.
