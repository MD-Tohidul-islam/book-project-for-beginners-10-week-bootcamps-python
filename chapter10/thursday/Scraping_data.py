from bs4 import BeautifulSoup
import requests
#  requesting page content
#  performing a request and outputting the status code

page = requests.get("http://www.arthurleej.com/e-love.html")
#  turning the response into a beautifulSoup object to extract data

soup = BeautifulSoup(page.content,'html.parser')

#  find method to scrape the text within the first bold tag
title = soup.find('b')
print(title)
print(title.get_text())  # extracts all text within element


#  find_all()

#  get all text within the bold element tag then output each
# poem_text = soup.find_all('b')
# for text in poem_text:
#     print(text.get_text())

# #  finding elements by attrinutes
# page2 = requests.get('http://github.com/Connor-SM')
# soup = BeautifulSoup(page2.content,'html.parser')
# username = soup.find_all('span',attrs={'class':'vcard-username'})
# print(username)  # will show that element has class of vcard-username among others
# print(username.get_text())
