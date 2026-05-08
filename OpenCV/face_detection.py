import cv2 as cv

"""---------------------------------------- Lady -------------------------------------
img = cv.imread("Pictures/lady.jpg")

# the face detection doesn't take care of the color of skin, so we will put it into gray
gray =cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#reading to the value  kept in the .xml
haar_cascade = cv.CascadeClassifier('haar_face.xml')

#face detection
face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1 , minNeighbors=3)

print(f'number of face found = {len(face_rect)}')

for (x,y,w,h) in face_rect:
    cv.rectangle(img,(x,y),(x+w,y+h+13),(0,255,0), thickness=2)

cv.imshow("Face detected",img)
cv.waitKey(0)
cv.destroyAllWindows()

"""

def rescale_image( frame, scale=0.75):
    height = int(frame.shape[0]*scale) # we put int() to transform frame.shape[0]*scale into an int
    width = int(frame.shape[1]*scale)

    dimension = (width,height) # /!\ NOT (heigth,width) because cv.resize() expect (width,height)

    return cv.resize(frame, dimension, interpolation = cv.INTER_AREA)


img = cv.imread("Pictures/group 2.jpg")

img_resized = rescale_image(img,1.5)
cv.imshow('Image 0',img);



# the face detection doesn't take care of the color of skin, so we will put it into gray
gray =cv.cvtColor(img_resized, cv.COLOR_BGR2GRAY)

#reading to the value  kept in the .xml
haar_cascade = cv.CascadeClassifier('haar_face.xml')

#face detection
face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.25542, minNeighbors=1)

print(f'number of face found = {len(face_rect)}')

for (x,y,w,h) in face_rect:
    cv.rectangle(img_resized,(x,y),(x+w,y+h),(0,255,0), thickness=2)

cv.imshow("Face detected",img_resized)
cv.waitKey(0)
cv.destroyAllWindows()