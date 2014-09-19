#Write a function tree_reverse to reverse elements of a nested-list recursively.
def tree_reverse(x):
	r = []
	y = x[::-1]
	for a in y:
        	if isinstance(a, list):
			r.append(tree_reverse(a))
		else:
			r.append(a)
	return r
print tree_reverse([[1,2],[3,[4,5]],6])
