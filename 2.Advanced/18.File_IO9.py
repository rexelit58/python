f=open('abc.txt')
f.read(3)
print(f.readline())
print(f.read(4))
print('Remaining Data:')
print(f.read())