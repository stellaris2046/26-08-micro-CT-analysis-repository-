---
name: mimics-mouse-jaw-analysis
description: Guide human-reviewed mouse maxilla and mandible micro-CT analysis, including calibrated MPR, M2 CEJ-ABC distances and furcation BV/TV region review. Use for mouse-jaw micro-CT workflows; not clinical diagnosis, microscope acquisition or measurement from uncalibrated screenshots.
license: MIT
---

# Mouse-jaw micro-CT analysis

Provide a source-bound, human-supervised workflow using the researcher's own images and calibrated imaging environment. This skill contains guidance and a distance calculator; it does not include image loaders, segmentation models, application-control tools or biological reference cases.

## Establish the analysis contract

Determine the requested endpoint, source series, jaw, tooth, acquisition geometry and permitted local output location. Use the imaging tool already selected by the researcher when it can preserve the required geometry. If the source or image interface is unavailable, provide planning only and name what is missing. Never report an image as inspected from a filename or narrative alone.

Before quantitative work, record a study profile with voxel geometry, plane/landmark conventions, intensity scaling, preprocessing, review requirements and endpoint parameters. Keep all study records outside the public skill distribution. Existing case acceptances remain local; do not transfer their coordinates or thresholds to another case.

## Workflow and completion criteria

1. **Source and calibration.** Read [source-and-coordinates.md](references/source-and-coordinates.md). Verify unique series identity, slice geometry and coverage. Continue only when the requested anatomy and physical-coordinate mapping are usable; otherwise report `HOLD` with the missing evidence.
2. **Anatomical orientation.** Establish M1–M3 whole-tooth identities and the tooth-row/occlusal references on raw grayscale MPR and neighboring views. Review plane selection before downstream measurements. A plausible 3D surface or an orthonormal mathematical basis alone does not verify anatomy.
3. **Endpoint procedure.** For CEJ–ABC, use [cej-abc.md](references/cej-abc.md). For BV/TV, use [bvtv.md](references/bvtv.md). Their geometry, landmark, mask and release decisions are separate.
4. **Review and calculation.** Save the source/coordinate record and diagnostic evidence before requesting review. Treat proposals as `CANDIDATE`, unresolved anatomy as `HOLD`, and only explicitly reviewed stages as `ACCEPTED`. The CEJ–ABC [calculator](scripts/calibrated_cej_abc_distance.py) performs arithmetic under the [input contract](references/measurement-tool.md); its success does not establish anatomical validity.
5. **Delivery.** Return the requested endpoint, units, parameter profile, reviewed source/geometry, measurement formula and unresolved limitations. Keep a diagnostic view with raw-source context separate from a publication display. Do not release measurements whose required geometry, landmarks, masks or side mapping remain unresolved.

## Invariants

- Identify CEJ, external alveolar crest, tooth, periodontal space and furcation anatomy using raw grayscale and continuity through neighboring slices in both directions. Thresholds propose structures; they do not settle ownership.
- Retain the original data and unmodified quantitative masks. Smoothing, hole filling and largest-component cleanup used for display cannot silently replace quantitative segmentation.
- Use physical units and explicitly record array order, orientation, origin, axis vectors, resampling and display transformations. Do not measure from resized layouts, screenshots or teaching annotations.
- Apply one documented global display mapping across a comparison. Display contrast is separate from segmentation and measurement.
- Keep acquisition resolutions and intensity scales comparable within an endpoint; validate any harmonization. Never infer an experimental group from filenames or scanner screen position.
- No grayscale thresholds, sphere size, segmentation buffer or repeatability tolerance are supplied as validated defaults. Record the study's choices and supporting evidence.
- Use authorized local tools only. This skill grants no permission to publish data, install software, start services or change a study protocol beyond the request. When another domain workflow already owns the analysis, use these endpoint requirements there instead of starting a competing pipeline.
