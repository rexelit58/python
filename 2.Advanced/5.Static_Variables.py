class Student:
    cname = "INFINIT"

    def __init__(self, name, rollno):
        self.name = name;
        self.rollno = rollno


s1 = Student("kav", 101)
s2 = Student("arasan", 102)
print(s1.name, s1.rollno, Student.cname)
print(s2.name, s2.rollno, Student.cname)


# modifying static variables
class Test:
    a = 10

    def __init__(self):
        Test.a = 20

    @classmethod
    def m1(cls):
        cls.a = 30
        Test.a = 40

    @staticmethod
    def m2():
        Test.a = 50


t = Test()
t.m1()
t.m2()
t.a = 60
print(Test.a)
print(t.a)


# modify static variables ex2:
class Test:
    x = 10

    def m1(self):
        self.y = 20


t1 = Test()
t2 = Test()
t1.x = 999
t1.y = 1000
print(t1.x, t1.y)
print(t2.x, t2.y)
