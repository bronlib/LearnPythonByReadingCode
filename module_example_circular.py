print("******** Start of module ", __name__, "********")

print(".. now starting in another module, but the following will be ignored ")
import module_string_study

print(" now going for a circular import by importing basic_python ")
import read_and_run_this_file_first
print(" but it is already loaded, so it will nog be loaded again. ")
print(" but note that it is just partially loaded because execution is now here.")

NEXT_TO_SAY = """so, note that circular imports don't crash as long as anything which 
is asked to be executed has either already been executed or loaded into memory
so it is possible to, from here, to access all variables, classes and functions
that have been either executed or loaded into memory up to the point of the import of this module in 
basic_python
"""
print(NEXT_TO_SAY)

read_and_run_this_file_first.this_is_a_function_with_two_parmeters("string", 100)


#the following commented out code will cause a crash if executed:
#basic_python.cannot_be_executed_in_another_module()
TO_REALIZE="""
the above commented out code will cause an "attribute error" because in the execution stack
the module basic_python does not yet posess the function cannot_be_executed_in_another_module()
It will just after this module has been executed and execution continues in the module
basic_python.  Through execution, variables, classes and functions may be added to
any classes or functions that have been executed or loaded into memory. 
"""
print(TO_REALIZE)

a = read_and_run_this_file_first.SimpleClass()
print("\n")
a.show_locals()
print("now a new local will be externally added to the instantiated class ")
a.new_local = 4
a.show_locals()
print("\n")

read_and_run_this_file_first.SimpleClass.new_class_variable = "WOW"

print(vars(read_and_run_this_file_first.SimpleClass))


print(vars(read_and_run_this_file_first.this_is_a_function_with_two_parmeters))
read_and_run_this_file_first.this_is_a_function_with_two_parmeters.its_first_static_variable = "My first"
print(vars(read_and_run_this_file_first.this_is_a_function_with_two_parmeters))


def function_here():
    a = 6
    print(vars())

function_here()



print("The internal variable of this module, __name__ is {}".format(__name__))

print("******** End  of module ", __name__, "********")

if __name__ == "__main__":


    print("If this module is the first to be executed, it becomes the 'main' module and its variable \
__name__ will have the value __main__. Otherwise, this module was just included by another module. in which case \
__name__ will be the file name of the module.")