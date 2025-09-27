"""Install OpenCV in Python, confirm cv2 imports, load an image, display it, save it back. No excuses until you can do this in under 2 minutes"""

import cv2 as cv
import os


image = "./image.png"
img = cv.imread(image)

cv.imshow("image", img)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imwrite("saved_1.png", img)


"""Can you, right now, write a 10-line script that:

Loads an image from disk,

Converts it to grayscale,

Applies Canny edge detection,

Saves the output as edges.png—without Googling?
"""

img = "./saved_1.png"
image = cv.imread(img)

gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
cv.imshow("gray", gray)
cv.imwrite("gray.png", gray)

canny = cv.Canny(gray, 120, 240)
cv.imwrite("canny.png", canny)


# Improved code with error checking


def save_canny(img_path):
    file = img_path.split(".")
    DIR = os.path.join("dir" + file[0])
    os.makedirs(DIR, exist_ok=True)
    img = cv.imread(img_path)

    if img is not None:
        cv.imwrite(f"saved_{img_path}", img)

    try:
        gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
        gray_p = os.path.join(DIR, "gray.png")
        cv.imwrite(gray_p, gray)
        canny = cv.Canny(gray, 120, 240)
        canny_ = os.path.join(DIR, "edges.png")
        cv.imwrite(canny_, canny)

    except Exception as e:
        print(f"Error in generating canny edges for {img_path}: {e}")


save_canny("./bron.png")
