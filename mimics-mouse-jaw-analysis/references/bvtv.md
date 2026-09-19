# Furcation-centered BV/TV review

This is a geometry and segmentation-review procedure, not a distributed segmentation implementation. Adopt an endpoint definition and study-specific parameters before calculation. Accepted CEJ–ABC measurements do not automatically validate a BV/TV region or tissue mask.

## Region geometry

Locate the M2 external root-trunk separation/furcation roof on calibrated grayscale source views. Trace the transition from common root trunk into separate external root bodies using transverse neighbors and both longitudinal directions. Distinguish this roof from the internal pulp floor and interradicular bone crest. Fused roots or competing roof locations require anatomical adjudication.

Persist the reviewed center in physical XYZ and source voxel ZYX, with the localization frame and evidence. Do not substitute a fixed depth below CEJ or another specimen's coordinates. Previously accepted CEJ points can support a provisional localization frame, but a plane fitted to them is not automatically the true occlusal plane.

For a spherical VOI, predefine and record the radius `r` in millimetres. Include native voxels whose physical centers satisfy `norm(voxel_center - accepted_center) <= r`. Inspect three orthogonal sections through the same center, with the complete sphere boundary in view, and verify full source coverage. Do not shrink or shift the region to follow surviving bone. Region dimensions are study choices; this distribution sets no universal radius.

## Tissue definition and segmentation

Maintain separate geometric VOI, whole-tooth exclusion, eligible tissue-volume (TV) and bone-volume (BV) masks. If using a sphere-minus-tooth definition, exclude the complete tooth envelopes, including pulp and canals, for every intersecting tooth. Specify whether any additional buffer or tissue exclusions apply and justify them before comparison. Preserve eligible marrow, periodontal/nonbone and resorption spaces according to that definition; TV must not be formed from surviving bone alone.

Choose preprocessing and thresholds using acquisition-specific evidence and an appropriate validation set. Apply a common validated configuration to compatible comparison groups. Record sensitivity analyses separately. An intensity cutoff used to assist CEJ/ABC review is not automatically a valid volume-segmentation threshold.

Inspect raw images with tooth/TV and bone overlays on matched planes and across the 3D region. Check that bone is contained in eligible TV, excluded teeth and bone are disjoint, all relevant teeth are excluded, and true disconnected bone is retained. Display-only smoothing, hole filling or largest-component cleanup cannot alter quantitative masks without an explicitly justified, reviewed quantitative method.

## Calculation and evidence

For a uniform native voxel grid, use its physical voxel volume `v`:

- `BV = bone_voxel_count * v`
- `TV = eligible_voxel_count * v`
- `BV/TV (%) = 100 * BV / TV`, with `TV > 0`

Record masks, geometry, voxel volume, units, parameters and review decisions. Use an appropriate physical-volume calculation if the geometry is not a uniform grid; simple voxel-count ratios must not silently substitute for it.

Assess center localization repeatability independently of mask/threshold repeatability. Report observed center displacement, region overlap and metric variation when evaluated; geometric construction alone is not proof of reproducible anatomical localization.

BMD/TMD requires density calibration and an explicit tissue definition. Trabecular thickness, spacing and number require a defined compartment and validated algorithms with edge handling. A mixed cortical/trabecular sphere does not automatically support trabecular-only metrics.
