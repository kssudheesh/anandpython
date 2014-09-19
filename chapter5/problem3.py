#Write a function findfiles that recursively descends the directory tree for the specified directory and generates paths of all the files in the tree.
import sys
import os
def findfiles(x):
	for root,dirs,files in os.walk(x):
		for name in files:	
			yield os.path.join(root,name)
for i in findfiles(sys.argv[1]):
	print i

