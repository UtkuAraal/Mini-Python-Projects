import random
import time
print("Blackjack Oyununa Hoşgeldiniz")
# kart_destesi = [[1, 4], [2, 4], [3, 4], [4, 4], [5, 4], [6, 4], [7, 4], [8, 4], [9, 4], [10, 4], [10, 4], [10, 4], [10, 4]] # ilk indeks değeri ikincisi kaç tane kaldı belirtiyor
i = 0
oyun = "devam"

def kart_dagit():
    rastgele_kart = random.randint(0, 12)
    gelen_kart = kart_destesi[rastgele_kart]
    if gelen_kart[1] == 0:
        while gelen_kart[1] == 0:
            gelen_kart = kart_destesi[rastgele_kart]

    kullanici_eli.append(gelen_kart[0])
    gelen_kart[1] -= 1

def bilgisayara_kart_dagit():
    rastgele_kart = random.randint(0, 12)
    gelen_kart = kart_destesi[rastgele_kart]
    if gelen_kart[1] == 0:
        while gelen_kart[1] == 0:
            gelen_kart = kart_destesi[rastgele_kart]

    bilgisayar_eli.append(gelen_kart[0])
    gelen_kart[1] -= 1

while oyun == "devam":
    kart_destesi = [[1, 4], [2, 4], [3, 4], [4, 4], [5, 4], [6, 4], [7, 4], [8, 4], [9, 4], [10, 4], [10, 4], [10, 4],
                    [10, 4]]
    kullanici_eli = []
    bilgisayar_eli = []
    kart_dagit()
    kart_dagit()
    bilgisayara_kart_dagit()
    bilgisayara_kart_dagit()

    # Bilgisayar için
    bilgisayar_toplam = 0
    for i in bilgisayar_eli:
        bilgisayar_toplam += i

    while bilgisayar_toplam < 15:
        bilgisayara_kart_dagit()
        bilgisayar_toplam = 0
        for i in bilgisayar_eli:
            bilgisayar_toplam += i

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

    if (bilgisayar_toplam >= 22) and (toplam >= 22):
        print("\nKimse kazanamadı")
    elif (bilgisayar_toplam >= 22) and not(toplam >= 22):
        print("\nİnsan Kazandı")
    elif not(bilgisayar_toplam >= 22) and (toplam >= 22):
        print("\nBilgisayar Kazandı")
    elif bilgisayar_toplam < toplam:
        print("\nİnsan Kazandı")
    elif bilgisayar_toplam > toplam:
        print("\nBilgisayar Kazandı")
    else:
        print("\nBerabere")

    print("""
        
        Bilgisayar : {}
        İnsan : {}
        
    """. format(bilgisayar_toplam, toplam))

    devam_icin = input("Oyuna devam etmek için (1), bitirmek için (2) : ")
    if devam_icin == 2:
        oyun = "bitti"




