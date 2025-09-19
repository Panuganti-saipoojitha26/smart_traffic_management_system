# File: vehicle_analysis.py

import cv2
import torch
import random

# Load YOLOv8 small model (CPU)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
model.to('cpu')

# Congestion thresholds
def predict_congestion(vehicle_count):
    if vehicle_count < 20:
        return "Low", 30
    elif vehicle_count < 50:
        return "Medium", 60
    else:
        return "High", 90

def analyze_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Image not found at {image_path}")
        return

    # Run detection
    results = model(img)

    # Filter only vehicles (car, bus, truck, motorcycle)
    vehicle_classes = ['car', 'bus', 'truck', 'motorcycle']
    detections = results.pandas().xyxy[0]
    vehicle_count = detections[detections['name'].isin(vehicle_classes)].shape[0]

    congestion, signal_time = predict_congestion(vehicle_count)

    print(f"Detected Vehicles: {vehicle_count}")
    print(f"Predicted Congestion: {congestion}")
    print(f"Suggested Signal Time: {signal_time} seconds")

# Example usage
if __name__ == "__main__":
    image_path = "traffic.jpg"  # replace with your actual image
    analyze_image(image_path)
