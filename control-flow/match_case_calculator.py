num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operator = input("choose the operation (+, -, *,/): ")

match operator:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 != 0:
            result = num1 / num2
        else:  # num2 == 0:
            print("Cannot divide by zero.")
    case _:
        print("Invalid operator")
print(f"The result is {result}")
