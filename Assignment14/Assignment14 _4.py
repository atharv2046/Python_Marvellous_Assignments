class student :
    School_name = "VNV School"

    def __init__(self,name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print("Student Name :",self.name)
        print("Student Roll No is :",self.roll_no)
        print("School Name is ",student.School_name)

Student1 = student("Atharv ", 10)
Student1.display()

student.School_name = "XYZ School "
Student1.display()
        