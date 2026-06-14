"""Fixed approach — rasterize PDF pages with PyMuPDF, then apply grid overlay."""

from __future__ import annotations

import os
from pathlib import Path

import cv2
import fitz  # PyMuPDF


def convert_pdf_to_png(pdf_path: str | Path, output_folder: str | Path = "output_images") -> list[str]:
    output_folder = Path(output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)
    image_paths: list[str] = []

    doc = fitz.open(pdf_path)
    for i, page in enumerate(doc):
        pix = page.get_pixmap(dpi=150)
        image_path = output_folder / f"page_{i + 1}.png"
        pix.save(image_path)
        image_paths.append(str(image_path))
    return image_paths


def overlay_grid(image_path: str, small_grid: int = 10, large_grid: int = 100) -> str:
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    for x in range(0, width, small_grid):
        cv2.line(image, (x, 0), (x, height), (200, 200, 200), 1)
    for y in range(0, height, small_grid):
        cv2.line(image, (0, y), (width, y), (200, 200, 200), 1)
    for x in range(0, width, large_grid):
        cv2.line(image, (x, 0), (x, height), (0, 0, 0), 2)
    for y in range(0, height, large_grid):
        cv2.line(image, (0, y), (width, y), (0, 0, 0), 2)

    output_path = image_path.replace(".png", "_grid.png")
    cv2.imwrite(output_path, image)
    return output_path


def process_pdf(pdf_path: str, output_folder: str = "output_images") -> list[str]:
    grids = []
    for png in convert_pdf_to_png(pdf_path, output_folder):
        grids.append(overlay_grid(png))
    return grids


if __name__ == "__main__":
    # Example: process_pdf("sample.pdf")
    print("Provide a PDF path to process_pdf()")
