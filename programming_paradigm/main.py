def safe_divide(numerator, denominator):
    """
    Performs division while handling errors such as division by zero and non-numeric inputs.
    """
    try:
        # Convert inputs to float for division
        num = float(numerator)
        denom = float(denominator)

        if denom == 0:
            return "Error: Cannot divide by zero."

        return f"The result of the division is {num / denom:.2f}"

    except ValueError:
        # Catch non-numeric input errors
        return "Error: Please enter numeric values only."
