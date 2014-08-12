#What will be the output of the following program?
# output: 1 2 1 
x = 1
def f():
	x = 2
	return x
print x
print f()
print x
