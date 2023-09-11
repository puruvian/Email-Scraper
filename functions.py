import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_soup(url: str) -> BeautifulSoup:
    '''
    Gets the html from a given url using the Requests module, and returns a BeauitfulSoup object
    '''
    response = requests.get(url)
    html = response.text
    return BeautifulSoup(html, 'html.parser')


def get_soup_after_js(url: str, wait_for: str, by_what=By.CLASS_NAME) -> BeautifulSoup:
    """
    Returns a BeautifulSoup object that's created with HTML from after a page fully loads. Uses a Selenium object with a
    Chrome Driver that's included in this repo. You may need to download a new driver for your browser depending on what
    browser and version you use.
    """
    driver = webdriver.Chrome()
    driver.get(url)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((by_what, wait_for))
    )
    html = driver.page_source
    driver.quit()

    return BeautifulSoup(html, "html.parser")


def write(emails: list[str], names: list[str], filename: str, last_names: bool):
    with open(f'emails_{filename}.txt', 'w') as f:
        for email in emails:
            f.write(email + '\n')

    if last_names:
        names = [name.split(' ')[-1] for name in names]

    with open(f'names_{filename}.txt', 'w') as f:
        for name in names:
            f.write(name + '\n')

    print(
        f"Program finished. You can find professor emails in emails_{filename}.txt and professor names "
        f"in names_{filename}.txt. These have both been created in your local directory.")
