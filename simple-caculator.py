def calculate() -> None:
    try:
        num1 = int(input("Enter first value: "))
        operator = input("Enter operation (+, -, *, /): ")
        num2 = int(input("Enter second value: "))

        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            if num2 == 0:
                return "Error: Cannot divide by zero"
            return num1 / num2
        else:
            return "Invalid operation. Please enter one of +, -, *, or /."
    except ValueError:
        return "Invalid input. Please enter valid numbers."

# Example usage
result = calculate()
print(result)
