fname=input('Enter the file name:')
f=open('input\\'+fname,'w')
feedback=input("Enter the feedback:")
f.write(feedback)
f.close()