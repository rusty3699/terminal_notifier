import time
import random
import noti

def simulate_execution(scenario):
    """Simulates execution based on the provided scenario."""
    try:
        if scenario == "success":
            print("Execution successful.")
            # Simulate successful execution
            time.sleep(2)
        elif scenario == "failure":
            print("Encountered failure during execution.")
            # Simulate failure
            raise Exception("Simulated failure.")
        elif scenario == "user_input_required":
            print("Waiting for user input...")
            # Notify before waiting for user input
            noti.notify_execution(scenario)
            time.sleep(1)  # Delay to ensure notification is displayed before input
            # Simulate waiting for user input
            user_input = input("Enter 'y' to continue, or 'n' to terminate: ")
            if user_input.lower() == 'y':
                print("Continuing...")
            else:
                print("Terminating...")
                raise KeyboardInterrupt
        elif scenario == "crash":
            print("Program crashed unexpectedly.")
            # Simulate crash
            raise Exception("Simulated crash.")
        else:
            print("Unknown scenario.")
    except KeyboardInterrupt:
        print("\nTerminating...")
        raise SystemExit(2)  # Exit code 2 for user input required
    except Exception as e:
        print(f"Error: {e}")
        raise SystemExit(1)  # Exit code 1 for failure

def main():
    # List of possible scenarios
    scenarios = ["success", "failure", "user_input_required", "crash"]

    # Choose a random scenario
    chosen_scenario = random.choice(scenarios)

    # Simulate execution based on the chosen scenario
    simulate_execution(chosen_scenario)

    # Notify the chosen scenario
    noti.notify_execution(chosen_scenario)

if __name__ == "__main__":
    main()
