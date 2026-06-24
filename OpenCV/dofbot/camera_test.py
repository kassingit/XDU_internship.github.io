import cv2 
import time
import pygame 
from PIL import Image, ImageDraw, ImageFont
import numpy
import ipywidgets.widgets as widgets


import cv2
cap = cv2.VideoCapture(0)

while True:
    success,frame = cap.read()
    if success:
        cv2.imshow(" Camera test ", frame)
    if cv2.waitKey(1) & 0xFF==ord('p'):
        break

cap.release()
cv2.destroyAllWindows()
