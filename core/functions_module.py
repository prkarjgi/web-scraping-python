# This file is used for handling html URLs
# This is imported as a module into the file execute.py
import urllib
from bs4 import BeautifulSoup
import re

#this function to read a URL and to open using urllib.urlopen()
def url_handle():
	url = input("Enter the url: ")
	file_handle = urllib.request.urlopen(url)
	soup = BeautifulSoup(file_handle, "html5lib")
	return soup

#this function searches in the content for a given html tag for a number and stores it in a list
def tags_search(html_soup, list_buffer):
	span_tags = html_soup('span')
	for tags in span_tags:
		string = str(tags)
		result = re.findall('([0-9]+)',string)
		list_buffer = list_buffer + result
	return list_buffer

#this function first converts the type of each list element from str to int, and then takes a sum of each int element
def list_sum(list1, total=0):
	for each in list1:
		total += int(each)
	return total

