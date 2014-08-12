# Write a function mutate to compute all words generated by a single mutation on a given word. A mutation is defined as inserting a character, deleting a character, replacing a character, or swapping 2 consecutive characters in a string. For simplicity consider only letters from a to z.
import sys
def mutate(x,y):
	m = []
	letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#inserting a character
	for i in range(0,len(x)+1):
		for j in letters:
			a = x[:i]+j+x[i:]
			m.append(a)
#deleting a character
	for i in range(0,len(x)):
		a = x[:i]+x[i+1:]
		m.append(a)
#replacing a character
	for i in range(0,len(x)):
                for j in letters:
                        a = x[:i]+j+x[i+1:]
                        m.append(a)
#swapping two consecutive characters
	for i in range(0,len(x)):
                a = x[:i]+x[i+1:i+2]+x[i:i+1]+x[i+2:]
                m.append(a)
	
	if y in m:
		print "True"
	else: print "False" 
mutate(sys.argv[2],sys.argv[1])

