class Book:

    def __init__(self):
        self.__price = 0

    def setprice(self,price):
        self.__price = price

    def getprice(self):
        return self.__price

obj = Book()
obj.setprice()
print("Book Price is :",obj.getprice())
        


