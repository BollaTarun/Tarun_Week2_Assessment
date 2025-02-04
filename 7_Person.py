
class Person:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(f"Person Details :\nName\t: {self.name}\nAge\t: {self.age}\n")
    
class Employee(Person):
    def __init__(self,name,age,id,dept,leaves):
        super().__init__(name,age)
        self.id=id
        self.dept=dept
        self.leaves=leaves
    
    def employee_details(self):
        print(f"Emp Name : {self.name}\nEmp ID\t: {self.id}\nAge\t: {self.age}\nDept\t: {self.dept}\nLeaves\t: {self.leaves}\n")

class Manager(Employee):

    def __init__(self,name,age,id,dept,leaves):
        super().__init__(name,age,id,dept,leaves)
    
    def approve_leave(self):
        if self.leaves>0:
            print("Leave Approved!!\n")
        else:
            print("Leave Not Approved!!\n")

print("Person :")
P=Person("Naveen",22)
P.display()

print("Employee :")
E=Employee("Raj",20,4,"CSM",33)
E.employee_details()

print("Manager :")
M=Manager("Dinesh",30,5,"CSM",10)
M.employee_details()
M.approve_leave()
M.display()


