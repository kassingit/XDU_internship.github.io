import cv2 as cv
## Image reading 
#Since Read.py and the picture are in the same folder, we will just us the name of the file
img = cv.imread('Intel-CPU1.jpg');

"""
cv.imshow('Image 0',img);
cv.waitKey(0)
cv.destroyAllWindows();
"""

# Image resizing 

def rescale_image( frame, scale=0.75):
    height = int(frame.shape[0]*scale) # we put int() to transform frame.shape[0]*scale into an int
    width = int(frame.shape[1]*scale)

    dimension = (width,height) # /!\ NOT (heigth,width) because cv.resize() expect (width,height)

    return cv.resize(frame, dimension, interpolation = cv.INTER_AREA)

img_resized = rescale_image(img,0.5)
cv.imshow('Image 0',img);
cv.imshow("Image resized", img_resized)
cv.waitKey(0)
cv.destroyAllWindows();
