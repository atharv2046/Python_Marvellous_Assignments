def main():
    print("ENter a number:")
    num = int(input())
    
    for i in range(1,num+1):
        print("Multiplication table of " + str(i) + " is:")
        for index in range(1,11):
            print("(i) X (index)" "=" +str(i*index))
        print()





if __name__ == "__main__":
    main()