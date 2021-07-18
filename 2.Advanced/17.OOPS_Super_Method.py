class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, name, age, rollno, marks):
        super().__init__(name, age)
        self.rollno = rollno
        self.marks = marks

    def display(self):
        super().display()
        print("Roll Number:", self.rollno)
        print("Marks:", self.marks)


class Teacher(Person):
    def __init__(self, name, age, salary, subject):
        super().__init__(name, age)
        self.salary = salary
        self.subject = subject

    def display(self):
        super().display()
        print("Sala ry:", self.salary)
        print("Subject:", self.subject)


s = Student("kavi", 23, 101, 90)
p = Teacher('Durga', 62, 10000, 'Python')

s.display()
p.display()
