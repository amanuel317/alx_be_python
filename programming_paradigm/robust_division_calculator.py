def safe_divide(numerator, denominator):
    try:
        # Attempt to convert inputs to float
        numerator = float(numerator)
        denominator = float(denominator)

        # Perform division
        result = numerator / denominator

        # Return result if successful
        return result

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."
