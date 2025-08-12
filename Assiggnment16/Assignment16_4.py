def main():
   filename = input("enter a file name you want to create :")
   fobj = open(filename,"w")

   for i in range(1,11):
         num = input("Enter number " + str(i) + ": ")
         fobj.write(num +"\n")
   



if __name__ == "__main__":
    main()