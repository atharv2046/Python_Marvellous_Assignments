
def Add(no1 ,no2):
    result = no1 + no2
    return result

def main():

    print("Enter first number :")
    no1 = int(input())

    print("Enter Second number :")
    no2 = int(input())

    result = Add(no1,no2)
    print("Additon is :",result)


if __name__ == "__main__":
    main()

