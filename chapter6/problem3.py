#Write a function unflatten_dict to do reverse of flatten_dict.
def unflatten_dict(dictionary):
	resultDict = {}
	for key, value in dictionary.items():
        	parts = key.split(".")
        	d = resultDict
        	for part in parts[:-1]:
            		if part not in d:
                		d[part] = {}
            		d = d[part]
        	d[parts[-1]] = value
    	return resultDict
print unflatten_dict({'a': 4, 'b.c.s': 2, 'g': 23, 'f': 100, 'x.y': 2, 'b.1': 3, 'x.z': 3, 'b.c.d': 4})
