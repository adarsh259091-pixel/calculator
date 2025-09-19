# calculator
🧮 Simple Calculator in Python

A simple calculator program written in Python that performs basic arithmetic operations: addition, subtraction, multiplication, and division.

📌 Features

➕ Addition

➖ Subtraction

✖️ Multiplication

➗ Division (with division-by-zero handling)

🚫 Handles invalid operators gracefully

📝 Code
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

🚀 Usage

You can call the function directly with numbers and an operator:

print(calculator(4, 6, '+'))   # Output: 10
print(calculator(10, 5, '-'))  # Output: 5
print(calculator(3, 7, '*'))   # Output: 21
print(calculator(8, 2, '/'))   # Output: 4.0
print(calculator(5, 0, '/'))   # Output: Error: Division by zero is not allowed \n 0
print(calculator(9, 3, '%'))   # Output: Invalid operator \n 0

📂 Project Structure
.
├── calculator.py   # Contains the calculator function
└── README.md       # Project documentation

▶️ How to Run

Save the code into a file called calculator.py.

Open a terminal or command prompt in the same directory.

Run the file with Python:
