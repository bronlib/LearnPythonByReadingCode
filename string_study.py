

print("******** Start of module ", __name__, "********")


value = "While you're here, we can also learn a bit about strings"
value += "The string assigned to value has just gotten larger with this string."

single_quote = 'A string starts and stops with either single quotes, or double quotes.'
embed_single_quote = "If it starts with double quotes, a 'single quote', ' can be included and will be ignored."
embed_double_quote = 'If a string starts with single quotes, any containing "double quotes" will " be ignored. '

newline = "By placing the newline character into a string, 'backslash n': \n the string starts on the next line"
print(newline)

value += "This shows how a string can span \
lines after giving a backslash   " \
"they are also implicitly if the backslash occurs outside the quotes.\n The following will print \
 this string, which has been appended to with every += operation."

print(value)

newstring = "Strings can be added together: " + single_quote + embed_double_quote + newline + "\nTo make new strings."

print(newstring)

string_with_newlines_embedded_implicitly = """Triple quoted strings are very special strings.
All of the physical lines it takes in this file will be at least the number the of lines when printing it.
I said "at least" because, it too can explicitly contain a new line character \nWhich causes the first letter of 'Which'
to be on a new line, along with the first letter of 'to'. 
"""

print(string_with_newlines_embedded_implicitly)

print("the arguments of a print statement", "separated by commas",
      "will be printed after replacing each comma will be replaced by a space",
      "and may span multiple lines of the file, but will be a single line in the print")

print("The print statement will print the string representation of any object", 1, "in this list")

print("At the end of this module, \nthe execution will return to the",
      "module in which it was imported. \nOtherwise it will end here.")

'''
This is three single quotes
'''

a = "single string"
b = a* 3
print(b)


print("******** End   of module ", __name__, "********")

