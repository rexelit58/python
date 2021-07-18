from threading import *
import time


def display():
    print(current_thread().name, '........started')
    time.sleep(3)
    print(current_thread().name, '........ended')


print('The number of active Threads:', active_count())
t1=Thread(target=display,name='ChildThread-1')
t2=Thread(target=display,name='ChildThread-2')
t3=Thread(target=display,name='ChildThread-3')
t1.start()
t2.start()
t3.start()
l=enumerate()
for t in l:
    print('Thread Name:',t.name)
    print('Thread Identification Number:',t.ident)
    print()

time.sleep(10)
for t in l:
    print('Thread Name:',t.name)
    print('Thread Identification Number:',t.ident)
    print()


