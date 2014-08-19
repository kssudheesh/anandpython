#Write a regular expression to validate a phone number.
import re
x = raw_input("enter an indian phone number with code(no + sign)")
if x.isdigit():
	match1 = re.search(r'^91\d{10}$',x)
	match2 = re.search(r'^\d{11}$',x)
	if match1:
		print 'valid mobile number'
	elif match2:
		print 'valid landline number'
	else:
		print 'invalid number'
else:
	print 'not a digit, invalid phone number'
