# PDF → grid overlay

## Problem

I needed to convert PDF/Word docs to PNG, then overlay a coordinate grid so researchers could click regions on research figures and map them to normalized `(x, y)` values.

## What went wrong (`attempt.py`)

`convert_pdf_to_png` loops over `images`, but **`images` is never defined** — I started the pipeline before wiring up a PDF renderer. Word conversion also flattens to plain text instead of a real layout render.

## Step-by-step solution notes

1. **Load source document:** accept PDF input first (image input optional).
2. **Rasterize pages:** use PyMuPDF (`fitz`) to convert each page into a PNG bitmap at fixed DPI.
3. **Overlay grid:** run existing OpenCV line-drawing logic (small + large grid).
4. **Export generated files:** save `*_grid.png` outputs page-by-page.
5. **Validate coordinates:** confirm grid spacing and labels align with expected pixel coordinates.

## Related repo

The working grid overlay + selector now lives in [color-recognition](https://github.com/JarvinChavez/color-recognition).
