# Multiple Inheritance:
class P1:
    def m1(self):
        print("P1 method")


class P2:
    def m1(self):
        print("P1 method")


class C(P1, P2): pass


c = C()
c.m1()