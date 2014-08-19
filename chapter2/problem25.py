#Provide an implementation for map using list comprehensions.
def map(f,x):return[f(i) for i in x]
def square(x): return x*x
print map(square, range(5))
