f=open('abc.txt')
print("File Name:",f.name)
print("File Mode:",f.mode)
print("Is File Readable?:",f.readable())
print("Is File Writable?:",f.writable())
print("Is File Closed:",f.closed)
f.close()
print("Is File Closed?",f.closed)