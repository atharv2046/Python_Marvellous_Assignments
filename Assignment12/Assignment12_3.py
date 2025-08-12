class Arithmetic :

    def __init__(self):
        self.Value1 = 0
        self.Value2= 0
       

    def Accept(self):
        self.Value1=float(input("Enter Value1 :"))
        self.Value2=float(input("Enter Value2 :"))

    def Addition(self):
        return self.Value2 + self.Value2

    def Subtraction(self):
        return self.Value2 - self.Value2
    
    def Multiplication(self):
        return self.Value2 * self.Value2
    
    def Division(self):
        if self.Value2 != 0:
            return self.Value2 / self.Value2
        else :
            return "Cannot Divide By Zero"


def main():
    a1 = Arithmetic()
    a1.Accept()
    print("Addition:", a1.Addition())
    print("Subtraction:", a1.Subtraction())
    print("Multiplication:", a1.Multiplication())
    print("Division:", a1.Division())

if __name__ == "__main__":
    main()