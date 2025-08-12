import os 

def main():
    filename = input("Enter File name :")

    if os.path.exists(filename):
        print(filename+"exists.")
    else:
        print(filename+"does not exist.")
        

if __name__ == "__main__":
    main()