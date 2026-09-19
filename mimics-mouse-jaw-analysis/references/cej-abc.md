# M2 CEJ–ABC protocol option

This procedure uses three sections through a reviewed M2 mesiodistal span and an axis-projected distance. The study must explicitly adopt this definition; it is different from a diagonal point-to-point distance or a different surface-based endpoint.

## Plane and section geometry

Establish the M1–M3 row and occlusal references from whole-crown, pulp and root continuity in calibrated orthogonal and neighboring views. Select a sagittal plane with supported tooth identities, sufficient visible anatomy and uncensored source coverage. Record departures from the selected orientation convention; a single-root direction need not equal the whole-row direction.

Review the M1–M2 and M2–M3 interfaces. Assign enamel branches to their actual teeth using source continuity, including merged, fragmented or oblique contacts. A threshold bridge, brighter isolated pixel or convenient midpoint is not by itself an accepted contact. Unresolved interfaces require review before defining the M2 span.

For the three-section option, freeze the reviewed mesial and distal M2 span anchors in the physical analysis frame. Define section anchors at 25%, 50% and 75% of that span and explicitly record the section normals. Sample transverse planes under that convention and orient their crown-to-root axes by calibrated rigid transforms. Do not relocate a section to obtain a more favorable crest or change anisotropic scaling to make a root look upright.

Retain the main plane and neighboring source-spaced sections on both sides; a main ±1/±2 stack is a useful review starting point. Record physical offsets and extend the search when anatomy remains uncertain. A distant context section is not equivalent to the immediate neighbor.

## Landmarks and side ownership

Review both sides of each section. Identify CEJ at the source-supported external enamel-to-dentin/cementum transition of the assigned tooth. Preserve genuine supported branches and distinguish threshold fragments from actual anatomy; do not define CEJ solely as the lowest pixel of any bright object.

Identify ABC on the external alveolar plate outside the complete M2 root set. The interradicular crest between roots is not the external plate crest for this endpoint. Trace the tooth, periodontal gap and alveolar plate through adjacent source views. Account for continuous coronal bone extensions even where a current image row lacks a tooth boundary. A largest component, tooth-overlap test or imposed expected crest height cannot replace this review.

Show the raw grayscale sections, tooth/enamel and alveolar candidates, and all six CEJ/ABC pairs (12 landmarks) with side labels. Keep rejected candidates and unresolved structures identifiable in the private review record. Accepted landmarks belong to the reviewed source and plane; teaching images do not provide replacement coordinates.

## Measurement and release

Freeze a unit rootward axis `u` in the physical plane. For each reviewed pair:

`distance_mm = abs(dot(ABC_mm - CEJ_mm, u))`

When the calibrated plane's v-axis is the rootward direction, this is `abs(ABC_v - CEJ_v)`. This is not the Euclidean length of a diagonal segment. The [calculator contract](measurement-tool.md) explains conversion from unresized pixel coordinates.

Retain all six values, missingness and review status. Do not silently average away an invalid landmark or treat the six within-jaw observations as six independent animals. The study's statistical design determines aggregation and the experimental unit.

Release only after source calibration, section geometry, landmark identity and required anatomical-side mapping pass review. Save physical coordinates before making a presentation figure. Repeat localization/annotation under an appropriate blinded design before claiming observer agreement or automated accuracy.
