
def Search(list , num):
    count = 0
    for i in list:
        if i == num :
            count += 1
    return count



def main():
     Numbers = []
     list = int(input("how many numbers you want to add into a list ?"))
     for i in range(list):
        print("Enter a number :",i+1)
        num = float(input())
        Numbers.append(num)
     print("Enter the number :")
     num = int(input())

     result = Search(Numbers , num)
     print("freuquency of ",num, "is",result)




if __name__ == "__main__":
    main()
