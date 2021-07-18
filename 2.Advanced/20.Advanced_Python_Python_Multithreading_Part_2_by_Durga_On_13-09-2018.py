# Creating a Thread by without extending Thread class
from threading import *


class Test:
    def m1(self):
        for i in range(10):
            print('Child Thread-1')


obj = Test()
t = Thread(target=obj.m1)
t.start()
for i in range(10):
    print('Main Thread-1')
