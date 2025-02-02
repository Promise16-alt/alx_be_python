def main():

    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
    match priority:
        case "high":
            message = f"'{task}' is a high priority task."
        case "medium":
            message = f"'{task}' is a medium priority task."
        case "low":
            message = f"'{task}' is a low priority task."
        case _:
            message = "Invalid priority entered. Please enter high, medium, or low."
            print(message)
            return
    if time_bound == "yes":
        message += " That requires immediate attention today!"
    elif time_bound == "no":
        message += " Consider completing it when you have free time."
    else:
        print("Invalid input for time sensitivity. Please enter yes or no.")
        return
    print("\nReminder:", message)

if __name__ == "__main__":
    main()t
