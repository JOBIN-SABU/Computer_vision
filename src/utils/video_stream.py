import cv2

def get_video_stream(source=0):
    """Open video stream (default: webcam)"""
    cap = cv2.VideoCapture(source)
    if not cap.isOpened():
        raise ValueError(f"Cannot open video source: {source}")
    return cap
