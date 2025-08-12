
Multiply = lambda x, y: x * y

def reducex(Task, Values):
    Result = 1
    for no in Values:
        Result = Task(Result, no)
    return Result 

def main():
    Data = []
    size = int(input("enter number of elements"))

    print("Enter elements")
    for i in range(size):
        num = int(input())
        Data.append(num)
    
    print("Input Data",Data)

    Rdata = reducex(Multiply, Data)
    print("Reduce Output:", Rdata)

if __name__ == "__main__":
    main()
