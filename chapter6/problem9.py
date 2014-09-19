#Write a function permute to compute all possible permutations of elements of a given list.
import itertools
def permute(x):
	return itertools.permutations(x)
print list(permute([1,2,3]))
