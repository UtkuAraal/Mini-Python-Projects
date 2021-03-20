import requests
from bs4 import BeautifulSoup

url = "https://www.doviz.com/"
response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, "html.parser")
dolar = float(soup.find_all("span", {"class": "value", "data-socket-key": "USD"})[0].text.replace(",", "."))
euro = float(soup.find_all("span", {"class": "value", "data-socket-key": "EUR"})[0].text.replace(",", "."))
altın = float(soup.find_all("span", {"class": "value", "data-socket-key": "EUR"})[0].text.replace(",", "."))
bist100 = float(soup.find_all("span", {"class": "value", "data-socket-key": "XU100"})[0].text.replace(",", "."))
bitcoin = float(soup.find_all("span", {"class": "value", "data-socket-key": "bitcoin"})[0].text[1:].replace(",", "."))
birimler =  [dolar, euro, altın, bitcoin]
while True:
    print("""
        Menü
    1- Bilgileri görüntüle
    2- Çevirme işlemi yap
    q- Çıkış
    """)

    secim = input("Seçiminiz: ").strip()

    if secim == "q":
        print("Programdan çıkış yapılıyor...")
        break
    elif secim == "1":
        print("""
            Dolar: {}
            Euro: {}
            Altın: {}
            Bist 100: {}
            Bitcoin: {}
        """.format(dolar, euro, altın, bist100, bitcoin))
    elif secim == "2":
        try:
            birim1 = int(input("""
                Dönüştümeyi istediğiniz birim
            1- Dolar
            2- Euro
            3- Altın
            4- Bitcoin
            
            Seçiminiz:"""))
            birim2 = int(input("""
                Dönüştümek istediğiniz birim
            1- Dolar
            2- Euro
            3- Altın
            4- Bitcoin
            
            Seçiminiz: """))
            miktar = int(input("Miktar: "))

            sonuc = (birimler[birim1 - 1] / birimler[birim2 - 1]) * miktar
            print("Sonuç:", sonuc)
        except ValueError:
            print("Lütfen sadece sayı giriniz!")
            continue
        except:
            print("Geçersiz seçim!")
            continue
    else:
        print("Yanlış tuşlama!")
        continue



