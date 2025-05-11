# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.

class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def display(self):
        print(f"Count: {self.count}")

c1 = Counter()

c1.increment()
c1.increment()
c1.increment()

c1.display()
