from threading import *


def display():
    for i in range(10):
        print('Child Thread')


t = Thread(target=display)  # Creation of Thread object to execute display
t.start()

for i in range(10):
    print('Main Thread')