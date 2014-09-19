#The built-in function enumerate takes an iteratable and returns an iterator over pairs (index, value) for each value in the source.
import itertools
def my_enumerate(x):
	return [(no,value) for no,value in itertools.izip(range(len(x)),x)]
for i,c in my_enumerate(['a','b','c']):
	print i,c
