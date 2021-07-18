from threading import *


def display():
    print('Child thread name:',current_thread().getName())


t = Thread(target=display)  # Creation of Thread object to execute display
t.start()

print('parent thread name:',current_thread().getName())