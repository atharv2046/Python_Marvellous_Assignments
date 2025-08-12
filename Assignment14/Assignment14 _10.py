class Employee:
    def __init__(self, name, salary, department):
        self.name = name            
        self._department = department  
        self.__salary = salary         

    def display(self):
        print(f"Name: {self.name}, Department: {self._department}, Salary: {self.__salary}")

obj= Employee("Amit", 60000, "IT")
obj.display()
