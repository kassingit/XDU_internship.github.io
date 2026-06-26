import numpy as np
import cv2

cap = cv2.VideoCapture(2)

def rescale_frame( frame, scale=0.75):
    height = int(frame.shape[0]*1.5*scale) 
    width = int(frame.shape[1]*scale)

    dimension = (width,height) # /!\ NOT (heigth,width) because cv.resize() expect (width,height)

    return cv2.resize(frame, dimension, interpolation = cv2.INTER_AREA)


while True:
    ret, img = cap.read()
    img_rescaled = rescale_frame(img,1.2)
    if not ret:
        break
    
    # Rotate 90° counter-clockwise
    img2 = cv2.rotate(img_rescaled, cv2.ROTATE_90_COUNTERCLOCKWISE)
    # OR for 90° clockwise:
    # img2 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    # OR for 180°:
    # img2 = cv2.rotate(img, cv2.ROTATE_180)
    
    cv2.imshow('rotated video', img2)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()