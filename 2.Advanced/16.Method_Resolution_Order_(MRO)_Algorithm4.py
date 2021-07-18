class D:
    def m1(self):
        print("D class method")
class E:
    def m1(self):
        print("E class method")
class F:
    def m1(self):
        print("F class method")
class B(D,E):
    def m1(self):
        print("B class method")
class C(D,F):
    def m1(self):
        print("C class method")
class A(B,C):pass
a=A()
a.m1() # A+B+C+D+E+F+0


