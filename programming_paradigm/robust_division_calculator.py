def safe_divide(numerator, denominator):
    try:
        # Try to convert inputs to floats
        num = float(numerator)
        denom = float(denominator)
        
        # Handle division by zero
        if denom == 0:
            return "Error: Cannot divide by zero."
        
        # Perform division and return the result
        return f"The result of the division is {num / denom:.2f}"
    
    except ValueError:
        # Handle non-numeric input
        return "Error: Please enter numeric values only."
