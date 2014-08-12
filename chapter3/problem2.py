#Write a program extcount.py to count number of files for each extension in the given directory. The program should take a directory name as argument and print count and extension for each available file extension.
import sys
import os
a = os.listdir(sys.argv[1]).split('.')

 
