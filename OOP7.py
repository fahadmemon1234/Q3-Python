# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.


class Employee:

    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN: {self.__ssn}")

e1 = Employee("Fahad", 10000, 123456789)

print(f"Public Name: {e1.name}")
print(f"Protected Salary: {e1._salary}")

try:
    print(f"Private SSN: {e1.__ssn}")
except AttributeError as e:
    print("Private variable cannot be accessed directly")

