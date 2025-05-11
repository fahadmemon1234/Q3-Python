# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "HBL"

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def change_bank_name(cls, name):
        cls.bank_name = name

    def display_info(self):
        print(f"Bank Name: {self.bank_name}")
        print(f"Name: {self.name}")
        print(f"Balance: {self.balance}")

b1 = Bank("Fahad", 1000)

b1.change_bank_name("UBL")

b1.display_info()
