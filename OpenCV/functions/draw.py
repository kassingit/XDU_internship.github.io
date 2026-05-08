import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')

#cv.imshow("Blank", blank)

# paint the image in a certain colour
"""
blank[200:300,300:400] = 0,255,0 # every pixel in white

cv.imshow("Green", blank)
cv.waitKey(0)
cv.destroyAllWindows()
"""

#d----raw a rectangle
cv.rectangle(blank,(0,0),(250,250), (0,255,0),thickness=2)
#cv.imshow("Rectangle", blank)

cv.rectangle(blank,(0,0),(250,250), (0,255,0),thickness=cv.FILLED) # we can replace cv.FILLED by -1
#cv.imshow("Rectangle FILLED", blank)

cv.rectangle(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2), (0,255,0),thickness=-1) # we can replace cv.FILLED by -1
#cv.imshow("Rectangle FILLED using shape", blank)

""" -------------- we could use the follow option ----------------------------
cv.rectangle(blank,(0,0),(250,250), (0,255,0),thickness=2,lineType=cv.LINE_4)
cv.imshow("Rectangle LINE 4", blank)

cv.rectangle(blank,(0,0),(250,250), (0,255,0),thickness=2,lineType=cv.LINE_8)
cv.imshow("Rectangle LINE 8", blank)

cv.rectangle(blank,(0,0),(250,250), (0,255,0),thickness=2,lineType=cv.LINE_AA)
cv.imshow("Rectangle LINE AA", blank)

"""

#---- Draw a circle
cv.circle(blank,(blank.shape[1]//2, blank.shape[0]//2),40,(0,0,255),thickness=5)


#-- draw line
cv.line(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2),(255,255,255),thickness=3)
#cv.imshow("Line",blank)


#-- write a text
cv.putText(blank,"Hello",((blank.shape[1]//2)+20, (blank.shape[0]//2)+200),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,255,255),2)
cv.imshow("Text", blank)
cv.waitKey(0)
cv.destroyAllWindows()