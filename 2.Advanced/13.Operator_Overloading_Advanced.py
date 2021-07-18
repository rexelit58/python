class Book:
    def __init__(self, pages):
        self.pages = pages

    def __str__(self):
        return 'The number of pages:' + str(self.pages)

    def __add__(self, other):
        total = self.pages + other.pages
        b = Book(total)
        return b

    def __mul__(self, other):
        total = self.pages * other.pages
        b = Book(total)
        return b


b1 = Book(100)
b2 = Book(100)
b3 = Book(100)
b4 = Book(100)

print(b1 + b2 + b3 + b4)
