class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        result_add = self.x + self.y
        return result_add

    def subtract(self):
        result_subtract = self.x - self.y
        return result_subtract

    def multiply(self):
        result_multiply = self.x * self.y
        return result_multiply

    def divide(self):
        if self.y != 0:
            result_divide = self.x // self.y
            return result_divide
        else:
            return "Error"


o = input()
x = int(input())
y = int(input())
calculator = Calculator(x, y)

if o == 'a':
        # Addition
        result_add = calculator.add()
        print(result_add)
elif o == 's':
        # Subtraction
        result_subtract = calculator.subtract()
        print(result_subtract)
elif o == 'm':
        # Multiplication
        result_multiply = calculator.multiply()
        print(result_multiply)
elif o == 'd':
        # Division
        result_divide = calculator.divide()
        print(result_divide)
