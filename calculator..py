def calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b != 0:
            return a / b
        else:
            print("Error: Division by zero is not allowed")
            return 0
    else:
        print("Invalid operator")
        return 0
