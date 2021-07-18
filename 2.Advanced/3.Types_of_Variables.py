class Student:
    cname = "DURGASOFT"

    def __init__(self, x, y):
        count = 0
        self.name = x
        self.rollno = y
    # Instace method
    def display(self):
        print("Hello myself is:", self.name)
        print("My Rollno is:", self.rollno)

    # declaring class level methods using @classmethod decorator
    @classmethod
    def getCollegeName(cls):
        print('College name:', cls.cname)

    # this type of method can be access through both way(available in class level and object level)
    @staticmethod
    def findAverage(x, y):
        print("Average:", (x + y) / 2)


s1 = Student("kavi", 100)
s2 = Student("arasan", 200)
s3 = Student("kling", 103)
Student.getCollegeName()
# static methods
s1.findAverage(100,2)
Student.findAverage(1000,100)

