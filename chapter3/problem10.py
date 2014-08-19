#Write a program myip.py to print the external IP address of the machine. Use the response from http://httpbin.org/get and read the IP address from there. The program should print only the IP address and nothing else.
import json
import urllib
print json.load(urllib.urlopen('http://httpbin.org/get'))['origin']
