def ChkPrime(num):
    if num<=1:
        return True
    
    for i in range(2,num):
        if(num % i == 0):
            return False
    return True

Multiply =lambda a :a*2
Maximum = lambda a,b : a if a > b else b



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

    Fdata = filterx(ChkPrime, Data)
    print("Filter Output:", Fdata)

    Mdata = mapx(Multiply, Fdata)
    print("Map Output:", Mdata)

    Rdata = reducex(Maximum, Mdata)
    print("Reduce Output:", Rdata)

if __name__ == "__main__":
    main()
