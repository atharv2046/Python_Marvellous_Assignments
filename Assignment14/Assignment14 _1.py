class Emplyoee :

    def __init__(self,name ,Emp_ID,Salary):
        self.name = name
        self.Emp_ID = Emp_ID
        self.salary = Salary

    def DisplayInfo(self):
        print("Employee Name :",self.name)
        print("Employee ID :",self.Emp_ID)
        print("Employee Salary :",self.salary)

def main():
    Obj1 = Emplyoee("Rohit",101,50000)
    Obj1.DisplayInfo()


if __name__ == "__main__":
    main()




