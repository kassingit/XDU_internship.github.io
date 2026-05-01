import cv2 as cv

img = cv.imread("/home/kelly/XDU_internship.github.io/OpenCV_Files/Pictures/Intel-CPU1.jpg")
cv.imshow("Original image",img)

#---------converting to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)


# -------- blur 
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow("Blur",blur)


#--------- Edge cascade
canny = cv.Canny(img, 125,175)
cv.imshow("Canny edge",canny)


#---------dilating the image
dilated = cv.dilate(img,(15,15), iterations=1)
cv.imshow("Dilated image",dilated)

cv.waitKey(0)
cv.destroyAllWindows()