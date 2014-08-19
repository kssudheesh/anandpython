#create a new virtualenv and install BeautifulSoup. BeautifulSoup is very good library for parsing HTML. Try using it to extract all HTML links from a webpage.
from bs4 import BeautifulSoup
import urllib
f = urllib.urlopen("http://www.gmail.com")
soup = BeautifulSoup(f)
print soup.findAll('a')

