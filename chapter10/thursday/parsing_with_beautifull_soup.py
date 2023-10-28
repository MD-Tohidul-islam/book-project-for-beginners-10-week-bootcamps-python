#  importing the beautifull soup and requests library
from bs4 import BeautifulSoup
import requests
#  requesting page content
#  performing a request and outputting the status code

page = requests.get("http://www.arthurleej.com/e-love.html")
#  turning the response into a beautifulSoup object to extract data

soup = BeautifulSoup(page.content,'html.parser')
print(soup.prettify())
