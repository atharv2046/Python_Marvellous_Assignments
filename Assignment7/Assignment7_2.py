double = lambda x: x * 2


def main():
    Data = []
    size = int(input("enter number of elements"))

    print("Enter elements")
    for i in range(size):
        num = int(input())
        Data.append(num)
    
    print("Input Data",Data)

    Mdata =list(map(double,Data))
    print("Doubled Data",Mdata)
if __name__ == "__main__":
    main()
