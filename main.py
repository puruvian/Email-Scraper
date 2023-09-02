from urllib.request import *
import ssl

import requests
from bs4 import BeautifulSoup

URL = "https://www.ics.uci.edu/faculty/"

response = requests.request(
    "GET", URL)

html = response.text
soup = BeautifulSoup(html, "html.parser")

tags = soup.find_all('a')
new_list = []
#this is a test line
for tag in tags:
    if '@' in tag.text:
        new_list.append(tag.text)

print(new_list)



