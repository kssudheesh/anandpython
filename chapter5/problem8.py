#Write a function peep, that takes an iterator as argument and returns the first element and an equivalant iterator.
def peep(x):
	it = []
	a = x.next()
	it.append(a)
	for i in x:
		it.append(i)
	it1 = iter(it)
	return a,it1
it = iter(range(5))
x,it1 = peep(it)
print x, list(it1)
