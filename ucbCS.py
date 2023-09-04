import requests
from bs4 import BeautifulSoup

# Change this to False if you want the full names of professors
LAST_NAMES = True
URL = "https://www2.eecs.berkeley.edu/Faculty/Lists/CS/faculty.html"

response = requests.get(URL)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

all_media_bodies = soup.find_all('div', recursive=True, class_="media-body")
media_bodies = []

for body in all_media_bodies:
    strong = body.findChild('strong', recursive=True)
    email_line = body.contents[3].contents[4]
    if "Emeritus" in strong.text or "Emerita" in strong.text or "Teaching" in strong.text:
        pass
    elif not '@' in email_line:
        pass
    else:
        media_bodies.append(body)

emails = []
names = []

counter = 0
for body in media_bodies:
    if LAST_NAMES:
        name = body.findChild('a', recursive=True).text.strip()
        names.append(name.split(' ')[-1])
    else:
        names.append(body.findChild('a', recursive=True).text.strip())
    p = body.findChild('p', recursive=True)  # finds the overarching p element
    line = p.contents[4]
    index = line.rfind(';')
    emails.append(line[index + 1:].strip())

with open('names_ucb.txt', 'w') as f:
    for name in names:
        f.write(name + '\n')

with open('emails_ucb.txt', 'w') as f:
    for email in emails:
        f.write(email + '\n')

print("Program finished. You can find professor emails in emails_ucb.txt and professor names in names_ucb.txt. These "
      "have both been created in your local directory.")