#Write a program wget.py to download a given URL. The program should accept a URL as argument, download it and save it with the basename of the URL. If the URL ends with a /, consider the basename as index.html.
import os
import urllib
import sys
def wget(x):
	a = os.path.basename(x)
	if a == "":
		urllib.urlretrieve(x,"index.html")
	else: 
		urllib.urlretrieve(x,a)
wget(sys.argv[1])

