from threading import *
def job():
    print('executed by child thread')

t=Thread(target=job)
print(t.isDaemon())# false-since main is non-daemon
t.setDaemon(True)
print(t.isDaemon())