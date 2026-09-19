# Source and physical coordinates

Bind one local analysis to a unique source series and an explicitly identified jaw. Preserve the original image values and metadata. Record the source identifier, series identity, dimensions, dtype, voxel spacing, orientation, origin and slice-order derivation in the private study record.

For DICOM, inspect `SeriesInstanceUID`, `ImageOrientationPatient`, `ImagePositionPatient`, `PixelSpacing` and relevant intensity-rescaling fields. Sort slices by their physical position along the slice normal; do not infer geometry from filenames or `SliceThickness` alone. Check duplicates, missing slices, inconsistent orientation and nonuniform spacing. A source with unresolved geometry is not ready for quantitative analysis. Raw-format conversion needs an independently verified reader and coordinate mapping; no converter is included here.

Distinguish image-array Z/Y/X, pixel row/column and physical X/Y/Z coordinates. DICOM `PixelSpacing` is row spacing followed by column spacing. A resampled MPR has its own output spacing and axes, which may differ from the input DICOM. Verify anisotropic spacing and transforms before measuring. Preserve the voxel-to-physical affine and the coordinate system's handedness/orientation.

Inspect whole-jaw and tooth-bearing coverage in multiple planes and near all boundaries. A wider display crop cannot repair tissue missing from the acquired volume or export. Return `HOLD` when truncation affects the endpoint.

For every accepted section, retain the physical plane origin, orthonormal in-plane axes and normal, output spacing/shape, interpolation method, crop, flip/rotation and neighboring-plane offsets. Keep landmark coordinates in calibrated plane units and source/physical coordinates, with a check that the transformations agree. A PNG or distance-only CSV does not retain this chain.

Use anatomical evidence to map native/display sides to buccal, palatal or lingual sides. Scanner axes, screen-left/right and a display flip are not sufficient. Unresolved side identity prevents a side-specific biological claim.

Save the protocol/profile version, source and array identifiers, reviewer decision and reason for any correction alongside the private numerical records. Preserve accepted versions when rerunning. Keep these records local; pseudonymous specimen IDs and image metadata can still reveal study information.
