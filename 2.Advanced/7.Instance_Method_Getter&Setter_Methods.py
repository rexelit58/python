class Student:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setMarks(self, marks):
        self.marks = marks

    def getMarks(self):
        self.marks


n = int(input("Enter Number of Students:"))
for i in range(n):
    name = input("Enter Student Name:")
    marks = int(input("Enter Student Marks:"))
    s = Student()
    s.setName(name)
    s.setMarks(marks)
    print("Hi", s.getName())
    print("Your marks are :", s.getMarks())
    print('*' * 20)
