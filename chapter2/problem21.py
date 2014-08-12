#Write a program wrap.py that takes filename and width as aruguments and wraps the lines longer than width.
import sys
l = int(sys.argv[2])
f = open(sys.argv[1]).readlines()
for i in f:
	for j in range(0,len(i),l):
		print i[j:j+l]
	
