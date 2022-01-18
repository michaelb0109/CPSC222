#Commment practice below
#comments are ignored in execution
#comments are used to document code in english

#PUT ALL IMPORT STATEMENTS AT TOP

import math

"""
this is a comment block print("test") does not print because of triple "double quotes"
"""

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

# GETTING USER INPUT
print("What is your favorite number:")
favNum = input()
print ("THE FAV NUM IS :", favNum)
print ("FAV NUM DOUBLED IS:" , favNum * 2)
print(type(favNum))

# if we want to arithmetically double the favNum, we need to "convert" favNum to an int or float
# this is called type conversion and there are built-in functions to do this

favNumInt = int(favNum)
print ("FAV NUM DOUBLED IS", favNumInt * 2)
"""
# FORMATTING DECIMALS

# Few different ways to do this
#1. C style (old school)
print(math.pi)
print("%.2f" % (math.pi))

#2. Pythonic way (new school)
print("{:.3f}".format(math.pi))

#3. round() actually rounds the number and it can be stored as such
print(round(math.pi, 15))

# CONDITIONALS (if statements)
# if some condition (AKA boolean condition) is true, then execute some code (body of if statement)

x = 5
if x == 5:
  print("THIS IS TRUE")
  # this is the body
  #boolean evaluates to true
  # standard indentation is 1 tab = 4 spaces
else:
  print ("NOT TRUE")