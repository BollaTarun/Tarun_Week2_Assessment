
from abc import ABC, abstractmethod

class ICalculator(ABC):

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def subtract(self):
        pass

    @abstractmethod
    def multiply(self):
        pass

    @abstractmethod
    def divide(self):
        pass

class BasicCalculator(ICalculator):

    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        return self.a+self.b
    
    def subtract(self):
        return self.a-self.b
    
    def multiply(self):
        return self.a*self.b

    def divide(self):
        if self.b!=0:
            return self.a/self.b
        else:
            return "Division with 0 is not posible!!!"

b=BasicCalculator(int(input("Enter Number 1:\n")),int(input("Enter Number 2:\n")))
print("Sum :",b.add())
print("Difference :",b.subtract())
print("Product :",b.multiply())
print("Division :",b.divide())     