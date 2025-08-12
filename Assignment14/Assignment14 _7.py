class person :
    def __init__(self, name , age):
        self.name = name 
        self.age = age 

class Teacher(person):
    def __init__(self,name,age,subject,salary):
        super().__init__(name,age)
        self.subject = subject
        self.salary = salary

    def display(self):
        print("Name :",self.name , "Age :",self.age , "Subject :",self.subject , "Salary :", self.salary)
     
def main():
    obj1 = Teacher("RAM",30,"Maths",40000)
    obj1.display()
if __name__ == "__main__":
    main()