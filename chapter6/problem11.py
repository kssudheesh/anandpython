#Write a function vectorize which takes a function f and return a new function, which takes a list as argument and calls f for every element and returns the result as a list.
def len(x): 
	i = 0
	for a in x:
		i = i+1
	return i
def square(x): return x*x
def vectorize(f):
    a = []
    def g(x):
        for i in x:
            a.append(f(i))
        return a
    return g
g = vectorize(square)
print g([1,2,3])
g = vectorize(len)
print g(['hello','world'])
g = vectorize(len)
print g([[1,2],[2,3,4]])

