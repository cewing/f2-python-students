#!/usr/bin/env python

"""
breakme.py

Examples of the most common Exceptions.

There are, of course almost infinite ways to do this!
"""

def name_error():
   return name_errror() # A typo is a common source of a name error.

def type_error(i, s):
	return i + s # if you pass and int and string in, you'll get a Type Error

def attribute_error(i):
	i.sort() # pass in anything without a sort method, like a number or string
	print i

def syntax_error():
    a = 5 + + 4

# call the functions to get the errors:
# the interpreter stops when you hit an error, so you need to uncomment one at a time.

# name_error()

# type_error(3, '4')

attribute_error('3.1458')


