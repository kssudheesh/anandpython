# Write a program that takes one or more filenames as arguments and prints all the lines which are longer than 40 characters.
import sys
def readfiles(filenames):
    for f in filenames:
        for line in open(f):
            yield line

def lengthcheck(n, lines):
    return (line for line in lines if len(line) >= n)

def printlines(lines):
    for line in lines:
        print line,

def main(n, filenames):
    lines = readfiles(filenames)
    lines = lengthcheck(n, lines)
    printlines(lines)
main(int(sys.argv[1]),sys.argv[2].split()) #give filenames as a string seperated by whitespace
