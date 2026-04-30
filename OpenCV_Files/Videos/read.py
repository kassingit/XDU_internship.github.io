import cv2 as cv

vd = cv.VideoCapture('dog.mp4');

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
