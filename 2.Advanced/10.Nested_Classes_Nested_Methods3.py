class Test:
    def m1(self):
        def sum(a, b):
            print("First argument:", a)
            print("Second argument:", b)
            print("Sum:", a + b)
            print("The product:", a * b)
            print('*' * 20)

        sum(10, 20)
        sum(100, 200)
        sum(1000, 2000)


t = Test()
t.m1()
