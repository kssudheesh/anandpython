#Write a function lensort to sort a list of strings based on length.
def lensort(x):
	for i in range(0,len(x)):
		for j in range(i+1,len(x)):
			if len(x[i]) > len(x[j]):
				x[i],x[j] = x[j],x[i]
	return x
print lensort(['python','perl','java','c','haskell','ruby'])
