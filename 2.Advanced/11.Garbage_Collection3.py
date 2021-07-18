import time
import sys


class Test:
    def __init__(self):
        print("Object Initialization...")


t1 = Test()
print(sys.getrefcount(t1))# output will be 2. 1st reference is self and 2 reference is t1
