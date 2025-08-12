def ChkPrime(num):
    if num <= 1:
        return False
    for i in range (2,num):
        if (num %i ==0):
            return False
    return True
    

def main():
    Data = []
    size = int(input("enter number of elements"))

    print("Enter elements")
    for i in range(size):
        num = int(input())
        Data.append(num)
    
    print("Input Data",Data)

    Fdata =list(filter(ChkPrime,Data))
    print("prime no's are",Fdata)
if __name__ == "__main__":
    main()
