#wothout considering the order of an parameter giving aruement is know as keyword argument
#keyword argument improves the readablity
def greet_user(first_name,last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome to india")


print("Start")
greet_user(last_name="arasan",first_name="kavi")
print("Finish")
