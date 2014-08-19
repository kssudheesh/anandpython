#Write a program antihtml.py that takes a URL as argument, downloads the html from web and print it after stripping html tags.
import sys
import urllib
import os
import re
x = sys.argv[1]
a  = os.path.basename(x)
if a == "":
	y="index.html"
else:
	y = a
urllib.urlretrieve(x,y)
f = open(y,'r')
lines = re.findall(r'(>)([\w+\s]*)(<)',f.read())
for line in lines:
		print line[1]
