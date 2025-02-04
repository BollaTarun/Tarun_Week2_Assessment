
class Student:

    def __init__(self,name,roll_number):
        self.name=name
        self.roll_number=roll_number

    def student_details(self):
        print(f"Student Details :\nName\t: {self.name}\nRoll No : {self.roll_number}")

S=Student("Krish","108")
S.student_details()

K=Student(input("Enter the Student Name :\n"),int(input("Enter the Student Roll No :\n")))
K.student_details()