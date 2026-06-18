"""
==> function without parameters and without return type
This type of function does not take any input and does not return any output.
It is used to perform a specific task or action without needing any data from the caller.
"""
def greet():
    print("Hello, welcome to Python programming!")


"""
==> function with parameters and without return type
This type of function takes input parameters but does not return any output.
It is used to perform a specific task or action based on the input provided by the caller.
"""
def greet_user(name):
    print("Hello " + name + ", welcome to Python programming!")


"""
==> function without parameters and with return type
This type of function does not take any input but returns a value to the caller.
It is used to perform a specific task or action and provide the result back to the caller.
"""
def get_year():
    year = 2026
    return year



"""
==> function with parameters and with return type
This type of function takes input parameters and returns a value to the caller.
It is used to perform a specific task or action based on the input provided by the caller and
provide the result back to the caller.
"""
def add(num1, num2):
    result = num1 + num2
    return result


















"""
==> function with parameters and without return type
This type of function takes input parameters but does not return any output.
It is used to perform a specific task or action based on the input provided by the caller.
"""
def greet_user(name):
    print("Hello " + name + ", welcome to Python programming!")


# greet()

# greet_user("Kavya")

# current_year = get_year()
# print(current_year)


sum = add(5,10)
print("sum of the given two numbers = ", sum)