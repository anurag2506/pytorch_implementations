"""Install OpenCV in Python, confirm cv2 imports, load an image, display it, save it back. No excuses until you can do this in under 2 minutes"""

"""Can you, right now, write a 10-line script that:

Loads an image from disk,

Converts it to grayscale,

Applies Canny edge detection,

Saves the output as edges.png—without Googling?
"""


# Improved code with error checking

import cv2 as cv
import os


def save_canny(img_path):
    file = img_path.split(".")
    DIR = os.path.join("dir" + file[0])
    os.makedirs(DIR, exist_ok=True)
    img = cv.imread(img_path)

    if img is not None:
        cv.imwrite(f"saved_{img_path}", img)

    try:
        gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
        gray_p = os.path.join(DIR, "gray.png")
        cv.imwrite(gray_p, gray)
        canny = cv.Canny(gray, 120, 240)
        canny_ = os.path.join(DIR, "edges.png")
        cv.imwrite(canny_, canny)

    except Exception as e:
        print(f"Error in generating canny edges for {img_path}: {e}")


save_canny("./bron.png")
