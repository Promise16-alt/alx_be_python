def safe_divide(numerator, denominator):
    """
    Performs division while handling errors such as division by zero and non-numeric inputs.
    """
    try:
        num = float(numerator)
        denom = float(denominator)

        if denom == 0:
            return "Error: Cannot divide by zero."

        return f"The result of the division is {num / denom:.2f}"

    except ValueError:
        return "Error: Please enter numeric values only.
