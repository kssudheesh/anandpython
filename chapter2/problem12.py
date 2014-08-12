#Write a function group(list, size) that take a list and splits into smaller lists of given size.
def group(x, y):
	z = []
	j = 0
	for i in range(0,len(x)):
		if (j<len(x)):
			z.append(x[i*y:(i+1)*y])	 
			j = j + y
	return z
print group([1, 2, 3, 4, 5 ,6, 7, 8, 9, 10, 11], 3)
