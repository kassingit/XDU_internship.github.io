import cv2 as cv
## Image reading 
#Since Read.py and the picture are in the same folder, we will just us the name of the file
img = cv.imread('Intel-CPU1.jpg');
cv.imshow('Image 0',img);
cv.waitKey(0)
cv.destroyAllWindows();


## video reading 