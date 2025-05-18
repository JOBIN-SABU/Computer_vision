import cv2

def preprocess_frame(frame, target_size=(640, 640)):
    """Resize frame before feeding to model"""
    return cv2.resize(frame, target_size)
