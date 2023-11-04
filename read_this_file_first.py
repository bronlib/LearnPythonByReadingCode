INTRODUCTION_WORDS="""
Python is a very descriptive and powerful computer language with a rich set of libraries covering wide set of domains.
Becuase it is usable in so many different domains, it is language many people can profit from once they learned it. 
It is the purpose of this course to getting someone started on that learning path...it also attempts lower the learning
threshold: it assumes a knowledge of English, access to a Python interpreter (www.python.org), and the understanding
of the existance of an "execution model" : (https://en.wikipedia.org/wiki/Execution_model): that there is this text, 
on the one hand and a computer on the other and what that computer will do with this code. 

This course will attempt to explain Python at different levels all at once: This file is the "top level" and is meant go
give insight to Pythons' execution model.This file includes other files which in turn give insight into the different
syntactical elements of Python. Those other files as imports in this file. 


It is usually directly interpreted, compiled to "byte codes" and executed in a virtual machine. The virtual machine used
can be other virtual machines such as Java (the compiler is called "Jython") or C# ( the compilier is called "IRONPYTHON")
but is per default "CPython". 

The execution model is very straight forward making it easy to simply "read the code" and create an expectation about 
what the result will be during execution.  Coupled with the readability of Python's simple syntax, even a person who 
is just beginning to read Python is able to formulate an expectation about what a program will do. 

Of course it is up to the Python programmer to keep his code "clean" so it "will read like well written pros" and "does
exactly what the reader expects".

I will attempt to illustrate this by introducing you to Python just by writing a "clean" Python program; giving
variables, methods, and classes expressive names and minimizing comments. 

I even began this file by assigning this text to the variable "introductionary_words" via the "=" operator, one the
first line of this file, which is called a "module" and note that a variable can only be created via an assignment
and its type is the type of the object which it is assigned to.  In Python, all "variables" are objects: they contain a set
of methods and variables. 

.... the following print statement will print these words .... And you will see them in the first lines if you 
execute this module. 

"""
print(INTRODUCTION_WORDS)

second_words="""
For example, this module is an object with an important variable "__name__", which reflects if this module is called
directly or indirectly via an "import". If it is called directly, the value of "__name__" will be "__main__", otherwise 
it will contain the modules' name, which is in this case "read_this_file_first".
"""
print(second_words)
print(__name__)   # this will be "__main__" if this file is executed

third_words="""
As mentioned, Python's execution model is litterally very straight forward. It starts by parsing the first module it is 
given, as a whole, and then executing the module by linearlly walking it through from the top to the bottom. 
When it reaches an import and then loads that file, parses it and starts executing it, and after it reaches its end,
continues after the import. Essential to remember is that each module is loaded only once, so each subsequent statement 
that instructs to import that module again will be ignored.  

"""
print(third_words)
import module_string_study

forth_words=""""
the following import will be skipped 
"""
print(forth_words)
import module_string_study
"""
.... and by the way, all of the text in a line after a '#'token is also skipped,
as the hash token marks the  start of a comment. You can see that text after the '#' after the above 'print(__name__)' will
not be seen in the execution of this module, along with these words, as they where not assigned to a variable
and printed. 

So, for example if you start by executing this module, after this file is parsed, the execution will start
with the assignment of the string above to INTRODUCTION_WORDS.
It will then: load and parse the module "module_string_study",
in which it will execute the print statement you see in there, and all subsequent statements,  and then exit the module
 and return to this module and print the "forth_words" etc... So in the execution of this module, the first and last 
 prints in the module "module_string_study" will only be seen once. 

It is also informative to execute this module in debug mode and single step through it one line at a time. 
The debugger will bring you into the modules: module_string_study. If you wish, you can start the execution in any of 
the modules that are included: in python, unlike many other languages, execution can start in any module: there is no 
"main" module in Python, like there is in other languages like C++. Where the execution starts is up to the user, 
and thus up to developer to inform the user which module to start with in order to give the user the 
experience the developer wants the user to have.

After processing this string, the interpreter will then executes the following: 
assignments of an integer, then a float and then executes an addition of numbers
and then of variables containing numbers. To explore more, then step into the module "module_arithmetic_study"
"""



import module_arithmetic_study


"""
Other important basic types are lists and dics
"""
import lists_and_dicts

INTRODUCTION_WORDS_PART2 = """...and execution proceeds.
It will not execute but load definitions: function defintions and class definitions
into memory, as source code
"""

import functions_and_classes


import yield_generators

#execution will now load, parse and execute "another_module"  module for the first time

print("\n\n*** going to another_module with extra new lines ****** \n\n")



def this_is_a_function_with_two_parmeters(parameter0, second):
    # indentation is essential: is shows scope
    print("parameter0:{}, second:{}".format(parameter0, second))

    local_variable = 2

    print("This build in function shows the interal variables available in this function:\n{}".format(locals()))
    print("end of function")


class SimpleClass:

    static_int_with_class_scope = 4

    def __init__(self):
        print("this function, or better called as method, will be executed when the class is created")
        self.dynamic_int_only_usable_after_class_is_created = 5


    def only_method(self):
        print("this method static if it does not access dynamic variables ")
        print("it may access static variables {}".format(SimpleClass.static_int_with_class_scope))

    def show_locals(self):
        print("locals in this object {}".format(vars(self)))


import example_circular

def cannot_be_executed_in_another_module():
    print("calling this function in another_module will cause a crash")




print("The internal variable of this module, __name__ is {}".format(__name__))

#however this code will crash because this module is not yet fully loaded
#example_circular.function_here()

"""
So normal practice: avoid circular references. If you include an import without
a circular reference to this module, you can use all function and classes in it
because you only depend on this imported module to be fully loaded. 
"""
import no_circular_reference

no_circular_reference.function_local()


if __name__ == "__main__":

    #this module is now considered fully loaded and now the circular referenced code can be executed

    example_circular.function_here()

    print("If this module is the first to be executed, it becomes the 'main' module and its variable \
__name__ will have the value __main__. Otherwise, this module was just included by another module. in which case \
__name__ will be the file name of the module.")