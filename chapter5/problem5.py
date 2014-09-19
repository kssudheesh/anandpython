#Write a function to compute the total number of lines of code in all python files in the specified directory recursively.
import sys
import os
def validfiles(x):
        for root,dirs,files in os.walk(x):
                for name in files:
                        if '.py' in name:
				yield os.path.join(root,name)                           
paths = validfiles(sys.argv[1])
count = 0
for path in paths:
	 count += len(open(path).readlines())
print count
	
