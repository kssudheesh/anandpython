#Write a function dups to find all duplicates in the list.
def dups(x):
        y = []
        z = []
	for i in x:
                if i not in y:
                        y.append(i)
		else:
			z.append(i)
        return z
print dups([1, 2, 1, 3, 2, 5])

