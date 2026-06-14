# PDF → grid overlay

## Problem

I needed to convert PDF/Word docs to PNG, then overlay a coordinate grid so researchers could click regions on research figures and map them to normalized `(x, y)` values.

## What went wrong (`attempt.py`)

`convert_pdf_to_png` loops over `images`, but **`images` is never defined** — I started the pipeline before wiring up a PDF renderer. Word conversion also flattens to plain text instead of a real layout render.

## How I'd solve it

1. **PDF → PNG:** use **PyMuPDF (`fitz`)** or `pdf2image` to rasterize each page at fixed DPI.
2. **Word → PNG:** export via LibreOffice headless, or skip Word and accept PDF/image inputs only.
3. **Grid overlay:** keep the OpenCV logic — it works once you have a real bitmap.
4. **Selection UI:** separate script (`select_grid.py` in [protein-motif-encoding](https://github.com/JarvinChavez/protein-motif-encoding)) exports normalized JSON coordinates.

## Related repo

The working grid overlay + selector lives in **protein-motif-encoding**.
