"""
This module is a brief introduction to Python's arithmetic
"""
print("\n******** Start of module ", __name__, "********\n")

INTEGER_NUMBER = 3
FLOAT_NUMBER = 0.3
ADDING_NUMBERS = 4 + 6
ADDING_TO_INTEGER = INTEGER_NUMBER + ADDING_NUMBERS


print("this is a simple way to print an integer")
print(INTEGER_NUMBER)
print("Or can contain", FLOAT_NUMBER, "and the result of the addition:", ADDING_NUMBERS,
      "\nand the result of", ADDING_TO_INTEGER, "noting that each ',' is replaced by a single space")


print("A nicer print result of numbers can be achieved by using the method 'format'",
      "\nwhen printing strings")
print("INTEGER_NUMBER={} and nicely with 4 spaces:{:4d}.".format(INTEGER_NUMBER, ADDING_TO_INTEGER))
# Or
ASSING_STRING_FIRST_TO_THIS_VARIABLE = "float={:2.4f}, decimal={:04d}, as string={:s}".format(FLOAT_NUMBER,
                                                                                ADDING_NUMBERS, "Like a string")
# then
print(ASSING_STRING_FIRST_TO_THIS_VARIABLE)

"""
There is also subtraction
"""
res = 4 - 5
print("result:", res)
res -= 10
print("res is now further decremented:{:d}".format(res))

"""
multiplication

integer division
real division
module
"""




print("\n******** End   of module ", __name__, "********\n")
