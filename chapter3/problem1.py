#Write a program to list all files in the given directory.
import sys
import os
print "files in current working directory:"
print os.listdir(os.getcwd())
print "files in given directory:"
print os.listdir(sys.argv[1])
