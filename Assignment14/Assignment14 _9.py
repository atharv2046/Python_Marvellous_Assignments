class product :
    def __init__(self,name, price):
        self.name = name 
        self.price = price

    def __eq__(self, value):
        return self.price == value.price
    
obj1 =product("pen",20)

obj2 = product("pencil",20)

print("Prices are equal :",obj1 == obj2)

