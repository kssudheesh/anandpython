#Write a function reverse to reverse a list. Can you do this without using list slicing?
def reverse(x):
	n = len(x)
	y = range(0, n)
	for i in range(0,n):
		y[n-(i+1)] = x[i]
	return y
print reverse([1,2,3,4])
print reverse(reverse([1, 2, 3, 4]))
