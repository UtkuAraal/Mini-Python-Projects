import requests
from bs4 import BeautifulSoup

url = "https://m.imdb.com/chart/top"
response = requests.get(url)

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi, "html.parser")

a = float(input("Rating'i giriniz: "))

basliklar = soup.find_all("h4")
ratingler = soup.find_all("span", {"class":"imdb-rating"})

for baslik, rating in zip(basliklar, ratingler):
    baslik = baslik.text
    rating = rating.text
    baslik = baslik.strip()
    baslik = baslik.replace("\n", "")
    rating = rating.strip()
    rating = rating.replace("\n", "")

    if float(rating) > a:
        print("Film İsmi: ", baslik)
        print("Rating: ", rating)
