# 11. Class Methods
# Assignment:
# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.


class Book:
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.total_books += 1

    @classmethod
    def increment_book_count(cls):
        cls.total_books +=1

b1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
b2 = Book("To Kill a Mockingbird", "Harper Lee")

print(f"Total books: {Book.total_books}")

Book.increment_book_count()

