#Write a program to print each line of a file in reverse order.
import sys
x = open(sys.argv[1]).readlines()
for line in x:
        print line[::-1]
