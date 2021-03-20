import sqlite3
import random
from functools import *

class Makale:
    def __init__(self, baslik, icerik, yazar, kategori, gun, karakter_sayisi, begeni = 0, numara = 1):
        self.baslik = baslik
        self.icerik = icerik
        self.yazar = yazar
        self.kategori = kategori
        self.gun = gun
        self.karakter_sayisi = karakter_sayisi
        self.begeni = begeni
        self.numara = numara

    def __str__(self):
        return """
                Kategori: {}\tBaşlık: {}\t\t\tNumara: {}
        İçerik: {}
        
        Yazar: {}\tGün: {}\tKarakter Sayısı: {}
        
        Beğeni: {}
        
        """.format(self.kategori, self.baslik, self.numara, self.icerik, self.yazar, self.gun, self.karakter_sayisi, self.begeni)

class Blog:
    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("Blog.db")
        self.cursor = self.baglanti.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS makaleler (Başlık TEXT, İçerik TEXT, Yazar TEXT, Kategori TEXT, Gün TEXT, Karakter_Sayısı INT, Beğeni INT, Numara INT)")
        self.baglanti.commit()

    def baglanti_kes(self):
        self.baglanti.close()

    def makale_basliklari(self):
        self.cursor.execute("Select Başlık, Kategori, Numara from makaleler")
        basliklar = self.cursor.fetchall()

        if len(basliklar) == 0:
            print("Kayıtlı makale bulunmamaktadır...")
        else:
            for i in basliklar:
                print("{}- {}   *{}".format(i[2], i[0], i[1]))

    def makale_ac(self, numara):
        self.cursor.execute("Select * From makaleler where Numara = ?", (numara,))
        makaleler = self.cursor.fetchall()

        if len(makaleler) == 0:
            print("{} numarasına ait makale bulunmamıştır...".format(numara))
        else:
            for i in makaleler:
                makale = Makale(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
                print(makale)

    def kullaniciya_ait_makaleler(self, kullanici_adi):
        self.cursor.execute("Select Başlık, Kategori, Numara, Beğeni From makaleler where Yazar = ?", (kullanici_adi,))
        makaleler = self.cursor.fetchall()

        if len(makaleler) == 0:
            print("Kullanıcıya ait uygun makale bulunmamıştır...")
        else:
            for i in makaleler:
                print("{}- {}   *{}   +: {}".format(i[2], i[0], i[1], i[3]))

    def makale_ekle(self, makale):
        self.cursor.execute("Select Numara From makaleler")
        numaralar = self.cursor.fetchall()

        if len(numaralar) != 0:
            makale.numara += max([i[0] for i in numaralar])

        self.cursor.execute("INSERT INTO makaleler Values(?, ?, ?, ?, ?, ?, ?, ?)", (makale.baslik, makale.icerik, makale.yazar, makale.kategori, makale.gun, makale.karakter_sayisi, makale.begeni, makale.numara))

        self.cursor.execute("Select * From makaleler where Yazar = ?", (makale.yazar,))
        sayi = self.cursor.fetchall()
        sayi = len(sayi)
        self.cursor.execute("UPDATE kullanicilar SET Makale_Sayisi = ? where Kullanıcı_Adı = ?", (sayi, makale.yazar))
        self.baglanti.commit()
        print("Makale başarıyla eklendi.")

    def makale_sil(self, giris, numara):
        self.cursor.execute("Select Yazar, Başlık From makaleler where Numara = ?", (numara,))
        yazar = self.cursor.fetchall()

        if len(yazar) == 0:
            print("{} numarasına ait kayıtlı makale bulunmamaktadır...".format(numara))
        elif yazar[0][0] != giris:
            print("Bu makale {} isimli kullanıcıya ait olduğu için silemezsiniz!".format(yazar[0][0]))
        else:
            self.cursor.execute("DELETE FROM makaleler where Numara = ?", (numara,))
            self.baglanti.commit()
            print("{} numaralı ve {} başlıklı makale başarı ile silindi.".format(yazar[0][0], yazar[0][1]))

    def kategoriye_gore_ara(self, kategori):
        self.cursor.execute("Select Başlık, Kategori, Numara From makaleler where Kategori = ?", (kategori,))
        makaleler = self.cursor.fetchall()

        if len(makaleler) == 0:
            print("Seçilen kategoriye ait makale bulunamamıştır...")
        else:
            for i in makaleler:
                print("{}- {}   *{}".format(i[2], i[0], i[1]))

    def basliga_gore_ara(self, baslik):
        self.cursor.execute("Select Başlık, Kategori, Numara From makaleler where Başlık = ?", (baslik,))
        basliklar = self.cursor.fetchall()

        if len(basliklar) == 0:
            print("Kayıtlı makale bulunmamaktadır...")
        else:
            for i in basliklar:
                if i[0].lower() == baslik.lower():
                    print("{}- {}   *{}".format(i[2], i[0], i[1]))

    def begeni_sayisi(self, sıralama):
        self.cursor.execute("Select Başlık, Kategori, Numara, Beğeni From makaleler")
        makaleler = self.cursor.fetchall()

        if len(makaleler) == 0:
            print("Kayıtlı makale bulunmamaktadır...")
        else:
            if sıralama == "artan":
                makaleler = sorted(makaleler, key= lambda x: x[3])
            else:
                makaleler = sorted(makaleler, key= lambda x: x[3], reverse= True)

            for i in makaleler:
                print("{}- {}   *{}\tBeğeni: {}".format(i[2], i[0], i[1], i[3]))

    def eklenme_zamanına_gore(self, sıralama):
        self.cursor.execute("Select Başlık, Kategori, Numara From makaleler")
        makaleler = self.cursor.fetchall()

        if len(makaleler) == 0:
            print("Kayıtlı makale bulunmamaktadır...")
        else:
            if sıralama == "ilk":
                makaleler = sorted(makaleler, key= lambda x: x[2])
            else:
                makaleler = sorted(makaleler, key= lambda x: x[2], reverse= True)

            for i in makaleler:
                print("{}- {}   *{}".format(i[2], i[0], i[1]))

    def son_eklenen_makale(self):
        self.cursor.execute("Select * From makaleler")
        makaleler = self.cursor.fetchall()

        if len(makaleler) == 0:
            print("Kayıtlı makale bulunmamaktadır...")
        else:
            makaleler = sorted(makaleler, key= lambda x: x[2])
            makale = makaleler[-1]
            son_makale = Makale(makale[0], makale[1], makale[2], makale[3], makale[4], makale[5], makale[6], makale[7])
            print(son_makale)


    def rastgele_makale_ac(self):
        self.cursor.execute("Select Numara From makaleler")
        numaralar = self.cursor.fetchall()

        if len(numaralar) == 0:
            print("Kayıtlı makale bulunmamaktadır...")
        else:
            numaralar = [i[0] for i in numaralar]
            rastgele = random.choice(numaralar)
            self.cursor.execute("Select * From makaleler where Numara = ?", (rastgele,))
            makaleler = self.cursor.fetchall()

            for i in makaleler:
                makale = Makale(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
                print(makale)

    def kullanici_toplam_begeni(self, yazar):
        self.cursor.execute("Select Beğeni From makaleler where Yazar = ?", (yazar,))
        begeniler = self.cursor.fetchall()

        if len(begeniler) == 0:
            print("Bu kullanıcıya ait içerik bulunmuyor!")
        else:
            begeniler = [i[0] for i in begeniler]
            begeniler = reduce(lambda x, y: x + y, begeniler)
            print("{} isimli kullanıcının toplam {} beğenisi bulunmakta.".format(yazar, begeniler))

    def yazarlar(self):
        self.cursor.execute("Select Yazar From makaleler")
        yazarlar = self.cursor.fetchall()

        if len(yazarlar) == 0:
            print("Kayıtlı makale bulunmamaktadır...")
        else:
            yazar = set()
            for i in yazarlar:
                yazar.add(i[0])
            for i in yazar:
                print(i)

    def kategoriler(self):
        self.cursor.execute("Select Kategori from makaleler")
        kategoriler = self.cursor.fetchall()

        if len(kategoriler) == 0:
            print("Kayıtlı makale bulunmamaktadır...")
        else:
            kategori = set()
            for i in kategoriler:
                kategori.add(i[0])

            for j in kategori:
                print(j)

    def kelimeye_gore_ara(self, kelime):
        self.cursor.execute("Select Başlık, Kategori, Numara, İçerik From makaleler")
        makaleler = self.cursor.fetchall()

        if len(makaleler) == 0:
            print("Kayıtlı makale bulunmamaktadır...")
        else:
            sayac = 0
            for i in makaleler:
                if kelime.lower() in i[3].lower():
                    print("{}- {}   *{}".format(i[2], i[0], i[1]))
                    sayac += 1
            print(sayac, "adet makale bulundu.")


    def profil_bilgileri(self):
        self.cursor.execute("Select Yazar From makaleler")
        yazarlar = self.cursor.fetchall()

        if len(yazarlar) == 0:
            print("Kayıtlı makale bulunmamaktadır")
        else:
            bilgiler = []
            for i in yazarlar:
                self.cursor.execute("Select Beğeni From makaleler where Yazar = ?", (i[0],))
                begeniler = self.cursor.fetchall()
                begeniler = [j[0] for j in begeniler]
                makale_sayisi = len(begeniler)
                begeniler = reduce(lambda x, y: x + y, begeniler)
                bilgi = [i[0], makale_sayisi, begeniler]

                if not(bilgi in bilgiler):
                    bilgiler.append(bilgi)

            for i in bilgiler:
                print("Yazar: {}\t\t\tMakale Sayısı: {}\t\t\tToplam Beğeni: {}".format(i[0], i[1], i[2]))

    def begen(self, numara):
        self.cursor.execute("Select Beğeni From makaleler where Numara = ?", (numara,))
        begeni_sayisi = self.cursor.fetchall()

        begeni_sayisi = begeni_sayisi[0][0] + 1

        self.cursor.execute("UPDATE makaleler SET Beğeni = ? where Numara = ?", (begeni_sayisi, numara))
        self.baglanti.commit()
        print("Beğeni kaydedildi!")


    def en_cok_begenilen(self):
        self.cursor.execute("Select * From makaleler")
        makaleler = self.cursor.fetchall()

        if len(makaleler) == 0:
            print("Kayıtlı makale bulunmamaktadır...")
        else:
            makaleler = sorted(makaleler, key= lambda x: x[6])
            makale = makaleler[-1]
            begenilen_makale = Makale(makale[0], makale[1], makale[2], makale[3], makale[4], makale[5], makale[6], makale[7])
            print(begenilen_makale)

    def baslik_icinde_ara(self, kelime):
        self.cursor.execute("Select Başlık, Kategori, Numara From makaleler")
        makaleler = self.cursor.fetchall()

        if len(makaleler) == 0:
            print("Kayıtlı makale bulunmamakatdır...")
        else:
            sayac = 0
            for i in makaleler:
                if kelime.lower() in i[0].lower():
                    print("{}- {}   *{}".format(i[2], i[0], i[1]))
                    sayac += 1
            print("{} adet makale başlığı ile eşleşti.".format(sayac))












