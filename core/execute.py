#
import html_handling as hh

#
soup_variable = hh.url_handle()
#
final_sum = 0

#
list1 = []

#
list1 = hh.tags_search(soup_variable, list1)

final_sum = hh.list_sum(list1)
print(final_sum)

