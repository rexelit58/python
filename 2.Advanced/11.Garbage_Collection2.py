import time


class Test:
    def __init__(self):
        print("Object initialization....")

    def __del__(self):
        print("Fulfilling last wish and performing cleanup activities.....");


t1 = Test()
t1 = None
# Garbage collector won't wait for even sleep function.before itself it'll destroy the object
time.sleep(10)
print("End of the application")
