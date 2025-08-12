class Rectangle :

    def __init__(self,Length ,Breadth):
        self.Length = Length
        self.Breadth = Breadth

    def Area(self):
        Area = self.Length *self.Breadth
        print("Area is :",Area)

    def Parameter(self):
        Parameter = 2 * (self.Length+ self.Breadth)
        print("Parameter is :",Parameter)


Obj1 = Rectangle(12,8)
Obj1.Area()
Obj1.Parameter()

    

