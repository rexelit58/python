numbers=[5,3,5,6,7]
#inserting the element at end of the list
numbers.append(20)
print(numbers)
#inserting in specific index
numbers.insert(2,12)
print(numbers)
#removing the element
numbers.remove(20)
print(numbers)
#removing all the elements in the list
#numbers.clear()
#print(numbers)
#removing the last item in the list
numbers.pop()
print(numbers)
#getting the index of the value
print(numbers.index(3))
#checking the value existence
print(50 in numbers)
#counting the number of existense of the element
print(numbers.count(5))
#sorting the list
numbers.sort()
print(numbers)
#sorting the list in descending order
numbers.reverse()
print(numbers)
#copying the list
numbers2=numbers.copy()
print(numbers2)





