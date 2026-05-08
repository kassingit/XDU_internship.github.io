import cv2 as cv
import numpy as np 

vd = cv.VideoCapture('dog.mp4');
vd2 =cv.VideoCapture('kitten.mp4');


def rescale_frame( frame, scale=0.75):
    height = int(frame.shape[0]*scale) # we put int() to transform frame.shape[0]*scale into an int
    width = int(frame.shape[1]*scale)

    dimension = (width,height) # /!\ NOT (heigth,width) because cv.resize() expect (width,height)

    return cv.resize(frame, dimension, interpolation = cv.INTER_AREA)



while True:
    isTrue, frame = vd.read()
    frame_resized = rescale_frame(frame,0.5)
    if isTrue:
        cv.imshow("resized video ",frame_resized)
        #display the frames avery 20 ms and get out of the video when the letter 'd' is pressed
        if cv.waitKey(20) & 0xFF ==ord('f') :
            break;
    else:
        break;

    isTrue, frame2 = vd2.read()
    frame_resized = rescale_frame(frame2,0.5)
    if isTrue:
        cv.imshow("resized video2 ",frame_resized)
        #display the frames avery 20 ms and get out of the video when the letter 'd' is pressed
        if cv.waitKey(20) & 0xFF ==ord('f') :
            break;
    else:
        break;


vc.release()
cv.destroyedAllWindows()  
"""

## LINE 4 , 6 and AA test

blank4  = np.zeros((500,500,3), dtype='uint8')
blank8  = np.zeros((500,500,3), dtype='uint8')
blankAA = np.zeros((500,500,3), dtype='uint8')

# Diagonal line — this is where the difference shows
cv.line(blank4,  (0, 0), (499, 499), (0,255,0), thickness=2, lineType=cv.LINE_4)
cv.line(blank8,  (0, 0), (499, 499), (0,255,0), thickness=2, lineType=cv.LINE_8)
cv.line(blankAA, (0, 0), (499, 499), (0,255,0), thickness=2, lineType=cv.LINE_AA)

cv.imshow("LINE_4",  blank4)
cv.imshow("LINE_8",  blank8)
cv.imshow("LINE_AA", blankAA)
cv.waitKey(0)
cv.destroyAllWindows()"""