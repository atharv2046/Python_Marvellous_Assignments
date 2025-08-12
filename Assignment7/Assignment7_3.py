CheckEven = lambda no: (no % 2 == 0)

def main():
    Data = []
    size = int(input("enter number of elements"))

    print("Enter elements")
    for i in range(size):
        num = int(input())
        Data.append(num)
    
    print("Input Data",Data)

    Fdata =list(filter(CheckEven,Data))
    print("Doubled Data",Fdata)
if __name__ == "__main__":
    main()
