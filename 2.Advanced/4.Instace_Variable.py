class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

    def info(self):
        self.marks = 60


s1 = Student("kavi", 101)
s1.info()
s1.age = 24
print(s1.__dict__)


s2 = Student("arasan", 103)
s2.wife = "still searching"
print(s2.__dict__)
