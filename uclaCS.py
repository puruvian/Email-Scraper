import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://samueli.ucla.edu/search-faculty/#cs"

driver = webdriver.Chrome()
driver.get(URL)
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "card_description"))
)
html = driver.page_source
driver.quit()

soup = BeautifulSoup(html, "html.parser")

a_tags = soup.find_all('a', class_="mailto-link")
emails = [a_tag.text.strip() for a_tag in a_tags]

with open("emails_ucla.txt", 'w') as f:
    for email in emails:
        f.write(f"{email}\n")
