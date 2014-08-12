#Write a function factorial to compute factorial of a number. Can you use the product function defined in the previous example to compute factorial?

def factorial(x):
        j = 1
        for i in range(1,x+1):
                j = j * i
        return j

print factorial(4)

