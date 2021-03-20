import requests
from bs4 import BeautifulSoup

url = "https://medium.com/"
response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, "html.parser")
print("Medium.com sitesindeki trend makaleler\n")
for i in soup.find_all("h2", {"class": "bw hu ek by jb jk jd je jl jg jh ga bz"}):
    print(i.text)
    print("*********")


