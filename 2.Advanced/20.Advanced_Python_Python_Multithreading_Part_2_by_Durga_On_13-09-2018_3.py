from threading import *
print(current_thread().getName())
#changing the name of the main thread
current_thread().setName("kaviThread")
print(current_thread().getName())
# another way to change thread name
current_thread().name="demoThread"
print(current_thread().getName())


