#Write a function profile, which takes a function as argument and returns a new function, which behaves exactly similar to the given function, except that it prints the time consumed in executing it.
def fib(n):
    if n is 0 or n is 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
def profile(f):
    	def g(x):
        	import time
        	start_time = time.clock()
		value = f(x)
                return time.clock() - start_time
	return g
fib = profile(fib)
print fib(25)
