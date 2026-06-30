# pip install ultralytics opencv-python

import cv2
from ultralytics import YOLO

# Load model
model = YOLO('exp-5.pt') 

# Vdeo source (0 = webcam , or paht to .mp4)
cap = cv2.VideoCapture(2)

def rescale_frame( frame, scale=0.75):
    height = int(frame.shape[0]*1.5*scale) 
    width = int(frame.shape[1]*scale)

    dimension = (width,height) # /!\ NOT (heigth,width) because cv.resize() expect (width,height)

    return cv2.resize(frame, dimension, interpolation = cv2.INTER_AREA)


while cap.isOpened():
    ret, frame_initial = cap.read()
    frame_rescaled = rescale_frame(frame_initial,1.2)
    frame = cv2.rotate(frame_rescaled, cv2.ROTATE_90_COUNTERCLOCKWISE)
    if not ret:
        break
    
    #run inference ( BRG frame is fine)
    results = model(frame, conf = 0.25, verbose=False)

    # process detections
    for result in results:
        boxes = result.boxes
        if boxes is None:
            continue
        
        xyxy = boxes.xyxy.cpu().numpy()
        confs = boxes.conf.cpu().numpy()
        clss = boxes.cls.cpu().numpy().astype(int)

        for (x1, y1, x2, y2), conf, cls in zip(xyxy, confs, clss):
            label = f"{result.names[cls]} {conf:.2f}"

            # Draw box
            cv2.rectangle(
                frame,
                (int(x1),int(y1)),
                (int(x2),int(y2)),
                (0,255,0),
                2,
            )


            # Draw label
            cv2.putText(
                frame,
                label,
                (int(x1), int(y1) - 8),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0,255,0),
                2,
            )
    cv2.imshow("YOLO Video",frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()