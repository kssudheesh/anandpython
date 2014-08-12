#Write a python function parse_csv to parse csv (comma separated values) files.
import sys
def parse_csv(x):
	f = open(x).readlines()
	print [[i.split(',')] for i in f]
parse_csv(sys.argv[1])
