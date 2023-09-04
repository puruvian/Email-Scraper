import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://samueli.ucla.edu/search-faculty/#cs"
# Change this to False if you want the full names of professors
LAST_NAMES = True

driver = webdriver.Chrome()
driver.get(URL)
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "card_description"))
)
html = driver.page_source
driver.quit()

soup = BeautifulSoup(html, "html.parser")

cards = soup.find_all('article', class_='card')
new_cards = []

for i in range(len(cards)):
    print(cards)
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
# a_tags = soup.find_all('a', class_="mailto-link")
# emails = [a_tag.text.strip() for a_tag in a_tags]

# name_tags = soup.find_all('h4', class_="people-title")
# names = [h4.findChildren()[0].text.strip() for h4 in name_tags]

with open("emails_ucla.txt", 'w') as f:
    for email in emails:
        f.write(f"{email}\n")

with open("names_ucla.txt", 'w') as f:
    if LAST_NAMES:
        for name in names:
            f.write(f"{name.split()[-1]}\n")
    else:
        for name in names:
            f.write(f"{name}\n")

print("Program finished. You can find professor emails in emails_ucla.txt and professor names in names_ucla.txt. These"
      " have both been created in your local directory.")
