#Write a function count_change to count the number of ways to change any given amount. Available coins are also passed as argument to the function.
def count_change(a, kinds=(50, 25, 10, 5, 1)):
        """Return the number of ways to change amount a using coin kinds."""
        if a == 0:
            return 1
        if a < 0 or len(kinds) == 0:
            return 0
        d = kinds[0]
        return count_change(a, kinds[1:]) + count_change(a - d, kinds)
#or this code
#def count_change(x, y):
#    count = [0] * (x + 1)
#    count[0] = 1
#    for i in y:
#        for j in range(i, x + 1):
#            count[j] += count[j - i]
#    return count[x]
print count_change(10, [1, 5])
print count_change(10, [1, 2])
print count_change(100, [1, 5, 10, 25, 50])

