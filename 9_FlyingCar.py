
class Car:
    
    def move(self):
        return "Moves using Wheels"
    
class Airplane:

    def move(self):
        return "Flys using Wings"

class FlyingCar(Car,Airplane):
    
    def move(self):
        return f"{Car.move(self)} and {Airplane.move(self)}"
    
F=FlyingCar()
print(F.move())

C=Car()
print(C.move())

A=Airplane()
print(A.move())