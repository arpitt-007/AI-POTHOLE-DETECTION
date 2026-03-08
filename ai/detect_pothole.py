import cv2
import requests
from ultralytics import YOLO
import datetime

model = YOLO("../model/pothole_model.pt")

cap = cv2.VideoCapture("../video/road_sample.mp4")

while True:

    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame)

    for r in results:

        boxes = r.boxes

        if boxes is not None:

            for box in boxes:

                x1,y1,x2,y2 = map(int,box.xyxy[0])

                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),2)

                cv2.putText(frame,"Pothole",
                            (x1,y1-10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.7,(0,0,255),2)

                data = {
                    "lat":12.9716,
                    "lon":77.5946,
                    "time":str(datetime.datetime.now())
                }

                requests.post(
                    "http://localhost:5000/add_pothole",
                    json=data
                )

    cv2.imshow("Detection",frame)

    if cv2.waitKey(1)==27:
        break

cap.release()
cv2.destroyAllWindows()