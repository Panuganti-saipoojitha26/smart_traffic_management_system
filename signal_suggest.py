def suggest_signal_timing(vehicle_count):
    """Suggest green light duration based on congestion."""
    if vehicle_count < 5:
        return 30  # seconds
    elif vehicle_count < 15:
        return 60
    else:
        return 90
