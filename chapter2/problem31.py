#Generalize the above implementation of csv parser to support any delimiter and comments.
import sys
def parse(x,y,z):
        f = open(x).readlines()
        print [i.split(str(y)) for i in f if i[0] != str(z)]
parse(sys.argv[1],sys.argv[2],sys.argv[3])

