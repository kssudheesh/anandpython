#Implement a program dirtree.py that takes a directory as argument and prints all the files in that directory recursively as a tree.
import sys
import os
s = "|  "
def tree(x,j=0):
	global b
	print s*j+os.path.basename(x)
	a = os.listdir(x)
	for i in a:
		b = os.path.join(x,i)
		if os.path.isdir(b): tree(b,j+1)
		elif i == a[-1]: print s*j+"`--"+i
		else: print s*j+"|--"+i
tree(sys.argv[1])
