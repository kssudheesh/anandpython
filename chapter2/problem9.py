#Write a function cumulative_product to compute cumulative product of a list of numbers.
def cumulative_product(x):
        pro = range(len(x))
        pro[0] = x[0]
        for i in range(1,len(x)):
                pro[i] = pro[i-1] * x[i]
        return pro
print cumulative_product([1, 2, 3, 4])
print cumulative_product([4, 3, 2, 1])

