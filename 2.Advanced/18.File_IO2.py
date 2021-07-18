# write mode
# f=open('abc.txt','w')
# To read and then write
#f=open('abc.txt','r+')
# To write then read .It will overwrite exiting data
#f=open('abc.txt','w+')
# To x--->exclusive mode
f=open('abc1.txt','x')

print("File Name:",f.name)
print("File Mode:",f.mode)
print("Is File Readable?:",f.readable())
print("Is File Writable?:",f.writable())
print("Is File Closed:",f.closed)
f.close()
print("Is File Closed?",f.closed)