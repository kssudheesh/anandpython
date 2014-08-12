#Cumulative sum of a list [a, b, c, ...] is defined as [a, a+b, a+b+c, ...]. Write a function cumulative_sum to compute cumulative sum of a list. Does your implementation work for a list of strings?
def cumulative_sum(x):
	sum= range(len(x))
	sum[0] = x[0]
	for i in range(1,len(x)):
		sum[i] = sum[i-1] + x[i]
	return sum
print cumulative_sum([1, 2, 3, 4])
print cumulative_sum([4, 3, 2, 1])
	
