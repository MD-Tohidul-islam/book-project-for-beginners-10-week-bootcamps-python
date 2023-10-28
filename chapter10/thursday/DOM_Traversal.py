#  accessing the children attribute
from bs4 import BeautifulSoup
import requests
#  requesting page content
#  performing a request and outputting the status code
#  traversing through the DOM using Beautiful Soup - using the children attribute
page = requests.get("http://www.arthurleej.com/e-love.html")
soup = BeautifulSoup(page.content,'html.parser')
print(soup.children)  # outputs and iterator object

#  understanding the types of children
for child in list(soup.children):
    print(type(child))

#  accessing the Tag object
html = list(soup.children)[2]
for section in html:
    print('\n\n Start of new section')
    print(section)

#  accessing the head element tag
head = list(html.children)[1]
for item in head:
    print('\n\n New Tag')
    print(item)
#  scraping the title text
title = list(head)[1]
print(title.string)  # string is used to extract text as well
print(type(title.string))  # result in navigablestring
print(title.get_text())
