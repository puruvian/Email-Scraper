import functions

URL = "https://www.ics.uci.edu/faculty/"
# Change this to False if you want the full names of professors
LAST_NAMES = True

soup = functions.get_soup(URL)


tags = soup.find_all('a')
emails = []
names = []

for tag in tags:
    if '@' in tag.text:
        emails.append(tag.text)
for i in range(len(tags)):
    if '@' in tags[i].text:
        names.append(tags[i - 1].text.strip())

functions.write(emails, names, 'uciCS', LAST_NAMES)
