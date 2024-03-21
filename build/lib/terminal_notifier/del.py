from notifier import notify_execution

def main():
    try:
        notify_execution(scenario="success")
        print("Notification sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
