#  importing the beautifull soup and requests library
from bs4 import BeautifulSoup
import requests
#  requesting page content
#  performing a request and outputting the status code

page = requests.get("http://www.arthurleej.com/e-love.html")
print(page)

#  outputting the request response content
print(page.content)
