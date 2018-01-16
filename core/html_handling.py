# This file is used for handling html URLs
import urllib
import BeautifulSoup

#function to read a URL and to open and read it using urllib.urlopen().read()
def url_handle():
	url = input("Enter the url")
	file_handle = urllib.urlopen(url).read()

