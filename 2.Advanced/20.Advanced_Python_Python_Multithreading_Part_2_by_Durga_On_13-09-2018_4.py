from threading import *
def test():
    print('Child Thread')
t=Thread(target=test)
t.start()

# printing the identification number
print('Main Thread Identification Number:',current_thread().ident)
print('Child Thread Identification Number:',t.ident)

