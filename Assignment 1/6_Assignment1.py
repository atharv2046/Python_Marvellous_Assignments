def ChkNumber(no):
    if no>0:
        print("The number  is positive")
    elif no<0:
        print("The Number is negative")
    else:
        print("The Number is zero")



def main():
    number = float(input("Enter a number :"))

    result = ChkNumber(number)

    print(result)



if __name__ == "__main__":
    main()