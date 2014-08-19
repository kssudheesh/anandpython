#Write a program to print directory tree. The program should take path of a directory as argument and print all the files in it recursively as a tree.
import sys
import os
b = "  "
def tree(x,j):
	global b
	print os.path.basename(x)
	a = os.listdir(x)
	for i in a:
		b = os.path.abspath(x+'/'+i)
		if os.path.isdir(b): tree(b,j+1)
		elif i == a[-1]: print "\--"+i
		else: print "|--"+i
tree(sys.argv[1],0)
