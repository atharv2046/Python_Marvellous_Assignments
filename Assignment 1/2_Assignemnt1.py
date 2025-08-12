def ChkNum(num):
    if(num % 2 ==0) :
        print("The number is Even")
    else:
        print("The number is Odd")
    

def main():
    print("Enter a number :")
    num = int(input())

    ChkNum(num)


if __name__ =="__main__":
    main()    