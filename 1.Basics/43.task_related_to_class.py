class Person:
    def __init__(self,name):
        self.name=name

    def talk(self):
        print(f"Hi,I am {self.name}")


jhon=Person("kavi")
jhon.talk()

bob=Person("Bob smith")
bob.talk()