#functions in python are defined using the def keyword followed by the function name and parenthesis
def add_numbers (a,b):
    return a + b 

result = add_numbers(1,2)
print(result)

# assigning a default value to a function parameter
def greet(name="Jessica"):
    return f" Hello {name}"

print(greet())
print(greet("John"))

# postional and keyword arguments
def print_numbers(*args):
    for i in args:
        print(i)

print_numbers(1,2,3,4,5)