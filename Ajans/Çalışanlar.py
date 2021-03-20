import sqlite3

class Çalışan:
    def __init__(self, isim, soyisim, pozisyon, maas, izin_gunu, kullandigi_izin, numara = 0):
        self.numara = numara
        self.isim = isim
        self.soyisim = soyisim
        self.pozisyon = pozisyon
        self.maas = maas
        self.izin_gunu = izin_gunu
        self.kullandigi_izin = kullandigi_izin

    def __str__(self):
        return """
            Numara: {}
            İsim: {}
            Soyisim: {}
            Pozisyon: {}
            Maaş: {}
            İzin Günü: {}
            Kullandigi İzin: {}        
        """.format(self.numara, self.isim, self.soyisim, self.pozisyon.capitalize(), self.maas, self.izin_gunu, self.kullandigi_izin)


class Oyuncu(Çalışan):

    def __init__(self, isim, soyisim, pozisyon, maas, izin_gunu, kullandigi_izin, kategori, uygunluk = "uygun", proje = "", baslangic = "", bitis = "", numara = 0):
        super().__init__(isim, soyisim, pozisyon, maas, izin_gunu, kullandigi_izin, numara)
        self.kategori = kategori
        self.uygunluk = uygunluk
        self.proje = proje
        self.baslangic = baslangic
        self.bitis = bitis

    def __str__(self):
        return """
            Numara: {}
            İsim: {}
            Soyisim: {}
            Pozisyon: {}
            Maaş: {}
            İzin Günü: {}
            Kullandigi İzin: {}        
            Kategori: {}
            Uygunluk: {}
               """.format(self.numara, self.isim, self.soyisim, self.pozisyon.capitalize(), self.maas, self.izin_gunu, self.kullandigi_izin, self.kategori.capitalize(), self.uygunluk.capitalize())
    def yardimciya(self):
        return """
            Numara: {}
            İsim: {}
            Soyisim: {}
            Pozisyon: {}
            Maaş: {}
            İzin Günü: {}
            Kullandigi İzin: {}        
            Uygunluk: {}
                       """.format(self.numara, self.isim, self.soyisim, self.pozisyon.capitalize(), self.maas, self.izin_gunu,
                                  self.kullandigi_izin, self.uygunluk.capitalize())

class Teknik(Çalışan):
    def __init__(self, isim, soyisim, pozisyon, maas, izin_gunu, kullandigi_izin, uygunluk="uygun", proje = "", baslangic = "", bitis = "", numara = 0):
        super().__init__(isim, soyisim, pozisyon, maas, izin_gunu, kullandigi_izin, numara)
        self.uygunluk = uygunluk
        self.proje = proje
        self.baslangic = baslangic
        self.bitis = bitis

    def __str__(self):
        return """
            Numara: {}
            İsim: {}
            Soyisim: {}
            Pozisyon: {}
            Maaş: {}
            İzin Günü: {}
            Kullandigi İzin: {}        
            Uygunluk: {}
                       """.format(self.numara, self.isim, self.soyisim, self.pozisyon.capitalize(), self.maas, self.izin_gunu,
                                  self.kullandigi_izin, self.uygunluk.capitalize())

class Çalışanlar:
    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("ajans.db")
        self.cursor = self.baglanti.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS çalışanlar (İsim TEXT, Soyisim TEXT, Pozisyon TEXT, Maaş INT, İzin_Günü INT, Kullandığı_izin INT, Kategori TEXT, Uygunluk TEXT, Proje TEXT, Baslangic TEXT, Bitis TEXT, Numara INT)")
        self.baglanti.commit()

    def baglanti_kes(self):
        self.baglanti.close()

    def calisanlari_listele(self, giris):
        self.cursor.execute("Select * From çalışanlar")
        calisanlar = self.cursor.fetchall()

        if len(calisanlar) == 0:
            print("Kayıtlı çalışan bulunmamaktadır...")
        else:
            for i in calisanlar:
                if i[2] == "ofis":
                    ofis = Çalışan(i[0], i[1], i[2], i[3], i[4], i[5], i[11])
                    print(ofis)
                elif i[2] == "teknik":
                    teknik = Teknik(i[0], i[1], i[2], i[3], i[4], i[5], i[7], i[8], i[9], i[10], i[11])
                    print(teknik)
                else:
                    if giris == "yardimci":
                        oyuncu = Oyuncu(i[0], i[1], i[2], i[3], i[4], i[5], "Yetki Yok!", i[7], i[8], i[9], i[10], i[11])
                    else:
                        oyuncu = Oyuncu(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11])
                    print(oyuncu)
    def calisan_ekle(self, calisan):
        self.cursor.execute("Select Numara From çalışanlar")
        numaralar = self.cursor.fetchall()

        if len(numaralar) == 0:
            numara = 1
        else:
            numaralar = [i[0] for i in numaralar]
            numara = max(numaralar) + 1

        if calisan.pozisyon == "oyuncu":
            self.cursor.execute("INSERT INTO çalışanlar Values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (calisan.isim, calisan.soyisim, calisan.pozisyon.lower(), calisan.maas, calisan.izin_gunu, calisan.kullandigi_izin, calisan.kategori.lower(), calisan.uygunluk, calisan.proje, calisan.baslangic, calisan.bitis, numara))
        elif calisan.pozisyon == "teknik":
            self.cursor.execute("INSERT INTO çalışanlar Values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (calisan.isim, calisan.soyisim, calisan.pozisyon.lower(), calisan.maas, calisan.izin_gunu, calisan.kullandigi_izin, "", calisan.uygunluk.lower(), calisan.proje, calisan.baslangic, calisan.bitis, numara))
        else:
            self.cursor.execute("INSERT INTO çalışanlar Values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (calisan.isim, calisan.soyisim, calisan.pozisyon.lower(), calisan.maas, calisan.izin_gunu, calisan.kullandigi_izin, "", "", "", "", "", numara))
        self.baglanti.commit()

    def calisan_sil(self, numara):
        self.cursor.execute("Select * From çalışanlar where Numara = ?", (numara,))
        calisan = self.cursor.fetchall()

        if len(calisan) == 0:
            print("Bu numaraya ait çalışan bulunmamaktadır...")
        else:
            self.cursor.execute("DELETE FROM çalışanlar where Numara = ?", (numara,))
            self.baglanti.commit()
            print("{} numaralı çalışan kaydı başarı ile silindi...".format(numara))

    def oyunculari_listele(self, giris):
        self.cursor.execute("Select * From çalışanlar where Pozisyon = 'oyuncu'")
        oyuncular = self.cursor.fetchall()

        if len(oyuncular) == 0:
            print("Kayıtlı oyuncu bulunmamaktadır...")
        else:
            for i in oyuncular:
                oyuncu = Oyuncu(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11])
                if giris == "mudur":
                    print(oyuncu)
                elif giris == "yardimci":
                    print(oyuncu.yardimciya())

    def teknikler_listele(self):
        self.cursor.execute("Select * From çalışanlar where Pozisyon = 'teknik'")
        teknikler = self.cursor.fetchall()

        if len(teknikler) == 0:
            print("Kayıtlı teknik ekip çalışanı bulunmamaktadır...")
        else:
            for i in teknikler:
                teknik = Teknik(i[0], i[1], i[2], i[3], i[4], i[5], i[7], i[8], i[9], i[10], i[11])
                print(teknik)

    def maas_guncelle(self, numara, tur, miktar):
        self.cursor.execute("Select Maaş From çalışanlar where Numara = ?", (numara,))
        maas = self.cursor.fetchall()

        if len(maas) == 0:
            print("Bu numaraya ait çalışan bulunmamaktadır...")
        else:
            eski_maas = maas[0][0]
            if tur == "yuzde":
                yeni_maas = eski_maas + int(eski_maas * miktar / 100)
            elif tur == "birim":
                yeni_maas = eski_maas + miktar
            else:
                raise Warning("Uygun olmayan değer!")

            self.cursor.execute("UPDATE çalışanlar SET Maaş = ? where Numara = ?", (yeni_maas, numara))
            self.baglanti.commit()
            print("{} numaralı çalışanın {} olan maaşı, {} olarak güncellenmiştir.".format(numara, eski_maas, yeni_maas))

    def oyuncu_numaralari(self):
        self.cursor.execute("Select İsim, Soyisim, Numara, Uygunluk, Kategori From çalışanlar where Pozisyon = 'oyuncu'")
        oyuncular = self.cursor.fetchall()
        if len(oyuncular) == 0:
            print("Kayıtlı oyuncu bulunmamaktadır...")
        else:
            for i in oyuncular:
                print("{} {} {} {} {}".format(i[3].capitalize(), i[4].capitalize(), i[0], i[1], i[2]))

    def proje_ata(self, numara, proje, baslangic, bitis):
        self.cursor.execute("Select Uygunluk, Proje, Baslangic, Bitis, İsim, Soyisim, Kategori, Pozisyon From çalışanlar where Numara = ?", (numara,))
        oyuncu = self.cursor.fetchall()

        if len(oyuncu) == 0:
            print("Bu numaraya ait çalışan bulunmamaktadır...")
        elif oyuncu[0][7] != "oyuncu":
            print("Seçtiğiniz çalışan oyuncu olarak çalışmamaktadır. {} ekibinde çalışmaktadır.".format(oyuncu[0][7]))
        elif oyuncu[0][0] != "uygun":
            print("{} nuamralı çalışan {} - {} tarhileri arasında {} projesiyle meşgul olduğu için atama yapamazsınız...".format(numara, oyuncu[0][2], oyuncu[0][3], oyuncu[0][1]))
        else:
            self.cursor.execute("UPDATE çalışanlar SET Uygunluk = 'mesgul', Proje = ?, Baslangic = ?, Bitis = ? where Numara = ?", (proje, baslangic, bitis, numara))
            self.baglanti.commit()
            print("{} {} isimli {} numaralı {} kategorisinden oyuncuya {} - {} tarihleri arasında {} proje ataması yapılmıştır.".format(oyuncu[0][4], oyuncu[0][5], numara, oyuncu[0][6].capitalize(), baslangic, bitis, proje))

    def teknik_numaralari(self):
        self.cursor.execute("Select İsim, Soyisim, Numara, Uygunluk from çalışanlar where Pozisyon = 'teknik'")
        teknikler = self.cursor.fetchall()

        if len(teknikler) == 0:
            print("Kayıtlı teknik ekip bulunmamaktadır...")
        else:
            for i in teknikler:
                print("{} {} {} {}". format(i[3].capitalize(), i[0], i[1], i[2]))

    def teknik_proje_ata(self, numara, proje, baslangic, bitis):
        self.cursor.execute("Select Uygunluk, Proje, Baslangic, Bitis, İsim, Soyisim, Pozisyon From çalışanlar where Numara = ?", (numara,))
        teknik = self.cursor.fetchall()

        if len(teknik) == 0:
            print("Bu numaraya ait çalışan bulunmamaktadır...")
        elif teknik[0][6] != "teknik":
            print("Seçtiğiniz çalışan teknik ekipten değildir. {} ekibinde çalışmaktadır.".format(teknik[0][6].capitalize()))
        else:
            self.cursor.execute("UPDATE çalışanlar SET Uygunluk = 'mesgul', Proje = ?, Baslangic = ?, Bitis = ? where Numara = ?",(proje, baslangic, bitis, numara))
            self.baglanti.commit()
            print("{} {} isimli {} numaralı teknik ekibi çalışanı {} - {} tarihleri arasında {} proje ataması yapılmıştır.".format(teknik[0][4], teknik[0][5], numara, baslangic, bitis, proje))

    def oyuncu_projesini_gor(self, numara):
        self.cursor.execute("Select * From çalışanlar where Numara = ?", (numara,))
        calisan = self.cursor.fetchall()

        if len(calisan) == 0:
            print("Bu numaraya ait çalışan bulunamaktadır...")
        elif calisan[0][7] != "mesgul":
            print("Bu çalışanın mevcut projesi yoktur...")
        elif calisan[0][2] != "oyuncu":
            print("Bu numaraya ait çalışan oyuncu bölümünden değildir. {} ekibindedir.".format(calisan[0][2]))
        else:
            for i in calisan:
                oyuncu = Oyuncu(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11])
            print("""
                Numara: {}
                İsim - Soyisim: {} {}
                Kategori: {}
                Proje: {}
                Başlangıç: {}
                Bitiş: {}
                
            """.format(oyuncu.numara, oyuncu.isim, oyuncu.soyisim, oyuncu.kategori.capitalize(), oyuncu.proje, oyuncu.baslangic, oyuncu.bitis))

    def teknik_projesini_gor(self, numara):
        self.cursor.execute("Select * From çalışanlar where Numara = ?", (numara,))
        calisan = self.cursor.fetchall()

        if len(calisan) == 0:
            print("Bu numaraya ait çalışan bulunmamaktadır...")
        elif calisan[0][7] != "mesgul":
            print("Bu çalışanın mevcut projesi yoktur...")
        elif calisan[0][2] != "teknik":
            print("Bu numaraya ait çalışan oyuncu bölümünden değildir. {} ekibindedir.".format(calisan[0][2].capitalize()))
        else:
            for i in calisan:
                teknik = Teknik(i[0], i[1], i[2], i[3], i[4], i[5], i[7], i[8], i[9], i[10], i[11])
            print("""
                Numara: {}
                İsim - Soyisim: {} {}
                Proje: {}
                Başlangıç: {}
                Bitiş: {}

            """.format(teknik.numara, teknik.isim, teknik.soyisim, teknik.proje, teknik.baslangic,
                       teknik.bitis))

    def calisan_numaralari(self):
        self.cursor.execute("Select Numara, İsim, Soyisim, Pozisyon From çalışanlar")
        calisanlar = self.cursor.fetchall()

        if len(calisanlar) == 0:
            print("Kayıtlı çalışan bulunmamaktadır...")
        else:
            for i in calisanlar:
                print("{} {} {} {}".format(i[0], i[1], i[2], i[3].capitalize()))

    def izin_gunu(self, numara, hak):
        self.cursor.execute("Select İzin_Günü, Kullandığı_izin From çalışanlar where Numara = ?", (numara,))
        gun = self.cursor.fetchall()

        if len(gun) == 0:
            print("Bu numaraya ait çalışan bulunmamaktadır...")
        elif hak <= 0:
            print("Hatalı giriş!")
        else:
            izin = gun[0][0]
            izin += hak
            kullanilan = gun[0][1]
            kalan = izin - kullanilan
            self.cursor.execute("UPDATE çalışanlar SET İzin_Günü = ? where Numara = ?", (izin, numara))
            self.baglanti.commit()
            print("{} numaralı çalışana {} gün daha izin tanımlanmıştır.\nToplam izin: {}\nKullanılan izin: {}\nKalan izin: {}".format(numara, hak, izin, kullanilan, kalan))

    def kullanilan_izin(self, numara, kullanilan):
        self.cursor.execute("Select Kullandığı_izin, İzin_Günü From çalışanlar where Numara = ?", (numara,))
        haklar = self.cursor.fetchall()

        if len(haklar) == 0:
            print("Bu numaraya ait çalışan bulunmamaktadır...")
        elif kullanilan <= 0:
            print("Hatalı giriş!")
        else:
            son_kullanilan = haklar[0][0] + kullanilan
            izin = haklar[0][1]
            kalan = izin - son_kullanilan
            self.cursor.execute("UPDATE çalışanlar SET Kullandığı_izin = ? where Numara = ?", (son_kullanilan, numara))
            self.baglanti.commit()
            print("{} numaralı çalışana {} gün kullanılan izin tanımlanmıştır.\nToplam izin: {}\nKullanılan izin: {}\nKalan izin: {}".format(numara, kullanilan, izin, son_kullanilan, kalan))

    def oyuncu_kategorisiz_numara(self):
        self.cursor.execute("Select Numara, İsim, Soyisim From çalışanlar where Pozisyon = 'oyuncu'")
        oyuncular = self.cursor.fetchall()

        if len(oyuncular) == 0:
            print("Kayıtlı oyuncu bulunmamaktadır...")
        else:
            for i in oyuncular:
                print("{} {} {}".format(i[0], i[1], i[2]))

    def ofis_isim_numara(self):
        self.cursor.execute("Select Numara, İsim, Soyisim From çalışanlar where Pozisyon = 'ofis'")
        ofisler = self.cursor.fetchall()

        if len(ofisler) == 0:
            print("Kayıtlı ofis çalışanı bulunmamaktadır...")
        else:
            for i in ofisler:
                print("{} {} {}".format(i[0], i[1], i[2]))

    def teknik_isim_numara(self):
        self.cursor.execute("Select Numara, İsim, Soyisim From çalışanlar where Pozisyon = 'teknik'")
        teknikler = self.cursor.fetchall()

        if len(teknikler) == 0:
            print("Kayıtlı teknik ekip çalışanı bulunmamaktadır...")
        else:
            for i in teknikler:
                print("{} {} {}".format(i[0], i[1], i[2]))
    def calisan_proje_liste(self):
        self.cursor.execute("Select Numara, İsim, Soyisim, Pozisyon, Uygunluk, Proje, Baslangic, Bitis From çalışanlar where Pozisyon = 'oyuncu' or Pozisyon = 'teknik'")
        calisanlar = self.cursor.fetchall()

        if len(calisanlar) == 0:
            print("Kayıtlı oyuncu veya teknik ekip çalışanı bulunmamaktadır...")
        else:
            for i in calisanlar:
                if i[4] !=  "uygun":
                    print("{} - {} - {} - {} - {} - {} - {} - {}".format(i[0], i[1], i[2], i[3].capitalize(), i[4].capitalize(), i[5], i[6], i[7]))

    def proje_sil(self, numara):
        self.cursor.execute("Select Uygunluk, Pozisyon, Proje From çalışanlar where Numara = ?", (numara,))
        bilgi = self.cursor.fetchall()

        if len(bilgi) == 0:
            print("Bu numaraya ait çalışan bulunmamaktadır...")
        elif bilgi[0][0] == "uygun":
            print("Bu çalışanın projesi bulunmamaktadır...")
        elif bilgi[0][1] == "ofis":
            print("Bu nuamraya ait çalışan ofis çalışanıdır. Proje işlemleri yapılamaz...")
        else:
            self.cursor.execute("UPDATE çalışanlar SET Uygunluk = 'uygun', Proje = '', Baslangic = '', Bitis = '' where Numara = ?", (numara,))
            self.baglanti.commit()
            print("{} numaralı çalışanın {} isimli projesi silinmiştir...".format(numara, bilgi[0][2]))


    def ofis_listle(self):
        self.cursor.execute("Select * From çalışanlar where Pozisyon = 'ofis'")
        ofisler = self.cursor.fetchall()

        if len(ofisler) == 0:
            print("Kayıtlı ofis çalışanı bulunmamaktadır...")
        else:
            for i in ofisler:
                ofis = Çalışan(i[0], i[1], i[2], i[3], i[4], i[5], i[11])
                print(ofis)

    def maas_gider(self):
        self.cursor.execute("Select Maaş From çalışanlar")
        maaslar = self.cursor.fetchall()
        toplam = 0
        if len(maaslar) == 0:
            return toplam
        else:
            for i in maaslar:
                toplam += i[0]
            return toplam


