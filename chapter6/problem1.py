#Implement a function product to multiply 2 numbers recursively using + and - operators only.
import sys
def product(x,y):
	if y == 0:
		return 0
	else:
		p = x + product(x,y-1)
		return p
print product(int(sys.argv[1]),int(sys.argv[2]))
