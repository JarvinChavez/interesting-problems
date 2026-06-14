"""Original attempt — PDF conversion never wired up (NameError: images)."""

import os
import cv2
from PIL import Image, ImageDraw, ImageFont
import docx


def convert_pdf_to_png(pdf_path, output_folder="output_images"):
    os.makedirs(output_folder, exist_ok=True)
    image_paths = []
    for i, image in enumerate(images):  # BUG: images is undefined
        image_path = os.path.join(output_folder, f"page_{i + 1}.png")
        image.save(image_path, "PNG")
        image_paths.append(image_path)
    return image_paths


def overlay_grid(image_path, small_grid=10, large_grid=100):
    image = cv2.imread(image_path)
    height, width, _ = image.shape
    for x in range(0, width, small_grid):
        cv2.line(image, (x, 0), (x, height), (200, 200, 200), 1)
    for y in range(0, height, small_grid):
        cv2.line(image, (0, y), (width, y), (200, 200, 200), 1)
    output_path = image_path.replace(".png", "_grid.png")
    cv2.imwrite(output_path, image)
    return output_path
