def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Division by zero is not allowed"
    else:
        return "Invalid operation!"

# Example usage:
operation = "+"
num1 = 5
num2 = 3
result = calculator(operation, num1, num2)
print(result)  # This will print 8 for the given example

operation = "/"
num1 = 10
num2 = 0
result = calculator(operation, num1, num2)
print(result)  # This will print "Division by zero is not allowed" for division by zero
