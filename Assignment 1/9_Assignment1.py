def Evennum(num):
    for i in range(2,num,2):
        print(i)

def main ():
    print("Enter a number:")
    number = int(input())

    Evennum(number)


   

if __name__ == "__main__":
    main()