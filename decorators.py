
print(f"\n\n******** starting module {__file__} as {__name__} *************\n\n")



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
    print(f"second function: {a}")
    return a()


second_function(print)
print("CALLING SINGLE FUNCTION:")
single_function()

print("same as if ")
my_decorator(single_function())



def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice


@do_twice
def greet(name):
    print(f"Hello {name}")


greet("me")



print(f"\n\n******** Ending module {__file__} as {__name__} *************\n\n")
