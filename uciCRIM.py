import re
import functions

URL = "https://cls.soceco.uci.edu/faculty"
# Change this to False if you want the full names of professors
LAST_NAMES = True

soup = functions.get_soup(URL)

field_tags = soup.find_all('a', string=re.compile('@'))
emails = [tag.text for tag in field_tags]


name_tags = soup.find_all('a', href=re.compile('https://socialecology.uci.edu/faculty'))
names = [name.text for name in name_tags]

functions.write(emails, names, 'uciCRIM', LAST_NAMES)
