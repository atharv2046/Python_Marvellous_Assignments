def Square_Add(num):
    for i in range(num):
        for j in range(1, num+ 1):
            print(j, end=" ")
        print()
    
def main():
    num = int(input( "Enter a number :"))

    Square = Square_Add(num)

    # print("The output is :",Square)

if __name__ == "__main__":
    main()
