class Student:
    ''' This class is developed by Durga for Demo purpose '''

    def __init__(self):
        print(id(self))


# self is nothing but an constructor
# id function print the object address
s = Student()
print(id(s))


class Employee:
    def __init__(self, a, b, c, d):
        self.eno = a
        self.ename = b
        self.esal = c
        self.eadd = d

    def info(self):
        print('*' *20)
        print("Employee Number:", self.eno)
        print("Employee Name:", self.ename)
        print("Employee Salary:", self.esal)
        print("Employee Address:", self.eadd)


e1 = Employee(1,"223","2233","223")
e1.info()
