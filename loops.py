import time
import sys

def main():
    try:
        # Loop from 1 to 10 with a 1-second delay
        for i in range(1, 11):
            print(i)
            time.sleep(1)  # Introduce a 1-second delay

        # Demonstrate waiting for user input scenario
        user_input = input("Enter 'y' to continue, or 'n' to terminate: ")
        if user_input.lower() == 'y':
            print("Continuing...")
        else:
            print("Terminating...")
            sys.exit(2)  # Exit with code 2 to indicate waiting for user input

        # Demonstrate failure scenario
        print("Simulating failure...")
        sys.exit(1)  # Exit with code 1 to indicate failure

    except KeyboardInterrupt:
        print("\nTerminating...")
        sys.exit(3)  # Exit with code 3 to indicate termination due to keyboard interrupt

if __name__ == "__main__":
    main()
