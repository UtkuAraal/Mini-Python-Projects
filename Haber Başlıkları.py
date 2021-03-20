import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
response = requests.get(url)

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi, "html.parser")

for i in soup.find_all("a", {"class":"storylink"}):
    print(i.text)
    print("*********")