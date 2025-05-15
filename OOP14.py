# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Department:
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees


class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def __str__(self):
        return f"Employee: {self.name}, Department: {self.department.name}"
    

d1 = Department("IT", [])
e1 = Employee("Fahad", d1)

print(e1)








