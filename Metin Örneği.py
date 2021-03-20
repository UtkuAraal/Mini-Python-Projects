import random
class Dosya():
    def __init__(self):
        with open("metin.txt", "r", encoding = "utf-8") as file:
            icerik = file.read()
            kelimeler = icerik.split()

            self.sade_kelimeler = list()

            for i in kelimeler:
                i = i.strip("\n")
                i = i.strip(",")
                i = i.strip(" ")
                i = i.strip(".")
                self.sade_kelimeler.append(i)

    def tum_kelimeler(self):
        kelime_kume = set()

        for i in self.sade_kelimeler:
            kelime_kume.add(i)
        print("Tüm kelimeler: ")
        for i in kelime_kume:
            print(i)
            print("*********")
    def kac_adet(self):
        sozluk = dict()
        for i in self.sade_kelimeler:
            if i in sozluk:
                sozluk[i] += 1
            else:
                sozluk[i] = 1

        for i, j in sozluk.items():
            print("{} kelimesinden {} tane var.".format(i, j))
            print("******************")

    def kac_adet_geciyor(self, word):
        ara = word.lower()
        defa = 0
        for i in self.sade_kelimeler:
            i = i.lower()
            if i == ara:
                defa += 1
        print("{} kelimesi metin içinde {} defa geçiyor.".format(word, defa))

    def rastgele(self):
        kelime = ""
        for i in range(1, 10):
            secilen = random.choice(self.sade_kelimeler)
            kelime += secilen + " "

        print("9 kelimelik rastgele cümle: ")
        print(kelime)


dosya = Dosya()

