# handling method overloadin by default argument
class Test:
    def __init__(self, a=None, b=None, c=None):
        print("constructor with 0|1|2|3 arguments")


t = Test()
t = Test(10)
t = Test(10, 20)
t = Test(10, 20, 30)


# handling method overloading by any number of arguments

class Test:
    def __init__(self, *a):
        print("constructor with any number of arguments")


t = Test()
t = Test(10)
t = Test(10, 20)
t = Test(10, 20, 30)
