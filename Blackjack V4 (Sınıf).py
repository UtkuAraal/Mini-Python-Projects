import random
import time
class Insan():
    deste = []

    def kart_cek(self):
        while True:
            rastgele = random.randint(0, 12)
            if kart_destesi[rastgele][1] == 0:
                continue
            else:
                self.deste.append(kart_destesi[rastgele][0])
                kart_destesi[rastgele][1] -= 1
                break

    def toplam(self):
        toplam = 0
        for i in self.deste:
            toplam += i
        return toplam

    def deste_temizle(self):
        self.deste = []

    def __len__(self):
        return len(self.deste)

class Bilgisayar():
    deste = []

    def kart_cek(self):
        while True:
            rastgele = random.randint(0, 12)
            if kart_destesi[rastgele][1] == 0:
                continue
            else:
                self.deste.append(kart_destesi[rastgele][0])
                kart_destesi[rastgele][1] -= 1
                break
    def toplam(self):
        toplam = 0
        for i in self.deste:
            toplam += i
        return toplam
    def deste_temizle(self):
        self.deste = []
    def __len__(self):
        return len(self.deste)
oyun = "devam"
while oyun == "devam":
    kart_destesi = [[1, 4], [2, 4], [3, 4], [4, 4], [5, 4], [6, 4], [7, 4], [8, 4], [9, 4], [10, 4], [10, 4], [10, 4],
                    [10, 4]]
    insan = Insan()
    bilgisayar = Bilgisayar()

    insan.deste_temizle()
    bilgisayar.deste_temizle()

    insan.kart_cek()
    insan.kart_cek()
    bilgisayar.kart_cek()
    bilgisayar.kart_cek()

    while bilgisayar.toplam() <= 15:
        bilgisayar.kart_cek()

    while True:
        print("Eliniz :", end=" ")
        for kart in insan.deste:
            print(kart, end=" ")

        if insan.toplam() >= 22:
            print("\nSınırı aştınız !")
            break

        işlem = input("\nKart Çekmek İçin : 1\nTamam Demek İçin 2 \nSeçiminiz : ")
        if işlem == "1":
            insan.kart_cek()
        elif işlem == "2":
            break

    if (insan.toplam() >= 22) and (bilgisayar.toplam() >= 22):
        print("Kimse kazanamadı.")
    elif not(insan.toplam() >= 22) and (bilgisayar.toplam() >= 22):
        print("İnsan Kazandı")
    elif (insan.toplam() >= 22) and not(bilgisayar.toplam() >= 22):
        print("Bilgisayar kazandı")
    elif insan.toplam() > bilgisayar.toplam():
        print("İnsan kazandı")
    elif insan.toplam() < bilgisayar.toplam():
        print("Bilgisayar kazandı")
    else:
        print("Berabere")

    print("""
    
    İnsan : {}
    Bilgisayar : {}
        
    """.format(insan.toplam(), bilgisayar.toplam()))
    time.sleep(3)
    
    devam_mi = input("Bir daha Oynamak İçin 1\nBitirmek için 2\nSeçiminiz : ")

    if devam_mi == "1":
        continue
    elif devam_mi == "2":
        oyun = "bitti"



