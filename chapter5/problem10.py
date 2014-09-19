#Implement a function izip that works like itertools.izip.
def izip(x,y):
	if len(x) < len(y):
		n = len(x)
	else:
		n = len(y)
	for i in range(n):
		yield (x[i],y[i])
zipped = izip([1,2,3,4],[5,3,8])
for values in zipped:
	print values
