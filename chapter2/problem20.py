#implement unix command grep. The grep command takes a string and a file as arguments and prints all lines in the file which contain the specified string.
import sys
f = open(sys.argv[1],'r')
a = f.readlines()
for i in a:
	if sys.argv[2] in i:
		print i
 
