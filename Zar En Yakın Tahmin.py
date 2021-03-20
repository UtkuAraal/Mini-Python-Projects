import random
import time

def aralik(sayi):
    if (sayi > 100) or (sayi <= 0):
        raise ValueError()
    else:
        pass


insan_puan = 0
bilgisayar_puan = 0

print("Sayı tahmin oyununa hoşgeldiniz...")
while True:
    if insan_puan == 10:
        print("İnsan kazandı!")
        devam = input("Devam etmek için E'ye basın ")
        if devam != "E":
            break
        else:
            insan_puan = 0
            bilgisayar_puan = 0
            print("******************")
    elif bilgisayar_puan == 10:
        print("Bilgisayar kazandı!")
        devam = input("Devam etmek için E'ye basın ")
        if devam != "E":
            break
        else:
            insan_puan = 0
            bilgisayar_puan = 0
            print("******************")
    print("------------------")
    sayi = random.randint(1, 100)
    try:
        insan_sayi = int(input("Tahmininiz:"))
        aralik(insan_sayi)
    except ValueError:
        print("Uygun değer giriniz!")
        continue

    bilgisayar_sayi = random.randint(1, 100)

    insan_fark = abs(sayi - insan_sayi)
    bilgisayar_fark = abs(sayi - bilgisayar_sayi)

    print("\nSayı: {}\tİnsan Tahmin: {}\tBilgisayar tahmin: {}".format(sayi, insan_sayi, bilgisayar_sayi))
    if insan_sayi == sayi and bilgisayar_sayi != sayi:
        print("İnsan doğru bildi! +2 puan!")
        insan_puan += 2
    elif insan_sayi != sayi and bilgisayar_sayi == sayi:
        print("Bilgisayar doğru bildi! +2 puan!")
        bilgisayar_puan += 2
    elif bilgisayar_fark > insan_fark:
        print("İnsan tahmini daha yakın. İnsan 1 puan kazandı!")
        insan_puan += 1
    elif insan_fark > bilgisayar_fark:
        print("Bilgisayar tahmini daha yakın. Bilgisayar 1 puan kazandı!")
        bilgisayar_puan += 1
    else:
        print("Berabere!")

    print("\nİnsan: {}\tBilgisayar: {}".format(insan_puan, bilgisayar_puan))
