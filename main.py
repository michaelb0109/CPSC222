#Commment practice below
#comments are ignored in execution
#comments are used to document code in english

#PUT ALL IMPORT STATEMENTS AT TOP

import math
import random

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
else: # if x not equal to 5
  print ("NOT TRUE")

# we also have elif (else if) for multiple alternative if statements
# use elif with multiple if conditions to test in a row-- the first one that is true will execute

x = 5
if x < 0:
  print("x is negative")
elif x > 0: #x > 0
  print("x is positive")
else:
  print("x is 0")

  #Loops- use a loop to repeat statements
  #we have for loops and while loops in python

  # for loop structure
  # for item in sequence:
  #  body (statements we want to repeat)

my_list = [1, 2, 3, 4, 5]
for item in my_list:
  print(item)
  #strings are sequences!
for character in "gonzaga":
  print(character)

  # we can generate our own sequences
  # built in function range() generates a sequence
  # range(9) # generates a sequence [0,9)

for i in range(9):
  print(i,end= " ")
print() # EXTRA PRINT IS JUST A NEWLINE

  # range(stop) : [0,stop)
  # range(start, stop) : [start,stop)
  # range(start, stop, step) : [start,stop) going up by step (increment)

for i in range(4,9):
    print(i, end= " ")
print()

for i in range(4,9,2):
  print(i, end= " ")
print()

for i in range(8,3,-2):
  print(i, end= " ")
print()

for i in range(2,40,2):
  print(i, end= ", ")
print(i + 2)

# while loop structure
# while some condition is true:
#  body
#  progress towards your condition being false

k = 2

while (k <= 40):
  print(k,end=",")
  k += 2 #progress
print(k)

#ADVANCED LOOPS
# like if statements, we can nest loops
# use break keyword to get an early exit from a loop

""""
while True:
  user_input = input("Enter 'stop' to exit loop:")
  if user_input == "stop":
    break
"""
#FUNCTIONS
# a function is a named sequence of statements
# use functions to minimize redundant code
# write once, call multiple times
# helps with code organization

# help(print)

# examples of function calls: help(), print(), round(), int(), input(),....
# we can write our own functions
# functions take inputs (arguments in the call, parameters in the function header)
# functions produce outputs (results AKA return values)
# function structure
# def function_name(parameter list):
#    body

# body does not execute until the function is called

# example 1: no parameters (no arguments supplied when we call the function)
# and no return value
def say_hello():
    print("hello")

say_hello() # function call

"""
for _ in range(5):
    say_hello()
"""
# example 2: one parameter (one argument when we call) and no return value

def say(message):  # message is a parameter
    print(message)

say("hi there")
say(5)

# TASK: define/call a function that accepts the radius of a circle and prints out the area of that circle

def circle_area(radius):
    area = math.pi * radius ** 2
    print("area:", area)

circle_area(1.0)

# example 3: 

def circle_area2(radius):
    area = math.pi * radius ** 2
    return area

result = circle_area2(2.0)
print("result:", result)

# example 4: one parameter and two return values
def circle_area_and_circum(radius):
    area = (radius ** 2) * math.pi
    circum = 2 * math.pi * radius
    return area, circum # tuple (immutable list)

results = circle_area_and_circum(5.0)
print("results:", results[0], results[1]) # results is a tuple
result1, result2 = circle_area_and_circum(5.0) # tuple unpacking
print(result1, result2)

# RANDOM NUMBERS
# often we need a random number to simulate something or to setup the initial state for an algorithm
# import random module
# if we want the same number everytime the program is run...
random.seed(1) # constant
# 1. produces reproducable results
# 2. debugging purposes

# let's simulate rolling a 6-sided die
die_roll = random.randint(1,6) #[1, 6]
print("die_roll:", die_roll)
die_roll = random.randrange(1,7) # [1, 7]
print("die_roll:", die_roll)