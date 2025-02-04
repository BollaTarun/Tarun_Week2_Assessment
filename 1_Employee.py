
class Employee:

    def __init__(self,name,id,department):
        self.name=name
        self.id=id
        self.department=department

    def display(self):
        print(f"Employee Details:\nName\t: {self.name}\nId\t: {self.id}\nDepartment : {self.department}")

emp=Employee(input("Enter the Employee Name :\n"),int(input("Enter the Employee ID :\n")),input("Enter the Department of the Employee :\n"))
emp.display()

emp1=Employee("Raj",33,"IT")
emp1.display()