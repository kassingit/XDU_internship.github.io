import cv2 as cv

vd = cv.VideoCapture('dog.mp4');

### -------------------------------- video reading
"""
while True:
    isTrue, frame = vd.read()
    if isTrue:
        cv.imshow("video 1",frame);
        #display the frames avery 20 ms and get out of the video when the letter 'd' is pressed
        if cv.waitKey(20) & 0xFF ==ord('f') :
            break;
    else:
        break;

vc.release()
cv.destroyedAllWindows()    
"""

##-----------------------------------  rescaling and resizing ( for image, video and live video)
def rescale_frame( frame, scale=0.75):
    height = int(frame.shape[0]*scale) # we put int() to transform frame.shape[0]*scale into an int
    width = int(frame.shape[1]*scale)

    dimension = (width,height) # /!\ NOT (heigth,width) because cv.resize() expect (width,height)

    return cv.resize(frame, dimension, interpolation = cv.INTER_AREA)


while True:
    isTrue, frame = vd.read()
    frame_resized = rescale_frame(frame,0.5)
    if isTrue:
        cv.imshow("Original video ",frame)
        cv.imshow("resized video ",frame_resized)

        #display the frames avery 20 ms and get out of the video when the letter 'd' is pressed
        if cv.waitKey(20) & 0xFF ==ord('f') :
            break;
    else:
        break;

vc.release()
cv.destroyedAllWindows()  

##----------------------------------- rescaling and resizing  ( for only live video)
def changeRes(width,height):
    Capture.set(3,width);
    Capture.set(4,height);
 