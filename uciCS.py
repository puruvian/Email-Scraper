import requests
from bs4 import BeautifulSoup

URL = "https://www.ics.uci.edu/faculty/"
# Change this to False if you want the full names of professors
LAST_NAMES = True

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
for i in range(len(tags)):
    if '@' in tags[i].text:
        new_names_list.append(tags[i-1].text.strip())


with open('emails_uci.txt', 'w') as f:
    for email in new_emails_list:
        f.write(email + '\n')

if LAST_NAMES:
    for i in range(len(new_names_list)):
        names = new_names_list[i].split(' ')
        new_names_list[i] = names[-1]

with open('names_uci.txt', 'w') as f:
    for name in new_names_list:
        f.write(name + '\n')

print("Program finished. You can find professor emails in emails_uci.txt and professor names in names_uci.txt. These "
      "have both been created in your local directory.")
