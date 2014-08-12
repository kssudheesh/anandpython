#Write a program reverse.py to print lines of a file in reverse order.
import sys
x = reversed(open(sys.argv[1]).readlines())
for line in x:
	print line
