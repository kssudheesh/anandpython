#Write a program to list all the files in the given directory along with their length and last modification time. The output should contain one line for each file containing filename, length and modification date separated by tabs.
import sys
import os
a = os.listdir(sys.argv[1])
print "filename \t size \t modificationtime"
for i in a:
	print i, "\t",os.stat(os.path.abspath(sys.argv[1]+'/'+i))[6],"\t",os.stat(os.path.abspath(sys.argv[1]+'/'+i))[8]
