#Ex:if name is less than 2 characters long
    #name must be at least 3 characters
#otherwise if it's more than 30 characters long
    #name can be maximum of 50 characters
#otherwise
    #name looks good

name ='kavi'
if len(name) < 3:
    print("Name must be atleast 3 characters")
elif len(name)>50:
    print("Name must be maximum of 50 characters")
else:
    print("Name looks good")


