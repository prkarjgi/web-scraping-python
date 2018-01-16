# This file is used for handling html URLs
import urllib
from bs4 import BeautifulSoup
import re

#function to read a URL and to open using urllib.urlopen()
def url_handle():
	url = input("Enter the url: ")
	file_handle = urllib.request.urlopen(url)
	soup = BeautifulSoup(file_handle, "html5lib")
	return soup

#
def tags_search(html_soup, list_buffer):
	span_tags = html_soup('span')
	for tags in span_tags:
		string = str(tags)
		result = re.findall('([0-9]+)',string)
		list_buffer = list_buffer + result
	return list_buffer

#
def list_sum(list1, total=0):
	for each in list1:
		total += int(each)
	return total

