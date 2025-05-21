class Calculator:
    def __init__(self, a: float, b: float, operation: str):
        self.a = a
        self.b = b
        self.operation = operation

    def calculate(self):
        if self.operation == "+":
            return self.a + self.b
        elif self.operation == "-":
            return self.a - self.b
        elif self.operation == "*":
            return self.a * self.b
        elif self.operation == "/":
            if self.b == 0:
                return "Error: Division by zero"
            return self.a / self.b
        else:
            return "Error: Invalid operation"

try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    calc = Calculator(a, b, operation)
    result = calc.calculate()
    print("Result:", result)

except ValueError:
    print("Error: Please enter valid numbers.")
