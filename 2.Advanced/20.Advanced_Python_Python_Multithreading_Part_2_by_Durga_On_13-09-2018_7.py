from threading import *
import time


def display():
    print(current_thread().name, '........started')
    time.sleep(3)
    print(current_thread().name, '........ended')


t1=Thread(target=display,name='ChildThread-1')
t2=Thread(target=display,name='ChildThread-2')
t1.start()
t2.start()
print(t1.name,' is Alive:',t1.isAlive())
print(t2.name,' is Alive:',t2.isAlive())
time.sleep(10)
print(t1.name,' is Alive:',t1.isAlive())
print(t2.name,' is Alive:',t2.isAlive())


