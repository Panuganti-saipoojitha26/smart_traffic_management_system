from utils import preprocess_image
import cv2

def count_vehicles(image):
    """Simple vehicle counting using contour detection."""
    processed = preprocess_image(image)
    _, thresh = cv2.threshold(processed, 200, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    vehicle_count = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:  # Minimum area to count as vehicle
            vehicle_count += 1
    return vehicle_count
