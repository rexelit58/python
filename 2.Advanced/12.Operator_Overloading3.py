class Book:
    def __init__(self, pages):
        self.pages = pages

    def __str__(self):
        return "The number of pages :" + str(self.pages)

    def __add__(self, other):
        return self.pages + other.pages



b1 = Book(100)
b2 = Book(100)
b3 = Book(300)
# while printing the object  magic method __str__ will get called
print(b1)
