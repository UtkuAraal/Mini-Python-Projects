import sqlite3


class Ürün:
    def __init__(self, urun_adi, marka, miktar, stok, fiyat, kategori, menşei, tedarikci):
        self.urun_adi = urun_adi
        self.marka = marka
        self.miktar = miktar
        self.stok = stok
        self.fiyat = fiyat
        self.kategori = kategori
        self.menşei = menşei
        self.tedarikci = tedarikci

    def __str__(self):
        return """
            Ürün Adı: {}
            Markası: {}
            Miktar: {}
            Stok Bilgisi: {}
            Fiyat: {}
            Kategori: {}
            Menşei: {}
            Tedarikçi: {}
        """.format(self.urun_adi, self.marka, self.miktar, self.stok, self.fiyat, self.kategori, self.menşei, self.tedarikci)

    def kullaniciya(self):
        return """
            Ürün Adı: {}
            Markası: {}
            Miktar: {}
            Stok Bilgisi: {}
            Fiyat: {}
            Kategori: {}
            Menşei: {}
        """.format(self.urun_adi, self.marka, self.miktar, self.stok, self.fiyat, self.kategori, self.menşei)

class Market:
    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("market.db")
        self.cursor = self.baglanti.cursor()
        sorgu = "CREATE TABLE IF NOT EXISTS ürünler (Ürün_Adı TEXT, Marka TEXT, Miktar INT, Stok INT, Fiyat INT, Kategori TEXT, Menşei TEXT, Tedarikçi TEXT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def baglanti_kes(self):
        self.baglanti.close()

    def urunleri_listele(self, giris):
        sorgu = "Select * From ürünler"
        self.cursor.execute(sorgu)
        urunler = self.cursor.fetchall()

        if len(urunler) == 0:
            print("Markette Ürün Bulunmuyor...")
        else:
            if giris == "kullanıcı":
                for i in urunler:
                    urun = Ürün(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
                    print(urun.kullaniciya())
            elif giris == "admin":
                for i in urunler:
                    urun = Ürün(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
                    print(urun)
    def urun_ekle(self, urun):
        sorgu = "INSERT INTO ürünler Values(?, ?, ?, ?, ?, ?, ?, ?)"
        self.cursor.execute(sorgu, (urun.urun_adi, urun.marka, urun.miktar, urun.stok, urun.fiyat, urun.kategori, urun.menşei, urun.tedarikci))
        self.baglanti.commit()
        print("İşlem Başarılı")

    def urun_sil(self, isim, miktar, marka):
        sorgu = "Select * From ürünler where Ürün_Adı = ? and Miktar = ? and Marka = ?"
        self.cursor.execute(sorgu, (isim, miktar, marka))
        urunler = self.cursor.fetchall()

        if len(urunler) == 0:
            print("Bu özelliklerde bir ürün bulunmamaktadır...")
        else:
            sorgu2 = "DELETE FROM ürünler where Ürün_Adı = ? and Miktar = ? and Marka = ?"
            self.cursor.execute(sorgu2, (isim, miktar, marka))
            self.baglanti.commit()
            print("Başarı ile silindi...")
    def urun_ara(self, isim, giris):
        sorgu = "Select * From ürünler where Ürün_Adı = ?"
        self.cursor.execute(sorgu, (isim,))
        urunler = self.cursor.fetchall()

        if len(urunler) == 0:
            print("Böyle bir ürün bulunmamaktadır...")
        else:
            if giris == "kullanıcı":
                for i in urunler:
                    urun = Ürün(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
                    print(urun.kullaniciya())
            elif giris == "admin":
                for i in urunler:
                    urun = Ürün(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
                    print(urun)
    def sırala(self, olcut, giris):
        sorgu = "Select * From ürünler"
        self.cursor.execute(sorgu)
        urunler = self.cursor.fetchall()

        if len(urunler) == 0:
            print("Kayıtlı ürün bulunmamaktadır...")
        else:
            if olcut == "artan":
                urunler = sorted(urunler, key = lambda x: x[4])
            else:
                urunler = sorted(urunler, key=lambda x: x[4], reverse= True)

            if giris == "kullanıcı":
                for i in urunler:
                    urun = Ürün(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
                    print(urun.kullaniciya())
            elif giris == "admin":
                for i in urunler:
                    urun = Ürün(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
                    print(urun)
    def satin_al(self, isim, boy, miktar):
        sorgu = "Select * From ürünler where Ürün_Adı = ? and Miktar = ?"
        self.cursor.execute(sorgu, (isim, boy))
        urunler = self.cursor.fetchall()

        if len(urunler) == 0:
            print("Böyle bir ürün bulunmamaktadır...")
        else:
            stok = urunler[0][3]
            if stok == 0:
                print("Bu ürün stokta yok")
            elif stok < miktar:
                print("Stoktan daha fazla satın alım yapamazsınız")
            else:
                stok -= miktar
                sorgu2 = "UPDATE ürünler SET Stok = ? where Ürün_Adı = ? and Miktar = ?"
                self.cursor.execute(sorgu2, (stok, isim, boy))
                self.baglanti.commit()
                print("Satın alımınız için teşekkür ederiz...")
    def kategoriler(self):
        sorgu = "Select Kategori From ürünler"
        self.cursor.execute(sorgu)
        kategoriler = self.cursor.fetchall()

        if len(kategoriler) == 0:
            print("Kayıtlı ürün bulunmamaktadır...")
        else:
            for i in kategoriler:
                print(i[0])
    def kategoriye_gore_ara(self, kategori, giris):
        sorgu = "Select * From ürünler where Kategori = ?"
        self.cursor.execute(sorgu, (kategori,))
        ürünler = self.cursor.fetchall()

        if len(ürünler) == 0:
            print("Kayıtlı ürün bulunmamaktadır...")
        else:
            if giris == "kullanıcı":
                for i in ürünler:
                    urun = Ürün(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
                    print(urun.kullaniciya())
            else:
                for i in ürünler:
                    urun = Ürün(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
                    print(urun)
    def icinde_gecen(self, kelime, giris):
        sorgu = "Select * From ürünler"
        self.cursor.execute(sorgu)
        ürünler = self.cursor.fetchall()

        if len(ürünler) == 0:
            print("Kayıtlı ürün bulunmamaktadır...")
        else:
            sayac = 0
            for i in ürünler:
                urun = Ürün(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
                if kelime in urun.urun_adi and giris == "kullanıcı":
                    print(urun.kullaniciya())
                    sayac += 1
                elif kelime in urun.urun_adi and giris == "admin":
                    print(urun)
                    sayac += 1
            print("Toplam {} adet ürün bulundu.".format(sayac))

    def fiyat_degistir(self, urun, boyu, yeni_fiyat):
        sorgu = "Select * From ürünler where Ürün_Adı = ? and Miktar = ?"
        self.cursor.execute(sorgu, (urun, boyu))
        ürünler = self.cursor.fetchall()

        if len(ürünler) == 0:
            print("Böyle bir ürün bulunmamaktadır...")
        elif yeni_fiyat < 0:
            print("Negatif sayı giremezsiniz...")
        else:
            eski_fiyat = ürünler[0][4]
            sorgu2 = "UPDATE ürünler SET Fiyat = ? where Ürün_Adı = ? and Miktar = ?"
            self.cursor.execute(sorgu2, (yeni_fiyat, urun, boyu))
            self.baglanti.commit()
            print("İşlem başarılı.\n{} isimli ürünün {} boyunun yeni fiyatı {} olarak ayarlandı (eski fiyatı: {})...".format(urun, boyu, yeni_fiyat, eski_fiyat))
    def stok_ekle(self, urun, boy, stok):
        sorgu = "Select * From ürünler where Ürün_Adı = ? and Miktar = ?"
        self.cursor.execute(sorgu, (urun, boy))
        ürünler = self.cursor.fetchall()

        if len(ürünler) == 0:
            print("Böyle bir ürün bulunmamaktadır...")
        else:
            stok += ürünler[0][3]
            sorgu2 = "UPDATE ürünler SET Stok = ? where Ürün_Adı = ? and Miktar = ?"
            self.cursor.execute(sorgu2, (stok, urun, boy))
            self.baglanti.commit()
            print("İşlem başarılı")
    def stok_bitenler(self):
        sorgu = "Select * From ürünler where Stok = 0"
        self.cursor.execute(sorgu)
        ürünler = self.cursor.fetchall()

        if len(ürünler) == 0:
            print("Stoğu biten ürün bulunmamaktadır...")
        else:
            for i in ürünler:
                urun = Ürün(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
                print(urun)
    def markaya_gore_ara(self, marka, giris):
        sorgu = "Select * From ürünler where Marka = ?"
        self.cursor.execute(sorgu, (marka,))
        ürünler = self.cursor.fetchall()

        if len(ürünler) == 0:
            print("Bu markaya ait kayıtlı ürün bulunmamaktadır...")
        else:
            for i in ürünler:
                urun = Ürün(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
                if giris == "kullanıcı":
                    print(urun.kullaniciya())
                else:
                    print(urun)
    def menşei_listele(self):
        sorgu = "Select Menşei From ürünler"
        self.cursor.execute(sorgu)
        menseiler = self.cursor.fetchall()

        if len(menseiler) == 0:
            print("Kayıtlı ürün bulunmamaktadır...")
        else:
            mensei = set()
            for i in menseiler:
                mensei.add(i[0])
            for i in mensei:
                print(i)
    def tedarikciler(self):
        sorgu = "Select Tedarikçi From ürünler"
        self.cursor.execute(sorgu)
        tedarikciler = self.cursor.fetchall()

        if len(tedarikciler) == 0:
            print("Kayıtlı ürün bulunmamaktadır...")
        else:
            tedarikci = set()
            for i in tedarikciler:
                tedarikci.add(i[0])
            for i in tedarikci:
                print(i)
    def markalar(self):
        sorgu = "Select Marka From ürünler"
        self.cursor.execute(sorgu)
        markalar = self.cursor.fetchall()

        if len(markalar) == 0:
            print("Kayıtlı ürün bulunmamaktadır...")
        else:
            marka = set()
            for i in markalar:
                marka.add(i[0])
            for i in marka:
                print(i)
    def mensei_gore_ara(self, mensei, giris):
        sorgu = "Select * From ürünler where Menşei = ?"
        self.cursor.execute(sorgu, (mensei,))
        ürünler = self.cursor.fetchall()

        if len(ürünler) == 0:
            print("Bu menşeiden ürün bulunmamaktadır...")
        else:
            for i in ürünler:
                urun = Ürün(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])

                if giris == "kullanıcı":
                    print(urun.kullaniciya())
                else:
                    print(urun)
    def tedarikciye_gore_ara(self, tedarikci):
        sorgu = "Select * From ürünler where Tedarikçi = ?"
        self.cursor.execute(sorgu, (tedarikci,))
        ürünler = self.cursor.fetchall()

        if len(ürünler) == 0:
            print("Bu tedarikçiye ait ürün bulunmamaktadır...")
        else:
            for i in ürünler:
                urun = Ürün(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
                print(urun)
    def markaya_gore_sil(self, marka):
        sorgu = "Select * From ürünler where Marka = ?"
        self.cursor.execute(sorgu, (marka,))
        ürünler = self.cursor.fetchall()

        if len(ürünler) == 0:
            print("Bu markaya ait ürün bulunmamaktadır...")
        else:
            sorgu2 = "DELETE FROM ürünler where Marka = ?"
            self.cursor.execute(sorgu2, (marka,))
            self.baglanti.commit()
            print("{} isimli markaya ait ürünler başarı ile silindi.".format(marka))

    def stok_biten_sil(self):
        sorgu = "Select * From ürünler where Stok = 0"
        self.cursor.execute(sorgu)
        ürünler = self.cursor.fetchall()

        if len(ürünler) == 0:
            print("Stoğu tükenen ürün bulunmamaktadır...")
        else:
            sorgu2 = "DELETE FROM ürünler where Stok = 0"
            self.cursor.execute(sorgu2)
            self.baglanti.commit()
            print("Silme işlemi başarılı.")

    def tedarikciye_gore_sil(self, tedarikci):
        sorgu = "Select * From ürünler where Tedarikçi = ?"
        self.cursor.execute(sorgu, (tedarikci,))
        ürünler = self.cursor.fetchall()

        if len(ürünler) == 0:
            print("Bu tedarikçiye ait ürün bulunmamaktadır...")
        else:
            sorgu2 = "DELETE FROM ürünler where Tedarikçi = ?"
            self.cursor.execute(sorgu2, (tedarikci,))
            self.baglanti.commit()
            print("Silme işlemi başarılı.")

    def kategori_sil(self, kategori):
        sorgu = "Select * From ürünler where Kategori = ?"
        self.cursor.execute(sorgu, (kategori,))
        ürünler = self.cursor.fetchall()

        if len(ürünler) == 0:
            print("Bu kategoriye ait ürün bulunmamaktadır...")
        else:
            sorgu2 = "DELETE FROM ürünler where Kategori = ?"
            self.cursor.execute(sorgu2, (kategori,))
            self.baglanti.commit()
            print("Silme işlemi başarılı.")

    def mensei_sil(self, mensei):
        sorgu = "Select * From ürünler where Menşei = ?"
        self.cursor.execute(sorgu, (mensei,))
        ürünler = self.cursor.fetchall()

        if len(ürünler) == 0:
            print("Bu menşeiye ait ürün bulunmamaktadır...")
        else:
            sorgu2 = "DELETE FROM ürünler where Menşei = ?"
            self.cursor.execute(sorgu2, (mensei,))
            self.baglanti.commit()
            print("{} menşeisine ait ürünler silindi.".format(mensei))

    def kategori_ve_markaya_gore_ara(self, kategori, marka, giris):
        sorgu = "Select * From ürünler where Kategori = ? and Marka = ?"
        self.cursor.execute(sorgu, (kategori, marka))
        ürünler = self.cursor.fetchall()

        if len(ürünler) == 0:
            print("Bu özelliklerde ürün bulunmamaktadır...")
        else:
            for i in ürünler:
                urun = Ürün(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
                if giris == "kullanıcı":
                    print(urun.kullaniciya())
                else:
                    print(urun)




