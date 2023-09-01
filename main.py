from urllib.request import *
import ssl
import requests


URL = "https://www.ics.uci.edu/faculty/"

response = requests.request(
    "GET", URL)

html = response.text




