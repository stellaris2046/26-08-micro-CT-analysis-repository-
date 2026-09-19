# Repository guidance

This is the public, data-free distribution of a mouse-jaw micro-CT skill.

- `mimics-mouse-jaw-analysis/SKILL.md` owns the reusable analysis workflow; its linked references own endpoint details. README files describe installation and capabilities.
- Keep study parameters, images, specimen identifiers, physical case records, local paths, private review history and credentials outside this repository. Test inputs must be newly invented synthetic data.
- Preserve calibration, source provenance and human anatomical-review gates. Do not turn a study-specific threshold, VOI size, or accepted case into a universal default.
- Do not claim an executable imaging pipeline, image inspection, application integration or biological validation that the distributed files do not provide.
- The distance calculator uses the Python standard library. Run `python -m unittest discover -s tests -v` for affected behavior and check local Markdown links when moving documentation.
- Review the actual staged files before publishing. `.gitignore` is not a privacy guarantee. Changes here do not authorize modification of a researcher's installed skill or study records.
