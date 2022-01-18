#Commment practice below
#comments are ignored in execution
#comments are used to document code in english

#PUT ALL IMPORT STATEMENTS AT TOP

import math

"""
this is a comment block print("test") does not print because of triple "double quotes"
"""


print("Hello World!")

#VARIABLES
x = 5 # read this as 'x is assigned 5' NOT x equals 5

# a variable stores a value
# a value has a data type
# a data type defines a range of values
# example: the int data type (short for integer) represents whole numbers

print(x)
print(type(x))

# if we want to reassign x to a different value

x = 5.5
print(type(x))

# example: the float data type(short for floating point number) represents numbers with fractional parts (DECIMALS)

x = "hello"
#example: the string data type represents a sequence of characters

print(x)
print(type(x))

x = "5"
print(x)
print(type(x))

#OPERATORS
#PEMDAS

print(4*5)

# / is floating point division (normal division)
print(5/2)
 
# // integer division
print (5//2)

# ** is exponentiation (power)
print(2**5) # if multiple **, they evaluate right to left
# we can also use the pow() function from the math module
# need to import the math module to use it
# a .py file AKA a module AKA script

print(math.pow(2, 5))