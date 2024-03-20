# from plyer import notification

# # Main function
# def main():
#     # Display notification
#     notification.notify(
#         title="Command Execution",
#         message="Command executed successfully!",
#         timeout=5  # Notification timeout in seconds
#     )

# if __name__ == "__main__":
#     main()
import subprocess
from plyer import notification

def main():
    try:
        # Execute loops.py using subprocess
        process = subprocess.Popen(['python', 'loops.py'])

        # Wait for loops.py to terminate
        process.wait()

        # Check the return code of loops.py to determine its termination status
        return_code = process.returncode

        # Handle different termination scenarios
        if return_code == 0:
            # Display notification if loops.py terminated successfully
            notification.notify(
                title="Loops.py Execution",
                message="Loops.py terminated successfully!",
                timeout=5
            )
        elif return_code == 1:
            # Display notification if loops.py terminated with an error
            notification.notify(
                title="Loops.py Execution",
                message="Loops.py terminated with an error!",
                timeout=5
            )
        elif return_code == 2:
            # Display notification if loops.py is waiting for user input
            notification.notify(
                title="Loops.py Execution",
                message="Loops.py is waiting for user input!",
                timeout=5
            )
        else:
            # Display a generic notification for other return codes
            notification.notify(
                title="Loops.py Execution",
                message=f"Loops.py terminated with return code: {return_code}",
                timeout=5
            )

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

