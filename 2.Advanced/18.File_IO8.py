f=open('abc.txt')
lines=f.readlines()
print(lines)
for line in lines:
    print(line,end='')