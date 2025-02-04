
from abc import ABC, abstractmethod

class IShape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(IShape):

    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def calculate_area(self):
        return self.length*self.breadth

class Circle(IShape):

    def __init__(self,radius):
        self.radius=radius

    def calculate_area(self):
        return 3.14*self.radius*self.radius
    
R=Rectangle(3,4)
print("Area of Rectangle : ",R.calculate_area())

C=Circle(10)
print("Area of Circle: ",C.calculate_area())