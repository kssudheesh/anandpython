#Write a program to count frequency of characters in a given file. Can you use character frequency to tell whether the given file is a Python program file, C program file or a text file?
import sys
def character_frequency(words):
        frequency = {}
        for w in words:
		for i in w:        
        		frequency[i] = frequency.get(i, 0) + 1
        return frequency
def read_words(filename):
    return open(filename).read().split()
def main(filename):
        frequency = character_frequency(read_words(filename))
        for character, count in sorted(frequency.items()):
                print character, count
main(sys.argv[1])

