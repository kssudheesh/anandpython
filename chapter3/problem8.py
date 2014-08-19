#Write a program links.py that takes URL of a webpage as argument and prints all the URLs linked from that webpage.
import sys
import urllib
import re
x = urllib.urlopen(sys.argv[1])
lines = re.findall(r'http://\w+\S*',x.read())
for line in lines:
                print line

