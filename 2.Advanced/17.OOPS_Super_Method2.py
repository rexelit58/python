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
        # Easy way,Direct way-One way to call a specific class parent method
        B.m1(self)

e=E()
e.m1()


