"""
Python Course: Learn Python By Reading Code
"""

INTRODUCTION_WORDS="""
Python is a very descriptive and powerful computer language with a rich set of libraries covering wide set of domains.
Becuase it is usable in so many different domains, it is language many people can profit from once they learned it. 
It is the purpose of this course to get someone started on that learning path...it also attempts to lower the learning
threshold: it assumes a knowledge of English, access to a Python interpreter (www.python.org), and the understanding
of the existance of an "execution model" : (https://en.wikipedia.org/wiki/Execution_model): 

   'In computing, a programming language consists of a syntax plus an execution model. 
   The execution model specifies the behavior of elements of the language. 
   By applying the execution model, one can derive the behavior of a program 
   that was written in terms of that programming language. 
   For example, when a programmer "reads" code, in their mind, 
   they walk through what each line of code does. 
   In effect they simulate the behavior inside their mind.
   What the programmer is doing is applying the execution model to the code, 
   which results in the behavior of the code. '
 
So this course will describe the behavior of the elements of the language. First elements are identified and then their
behavior will be described. 

The first element to notice is this file. Because it contains Python code, this file is referred to as a 'module'. In the execution
model, this module is first "parsed": the file is read-in and checked for correctness. If it is correct, this file will
then be translated into "byte codes" and executed in a virtual machine. This process is very straight forward and linear,
making it easy to "read the code" and create an expectation about its behavior.

The next element to notice is a "variable". You already encountered one in the beginning of this file, and the identifier
of that variable is "INTRODUCTION_WORDS". It is a variable because it is directly followed by, perhaps the most essential element
in the Python language: the token '=' : the "assignment operator". The assignement operator assigns the variable to what is to the 
right of the '=' token. The assignment determines the variables "type" and "value". In this case the variable, whose 
identifier is "INTRODUCTION_WORDS", will be given the type "String" and whose value is all of the tokens from the start : 
the three consecutive '"' tokens to the next occurance of three consecutive '"'  tokens and ends with a newline. 

Taken together, namely the:
     -Identifier
     -the assignment operator
     -the string following it, 
     -a newline,
is an example of a 'Python Statement'; a statement is something that the Python interpreter can execute. 
The definition of a Python statement will be given later. For now it is important to understand that the resulting
'behavior' of this statement is that the identifier 'INTRODUCTION_WORDS' can now be used to represent this
string. 

The line after the end of this string is also a Python Statement: which contains the function "print" whose 
parameter is the variable 'INTRODUCTION_WORDS'. 

A function is a block of statements which is executed when called. 

In this case, the resulting behavior of the function 'print' is printing out of this string. 

Important here, is that if this module is executed, the first thing that will be seen is the printing of
the variable 'INTRODUCTION_WORDS'.
"""
print(INTRODUCTION_WORDS)

second_words="""You can now see that this module contains a second variable called "second_words", whose type is
string and value are all of the tokens between the triple '"' tokens and ends in a newline.

In Python, all "variables" are objects: they contain a set of funtions and objects. Functions belonging
to an object are referred to as the objects 'methods'.

As you can read in https://docs.python.org/3/reference/datamodel.html:

    Objects are Python’s abstraction for data. All data in a Python program is represented 
    by objects or by relations between objects. 
    (In a sense, and in conformance to Von Neumann’s model of a “stored program computer”, 
    code is also represented by objects.)

    Every object has an identity, a type and a value. 
    An object’s identity never changes once it has been created; 
    you may think of it as the object’s address in memory. 
    
The '=' operator assigns an object to an identity and the print() function prints out the contents
of that object given the objects identity. 

Another example of an object is this module. This object contains the identifier  "__name__", whose type is string and 
whose value is dependent on how the module was executed. If it was the first module to be executed, the value
will be "__main__", otherwise it will be the files' file name. The file name of this module is "read_this_file_first.py".
Another identifier of this module is __doc__. This value is also String and its value is:  

      Python Course: Learn Python By Reading Code

The idenfier "__doc__" of a module will contain a value, of the type string, if the first element in the file is a strng.
"""
print(second_words)
print(__name__)
print("start doc string", __doc__, "end doc string", "each string, after the first one will be prepended by a space.")

third_words="""
The result of the previous print statement is the printing of the text "__main__", and the next lines
will be the result of the third print statement. 

Python modules can embed an unlimited number of other Python modules via the "import" statement. It supports 
unlimited nesting, but cyclic imports (importing a file that was imported at a higher level) is forbidden and
results in an error.  Thanks to Pythons linear execution model, it is easy to predict the behavior of an 
import statement. When the execution reaches an import statement, it then searches for that file, reads it in, 
parses it and then executes it. Once that import statement is completed the execution proceeds to the next statement.

So the behavior of the following import statement will be that the file "operators_and_statements" will be searched, 
then parsed and then executed. 

...and in this course the imports are used to go into detail about the other elements of Python....
"""
print(third_words)
import module_operators_and_statements
forth_words="""

Essential to remember is that each module is loaded and executed only once, so each subsequent import statement 
of that same module will be ignored. 

So following import will be skipped.
You will see that in the print out, you will see that "Start..." and "End..." are only printed once. 
"""
print(forth_words) #This is a comment. All tokens after the hash token yp to and including the newline are skipped during excution.
import module_operators_and_statements
print("The module 'operators_and_statements' was skipped\n")
"""
.... and by the way, all of the text in a line after a '#'token are also skipped,
as the hash token marks the  start of a comment. You can see that text after the '#' after the above 'print(forth_words) ' will
not be seen in the execution of this module. 

Also this string will be skipped because it is not assigned to a variable or is a doc string.  

It is informative to execute this module in debug mode and single step through it one line at a time. 
The debugger will bring you into the modules: string_study. If you wish, you can start the execution in any of 
the modules that are included: in python, unlike many other languages, execution can start in any module: there is no 
"main" module in Python, like there is in other languages like C++. Where the execution starts is up to the user, 
and thus up to developer to inform the user which module to start with in order to give the user the 
experience the developer wants the user to have.

"""
import module_arithmetic_study
"""
Other important basic types are lists and dics
"""
import module_lists_and_dicts

INTRODUCTION_WORDS_PART2 = """...and execution proceeds.
It will not execute but load definitions: function defintions and class definitions
into memory, as source code
"""

import module_functions_and_classes


import module_yield_generators

import module_decorators

#execution will now load, parse and execute "another_module"  module for the first time

print("\n\n*** going to another_module with extra new lines ****** \n\n")



def this_is_a_function_with_two_parmeters(parameter0, second):
    # indentation is essential: is shows scope
    print("parameter0:{}, second:{}".format(parameter0, second))

    local_variable = 2

    print("This build in function shows the interal variables available in this function:\n{}".format(locals()))
    print("end of function")


class SimpleClass:
    "This is a simple class with a simple doc string"

    static_int_with_class_scope = 4

    def __init__(self):
        "This is called when the class is initialized"
        print("this method will be executed when the class is created")
        self.dynamic_int_only_usable_after_class_is_created = 5


    def a_static_method(parm):
        """This method will only access static variables and can therefore be called
        without intializing the class
        """
        print("It may access static variables: {}".format(SimpleClass.static_int_with_class_scope))
        print(f"and its parmeter: {parm}")
        return parm*SimpleClass.static_int_with_class_scope

    def show_locals(self):
        "This method shows all of the local variables"
        print("locals in this object {}".format(vars(self)))

print("Here is the result of the build-in help of simple class")
help(SimpleClass)

print("Calling without initializing (see no printout):", SimpleClass.a_static_method(2))
print("Calling directly, not in a print statement, shows the print out")
result = SimpleClass.a_static_method(4)
print(f"Here above the print-out and result ={result}")
SimpleClass().show_locals()
print("above you see the print out of the initialization process \n")


import module_example_circular

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
import module_no_circular_reference

module_no_circular_reference.function_local()

help(__name__)

if __name__ == "__main__":

    #this module is now considered fully loaded and now the circular referenced code can be executed

    module_example_circular.function_here()

    print("If this module is the first to be executed, it becomes the 'main' module and its variable \
__name__ will have the value __main__. Otherwise, this module was just included by another module. in which case \
__name__ will be the file name of the module.")