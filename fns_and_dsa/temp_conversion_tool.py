# ✅ Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius using the global conversion factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit using the global conversion factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    """Handles user input and performs temperature conversion based on user choice."""
    try:
        temperature = float(input("Enter the temperature to convert: ").strip())  # ✅ Ensures input is a number
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)  # ✅ Calls correct function
            print(f"{temperature}°C is {converted_temp:.2f}°F")
        elif unit == 'F':
            converted_temp = convert_to_celsius(temperature)  # ✅ Calls correct function
            print(f"{temperature}°F is {converted_temp:.2f}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")  # ✅ Handles invalid unit

    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")  # ✅ Handles non-numeric input

if __name__ == "__main__":
    main()  # ✅ Ensures script runs when executed
