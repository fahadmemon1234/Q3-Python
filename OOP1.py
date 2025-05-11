
# 1. Using self
# Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.



class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display_info(self):
        print(f"StudentName: {self.name}")
        print(f"Marks: {self.marks}")
        
s1 = Student("Fahad", 85)

s1.display_info()
