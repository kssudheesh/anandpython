# Implement unix commands head and tail. The head and tail commands take a file as argument and prints its first and last 10 lines of the file respectively.
import sys
x = open(sys.argv[1]).readlines()
for i in x[0:10]:
	print i
for i in x[(len(x)-10):len(x)]:
	print i

