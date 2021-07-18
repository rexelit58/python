# witing a array
f=open('abc.txt','w')
l=['Sunny\n','Bunny\n','Chinny\n','Vinny\n']
f.writelines(l)
f.close()
print('write operation closed')