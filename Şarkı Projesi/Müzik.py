import sqlite3
class Şarkı:
    def __init__(self, sarki_ismi, turu, dil, sanatci, album, produksiyon, sarki_suresi, satis_rakami = 0, kazanc = 0):
        self.sarki_ismi = sarki_ismi
        self.turu = turu
        self.dil = dil
        self.sanatci = sanatci
        self.album = album
        self.produksiyon = produksiyon
        self.sarki_suresi = sarki_suresi
        self.satis_rakami = satis_rakami
        self.kazanc = kazanc

    def __str__(self):
        return "\nŞarkı ismi: {}\nTür: {}\nDil: {}\nSanatçı: {}\nAlbüm: {}\nProdüksiyon: {}\nŞarkı Süresi: {}\nSatış Rakamı: {}\nKazanç: {}".format(self.sarki_ismi, self.turu, self.dil, self.sanatci, self.album, self.produksiyon, self.sarki_suresi, self.satis_rakami, self.kazanc)

    def kullaniciya_goster(self):
        return "\nŞarkı ismi: {}\nTür: {}\nDil: {}\nSanatçı: {}\nAlbüm: {}\nProdüksiyon: {}\nŞarkı Süresi: {}".format(self.sarki_ismi, self.turu, self.dil, self.sanatci, self.album, self.produksiyon, self.sarki_suresi)


class Uygulama:
    def __init__(self):
        self.baglanti_olustur()
        self.file = open("Log.txt", "a", encoding="utf-8")

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("müzik.db")
        self.cursor = self.baglanti.cursor()
        sorgu = "CREATE TABLE IF NOT EXISTS şarkılar (Şarkı_İsmi TEXT, Türü TEXT, Dil TEXT, Sanatçı TEXT, Albüm TEXT, Prodüksiyon TEXT, Şarkı_Süresi INT, Satış_Rakamı INT, Kazanç INT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def baglantiyi_kes(self):
        self.baglanti.close()
        self.file.close()

    def muzikleri_listele(self, giris):
        sorgu = "Select * From şarkılar"
        self.cursor.execute(sorgu)
        şarkılar = self.cursor.fetchall()

        if len(şarkılar) == 0:
            print("Kayıtlı Şarkı bulunmamaktadır...")
        elif giris == "kullanıcı":
            for i in şarkılar:
                sarki = Şarkı(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
                print(sarki.kullaniciya_goster())
        elif giris == "admin":
            for i in şarkılar:
                sarki = Şarkı(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
                print(sarki)

    def muzik_ekle(self, sarki):
        sorgu = "INSERT INTO şarkılar Values(?, ?, ?, ?, ?, ?, ?, ?, ?)"
        self.cursor.execute(sorgu, (sarki.sarki_ismi, sarki.turu, sarki.dil, sarki.sanatci, sarki.album, sarki.produksiyon, sarki.sarki_suresi, sarki.satis_rakami, sarki.kazanc))
        self.baglanti.commit()
        print("İşlem Başarılı")
        self.file.write("admin " + sarki.sarki_ismi + " isimli bir şarkı ekledi\n")

    def muzik_sorgula(self, sarki_ismi, giris):
        sorgu = "Select * From şarkılar where Şarkı_İsmi = ?"
        self.cursor.execute(sorgu, (sarki_ismi,))
        şarkılar = self.cursor.fetchall()

        if len(şarkılar) == 0:
            print("Böyle bir şarkı bulunmamaktadır...")
        elif giris == "kullanıcı":
            for i in şarkılar:
                sarki = Şarkı(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
                print(sarki.kullaniciya_goster())
        elif giris == "admin":
            for i in şarkılar:
                sarki = Şarkı(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
                print(sarki)
    def sarki_sil(self, sarki_ismi):
        sorgu = "Select * From şarkılar where Şarkı_İsmi = ?"
        self.cursor.execute(sorgu, (sarki_ismi,))
        şarkılar = self.cursor.fetchall()

        if len(şarkılar) == 0:
            print("Bu İsimde Bir Şarkı Bulunmamaktadır...")
        else:
            sorgu2 = "Delete From şarkılar where Şarkı_İsmi = ?"
            self.cursor.execute(sorgu2, (sarki_ismi,))
            self.baglanti.commit()
            print("İşlem Başarılı")
            self.file.write("admin " + sarki_ismi + " isimli şarkıyı sildi\n")

    def ture_gore_ara(self, tur, giris):
        sorgu = "Select * From şarkılar where Türü = ?"
        self.cursor.execute(sorgu, (tur,))
        şarkılar = self.cursor.fetchall()
        if len(şarkılar) == 0:
            print("Bu türde kayıtlı şarkı bulunmamaktadır...")
        elif giris == "kullanıcı":
            for i in şarkılar:
                sarki = Şarkı(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
                print(sarki.kullaniciya_goster())
        elif giris == "admin":
            for i in şarkılar:
                sarki = Şarkı(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
                print(sarki)
    def sanatciya_gore_ara(self, sanatci, giris):
        sorgu = "Select * From şarkılar where Sanatçı = ?"
        self.cursor.execute(sorgu, (sanatci,))
        şarkılar = self.cursor.fetchall()

        if len(şarkılar) == 0:
            print("Bu sanatçıya ait kayıtlı şarkı bulunmamaktadır...")
        elif giris == "kullanıcı":
            for i in şarkılar:
                sarki = Şarkı(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
                print(sarki.kullaniciya_goster())
        elif giris == "admin":
            for i in şarkılar:
                sarki = Şarkı(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
                print(sarki)
    def produksiyona_gore_ara(self, produksiyon, giris):
        sorgu = "Select * From şarkılar where Prodüksiyon = ?"
        self.cursor.execute(sorgu, (produksiyon,))
        şarkılar = self.cursor.fetchall()

        if len(şarkılar) == 0:
            print("Bu prodüksiyona ait kayıtlı şarkı bulunmamaktadır...")
        elif giris == "kullanıcı":
            for i in şarkılar:
                sarki = Şarkı(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
                print(sarki.kullaniciya_goster())
        elif giris == "admin":
            for i in şarkılar:
                sarki = Şarkı(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
                print(sarki)

    def toplam_sure(self):
        sorgu = "Select Şarkı_Süresi From şarkılar"
        self.cursor.execute(sorgu)
        sureler = self.cursor.fetchall()
        toplam = 0
        for i in sureler:
            toplam += i[0]
        print("Toplam Süre: {}".format(toplam))

    def muzik_al(self, isim):
        sorgu = "Select * From şarkılar where Şarkı_İsmi = ?"
        self.cursor.execute(sorgu, (isim,))
        şarkılar = self.cursor.fetchall()

        if len(şarkılar) == 0:
            print("Böyle bir şarkı bulunmamaktadır.")
        else:
            satıs = şarkılar[0][7]
            kazanc = şarkılar[0][8]
            satıs += 1
            kazanc += 10
            sorgu2 = "UPDATE şarkılar SET Satış_Rakamı = ? where Şarkı_İsmi = ?"
            sorgu3 = "UPDATE şarkılar SET Kazanç = ? where Şarkı_İsmi = ?"
            self.cursor.execute(sorgu2, (satıs, isim))
            self.cursor.execute(sorgu3, (kazanc, isim))
            self.baglanti.commit()
            print("Satın Alımınız İçin Teşekkür Ederiz...")
            self.file.write("kullanıcı " + isim + " isimli şarkı satın aldı\n")

    def toplam_kazanc(self):
        sorgu = "Select Kazanç From şarkılar"
        self.cursor.execute(sorgu)
        kazanclar = self.cursor.fetchall()

        if len(kazanclar) == 0:
            print("Kayıtlı Satış Bulunmamaktadır...")
        else:
            toplam = 0
            for i in kazanclar:
                toplam += i[0]
            print("Toplam Kazanç: {}".format(toplam))
    def produksiyona_gore_sil(self, produksiyon):
        sorgu = "Select * From şarkılar where Prodüksiyon = ?"
        self.cursor.execute(sorgu, (produksiyon,))
        produksiyonlar = self.cursor.fetchall()
        if len(produksiyonlar) == 0:
            print("Bu Prodüksiyona Ait Şarkı Bulunmamaktadır...")
        else:
            sorgu2 = "DELETE FROM şarkılar where Prodüksiyon = ?"
            self.cursor.execute(sorgu2, (produksiyon,))
            self.baglanti.commit()
            print("İşlem Başarılı...")

    def sanatciya_gore_sil(self, sanatci):
        sorgu = "Select * From şarkılar where Sanatçı = ?"
        self.cursor.execute(sorgu, (sanatci,))
        sarkilar = self.cursor.fetchall()

        if len(sarkilar) == 0:
            print("Bu Sanatçıya Ait Kayıtlı Şarkı Bulunmamaktadır...")
        else:
            sorgu2 = "DELETE FROM şarkılar where Sanatçı = ?"
            self.cursor.execute(sorgu2, (sanatci,))
            self.baglanti.commit()
            print("İşlem Başarılı...")
    def cok_satan(self):
        sorgu = "Select * From şarkılar"
        self.cursor.execute(sorgu)
        şarkılar = self.cursor.fetchall()

        if len(şarkılar) == 0:
            print("Kayıtlı Şarkı Bulunmamaktadır...")
        else:
            şarkılar = sorted(şarkılar, key = lambda x: x[7], reverse= True)
            for i in şarkılar[:3]:
                sarki = Şarkı(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
                print(sarki)
    def produksiyon_sarki_sayisi(self, produksiyon):
        sorgu = "Select * From şarkılar where Prodüksiyon = ? "
        self.cursor.execute(sorgu, (produksiyon,))
        şarkılar = self.cursor.fetchall()

        if len(şarkılar) == 0:
            print("Bu Prodüksiyona Ait Şarkı Bulunmamaktadır...")
        else:
            print("{} Prodüksiyonuna Ait {} Şarkı Bulunmaktadır.".format(produksiyon, len(şarkılar)))
    def sanatci_sarki_sayisi(self, sanatci):
        sorgu = "Select * From şarkılar where Sanatçı = ?"
        self.cursor.execute(sorgu, (sanatci,))
        şarkılar = self.cursor.fetchall()
        if len(şarkılar) == 0:
            print("Seçili Sanatçıya Ait Kayıtlı Şarkı Bulunmamaktadır...")
        else:
            print("{} İsimli Sanatçıya Ait {} Şarkı Bulunmaktadır.".format(sanatci, len(şarkılar)))
    def sanatci_cok_dinlenen(self, sanatci):
        sorgu = "Select * From şarkılar where Sanatçı = ?"
        self.cursor.execute(sorgu, (sanatci,))
        şarkılar = self.cursor.fetchall()

        if len(şarkılar) == 0:
            print("Seçili Sanatçıya Ait Şarkı Bulunmamaktadır...")
        else:
            şarkılar = sorted(şarkılar, key=lambda x: x[7], reverse=True)
            for i in şarkılar[:3]:
                sarki = Şarkı(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
                print(sarki)

    def dile_gore_ara(self, dil):
        sorgu = "Select * From şarkılar where Dil = ?"
        self.cursor.execute(sorgu, (dil,))
        şarkılar = self.cursor.fetchall()

        if len(şarkılar) == 0:
            print("Bu Dilde Kayıtlı Şarkı Bulunmamaktadır...")
        else:
            for i in şarkılar:
                sarki = Şarkı(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
                print(sarki)

    def genel_bilgiler(self):
        sorgu = "Select * From şarkılar"
        self.cursor.execute(sorgu)
        şarkılar = self.cursor.fetchall()
        sanatcilar = set()
        produksiyonlar = set()
        if len(şarkılar) == 0:
            print("Kayıtlı Şarkı Bulunmamaktadır...")
        else:
            for i in şarkılar:
                sanatcilar.add(i[3])
                produksiyonlar.add(i[5])
            print("""
                Toplam Şarkı Sayısı: {}
                Toplam Sanatçı Sayısı: {}
                Toplam Prodüksiyon Sayısı: {}
            """.format(len(şarkılar), len(sanatcilar), len(produksiyonlar)))
    def produksiyonlar(self):
        sorgu = "Select Prodüksiyon From şarkılar"
        self.cursor.execute(sorgu)
        prodüksiyonlar = self.cursor.fetchall()
        prods = set()
        if len(prodüksiyonlar) == 0:
            print("Kayıtlı Prodüksiyon Bulunmamaktadır...")
        else:
            for i in prodüksiyonlar:
                prods.add(i[0])

            for i in prods:
                print(i)
    def sanatcilar(self):
        sorgu = "Select Sanatçı From şarkılar"
        self.cursor.execute(sorgu)
        sanatcilar = self.cursor.fetchall()
        sanatci = set()
        if len(sanatcilar) == 0:
            print("Kayıtlı Sanatçı Bulunmamaktadır...")
        else:
            for i in sanatcilar:
                sanatci.add(i[0])
            for i in sanatci:
                print(i)
    def albume_gore_ara(self, album):
        sorgu = "Select * From şarkılar where Albüm = ?"
        self.cursor.execute(sorgu, (album,))
        şarkılar = self.cursor.fetchall()
        if len(şarkılar) == 0:
            print("Böyle Bir Albüm Bulunmamaktadır...")
        else:
            for i in şarkılar:
                sarki = Şarkı(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
                print(sarki)
    def sanatci_album_sayisi(self, sanatci):
        sorgu = "Select Albüm From şarkılar where Sanatçı = ?"
        self.cursor.execute(sorgu, (sanatci,))
        albumler = self.cursor.fetchall()
        album = set()
        if len(albumler) == 0:
            print("Bu Sanatçıya Ait Kayıtlı Albüm Bulunmamaktadır...")
        else:
            for i in albumler:
                album.add(i[0])
            print("Sanatçının {} Albümü Vardır.".format(len(album)))
            for i in album:
                print(i)
    def en_cok_satan_sanatcilar(self):
        sorgu = "Select * From şarkılar"
        self.cursor.execute(sorgu)
        şarkılar = self.cursor.fetchall()
        sıralama = dict()
        if len(şarkılar) == 0:
            print("Kayıtlı Şarkı Bulunmamaktadır...")
        else:
            for i in şarkılar:
                if i[3] in sıralama:
                    sıralama[i[3]] += i[7]
                else:
                    sıralama[i[3]] = i[7]
            print("En Çok Satan 3 Sanatçı: ")
            sıralanmıs_satis = sorted(sıralama.values(), reverse= True)
            for i in range(0, 3):
                for j, k in sıralama.items():
                    if sıralanmıs_satis[i] == k:
                        print(i+1,"-", j, "Satış Sayısı:", k)
    def sanatci_satis_sayisi(self, sanatci):
        sorgu = "Select Satış_Rakamı From şarkılar where Sanatçı = ?"
        self.cursor.execute(sorgu, (sanatci,))
        rakamlar = self.cursor.fetchall()
        if len(rakamlar) == 0:
            print("Bu İsimde Kayıtlı Sanatçı Bulunmamaktadır...")
        else:
            toplam = 0
            for i in rakamlar:
                toplam += i[0]
            print("{} İsimli Sanatçının Toplam Satışı : {}".format(sanatci, toplam))





