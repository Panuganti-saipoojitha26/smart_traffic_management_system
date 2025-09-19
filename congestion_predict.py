def predict_congestion(vehicle_count):
    """Simple congestion prediction."""
    if vehicle_count < 5:
        return "Low"
    elif vehicle_count < 15:
        return "Moderate"
    else:
        return "High"
