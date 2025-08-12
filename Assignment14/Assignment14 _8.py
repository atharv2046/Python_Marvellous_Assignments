class Vechile:
    
    def start(self):
        print("Vechile Started")

class Car(Vechile) :
     def start(self):
         super().start()
         print("Car started without keyless ignition")

obj = Car()
obj.start()