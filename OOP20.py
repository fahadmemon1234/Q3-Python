# 20. Creating a Custom Exception
# Assignment:
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.


class InvalidAgeError(Exception):
    def __init__(self, message):
        self.message = message

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18")
    return True

try:
    age = int(input("Enter your age: "))
    check_age(age)
    print("Age is valid")
except InvalidAgeError as e:
    print(e)



