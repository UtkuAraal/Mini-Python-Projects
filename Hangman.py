import random
import time
alan = [" ", " ", " ", " ", " ", " ", " ", " "]
dolu = ["O", "|", "--", "|", "--", "|", "/", "\\"]
kelimeler = ["merhaba", "deneme", "nasılsın", "harika", "mükemmel"]
deneme = 0
secilen_kelime = random.choice(kelimeler)
olmayan = []
secilen_liste = list(secilen_kelime)
ekran = list("_" for i in range(0, len(secilen_kelime)))

def ekran_doldur():
    global deneme
    alan[deneme] = dolu[deneme]
    deneme += 1

while True:
    print("""
         ----------------
        |               |
        {}               |
        {}               |
      {}{}{}             |
        {}               |
       {}{}               | 
                        |
                        |
                     ---------   
    
    """.format(alan[0], alan[1], alan[2], alan[3], alan[4], alan[5], alan[6], alan[7], ))
    for i in ekran:
        print(i, end = " ")
    print("\nBulunmayanlar : ", end = "\t")
    for i in olmayan:
        print(i, end = " ")

    if alan == dolu:
        print("\nÜzgünüm haklarınız bitti! kelimemiz : {}".format(secilen_kelime))
        break
    elif ekran == secilen_liste:
        print("\nTebrikler buldunuz!")
        break

    cevap = input("\nHarf mi yoksa tahmin mi (h/t):")
    if cevap == "h":
        harf = input("Harf girin : ")

        if harf in secilen_kelime:
            print("Seçilen harfden {} adet var.".format(secilen_kelime.count(harf)))
            yer = []
            for i, j in enumerate(secilen_kelime):
                if j == harf:
                    yer.append(i)
            for i in yer:
                ekran[i] = harf
                time.sleep(2)
        else:
            print("Üzgünüm kelimede {} harfi yok".format(harf))
            ekran_doldur()
            olmayan.append(harf)
            time.sleep(2)
    elif cevap == "t":
        tahmin = input("Tahmininiz : ")

        if tahmin == secilen_kelime:
            print("Tebrikler Doğru Tahmin !")
            break
        else:
            print("Üzgünüm bilemediniz!")
            ekran_doldur()
            time.sleep(2)






