# from functools import reduce

# filtercondition = lambda no: 70<= no <=90
# Increase = lambda no :no+10
# Multiply = lambda a,b : a*b

# def filterx(Task , Values):
#     result = []
#     for no in Values :
#         if Task (no):
#             result.append(no)
#     return result

# def mapx(Task , Values):
#     result = []

#     for no in Values:
#         result.append(Task(no))
#     return result


# def reducex(Task, Values):
#     Result = 1
#     for no in Values:
#         Result = Task(Result,no)
#     return Result

# def main():
#     List = []

    
#     size = int(input("enter the elements :"))

#     for i in range(size):
#         print("Enter a number :")
#         num = float(input())
#         List.append(num)
    
#     print("Input Data",List)

#     Fdata = filterx(lambda no: 70<= no <=90,List)
#     print("Filter count",Fdata)

#     Mdata = mapx(lambda no :no+10,Fdata)
#     print("Map Count :",Mdata)
    
#     Rdata = reducex(lambda a,b : a*b ,Mdata)
#     print("Reduce Output :",Rdata)


# if __name__ == "__main__":
#     main()


# CheckEven = lambda no: (no % 2 == 0)
# Increase = lambda no: no + 1
# Sum = lambda a, b: a + b

filtercondition = lambda no:70<= no <=90
Increase = lambda no :no + 10
Multiply = lambda a,b : a * b

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

    Fdata = filterx(lambda no: 70<= no <=90, Data)
    print("Filter Output:", Fdata)



    Mdata = mapx(lambda no :no+10, Fdata)
    print("Map Output:", Mdata)

    Rdata = reducex(lambda a,b : a*b, Mdata)
    print("Reduce Output:", Rdata)

if __name__ == "__main__":
    main()
