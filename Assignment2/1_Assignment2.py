import Arthimetic

def main():
    operation1= int(input("Enter first number :"))

    operation2= int(input("Enter second number :"))

    Add = Arthimetic.Add(operation1,operation2)
    Sub = Arthimetic.Sub(operation1,operation2)
    Mult = Arthimetic.Mult(operation1,operation2)
    Div = Arthimetic.Div(operation1,operation2)

    print("The Additoon is :",Add)
    print("The Substraction is :",Sub)
    print("The Multiplication is :",Mult)
    print("The Division is :",Div)

if __name__ == "__main__":
    main()