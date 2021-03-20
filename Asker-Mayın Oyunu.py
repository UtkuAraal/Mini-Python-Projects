import random
import time
print("Asker - Mayın oyununa hoşgeldiniz...")
insan_puan = 0
bilgisayar_puan = 0

sıra = "insan"

def harita_yaz(harita, asker_yer):
    print("Mayınlar : {} {} {}".format(harita[1], harita[2], harita[3]))
    print("Askerler : {} {} {}".format(asker_yer[0], asker_yer[1], asker_yer[2]))
    print("İnsan: {}\tBilgisayar: {}".format(insan_puan, bilgisayar_puan))
    time.sleep(5)


while True:
    harita = {1: 0, 2: 0, 3: 0}
    if insan_puan >= 10:
        print("İnsan kazandı!")
        break
    elif bilgisayar_puan >= 10:
        print("Bilgisayar kazandı!")
        break

    print("Saldırı sırası {}".format(sıra))
    time.sleep(5)

    if sıra == "insan":
        while True:
            asker_sayisi = 0
            asker_yeri = [0, 0, 0]
            i = 0
            while i < 3:
                try:
                    asker = int(input("{}. yola kaç asker göderilecek: ".format(i + 1)))
                except ValueError:
                    print("Sadece rakam!")
                    continue

                if (asker_sayisi + asker) > 3:
                    print("Gönderebileceğiniz toplam asker sayısı 3!")
                    continue
                elif asker < 0:
                    print("Negatif değer giremezsiniz!")
                    continue
                elif i == 2 and (asker_sayisi + asker) < 3:
                    print("3 asker göndermek zorundasınız!")
                    continue
                asker_sayisi += asker
                asker_yeri[i] = asker
                i += 1
            cevap = input("Emin misiniz? (E/H): ")

            if cevap == "E":
                break

        mayin_sayisi = 0
        j = 1
        while j < 4:
            kalan = 3 - mayin_sayisi
            mayin = random.randint(0, kalan + 1)
            if (mayin_sayisi + mayin) > 3:
                continue
            elif j == 3 and (mayin_sayisi + mayin) < 3:
                continue
            mayin_sayisi += mayin
            harita[j] = mayin
            j += 1
        for i in range(0, 3):
            if asker_yeri[i] > harita[i + 1]:
                sayi = asker_yeri[i] - harita[i + 1]
                print("{}. yoldan {} sayıda asker karşıya geçti!".format(i + 1, sayi))
                insan_puan += sayi
            else:
                if asker_yeri[i] == 0:
                    print("{}. yoldan karşıya hiç asker geçmedi!".format(i + 1))
                else:
                    print("{}. yoldan karşıya hiç asker geçemedi!".format(i + 1))
        harita_yaz(harita, asker_yeri)
        sıra = "bilgisayar"
    elif sıra == "bilgisayar":
        asker_sayi = 0
        asker_yeri = [0, 0, 0]
        i = 0
        while i < 3:
            kalan = 3 - asker_sayi
            asker = random.randint(0, kalan + 1)
            if (asker_sayi + asker) > 3:
                continue
            elif i == 2 and (asker_sayi + asker) < 3:
                continue
            asker_sayi += asker
            asker_yeri[i] = asker
            i += 1
        while True:
            mayin_sayisi = 0
            j = 1

            while j < 4:
                try:
                    mayin = int(input("{}. yol için mayın sayısı: ".format(j)))
                except ValueError:
                    print("Sadece rakam!")
                    continue
                if (mayin_sayisi + mayin) > 3:
                    print("Toplam mayın sayısı 3 ten büyük olamaz!")
                    continue
                elif mayin < 0:
                    print("Negatif değer giremezsiniz!")
                    continue
                elif j == 3 and (mayin_sayisi + mayin) < 3:
                    print("3 mayın hakkını kullanmak zorundasınız!")
                    continue
                mayin_sayisi += mayin
                harita[j] = mayin
                j += 1
            cevap = input("Emin misiniz? (E/H): ")

            if cevap == "E":
                break

        for i in range(0, 3):
            if asker_yeri[i] > harita[i + 1]:
                gecen = asker_yeri[i] - harita[i + 1]
                print("{}. yoldan {} sayıda asker geçti!".format(i + 1, gecen))
                bilgisayar_puan += gecen
            else:
                if asker_yeri[i] == 0:
                    print("{}. yoldan karşıya hiç asker geçmedi!".format(i + 1))
                else:
                    print("{}. yoldan karşıya hiç asker geçemedi!".format(i + 1))
        harita_yaz(harita, asker_yeri)
        sıra = "insan"
