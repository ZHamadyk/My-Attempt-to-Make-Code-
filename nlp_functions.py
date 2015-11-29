
from bs4 import BeautifulSoup as BS 

import sys
reload(sys)
sys.setdefaultencoding('Cp1252')


def url_open():
	import urllib
	input = raw_input("Enter URL: ")
	r = urllib.urlopen(input).read()
	url_open.soup = BS(r).body.get_text()
	

def file_open():
	print "File Format: 'foo.txt', include quotation"
	input = raw_input("Enter File: ")
	r = open(input).read()
	file_open.soup = BS(r).get_text()
	
	
def choice():
	print "Enter 'web' or 'text', respectively"
	choice = raw_input("Are we working with web or text file? ")
	if choice == "web":
		url_open()
	elif choice == "text":
		file_open
	

