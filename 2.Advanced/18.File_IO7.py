# Reading a file
f=open('abc.txt')
# reading all the lines
# data=f.read()
# reading first 10 characters
#data=f.read(10)
# reading line by line.By default print method will add the /n
data=f.readline()
print(data,end='')
data=f.readline()
print(data,end='')