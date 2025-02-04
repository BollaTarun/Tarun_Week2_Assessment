
class Animal:

    def speak(self):
        return "Animal Sounds"

class Dog(Animal):

    def speak(self):
        return "Bark"

class Cat(Animal):

    def speak(self):
        return "Meow"

C=Cat()
print(C.speak())

D=Dog()
print(D.speak())
