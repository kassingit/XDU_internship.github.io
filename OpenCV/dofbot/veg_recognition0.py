import requests
import cv2

endpoint = "https://predict-6a3e07f056f70c6e228d-dproatj77a-df.a.run.app"
with open("key.txt",'r') as f:
    api_key= f.read().strip()
img_path= "/home/kelly/XDU_internship.github.io/OpenCV/dofbot/image_for_test/_poivron_m_lange_de_couleurs_bio-c-a-mr-1.jpg"

# send image to API
with open(img_path,"rb") as f:
    response = requests.post(
        f"{endpoint}/predict",
        headers={"X-API-Key": api_key},
        files={"file": f},
        data={"conf": 0.25, "iou": 0.7}
        )
    

data = response.json()
print(data)


# Load image
img = cv2.imread(img_path)
if img is None:
    raise ValueError("Image not found. Check the path!")


# Draw detections
for result in data['images'][0]['results']:
    box = result['box']
    x1 ,y1, x2, y2 = int(box['x1']),int(box['y1']),int(box['x2']), int(box['y2'])
    label = f"{result['name']} {result['confidence']:.2f}"
    color = (255,0,0)
    cv2.rectangle(img, (x1,y1), (x2, y2), color, 2)
    cv2.putText(img,label, (x1,y1-10),cv2.FONT_HERSHEY_SIMPLEX,1.0, color, 3)


# Resize to fit screen
screen_width = 1200 # adjust to the screen width
screen_height = 800 # adjust to the screen height
h, w = img.shape[:2]
scale = min(screen_width / w, screen_height / h)
#img_resized = cv2.resize(img, (int(w*scale), int(h*scale)))
img_resized = cv2.resize(img, (int(w), int(h)))

# show the image
cv2.imshow("YOLO Result", img_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()