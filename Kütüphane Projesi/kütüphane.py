import sqlite3
import time

class Kitap:
    def __init__(self, isim, yazar, yayınevi, tür, baskı):
        self.isim = isim
        self.yazar = yazar
        self.yayınevi = yayınevi
        self.tür = tür
        self.baskı = baskı

    def __str__(self):
        return "\nKitap ismi: {}\nYazar: {}\nYayınevi: {}\nTür: {}\nBaskı: {}\n".format(self.isim, self.yazar, self.yayınevi, self.tür, self.baskı)

class Kütüphane():
    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("kütüphane.db")
        self.cursor = self.baglanti.cursor()

        sorgu = "Create Table If not exists kitaplar (İsim TEXT, Yazar TEXT, Yayınevi TEXT, Tür TEXT, Baskı INT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def baglantiyi_kes(self):
        self.baglanti.close()

    def kitapları_goster(self):
        sorgu = "Select * From kitaplar"
        self.cursor.execute(sorgu)
        kitaplar = self.cursor.fetchall()
        if len(kitaplar) == 0:
            print("Kütüphanede kitap bulunmuyor!")
        else:
            for i in kitaplar:
                kitap = Kitap(i[0], i[1], i[2], i[3], i[4])
                print(kitap)


    def kitap_sorgula(self, isim):
        sorgu = "Select * From kitaplar where İsim = ?"
        self.cursor.execute(sorgu, (isim,))
        kitaplar = self.cursor.fetchall()
        if len(kitaplar) == 0:
            print("Böyle bir kitap bulunmuyor!")
        else:
            kitap = Kitap(kitaplar[0][0], kitaplar[0][1], kitaplar[0][2], kitaplar[0][3], kitaplar[0][4], )
            print(kitap)

    def kitap_ekle(self, kitap):
        sorgu = "Insert into kitaplar Values(?, ?, ?, ?, ?)"
        self.cursor.execute(sorgu, (kitap.isim, kitap.yazar, kitap.yayınevi, kitap.tür, kitap.baskı))
        self.baglanti.commit()

    def kitap_sil(self, isim):
        sorgu = "Select * From kitaplar where İsim = ?"
        self.cursor.execute(sorgu, (isim,))
        kitaplar = self.cursor.fetchall()
        if len(kitaplar) == 0:
            print("Böyle bir kitap bulunmamaktadır...")
        else:
            sorgu2 = "Delete From kitaplar where İsim = ?"
            self.cursor.execute(sorgu2, (isim,))
            self.baglanti.commit()
            print("Kitap Silindi...")
    def baskı_yukselt(self, isim):
        sorgu = "Select * From kitaplar where İsim = ?"
        self.cursor.execute(sorgu, (isim,))
        kitaplar = self.cursor.fetchall()

        if len(kitaplar) == 0:
            print("Böyle bir kitap bulunmuyor...")
        else:
            baskı = kitaplar[0][4]
            baskı +=1
            sorgu2 = "Update kitaplar set Baskı = ? where İsim = ?"
            self.cursor.execute(sorgu2, (baskı, isim))
            self.baglanti.commit()

    def yayınevine_gore_listele(self, yayınevi):
        sorgu = "Select * From kitaplar where Yayınevi = ?"
        self.cursor.execute(sorgu, (yayınevi,))
        kitaplar = self.cursor.fetchall()
        if len(kitaplar) == 0:
            print("Bu yayın evine ait kitap bulunmamaktadır.")
        else:
            for i in kitaplar:
                kitap = Kitap(i[0], i[1], i[2], i[3], i[4])
                print(kitap)
    def ture_gore_ara(self, tür):
        sorgu = "Select * From kitaplar where Tür = ?"
        self.cursor.execute(sorgu, (tür,))
        kitaplar = self.cursor.fetchall()

        if len(kitaplar) == 0:
            print("Bu türde kitap bulunmamaktadır...")
        else:
            for i in kitaplar:
                kitap = Kitap(i[0], i[1], i[2], i[3], i[4])
                print(kitap)
    def yayınevleri_sırala(self):
        sorgu = "Select Yayınevi From kitaplar"
        self.cursor.execute(sorgu)
        yayınevleri = self.cursor.fetchall()

        if len(yayınevleri) == 0:
            print("Kayıtlı yayınevi bulunmamaktadır...")
        else:
            for i in yayınevleri:
                print(i[0])
    def turler(self):
        sorgu = "Select Tür From kitaplar"
        self.cursor.execute(sorgu)
        türler = self.cursor.fetchall()
        if len(türler) == 0:
            print("Kayıtlı tür bulunmamaktadır...")
        else:
            for i in türler:
                print(i[0])
    def yayınevi_kitap_sil(self, yayınevi):
        sorgu = "Select * From kitaplar where Yayınevi = ?"
        self.cursor.execute(sorgu, (yayınevi,))
        yayınevleri = self.cursor.fetchall()
        if len(yayınevleri) == 0:
            print("Bu yayın evine ait kayıtlı kitap bulunmamaktadır...")
        else:
            sorgu2 = "Delete From kitaplar where Yayınevi = ?"
            self.cursor.execute(sorgu2, (yayınevi,))
            self.baglanti.commit()
            print("{} yayınevine ait kitaplar silindi...".format(yayınevi))
    def hepsini_sil(self):
        sorgu = "Select * From kitaplar"
        self.cursor.execute(sorgu)
        kitaplar = self.cursor.fetchall()
        if len(kitaplar) == 0:
            print("Kayıtlı kitap bulunmamaktadır...")
        else:
            sorgu2 = "Delete From kitaplar"
            self.cursor.execute(sorgu2)
            self.baglanti.commit()
            print("Bütün kayıtlar silindi...")
    def yazara_gore_ara(self, yazar):
        sorgu = "Select * From kitaplar where Yazar = ?"
        self.cursor.execute(sorgu, (yazar,))
        kitaplar = self.cursor.fetchall()

        if len(kitaplar) == 0:
            print("Bu yazara ait kitap bulunmamaktadır...")
        else:
            for i in kitaplar:
                kitap = Kitap(i[0], i[1], i[2], i[3], i[4])
                print(kitap)
    def alfabetik_sıra(self):
        sorgu = "Select * From kitaplar"
        self.cursor.execute(sorgu)
        kitaplar = self.cursor.fetchall()
        if len(kitaplar) == 0:
            print("Sıralanacak Kitap Bulunmuyor...")
        else:
            kitaplar = sorted(kitaplar, key=lambda elem: elem[0])
            for i in kitaplar:
                kitap = Kitap(i[0], i[1], i[2], i[3], i[4])
                print(kitap)
