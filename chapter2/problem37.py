#Write a function valuesort to sort values of a dictionary based on the key.
import sys
def valuesort(x):
	return [values for keys, values in sorted(x.items())]
print valuesort({'x':1,'y':2,'a':3})

         
