def safe_divide(numerator, denomenator):
    try:
        if denomenator == 0:
            raise ZeroDivisionError
        else:
            result = float(numerator) / float(denomenator)
            return result

    except ValueError:
        return "Error: Please Enter numeric values only"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
