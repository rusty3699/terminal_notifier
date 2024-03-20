import time
import noti

def main():
    try:
        # Loop from 1 to 4 with a 1-second delay
        for i in range(1, 4):
            print(i)
            time.sleep(1)  # Introduce a 1-second delay

        # Simulate success scenario
        noti.notify_execution("success")

        # Simulate waiting for user input scenario
        # In a real scenario, this part would prompt for user input
        user_input = input("Enter 'y' to continue, or 'n' to terminate: ")
        if user_input.lower() == 'y':
            print("Continuing...")
        else:
            print("Terminating...")
            raise KeyboardInterrupt

        # Simulate failure scenario
        # In a real scenario, this part would encounter an error
        raise Exception("Simulating failure...")

    except KeyboardInterrupt:
        print("\nTerminating...")
        # Exit with code 2 to indicate termination due to user input required
        exit_code = 2
        noti.notify_execution("user_input_required")
        raise SystemExit(exit_code)  # Raise SystemExit to ensure proper exit code

    except Exception as e:
        print(f"Error: {e}")
        # Exit with code 1 to indicate failure
        exit_code = 1
        noti.notify_execution("failure")
        raise SystemExit(exit_code)  # Raise SystemExit to ensure proper exit code

    finally:
        # Simulate cleanup or crash scenario
        # In a real scenario, this part might handle unexpected errors or cleanup tasks
        print("Performing cleanup...")
        noti.notify_execution("crash")

if __name__ == "__main__":
    main()
