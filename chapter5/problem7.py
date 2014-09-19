#Write a program split.py, that takes an integer n and a filename as command line arguments and splits the file into multiple small files with each having n lines.
import sys
i = 0
j = 0
def reader(x):
	for line in open(x).readlines():
		yield line
def newfile(n,x):
	global i,j
	if x.strip() != '':
		f = open('%d.txt'%j,'a')
		f.write(x)	
		f.close()
		i = i + 1
		if i % n == 0:
			j += 1
			i = 0		
n = int(sys.argv[1])
x = sys.argv[2]
lines = reader(x)
for line in lines:
	newfile(n,line)

