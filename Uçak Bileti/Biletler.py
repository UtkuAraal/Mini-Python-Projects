import sqlite3

class Bilet:
    def __init__(self, numara, nereden, nereye, saat, tarih, bos_bus_yolcu_sayisi, bos_eko_yolcu_sayisi, dolu_bus_yolcu_sayisi, dolu_eko_yolcu_sayisi, ucak_sirketi, ucus_suresi, fiyati, rotar):
        self.numara = numara
        self.nereden = nereden
        self.nereye = nereye
        self.saat = saat
        self.tarih = tarih
        self.bos_bus_yolcu_sayisi = bos_bus_yolcu_sayisi
        self.bos_eko_yolcu_sayisi = bos_eko_yolcu_sayisi
        self.dolu_bus_yolcu_sayisi = dolu_bus_yolcu_sayisi
        self.dolu_eko_yolcu_sayisi = dolu_eko_yolcu_sayisi
        self.ucak_sirketi = ucak_sirketi
        self.ucus_suresi = ucus_suresi
        self.fiyati = fiyati
        self.rotar = rotar
    def __str__(self):
        return """{}  {} - {}  {}--{}  {}                 {}                     {}             {}      {}      {}
        """.format(self.numara, self.nereden, self.nereye, self.saat, self.tarih, self.bos_bus_yolcu_sayisi, self.bos_eko_yolcu_sayisi, self.ucak_sirketi, self.ucus_suresi, self.fiyati, self.rotar)

class Biletler:
    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("Uçak.db")
        self.cursor = self.baglanti.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS biletler (Numara TEXT, Nereden TEXT, Nereye TEXT, Saat TEXT, Tarih TEXT, Boş_Bus_Yolcu_Sayısı INT, Boş_Eko_Yolcu_Sayısı INT, Dolu_Bus_Yolcu_Sayısı INT, Dolu_Eko_Yolcu_Sayısı INT, Uçak_Şirketi TEXT, Uçus_Süresi INT, Fiyatı INT, Rötar TEXT, Yolcu_Listesi TEXT)")
        self.baglanti.commit()

    def baglantiyi_kes(self):
        self.baglanti.close()

    def tablo(self):
        print("Numara   Nereden-Nereye   Saat-Tarih   Business koltuk   Ekonomi Koltuk   Uçak Şirketi   Uçuş Süresi   Fiyat   Rötar")

    def bilet_ekle(self, bilet):
        self.cursor.execute("Select * From biletler where Numara = ?", (bilet.numara,))
        kayitlar = self.cursor.fetchall()

        if len(kayitlar) != 0:
            print("Bu numaraya ait bir uçuş kaydı bulunmakta!")
        else:
            self.cursor.execute("INSERT INTO biletler Values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (bilet.numara, bilet.nereden, bilet.nereye, bilet.saat, bilet.tarih, bilet.bos_bus_yolcu_sayisi, bilet.bos_eko_yolcu_sayisi, bilet.dolu_bus_yolcu_sayisi, bilet.dolu_eko_yolcu_sayisi, bilet.ucak_sirketi, bilet.ucus_suresi, bilet.fiyati, bilet.rotar, ""))
            self.baglanti.commit()
            print("{} numaralı uçuş ilanı başarıyla sisteme girilmiştir!".format(bilet.numara))

    def biletler(self):
        self.cursor.execute("Select * From biletler")
        biletler = self.cursor.fetchall()

        if len(biletler) == 0:
            print("Kayıtlı uçuş bulunmamaktadır...")
        else:
            self.tablo()
            for i in biletler:
                bilet = Bilet(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12])
                print(bilet)

    def kayit_sil(self, numara):
        self.cursor.execute("Select * From biletler where Numara = ?", (numara,))
        ucus = self.cursor.fetchall()

        if len(ucus) == 0:
            print("Bu numaraya ait uçuş kaydı bulunmamaktadır...")
        else:
            self.cursor.execute("DELETE FROM biletler where Numara = ?", (numara,))
            self.baglanti.commit()
            print("{} nuamralı uçuş kaydı başarı ile silinmiştir...".format(numara))

    def ucus_numarası_ara(self, numara):
        self.cursor.execute("Select * From biletler where Numara = ?", (numara,))
        biletler = self.cursor.fetchall()

        if len(biletler) == 0:
            print("{} uçuş numarasıyla kayıtlı bilet bulunmamaktadır...".format(numara))
        else:
            self.tablo()
            for i in biletler:
                bilet = Bilet(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12])
                print(bilet)

    def bilet_al(self, numara, koltuk, kimlik):
        self.cursor.execute("Select Boş_Bus_Yolcu_Sayısı, Boş_Eko_Yolcu_Sayısı, Yolcu_Listesi, Dolu_Bus_Yolcu_Sayısı, Dolu_Eko_Yolcu_Sayısı From biletler where Numara = ?", (numara,))
        bilet = self.cursor.fetchall()

        if len(bilet) == 0:
            print("{} numarasına ait uçuş kaydı bulunmamaktadır...".format(numara))
        else:
            durum = True
            if koltuk == "business" and bilet[0][0] == 0:
                print("Business için boş koltuk kalmamıştır!")
                durum = False
            elif koltuk == "ekonomi" and bilet[0][1] == 0:
                print("Ekonomi için boş koltuk kalmamıştır!")
                durum = False

            if durum:
                yolcular = bilet[0][2] + "," + str(kimlik)
                if koltuk == "business":
                    sayi = bilet[0][0] - 1
                    dolu = bilet[0][3] + 1
                    self.cursor.execute("UPDATE biletler SET Boş_Bus_Yolcu_Sayısı = ?, Yolcu_Listesi = ?, Dolu_Bus_Yolcu_Sayısı = ? where Numara = ?", (sayi, yolcular, dolu, numara))
                else:
                    sayi = bilet[0][1] - 1
                    dolu = bilet[0][4] + 1
                    self.cursor.execute("UPDATE biletler SET Boş_Bus_Yolcu_Sayısı = ?, Yolcu_Listesi = ?, Dolu_Bus_Yolcu_Sayısı = ? where Numara = ?", (sayi, yolcular, dolu, numara))

                self.baglanti.commit()
                print("{} numaralı uçuşun {} bölümüne biletiniz kaydedilmiştir...".format(numara, koltuk))

    def yolcu_listesi(self, numara):
        self.cursor.execute("Select Yolcu_Listesi From biletler where Numara = ?", (numara,))
        yolcular = self.cursor.fetchall()

        if len(yolcular) == 0:
            print("Kayıtlı yolcu bulunmamaktadır...")
        else:
            yolcular = yolcular[0][0]
            liste = yolcular.split(",")
            for i in liste:
                print(i)

    def fiyata_gore_sirala(self):
        self.cursor.execute("Select * From biletler")
        biletler = self.cursor.fetchall()

        if len(biletler) == 0:
            print("Kayıtlı uçuş bulunmamaktadır...")
        else:
            biletler = sorted(biletler, key= lambda x: x[11])
            self.tablo()
            for i in biletler:
                bilet = Bilet(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12])
                print(bilet)

    def yolcu_ara(self, kimlik):
        self.cursor.execute("Select Numara, Yolcu_Listesi From biletler")
        bilgiler = self.cursor.fetchall()

        if len(bilgiler) == 0:
            print("Kayıtlı uçuş bulunmamaktadır...")
        else:
            sayac = 0
            for i in bilgiler:
                numara = i[0]
                yolcu_listesi = i[1].split(",")

                for j in yolcu_listesi:
                    if j == "":
                        pass
                    elif int(j) == kimlik:
                        print("{} kimlik numaralı yolcunun {} numaralı uçuşta kaydı bulunmaktadır.".format(kimlik, numara))
                        sayac += 1
            print("{} kimlik numaralı yolcunun {} adet kaydı bulunmaktadır.".format(kimlik, sayac))

    def yere_gore_ara(self, nereden, nereye):
        self.cursor.execute("Select * From biletler where Nereden = ? and Nereye  = ?", (nereden, nereye))
        biletler = self.cursor.fetchall()

        if len(biletler) == 0:
            print("Aranan kriterde uçak kaydı bulunmamaktadır...")
        else:
            self.tablo()
            for i in biletler:
                bilet = Bilet(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12])
                print(bilet)

    def kalkıs_yerine_gore(self, nereden):
        self.cursor.execute("Select * From biletler where Nereden = ?", (nereden,))
        biletler = self.cursor.fetchall()

        if len(biletler) == 0:
            print("Seçili yerden kalkacak uçak kaydı bulunmamaktadır...")
        else:
            self.tablo()
            for i in biletler:
                bilet = Bilet(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12])
                print(bilet)

    def varis_yerine_gore(self, nereye):
        self.cursor.execute("Select * From biletler where Nereye = ?", (nereye,))
        biletler = self.cursor.fetchall()

        if len(biletler) == 0:
            print("Seçili yere giden uçak kaydı bulunmamaktadır...")
        else:
            self.tablo()
            for i in biletler:
                bilet = Bilet(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12])
                print(bilet)

    def tarihe_gore_ara(self, tarih):
        self.cursor.execute("Select * From biletler where Tarih = ?", (tarih,))
        biletler = self.cursor.fetchall()

        if len(biletler) == 0:
            print("Seçilen tarihe kayıtlı uçak bulunmamaktadır...")
        else:
            self.tablo()
            for i in biletler:
                bilet = Bilet(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12])
                print(bilet)

    def ucak_doluluk_bilgisi(self, numara):
        self.cursor.execute("Select Boş_Bus_Yolcu_Sayısı, Boş_Eko_Yolcu_Sayısı, Dolu_Bus_Yolcu_Sayısı, Dolu_Eko_Yolcu_Sayısı, Uçak_Şirketi From biletler where Numara = ?", (numara,))
        biletler = self.cursor.fetchall()

        if len(biletler) == 0:
            print("{} numaralı uçuş kaydı bulunmamaktadır...")
        else:
            for i in biletler:
                bus_dolu = (i[2] * 100) / (i[0] + i[2])
                eko_dolu = (i[3] * 100) / (i[1] + i[3])
                print("""{} numaralı uçağın;
                Business Doluluk Oranı: {}
                Ekonomi Doluluk Oranı: {}
                """.format(numara, bus_dolu, eko_dolu))

    def ucak_sirketine_gore_ara(self, sirket):
        self.cursor.execute("Select * From biletler where Uçak_Şirketi = ?", (sirket,))
        biletler = self.cursor.fetchall()

        if len(biletler) == 0:
            print("{} uçak şirketine ait kayıtlı uçuş bulunmamaktadır...".format(sirket))
        else:
            self.tablo()
            for i in biletler:
                bilet = Bilet(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12])
                print(bilet)

    def rotarlar(self):
        self.cursor.execute("Select Numara, Uçak_Şirketi, Rötar From biletler where Rötar != '' and Rötar != 'yok'")
        bilgiler = self.cursor.fetchall()

        if len(bilgiler) == 0:
            print("Rötarlı uçak bulunmamaktadır...")
        else:
            print("Numara   Uçak-Şirketi   Rötar")
            for i in bilgiler:
                print("{}       {}       {}".format(i[0], i[1], i[2]))

    def rotar_ayarla(self, numara, rotar):
        self.cursor.execute("Select * From biletler where Numara = ?", (numara,))
        ucus = self.cursor.fetchall()

        if len(ucus) == 0:
            print("{} numarası ile kayıtlı uçuş bulunmamaktadır...")
        else:
            self.cursor.execute("UPDATE biletler SET Rötar = ? where Numara = ?", (rotar, numara))
            self.baglanti.commit()
            print("{} uçuş numaralı uçak için {} süreli rötar kaydı yapılmıştır.".format(numara, rotar))

