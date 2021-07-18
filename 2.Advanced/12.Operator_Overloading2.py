class Book:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self, other):
        return self.pages+other.pages

    def __sub__(self, other):
        return  self.pages-other.pages

    def __mul__(self, other):
        return self.pages*other.pages

b1=Book(300)
b2=Book(200)
print(b1+b2)
print(b1-b2)
print(b1*b2)
