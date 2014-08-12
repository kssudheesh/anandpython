#Implement a function product, to compute product of a list of numbers
def product(x):
	j = 1
	for i in x: 
		j = j * i
	return j
		
print product([1, 2, 3, 4])
