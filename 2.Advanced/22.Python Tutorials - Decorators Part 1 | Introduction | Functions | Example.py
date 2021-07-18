def str_upper(func):
    def inner():
        str1 = func()
        return str1.upper()
    return inner

@str_upper
def print_str():
    return "good morning"

print(print_str())