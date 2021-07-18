from threading import *
mt=current_thread()
# checking weather the thread is a daemon or not
print(mt.isDaemon())
print(mt.daemon)