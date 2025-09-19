from utils import load_image
from vehiclecount import count_vehicles
from congestion_predict import predict_congestion
from signal_suggest import suggest_signal_timing
from dashboard import show_dashboard

def main():
    image_path = "traffic.jpg"  # Make sure your image is here
    image = load_image(image_path)

    vehicles = count_vehicles(image)
    congestion = predict_congestion(vehicles)
    signal_time = suggest_signal_timing(vehicles)

    print(f"Detected Vehicles: {vehicles}")
    print(f"Predicted Congestion: {congestion}")
    print(f"Suggested Signal Time: {signal_time} seconds")

    show_dashboard(vehicles, congestion, signal_time)

if __name__ == "__main__":
    main()
