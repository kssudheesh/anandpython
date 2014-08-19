#Write a function make_slug that takes a name converts it into a slug. A slug is a string where spaces and special characters are replaced by a hyphen, typically used to create blog post URL from post title. It should also make sure there are no more than one hyphen in any place and there are no hyphens at the biginning and end of the slug.
import sys
import re
def make_slug(x):
	a = '-'.join(re.findall(r'\w+',x))
	print a
make_slug(sys.argv[1])
