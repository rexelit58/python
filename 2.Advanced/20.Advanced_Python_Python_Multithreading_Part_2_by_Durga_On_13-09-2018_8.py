from threading import *
import time
def display():
    for i in range(10):
        print('Seetha Thread')
        time.sleep(3)
t=Thread(target=display)
t.start()
# specifying the waiting time
t.join(5)
for i in range(10):
    print('Rama Thread')