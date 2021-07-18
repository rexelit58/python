# Hierarchical Inheritance:
class P:
    def m1(self):
        print("Parent method")


class C1(P):
    def m2(self):
        print("Child method")


class C2(P):
    def m3(self):
        print("Sub Child method")


c = C1()
c.m1()
c.m2()