print("******** Start of module ", __name__, "********")

"""
A list in Python is litterly a list of objects. The objects may be of different 
types. 
"""
c =["hello", 1]
#c = "hello"

a = [1, 2,3,4,5, c]
print(a)
b = a.copy()
b.append(6)
print("b is ",b)
print("a is ",a)

def change(c):
    c.append(7)


change( b)

print("b is ",b)
print("a is ",a)

print("b[5]", b[5])
b[5] += "4"

print("a is ",a)
print("b is ",b)




print("******** Start of module ", __name__, "********")



