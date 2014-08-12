# Improve the unique function written in previous problems to take an optional key function as argument and use the return value of the key function to check for uniqueness.
def unique(x):
        y = []
        for i in x: 
                if i.lower() not in y:
                        y.append(i)
        return y
print unique(["python","java","Python","Java"])

