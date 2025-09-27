'''Install OpenCV in Python, confirm cv2 imports, load an image, display it, save it back. No excuses until you can do this in under 2 minutes'''

import cv2 as cv
image = './image.png'
img = cv.imread(image)

cv.imshow("image",img)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imwrite("saved_1.png", img)


'''Can you, right now, write a 10-line script that:

Loads an image from disk,

Converts it to grayscale,

Applies Canny edge detection,

Saves the output as edges.png—without Googling?
'''

img = './saved_1.png'
image = cv.imread(img)

gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
cv.imshow("gray",gray)
cv.imwrite("gray.png",gray)

canny = cv.Canny(gray,120,240)
cv.imwrite("canny.png",canny)