l = [x*x for x in range(10000000000000000000000000000000000000000000000000000)]
# print(l) # we get the memory error
# To solve this we can go for decorator
while True:
    print(next(l))
