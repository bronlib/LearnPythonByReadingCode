


def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Bob")


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

# my_function_call = my_dectorator(single_function)

@my_decorator
def single_function():
    print("In single function")


def second_function(a):
    print("second function")

#
# second_function()
# print("CALLING SINGLE FUNCTION:")
# single_function()
#
# print("same as if ")
# my_decorator(single_function())
#

@second_function
def hi():
    print("hi")

hi()
# #
# # def do_twice(func):
# #     def wrapper_do_twice(*args, **kwargs):
# #         func(*args, **kwargs)
# #         func(*args, **kwargs)
# #     return wrapper_do_twice
# #
#
# @do_twice
# def greet(name):
#     print(f"Hello {name}")
#
#
# greet("me")