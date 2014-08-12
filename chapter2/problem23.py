#Write a program center_align.py to center align all lines in the given file.
import sys
f = open(sys.argv[1]).readlines()
for i in f:
	print i.center(60,' ')
