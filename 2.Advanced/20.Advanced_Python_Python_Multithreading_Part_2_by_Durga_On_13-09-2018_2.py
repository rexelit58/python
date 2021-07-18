import time
from threading import Thread


def doubles(numbers):
    for n in numbers:
        time.sleep(1)
        print('Double Value:', 2 * n)


def squares(numbers):
    for n in numbers:
        time.sleep(1)
        print('Square value:', n * n)


numbers = [1, 2, 3, 4, 5, 6]
beginTime = time.time()
# single thread execution flow
# doubles(numbers)
# squares(numbers)

# Multi thread based execution flow
t1=Thread(target=doubles,args=(numbers,))
t2=Thread(target=squares,args=(numbers,))
t1.start()
t2.start()
t1.join()
t2.join()
endTime = time.time()
print('The total time taken is :', endTime - beginTime)
