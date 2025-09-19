import matplotlib.pyplot as plt

def show_dashboard(vehicle_count, congestion, signal_time):
    """Display a simple dashboard."""
    labels = ['Vehicle Count', 'Suggested Signal Time']
    values = [vehicle_count, signal_time]

    plt.figure(figsize=(6, 4))
    plt.bar(labels, values, color=['blue', 'green'])
    plt.title(f"Traffic Dashboard - Congestion: {congestion}")
    plt.ylim(0, max(values) + 10)
    plt.show()
