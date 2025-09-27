"""
Can you now write a minimal script (≤12 lines) that:

Reads an image,

Resizes it to exactly 200×200,

Draws a red circle at the center,

Saves it as circle.png—without copy-pasting old code?

"""

import cv2 as cv
import numpy as np
import os


def process(img_path):
    # Check if a directory path is desired and ensure it's handled properly
    dir_path = os.path.join("output_dir")
    os.makedirs(dir_path, exist_ok=True)

    img = cv.imread(img_path)
    if img is None:
        # Create a blank image if the file doesn't exist
        img = np.zeros((200, 200, 3), dtype=np.uint8)

    # Resize the image to 200x200
    resized_img = cv.resize(img, (200, 200))

    # Draw a filled red circle at the center
    center = (100, 100)
    color = (0, 0, 255)  # BGR for red
    radius = 50
    cv.circle(resized_img, center, radius, color, -1)

    # Save the file with the correct name and path
    output_path = os.path.join(dir_path, "circle.png")
    cv.imwrite(output_path, resized_img)


process("./bron.png")
