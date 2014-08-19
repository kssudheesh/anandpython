#Write a program csv2xls.py that reads a csv file and exports it as Excel file. The prigram should take two arguments. The name of the csv file to read as first argument and the name of the Excel file to write as the second argument.
import sys
import tablib
data = tablib.Dataset()
with open(sys.argv[1],'r') as f:
	data = f.read()
with open(sys.argv[2],'wb') as f:
	f.write(data)


