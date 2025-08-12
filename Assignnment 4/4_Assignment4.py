ChkEven = lambda no : (no%2 == 0)
Square = lambda no : no*no
Sum = lambda a,b : a+b



def filterx(Task, Values):
    Result = []
    for no in Values:
        if Task(no):
            Result.append(no)
    return Result

def mapx(Task, Values):
    Result = []
    for no in Values:
        Result.append(Task(no))
    return Result  

def reducex(Task, Values):
    Result = 0
    for no in Values:
        Result = Task(Result, no)
    return Result  

def main():
    Data = []
    print("No of elements:")
    size = int(input())

    print("Enter the numbers:")
    for i in range(size):
        num = int(input())
        Data.append(num)

    print("Input Data:", Data)

    Fdata = filterx(ChkEven, Data)
    print("Filter Output:", Fdata)

    Mdata = mapx(Square, Fdata)
    print("Map Output:", Mdata)

    Rdata = reducex(Sum, Mdata)
    print("Reduce Output:", Rdata)

if __name__ == "__main__":
    main()
