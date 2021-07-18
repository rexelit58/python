numbers=[5,3,5,6,7]
unique=[]
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)