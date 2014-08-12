#Write a function invertdict to interchange keys and values in a dictionary. For simplicity, assume that all values are unique.
def invertdict(x):
	i = {}
	for keys,values in x.items():
		i[values] = keys
	return i
print invertdict({'x':1,'y':2,'z':3})
