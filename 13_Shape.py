
class Shape:

    def area(self):
        pass

class Square(Shape):

    def __init__(self,side):
        self.side=side

    def area(self):
        return self.side * self.side

class Triangle(Shape):

    def __init__(self,base,height):
        self.base=base
        self.height=height
        
    def area(self):
        return 0.5 * self.base * self.height
    
T=Triangle(4,5)
print("Area of Triangle :",T.area())

S=Square(5)
print("Area of Square :",S.area())