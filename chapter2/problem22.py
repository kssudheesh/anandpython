#The above wrap program is not so nice because it is breaking the line at middle of any word. Can you write a new program wordwrap.py that works like wrap.py, but breaks the line only at the word boundaries?
import textwrap
import sys
f = open(sys.argv[1]).readlines()
for i in f:
	j = textwrap.wrap(i,30)
	for k in j:
		print k
