"""
This module describes the use of function and classes
"""
print("******** Start of module ", __name__, "********")



def this_is_a_function_with_two_parmeters(parameter0, second):
    # indentation is essential: is shows scope
    print("parameter0:{}, second:{}".format(parameter0, second))

    local_variable = 2

    print("This build in function shows the interal variables available in this function:\n{}".format(locals()))
    print("end of function")




this_is_a_function_with_two_parmeters(2, "Second parm")


class SimpleClass:
    "This is a simple class with a simple doc string"

    static_int_with_class_scope = 4

    def __init__(self):
        "This is called when the class is initialized"
        print("this method will be executed when the class is created")
        self.dynamic_int_only_usable_after_class_is_created = 5


    def __del__(self):
        """
        In contrast with __init__, this one is rarely defined because "garbage cleanup"
        of all the variables are performed automatically. Its is only needed
        if this class used resources outside of Python that will not shut down
        when this class is shut down.
        """
        print("this one is called when the instatiation of this class goes out of scope")


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

observation="""
As said before, everything in Python is an object, which includes integers, strings, lists, dicts....
SimpleClass above, shows basic elements that are available in every object: there are:
 static variables: variables that are defined outside of the methods
"""

print(SimpleClass.static_int_with_class_scope)
SimpleClass.static_int_with_class_scope = 10
print("mew value" , SimpleClass.static_int_with_class_scope)
sc = SimpleClass()
sc.show_locals()
print("\n And now we are going to dynamically expand the instance 'sc' of class 'SimpleClass' ")
sc.added_method = this_is_a_function_with_two_parmeters
sc.show_locals()
sc.added_method("a",1)

print("To be clear, new instande of Simple Class will not have 'added_method'")
sc2 = SimpleClass()
sc2.show_locals()


print("******** End  of module ", __name__, "********")
