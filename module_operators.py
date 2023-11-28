"""
Python  operators
reference: https://docs.python.org/3/reference/lexical_analysis.html#operators
"""

print("******** Start of module ", __name__, "********")


"""" 

The following tokens are operators:

+       -       *       **      /       //      %      @
<<      >>      &       |       ^       ~       :=
<       >       <=      >=      ==      !=

We will now walk them through one by one
"""

a = 1 + 1
print(f"The behavior of the + operator is always adddition:{a} = 1 + 1")

longer = "Part 1" + ", Part 2"
print(f"The exact behavior is type dependent: {longer}")

b = a - 1
print(f"The behavior of the - is always subtraction: {b}={a}-1")

c = 2 * 3
print(f"The behavior of the * is multiplication: {c}= 2 * 3")

n = 3
d = "1 2,"*n
print(f"For strings it multiplies the entire string {d} n times")

e = 2 ** 3
print(f"The behavior of the ** is power: {e}= 2**3")

f  = 5 / 2
print(f"The behavior of the / is divide resulting in a float {f}= 5/2")


print("******** End  of module ", __name__, "********")