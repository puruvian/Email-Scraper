import requests
from bs4 import BeautifulSoup
import re

URL = "https://www.ics.uci.edu/faculty/"

response = requests.request(
    "GET", URL)

html = response.text
soup = BeautifulSoup(html, "html.parser")

tags = soup.find_all('a')
new_emails_list = []
new_names_list = []

for tag in tags:
    if '@' in tag.text:
        new_emails_list.append(tag.text)
print(tags)
for i in range(len(tags)):
    if '@' in tags[i].text:
        new_names_list.append(tags[i-1].text.strip())


with open('emails.txt', 'w') as f:
    for email in new_emails_list:
        f.write(email + '\n')

with open('names.txt', 'w') as f:
    for name in new_names_list:
        f.write(name + '\n')


