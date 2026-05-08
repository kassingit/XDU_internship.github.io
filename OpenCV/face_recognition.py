import cv2 as cv
import numpy as np

haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = ['Mindy Kaling', 'Elton John', 'Ben Afflek', 'Jerry Seinfield', 'Madonna']

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread(r'/home/kelly/XDU_internship.github.io/OpenCV/val/mindy_kaling/3.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#detection of the person

face_rect = haar_cascade.detectMultiScale(gray,1.2,4)

for (x,y,w,h) in face_rect:
    face_roi = gray[y:y+h,x:x+h]

    label,confidence = face_recognizer.predict(face_roi)
    print(f'label = {people[label]} with a confidence = {confidence}')

    cv.putText(img,str(people[label]),(20,20),cv.FONT_HERSHEY_COMPLEX,1.1,(0,255,0),thickness=2)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow("Detected face",img)
cv.waitKey(0)
cv.destroyAllWindows()