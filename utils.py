import cv2
import numpy as np

def load_image(path):
    """Load an image from disk."""
    try:
        image = cv2.imread(path)
        if image is None:
            raise FileNotFoundError(f"Image not found at {path}")
        return image
    except Exception as e:
        print(e)
        raise

def preprocess_image(image):
    """Convert to grayscale and apply blur."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    return blurred
