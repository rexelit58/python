class Student:
    '''This class is developed '''
    def __init__(self,rollno,name):
        self.rollno = rollno
        self.name = name

    def talk(self):
        print("Hell my name is:",self.name)
        print("My rollno is:",self .rollno)


s =  Student(100,"kavi")
print(s.name)
print(s.rollno)
s.talk()
