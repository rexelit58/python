matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0][1])
#modifying the value
matrix[0][1]=20
print(matrix[0][1])
#iterating all the items in a list
for row in matrix:
    for item in row:
        print(item)
