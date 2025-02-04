
class Electronics:

    def requirement(self):
        print("Runs on Electricity.")

class MobilePhone(Electronics):

    def size(self):
        print("Easy to carry.")

class SmartPhone(MobilePhone):

    def usage(self):
        print("Easy to handle.")

print("Smart Phone :")   
S=SmartPhone()
S.requirement()
S.size()
S.usage()

print("Mobile Phone :")
M=MobilePhone()
M.requirement()
M.size()

print("Electronic Devices :")
E=Electronics()
E.requirement()
