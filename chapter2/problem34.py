#Improve the above program to print the words in the descending order of the number of occurrences.
import sys
def word_frequency(words):
	frequency = {}
    	for w in words:
        	frequency[w] = frequency.get(w, 0) + 1
    	return frequency
def read_words(filename):
    return open(filename).read().split()
def main(filename):
	frequency = word_frequency(read_words(filename))
	for word, count in reversed(sorted(frequency.items(), key = lambda x: [1])):
        	print word, count
main(sys.argv[1])
