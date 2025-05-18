import cv2

def draw_boxes(frame, results):
    """Draw detected bounding boxes on frame"""
    for box in results[0].boxes.xyxy:
        x1, y1, x2, y2 = map(int, box)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Green box
    return frame

