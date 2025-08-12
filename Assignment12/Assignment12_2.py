class Circle :
    PI = 3.14

    def __init__(self):
        self.radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.radius =float(input("Enter radius :"))

    def CalculateArea(self):
        self.Area = self.PI *self.radius*self.radius

    def CalculateCircumference(self):
        self.Circumference = 2*self.PI* self.radius

    def Display(self):
        print("Radius :",self.radius)
        print("Area :",self.Area)
        print("Circumference :",self.Circumference)

c1 = Circle()
c1.Accept()
c1.CalculateArea()
c1.CalculateCircumference()
c1.Display()