# reading a data from one file and writing it into another file
f1=open('input.txt')
f2=open('output.txt','w')
f2.write(f1.read())
f1.close()
f2.close()
print('Data copied from input.txt to output.txt')