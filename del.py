# import noti

# # Trigger notification for a custom scenario with a custom message
# noti.notify_execution(scenario="custom", custom_message="hello anish")

import time
import random
import noti

def train_model():
    """Simulates training a machine learning model."""
    try:
        print("Training the machine learning model...")
        # Simulate training process
        for epoch in range(1, 6):
            print(f"Epoch {epoch}/5: Training in progress...")
            time.sleep(2)  # Simulate training for 2 seconds

        # Simulate random scenario
        chosen_scenario = random.choice(["success", "failure", "user_input_required", "crash"])
        return chosen_scenario

    except KeyboardInterrupt:
        print("\nTraining interrupted by user.")
        raise SystemExit(2)  # Exit code 2 for user input required
    except Exception as e:
        print(f"Error during training: {e}")
        raise SystemExit(1)  # Exit code 1 for failure

def main():
    # Train the model
    scenario = train_model()

    # Notify the scenario
    noti.notify_execution(scenario)

if __name__ == "__main__":
    main()
