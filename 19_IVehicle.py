
from abc import ABC, abstractmethod

class IVehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(IVehicle):

    def start_engine(self):
        print("Car has started.")

    def stop_engine(self):
        print("Car has Stopped.")


class Bike(IVehicle):

    def start_engine(self):
        print("Bike has started.")

    def stop_engine(self):
        print("Bike has Stopped.")

class Truck(IVehicle):

    def start_engine(self):
        print("Truck has started.")

    def stop_engine(self):
        print("Truck has Stopped.")


B=Bike()
B.start_engine()
B.stop_engine()

C=Car()
C.start_engine()
C.stop_engine()

T=Truck()
T.start_engine()
T.stop_engine()