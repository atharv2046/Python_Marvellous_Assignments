def main():
    no1 = float(input("enter number 1:"))
    no2 = float(input("enter number 2:"))
    no3 = float(input("enter number 3:"))

    if no1 >= no2:
        if no1 >= no3:
            largest = no1
        else:
            largest = no3
    else :
        if no2>= no3:
            largest = no2
        else:
            largest = no3
    print("largest number is :",largest)

if __name__ =="__main__":
    main()
