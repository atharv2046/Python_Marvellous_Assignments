def Add_factor(n):
    Add = 0
    for i in range(1,n):
        if n%i ==0:
            Add += i
    return Add

    
   

def main():
    print("Enter a number :")
    number = int(input())

    Factor = Add_factor(number)

    print("Sum of FActors is :",Factor)



if __name__== "__main__":
    main()