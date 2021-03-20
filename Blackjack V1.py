import random
import time
print("Blackjack Oyununa Hoşgeldiniz")
kart_destesi = [[1, 4], [2, 4], [3, 4], [4, 4], [5, 4], [6, 4], [7, 4], [8, 4], [9, 4], [10, 4], [10, 4], [10, 4], [10, 4], ] # ilk indeks değeri ikincisi kaç tane kaldı belirtiyor

kullanici_eli = []
i = 0

def kart_dagit():
    rastgele_kart = random.randint(0, 12)
    gelen_kart = kart_destesi[rastgele_kart]
    if gelen_kart[1] == 0:
        while gelen_kart[1] == 0:
            gelen_kart = kart_destesi[rastgele_kart]

    kullanici_eli.append(gelen_kart[0])
    gelen_kart[1] -= 1


kart_dagit()
kart_dagit()
print("Eliniz: ", kullanici_eli[0], kullanici_eli[1])

while True:
    toplam = 0
    for i in kullanici_eli:
        toplam += i
    if toplam >= 22:
        print("\nDaha fazla kart çekemezsiniz Oyun Bitti!")
        break

    cevap = input("\nKart Çekmek İçin (1), Durmak İçin (2): ")


    if cevap == "1":
        kart_dagit()
        for i in kullanici_eli:
            print(i, end = " ")
    elif cevap == "2":
        for i in kullanici_eli:
            print(i, end = " ")
        break

if toplam == 21:
    print("\nTebrikler Oyunu Kazandınız +10")
elif toplam >= 18 and toplam < 21:
    print("\n+5 puan")
else:
    print("\nMaalesef puan veremiyorum")




