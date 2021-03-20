import sqlite3

class Çalışan:

    def __init__(self, isim, soyisim, telefon, email, numara, pozisyon, maas, izin_sayisi = 15, kullandigi_izin = 0):
        self.isim = isim
        self.soyisim = soyisim
        self.telefon = telefon
        self.email = email
        self.numara = numara
        self.pozisyon = pozisyon
        self.maas = maas
        self.izin_sayisi = izin_sayisi
        self.kullandigi_izin = kullandigi_izin

    def __str__(self):
        return """
            İsim: {}
            Soyisim: {}
            Telefon: {}
            E-mail: {}
            Numara: {}
            Pozisyon: {}
            Maaş: {}
            İzin Günü Sayısı: {}
            Kullandığı İzin: {}
        """.format(self.isim, self.soyisim, self.telefon, self.email, self.numara, self.pozisyon, self.maas, self.izin_sayisi, self.kullandigi_izin)


class Çalışanlar:

    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("Çalışanlar.db")
        self.cursor = self.baglanti.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS çalışanlar (İsim TEXT, Soyisim TEXT, Telefon INT, Email TEXT, Numara INT, Pozisyon TEXT, Maaş INT, İzin_Sayısı INT, Kullandığı_İzin INT)")
        self.baglanti.commit()

    def baglantiyi_kes(self):
        self.baglanti.close()

    def calisan_ekle(self, calisan):
        self.cursor.execute("Select * From çalışanlar where Numara = ?", (calisan.numara,))
        calisanlar = self.cursor.fetchall()

        if len(calisanlar) != 0:
            print("Bu numara bir çalışana ait!")
        else:
            self.cursor.execute("INSERT INTO çalışanlar Values(?, ?, ?, ?, ?, ?, ?, ?, ?)", (calisan.isim, calisan.soyisim, calisan.telefon, calisan.email, calisan.numara, calisan.pozisyon, calisan.maas, calisan.izin_sayisi, calisan.kullandigi_izin))
            self.baglanti.commit()
            print("{} numaralı çalışan ekleme işlemi başarılı!".format(calisan.numara))

    def calisan_listele(self):
        self.cursor.execute("Select * From çalışanlar")
        calisanlar = self.cursor.fetchall()

        if len(calisanlar) == 0:
            print("Kayıtlı çalışan bulunmamaktadır...")
        else:
            for i in calisanlar:
                calisan = Çalışan(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
                print(calisan)

    def calisan_sil(self, numara):
        self.cursor.execute("Select * From çalışanlar where Numara = ?", (numara,))
        calisanlar = self.cursor.fetchall()

        if len(calisanlar) == 0:
            print("Bu numaraya ait çalışan bulunmamaktadır!")
        else:
            self.cursor.execute("DELETE FROM çalışanlar where Numara = ?", (numara,))
            self.baglanti.commit()
            print("{} numaralı çalışan kayıtlardan silindi!".format(numara))

    def pozisyona_gore_ara(self, pozisyon):
        self.cursor.execute("Select * From çalışanlar where Pozisyon = ?", (pozisyon,))
        calisanlar = self.cursor.fetchall()

        if len(calisanlar) == 0:
            print("Bu pozisyonda çalışan bulunmamaktadır...")
        else:
            for i in calisanlar:
                calisan = Çalışan(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
                print(calisan)

    def calisan_numaralari_goster(self):
        self.cursor.execute("Select İsim, Soyisim, Numara from çalışanlar")
        bilgiler = self.cursor.fetchall()

        if len(bilgiler) == 0:
            print("Kayıtlı çalışan bilgisi bulunmamaktadır...")
        else:
            for i in bilgiler:
                print("{} {} : {}".format(i[0], i[1], i[2]))

    def calisan_maas_guncelle(self, numara, miktar, secenek):
        self.cursor.execute("Select Maaş From çalışanlar where Numara = ?", (numara,))
        maas = self.cursor.fetchall()

        if len(maas) == 0:
            print("Bu numaraya ait çalışan bulunmamaktadır...")
        else:
            if secenek == "yuzde":
                yeni_maas = maas[0][0] + (maas[0][0] * (miktar / 100))
                yeni_maas = int(yeni_maas)
            else:
                yeni_maas = maas[0][0] + miktar

            self.cursor.execute("UPDATE çalışanlar SET Maaş = ? where Numara = ?", (yeni_maas, numara))
            self.baglanti.commit()
            print("{} numaralı çalışan maaşı {} olarak ayarlanmıştır.".format(numara, yeni_maas))

    def calisan_sorgula(self, numara):
        self.cursor.execute("Select * From çalışanlar where Numara = ?", (numara,))
        calisanlar = self.cursor.fetchall()

        if len(calisanlar) == 0:
            print("Bu numaraya ait çalışan bulunmamaktadır...")
        else:
            for i in calisanlar:
                calisan = Çalışan(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
                print(calisan)


    def izin_ver(self, numara, gun):
        self.cursor.execute("Select * From çalışanlar where Numara = ?", (numara,))
        calisanlar = self.cursor.fetchall()

        if len(calisanlar) == 0:
            print("Bu numaraya ait çalışan bulunmamaktadır...")
        else:
            izin = calisanlar[0][7] + gun
            self.cursor.execute("UPDATE çalışanlar SET İzin_Sayısı = ? where Numara = ?",(izin, numara))
            self.baglanti.commit()
            print("{} izin günü başarıyla tanımlandı.".format(gun))

    def izin_kullandi(self, numara, gun):
        self.cursor.execute("Select İzin_Sayısı, Kullandığı_İzin From çalışanlar where Numara = ?", (numara,))
        bilgi = self.cursor.fetchall()

        if len(bilgi) == 0:
            print("Bu numaraya ait çalışan bulunmamaktadır...")
        elif bilgi[0][0] < (bilgi[0][1] + gun):
            print("İzin gününü geçiyor! Tanımlama yapılamadı!\nGirebileceğiniz maksimum izin kullanma miktarı: {}".format(bilgi[0][0] - bilgi[0][1]))
        else:
            kullanilan = bilgi[0][1] + gun
            self.cursor.execute("UPDATE çalışanlar SET Kullandığı_İzin = ? where Numara = ?", (kullanilan, numara))
            self.baglanti.commit()
            print("{} kullanılan izin başarıyla eklendi!".format(gun))

    def isimle_numara_ara(self, isim, soyisim):
        self.cursor.execute("Select Numara From çalışanlar where İsim = ? and Soyisim = ?", (isim, soyisim))
        bilgi = self.cursor.fetchall()

        if len(bilgi) == 0:
            print("Bu isim ve soyisimde kayıtlı çalışan yok...")
        else:
            print("{} {} : {}".format(isim, soyisim, bilgi[0][0]))

    def odenen_maaslar(self):
        self.cursor.execute("Select Maaş From çalışanlar")
        bilgiler = self.cursor.fetchall()

        if len(bilgiler) == 0:
            print("Kayıtlı çalışan bulunmamaktadır!")
        else:
            toplam = 0
            for i in bilgiler:
                toplam += i[0]
            print("Ödenen toplam maaş: {}".format(toplam))

    def isimle_bilgi(self, isim, soyisim):
        self.cursor.execute("Select * From çalışanlar")
        calisanlar = self.cursor.fetchall()

        if len(calisanlar) == 0:
            print("Kayıtlı çalışan bulunmamaktadır...")
        else:
            sayac = 0
            for i in calisanlar:
                if (isim.lower() == i[0].lower()) and (soyisim.lower() == i[1].lower()):
                    calisan = Çalışan(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
                    print(calisan)
                    sayac += 1
            print("{} adet çalışan bulundu.".format(sayac))
















