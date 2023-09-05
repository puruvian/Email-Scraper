import functions

URL = "https://samueli.ucla.edu/search-faculty/#cs"
# Change this to False if you want the full names of professors
LAST_NAMES = True

soup = functions.get_soup_after_js(URL, 'card_description')

cards = soup.find_all('article', class_='card')
new_cards = []

for i in range(len(cards)):
    i_tag = cards[i].findChildren(recursive=True, name='i')[0]
    if "Emeritus" in i_tag.text or "Emerita" in i_tag.text:
        pass
    else:
        new_cards.append(cards[i])

emails = []
names = []
for card in new_cards:
    a_tag = card.findChild(name='a', recursive=True, class_="mailto-link")
    emails.append(a_tag.text.strip())

    h4_tag = card.findChild(name='h4', class_="people-title", recursive=True)
    names.append(h4_tag.findChildren()[0].text.strip())

functions.write(emails, names, 'uclaCS', LAST_NAMES)
