# Create a Student class with name, roll_number, and marks. Print student details.

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print(f"Student: {self.name}, Roll No: {self.roll_no}, Marks: {self.marks}")

s1 = Student("Aayush Raj Giri", 231005, 73)
s1.display()