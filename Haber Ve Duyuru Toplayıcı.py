import requests
from bs4 import BeautifulSoup

url = "https://www.mcbu.edu.tr/"
response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, "html.parser")

print("Celal Bayar Üniversitesi'ne Ait Son Duyurular Ve Haberler\n")

for i in soup.find_all("a", {"class": "DuyuruveHaberLink"}):
    print(i.text)
    print("*********")


