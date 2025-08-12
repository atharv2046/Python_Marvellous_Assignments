class Calculator:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def add(self):
        return self.value1 + self.value2

    def sub(self):
        return self.value1 - self.value2

    def multiply(self):
        return self.value1 * self.value2

    def divide(self):
        if self.value2 != 0:
            return self.value1 / self.value2
        else:
            return "Cannot divide by zero"

def main():
    value1 = float(input("Enter the first value: "))
    value2 = float(input("Enter the second value: "))

    calci = Calculator(value1, value2)

    print("Addition:", calci.add())
    print("Subtraction:", calci.sub())
    print("Multiplication:", calci.multiply())
    print("Division:", calci.divide())

if __name__ == "__main__":
    main()
