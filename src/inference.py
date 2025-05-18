import cv2
import torch
from ultralytics import YOLO

# Ensure PyTorch runs on CPU
device = "cpu"
model = YOLO("models/yolov8n.pt").to(device)  # Load YOLOv8 model

# Start video capture
cap = cv2.VideoCapture(0)  # Webcam input

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run object detection
    results = model(frame)

    # Annotate frame
    annotated_frame = results[0].plot()

    # Show output in real-time
    cv2.imshow("Real-Time Object Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Quit on 'q' key
        break

cap.release()
cv2.destroyAllWindows()
