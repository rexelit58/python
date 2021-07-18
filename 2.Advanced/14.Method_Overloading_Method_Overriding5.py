class P:
    def property(self):
        print("cash+land+gold+power")

    def marry(self):
        print("neha sharma")

class C(P):
    def marry(self):
        super().marry()
        print("Priyanka Arul Mohan")


c=C()
c.property()
c.marry()