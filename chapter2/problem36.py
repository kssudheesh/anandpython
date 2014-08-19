# Write a program to find anagrams in a given list of words. Two words are called anagrams if one word can be formed by rearranging letters of another. 
import itertools
def anagrams(x):
	a = [list(g) for key,g in itertools.groupby(sorted(x,key = sorted),sorted)]
	return a
print anagrams(['eat','ate','done','tea','soup','node'])
				
