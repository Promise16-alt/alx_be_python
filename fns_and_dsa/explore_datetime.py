from datetime import datetime, timedelta

def display_current_datetime():
    """Displays the current date and time in a formatted way."""
    current_date = datetime.now()  # ✅ Stores current date inside `current_date`
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # ✅ Formats output
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    """Calculates and displays a future date based on user input."""
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: ").strip())  # ✅ Ensures input is an integer
        future_date = datetime.now() + timedelta(days=days_to_add)  # ✅ Stores future date inside `future_date`
        formatted_future_date = future_date.strftime("%Y-%m-%d")  # ✅ Formats output
        print(f"Future date: {formatted_future_date}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

def main():
    """Runs both functions to display the current datetime and future date calculation."""
    display_current_datetime()  # ✅ Calls `display_current_datetime`
    calculate_future_date()  # ✅ Calls `calculate_future_date`

if __name__ == "__main__":
    main()  # ✅ Ensures the script runs properly when execute
