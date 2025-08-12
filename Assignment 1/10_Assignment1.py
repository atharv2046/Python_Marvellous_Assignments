def name_length(name):
    return len(name) 

def main():
    user_name = input("Enter the name: ")
    length = name_length(user_name)

    print("The length of your user name is ",length)
    


    

if __name__ == "__main__":
    main()