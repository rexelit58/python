class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __mul__(self, other):
        return self.salary * other.days


class TimeSheet:
    def __init__(self, name, days):
        self.name = name
        self.days = days

    def __mul__(self,other):
        return self.days*other.salary


e = Employee('Durga', 500)
t = TimeSheet('Durga', 25)
print('This Month Salary:', e * t)
print('This Month Salary:', t * e)
