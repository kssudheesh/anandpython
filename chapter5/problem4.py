#Write a function to compute the number of python files (.py extension) in a specified directory recursively
import sys
import os
def countpy(x):
        for root,dirs,files in os.walk(x):
                for name in files:
                        if '.py' in name:
				yield name
count = 0
names = countpy(sys.argv[1])
for i in names:
	count += 1
print count
	
	

