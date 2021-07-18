class Person:
    def __init__(self,name,dd,mm,yyyy):
        self.name=name
        self.dob = self.DOB(dd,mm,yyyy)

    def display(self):
        print("Name:",self.name)
        self.dob.display()

    class DOB:
        def __init__(self,dd,mm,yyyy):
            self.dd = dd
            self.mm=mm
            self.yyyy=yyyy
        def display(self):
            print("Date of Birth:{}/{}/{}".format(self.dd,self.mm,self.yyyy))

p = Person("Sunny",25,5,2001)
p.display()
p.dob.display()