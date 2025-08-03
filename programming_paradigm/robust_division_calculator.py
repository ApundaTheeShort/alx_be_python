def safe_divide(numerator, denominator):
    try:
        if denominator == 0:
            raise ZeroDivisionError
        else:
            result = float(numerator) / float(denominator)
            return result

    except ValueError:
        return "Error: Please Enter numeric values only"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
