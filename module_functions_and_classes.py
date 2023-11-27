"""
This module describes the use of function and classes
"""
print("******** Start of module ", __name__, "********")




def this_is_a_function_with_two_parmeters(parameter0, second):
    # indentation is essential: is shows scope
    print("parameter0:{}, second:{}".format(parameter0, second))

    local_variable = 2

    print("This built in function shows the interal variables available in this function:\n{}".format(locals()))
    print("end of function")


this_is_a_function_with_two_parmeters(2, "Second parm")

static_int_with_class_scope= "wierd"

class SimpleClass:

    static_int_with_class_scope = 4

    def __init__(self):
        print("this function, or better called as method, will be executed when the class is created")
        self.dynamic_int_only_usable_after_class_is_created = 5
        self.static_int_with_class_scope = "Hello"
        SimpleClass.static_int_with_class_scope += 1

    def __del__(self):
        print("going out of scope")


    def static_method(self):
        global static_int_with_class_scope
        static_int_with_class_scope = "Changed "
        print("this method static if it does not access dynamic variables ")
        print("it may access static variables {}".format(SimpleClass.static_int_with_class_scope))

    def show_locals(self):
        print("locals in this object {}".format(vars(self)))

observation="""
As said before, everything in Python is an object, which includes integers, strings, lists, dicts....
SimpleClass above, shows basic elements that are available in every object: there are:
 static variables: variables that are defined outside of the methods
"""

print(SimpleClass.static_int_with_class_scope)
SimpleClass.static_int_with_class_scope = 10
print("mew value" , SimpleClass.static_int_with_class_scope)
sc = SimpleClass()
sc.static_method()
sc.show_locals()
print("\n And now we are going to dynamically expand the instance 'sc' of class 'SimpleClass' ")
sc.added_method = this_is_a_function_with_two_parmeters
sc.show_locals()
sc.added_method("a",1)

print("To be clear, new instande of Simple Class will not have 'added_method'")
sc2 = SimpleClass()
sc2.show_locals()


print("******** End  of module ", __name__, "********")
