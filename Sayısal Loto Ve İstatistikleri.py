import random

def aralik(sayi):
    if (sayi < 1) or (sayi > 59):
        raise Warning("Uygun değer giriniz!")


istatistik = dict()

while True:
    print("\n------------------\n\n\n")
    sayilar = list()

    for i in range(6):
        rastgele = random.randint(1, 59)
        sayilar.append(rastgele)
        if rastgele in istatistik.keys():
            istatistik[rastgele] += 1
        else:
            istatistik[rastgele] = 1

    secilen = list()

    for i in range(6):
        while True:
            try:
                sayi = int(input("{}. sayı: ".format(i + 1)))
                aralik(sayi)
            except ValueError:
                print("Sadece sayı giriniz!")
                continue
            except Warning as hata:
                print(hata)
                continue
            break
        secilen.append(sayi)

    bildi = 0
    for i in secilen:
        if i in sayilar:
            bildi += 1

    print("\nDoğru tahmin sayısı:", bildi)

    print("Sayılar:", end= " ")
    sayilar.sort()
    for i in sayilar:
        print(i, end= " ")

    print("\n\nTahminler:", end= " ")
    secilen.sort()
    for i in secilen:
        print(i, end= " ")


    print("\n\n\nİstatistikler\n")
    sıralı = []
    for i, j in istatistik.items():
        sıralı.append((i, j))

    sıralı = sorted(sıralı, key= lambda x: x[1], reverse= True)

    if len(sıralı) < 10:
        kez = len(sıralı)
    else:
        kez = 10

    for i in range(kez):
        print("{} sayısı {} kez çıktı.".format(sıralı[i][0], sıralı[i][1]))

    cevap = input("Tekrar oynamak için E' yi tuşlayın. Çıkmak için herhangi bir tuşlama yapın. ")
    if cevap == "E":
        print("Yeni oyun başlıyor...")
        continue
    else:
        print("Oyundan çıkılıyor...")
        break



