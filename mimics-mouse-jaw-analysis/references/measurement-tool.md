# Distance calculator contract

`scripts/calibrated_cej_abc_distance.py` accepts a JSON object containing:

- `pixel_spacing_mm`: `[sx, sy]`, positive millimetres per **column/x**, then **row/y**, of the quantitative MPR raster. Reverse DICOM's row/column `PixelSpacing` order only when that spacing actually describes this raster. For resampled MPR, use its output spacing.
- `axis_unit_xy`: the rootward direction in the **physical plane's x/y basis**. The tool normalizes any nonzero finite vector. The default `[0, 1]` is appropriate only when y is already the reviewed rootward direction. A direction defined in pixel units must first be converted using the raster's spacing.
- `measurements`: nonempty list of items with a local `id`, `cej_xy` and `abc_xy`, each coordinate pair in **column/x, row/y** order on the same unresized raster.

The tool computes `abs(dot([(abc_x-cej_x)*sx, (abc_y-cej_y)*sy], normalized_axis))`. Output distances are in millimetres. It does not locate CEJ or ABC, read DICOM, verify coordinate transforms, establish side identity, or grant measurement-release approval. Keep the full source/physical-coordinate record separately.

Both `--output-json` and `--output-csv` are required for file calculation. Create their parent directory first and select unused filenames; existing output files are overwritten. Use local study storage for real inputs/outputs. The repository's synthetic example is only an arithmetic demonstration.
