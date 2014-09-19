#Write a function flatten_dict to flatten a nested dictionary by joining the keys with . character.
def flatten_dict(x,flattened = None,y = []):
	if flattened is None:
		flattened = {}
	for a in x:
		if isinstance(x[a],dict):
			flatten_dict(x[a],flattened,y+[a])
		else:
			flattened['.'.join(y+[a])] = x[a]
	return flattened
print flatten_dict({'x':{'y':2,'z':3},'a':4,'b':{'1':3,'c':{'s':2,'d':4}},'f':100,'g':23})
