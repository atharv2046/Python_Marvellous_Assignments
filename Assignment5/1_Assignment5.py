def sum(no1 ,no2):
    res = no1+no2
    return res

def Diff(no1,no2):
    res = no1 - no2
    return res

def Prod(no1,no2):
    res = no1*no2
    return res

def Div(no1,no2):
    res = no1 /no2
    return res

def main():
    no1= int(input("Enter first number :"))
    no2 = int(input("Enter Second Number:"))

    Add = sum(no1,no2)
    print("Sum is :",Add)

    Sub = Diff(no1,no2)
    print("Substraction is :",Sub)

    Mult = Prod(no1,no2)
    print("Multplication is :",Mult)

    Division = Div(no1,no2)
    print("Division is :",Division)



if __name__ == "__main__":
    main()