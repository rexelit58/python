class A:
    def m1(self):
        print("A Class method")


class B(A):
    def m1(self):
        print("B Class method")


class C(B):
    def m1(self):
        print("C Class method")


class D(C):
    def m1(self):
        print("C Class method")


class E(D):
    def m1(self):
        super(C, self).m1()


e = E()
e.m1()
