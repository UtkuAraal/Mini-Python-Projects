import requests
from bs4 import BeautifulSoup

url = "http://data.fixer.io/api/latest?access_key=6e4492de42211daa7dd5f696214fdd4d"
response = requests.get(url)
response_json = response.json()

doviz1 = input("Çevirilecek birim: ")
doviz2 = input("Çevirmek istediğiniz birim: ")
miktar = float(input("Miktar: "))

sonuc = (response_json["rates"][doviz2] / response_json["rates"][doviz1]) * miktar
print(sonuc)
