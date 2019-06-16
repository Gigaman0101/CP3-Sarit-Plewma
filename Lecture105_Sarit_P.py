class Vehicle:
    licenseCode = ""
    serialCode = ""
    face = ""
    def turnOnAirConditioner(self):
        print("Turn on : Air")
class Car(Vehicle):
    def sayHello(self):
        print("Hello World")
class Pickup(Vehicle):
    def sayYes(self):
        print("Yes!!")
class Van(Vehicle):
    def sayNo(self):
        print("No!!")
class Estatecar(Vehicle):
    def sayNo(self):
        print("No!!")

car1 = Car()
car1.turnOnAirConditioner()
van1 = Van()
van1.turnOnAirConditioner()
pickup1 = Pickup()
pickup1.turnOnAirConditioner()
estatecar1 = Estatecar()
estatecar1.turnOnAirConditioner()
