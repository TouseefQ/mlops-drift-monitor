import time
import random
from prometheus_client import start_http_server, Gauge

# 1. Define the Metric
# A 'Gauge' is a metric that can go up and down (like a speedometer)
ACCURACY_GAUGE = Gauge('model_accuracy', 'Current accuracy of the AI model')

def simulate_model_predictions():
    """
    Simulates a model that degrades over time.
    """
    # Start the metric server on port 8000 so Prometheus can read it
    start_http_server(8000)
    print("Combined API and Metrics server running on port 8000...")
    
    start_time = time.time()
    
    while True:
        elapsed_time = time.time() - start_time
        
        # LOGIC:
        # If the script has been running for less than 60 seconds, 
        # the model is "Good" (Accuracy between 90% and 99%)
        if elapsed_time < 60:
            current_accuracy = random.uniform(0.90, 0.99)
            print(f"Model is Healthy. Accuracy: {current_accuracy:.2f}")
            
        # After 60 seconds, the model "Drifts" (Accuracy drops to 50%-80%)
        else:
            current_accuracy = random.uniform(0.50, 0.80)
            print(f"ALERT: Model Drifting! Accuracy: {current_accuracy:.2f}")
        
        # 2. Update the Metric
        # This pushes the value to the exposed port
        ACCURACY_GAUGE.set(current_accuracy)
        
        # Wait 2 seconds before the next prediction
        time.sleep(2)

if __name__ == '__main__':
    simulate_model_predictions()