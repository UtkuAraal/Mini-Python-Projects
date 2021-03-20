import requests
from bs4 import BeautifulSoup
import random

url = "https://news.ycombinator.com/"
response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, "html.parser")
haber = random.choice(soup.find_all("a", {"class": "storylink"}))
print(haber.text)


