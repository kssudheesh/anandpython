#Write a function treemap to map a function over nested list.
def treemap(f,x):
        r = []
        for a in x:
                if isinstance(a, list):
                        r.append(treemap(f,a))
                else:
                        r.append(f(a))
        return r
print treemap(lambda x: x*x,[1,2,[3,4,[5]]])


