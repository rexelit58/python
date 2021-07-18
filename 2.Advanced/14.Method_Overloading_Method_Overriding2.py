class Test:
    def sum(self, a=None, b=None, c=None):
        if a != None and b != None and c != None:
            print('The sum of 3 numbers:', a + b + c)
        elif a != None and b != None:
            print("The sum of 2 numbers:", a + b)
        else:
            print("Please provide 2 or 3 arguments")


t = Test()
t.sum(10, 20, 30)
