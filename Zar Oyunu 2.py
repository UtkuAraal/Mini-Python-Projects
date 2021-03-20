import random
import time


def uygun_mu(sayi):
    if sayi < 1 or sayi > 6:
        raise Warning("Sadece 1-6 arasında rakam giriniz!")
    else:
        pass

insan_puan = 10
bilgisayar_puan = 10

print("Zar Oyununa Hoşgeldiniz!\n")
oyun = "devam"
while True:

    if insan_puan == 0 and bilgisayar_puan == 0:
        print("\nBerabere!")
        oyun = "bitti"
    elif insan_puan == 0:
        print("\nBilgisayar kazandı!")
        oyun = "bitti"
    elif bilgisayar_puan == 0:
        print("\nİnsan kazandı!")
        oyun = "bitti"

    if oyun == "bitti":
        cevap = input("\nTekrar oynamak istermisiniz ? (E/H): ")
        if cevap == "E":
            insan_puan = 10
            bilgisayar_puan = 10
            print("\nYeni oyun\n------------------")
        elif cevap == "H":
            print("\nOyundan çıkılıyor...")
            break

    zar = random.randint(1, 6)

    try:
        insan_tahmin = int(input("\nZar tahmininiz: "))
        uygun_mu(insan_tahmin)
    except ValueError:
        print("Sadece rakam giriniz!")
    except Warning as hata:
        print(hata)
    time.sleep(1)
    bilgisayar_tahmin = random.randint(1, 6)

    if bilgisayar_tahmin == zar and insan_tahmin == zar:
        print("\nİki oyuncu da bildi!")
    elif bilgisayar_tahmin == zar:
        print("\nBilgisayar doğru tahmin etti!")
        insan_puan -= 1
    elif insan_tahmin == zar:
        print("\nİnsan doğru tahmin etti!")
        bilgisayar_puan -= 1
    else:
        print("\nİki oyuncu da tutturamadı!")
        insan_puan -= 1
        bilgisayar_puan -= 1
    time.sleep(1)
    print("\nİnsan puan: {}\nBilgisayar puan: {}\n\nZar: {}   İnsan tahmini: {}   Bilgisayar tahmini: {}".format(insan_puan, bilgisayar_puan, zar, insan_tahmin, bilgisayar_tahmin))
    time.sleep(1)