#Write a program mydoc.py to implement the functionality of pydoc. The program should take the module name as argument and print documentation for the module and each of the functions defined in that module.
import sys
from inspect import getmembers,isfunction
x = __import__(sys.argv[1])
print 'DESCRIPTION'
print x.__doc__
print 'FUNCTIONS'
functions = [i for i in getmembers(x) if isfunction(i[1])] 
for function in functions:
	print function[0]

