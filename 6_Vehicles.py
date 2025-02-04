
class Vehicle:

    def __init__(self,brand):
        self.brand=brand

    def branding(self):
        print("Brand of Vehicle :",self.brand)

class Car(Vehicle):

    def __init__(self,brand):
        super().__init__(brand)
    def wheels(self):
        print("This is a 4 Wheeler Vehicle.")
    def fuel_type(self):
        print("Fuel Type can be Petrol or Diesel.")

class Bike(Vehicle):

    def __init__(self,brand):
        super().__init__(brand)
    def wheels(self):
        print("This is a 2 Wheeler Vehicle.")
    def fuel_type(self):
        print("Fuel Type is Petrol.")

class ElectricCar(Car):
    
    def __init__(self,brand):
        super().__init__(brand)
    def battery_capacity(self):
        print("Battery Capacity is 50000mAH.")

print("Vehicle :")
V=Vehicle("Hero")
V.branding()

print("\nCar :")
C=Car("Hero")
C.branding()
C.wheels()
C.fuel_type()

print("\nBike :")
B=Bike("Hero")
B.branding()
B.wheels()
B.fuel_type()

print("\nElectric Car :")
E=ElectricCar("Tata")
E.branding()
E.wheels()
E.fuel_type()
E.battery_capacity()