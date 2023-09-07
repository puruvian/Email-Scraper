import functions

URL = "https://www.ics.uci.edu/faculty/"
# Change this to False if you want the full names of professors
LAST_NAMES = True

soup = functions.get_soup(URL)

all_tags = soup.find_all('a')

# Get only the <a> tags that have an email
email_tags = [tag for tag in all_tags if '@' in tag.text]
del all_tags

# Remove Emeritus and Emerita faculty
tags = []
for tag in email_tags:
    title = tag.parent.parent.findChild('strong').text  # Get the tag that corresponds to a professors title
    if "Emeritus" in title or "Emerita" in title or "Teaching" in title or "Lecturer" in title:
        pass
    else:
        tags.append(tag)
del email_tags

names = [tag.parent.parent.findChild('a').text for tag in tags]
emails = [tag.text for tag in tags]

functions.write(emails, names, 'uciCS', LAST_NAMES)
