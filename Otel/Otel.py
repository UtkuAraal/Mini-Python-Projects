import sqlite3
import random

class Oda:
    def __init__(self, numara, durum = "boş", baslangic_rezervasyon = "yapılmadı", bitis_rezervasyon = "yapılmadı", isim = "", soyisim= "", telefon = 0, gun = 0, ucret = 0):
        self.numara = numara
        self.durum = durum
        self.baslangic_rezervasyon = baslangic_rezervasyon
        self.bitis_rezervasyon = bitis_rezervasyon
        self.isim = isim
        self.soyisim = soyisim
        self.telefon = telefon
        self.gun = gun
        self.ucret = ucret

    def __str__(self):
        return """
            Oda;
        Numarası: {}
        Durumu: {}
        Rezervasyon Başlangıcı: {}
        Rezervasyon Bitişi: {}
        İsim Soyisim: {} {}
        Telefon: {}
        Kaç Gün Kalacaklar: {}
        Ücret: {}
        
        """.format(self.numara, self.durum, self.baslangic_rezervasyon, self.bitis_rezervasyon, self.isim.capitalize(), self.soyisim.capitalize(), self.telefon, self.gun, self.ucret)

class Otel:
    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("Otel.db")
        self.cursor = self.baglanti.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS odalar (Numara INT, Durum TEXT, Başlangıç_Rezervasyonu TEXT, Bitiş_Rezervasyonu TEXT, İsim TEXT, Soyisim TEXT, Telefon INT, Gün INT, Ücret INT)")
        self.baglanti.commit()

    def baglantiyi_kes(self):
        self.baglanti.close()

    def oda_tanimla(self):
        for i in range(1, 31):
            oda = Oda(i)
            self.cursor.execute("INSERT INTO odalar Values(?, ?, ?, ?, ?, ?, ?, ?, ?)", (oda.numara, oda.durum, oda.baslangic_rezervasyon, oda.bitis_rezervasyon, oda.isim, oda.soyisim, oda.telefon, oda.gun, oda.ucret))
            self.baglanti.commit()

    def bos_oda_sayisi(self):
        self.cursor.execute("Select Numara From odalar where Durum = ?", ("boş",))
        bos_numaralar = self.cursor.fetchall()
        return len(bos_numaralar)

    def oda_ver(self, baslangic, bitis, isim, soyisim, telefon, gun):
        self.cursor.execute("Select Numara From odalar where Durum = 'boş'")
        bos_numaralar = self.cursor.fetchall()

        if len(bos_numaralar) == 0:
            print("Boş oda bulunmamaktadır...")
        else:
            bos_numaralar = [i[0] for i in bos_numaralar]
            oda = random.choice(bos_numaralar)
            ucret = gun * 50
            self.cursor.execute("UPDATE odalar SET Durum = 'dolu', Başlangıç_Rezervasyonu = ?, Bitiş_Rezervasyonu = ?, İsim = ?, Soyisim= ?, Telefon = ?, Gün = ?, Ücret = ? WHERE Numara = ?", (baslangic, bitis, isim.lower(), soyisim.lower(), telefon, gun, ucret, oda))
            self.baglanti.commit()
            print("{} {} isimli müşteriye {} numaralı oda başarıyla tanımlanmıştır!".format(isim, soyisim, oda))

    def oda_bosalt(self, numara):
        self.cursor.execute("Select Durum, Ücret From odalar where Numara = ?", (numara,))
        oda = self.cursor.fetchall()

        if oda[0][0] == "boş":
            print("{} numaralı oda zaten boş gözükmektedir...".format(numara))
        else:
            ucret = oda[0][1]
            self.cursor.execute("UPDATE odalar SET Durum = 'boş', Başlangıç_Rezervasyonu = 'yapılmadı', Bitiş_Rezervasyonu = 'yapılmadı', İsim = '', Soyisim= '', Telefon = 0, Gün = 0, Ücret = 0 WHERE Numara = ?", (numara,))
            self.baglanti.commit()
            print("{} numaralı oda başarı ile boşaltılmıştır. Odanın ücreti: {}".format(numara, ucret))


    def oda_bilgileri(self):
        self.cursor.execute("Select * From odalar")
        odalar = self.cursor.fetchall()

        for i in odalar:
            oda = Oda(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
            print(oda)

    def oda_durumlari(self):
        self.cursor.execute("Select Numara, Durum From odalar")
        odalar = self.cursor.fetchall()

        for i in odalar:
            print("Numara: {}\tDurum: {}".format(i[0], i[1]))

    def dolu_odalar(self):
        self.cursor.execute("Select * From odalar where Durum = 'dolu'")
        odalar = self.cursor.fetchall()

        if len(odalar) == 0:
            print("Dolu oda bulunmamaktadır...")
        else:
            for i in odalar:
                oda = Oda(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
                print(oda)

    def en_uzun_sure_rezerveli(self):
        self.cursor.execute("Select Numara, Gün, İsim, Soyisim From odalar where Durum = 'dolu'")
        bilgiler = self.cursor.fetchall()

        if len(bilgiler) == 0:
            print("Dolu oda bulunmamaktadır...")
        else:
            bilgiler = sorted(bilgiler, key= lambda x: x[1], reverse= True)
            for i in range(4):
                print("Numara: {}\tRezervasyonlu Gün Sayısı: {}\tİsim Soyisim: {} {}".format(bilgiler[i][0], bilgiler[i][1], bilgiler[i][2], bilgiler[i][3]))

    def en_yuksek_ucretli(self):
        self.cursor.execute("Select Numara, Ücret, İsim, Soyisim From odalar where Durum = 'dolu'")
        odalar = self.cursor.fetchall()

        if len(odalar) == 0:
            print("Dolu oda bulunmamaktadır...")
        else:
            odalar = sorted(odalar, key= lambda x: x[1], reverse= True)
            for i in range(4):
                print("Numara: {}\tÜcreti: {}\tİsim Soyisim: {} {}".format(odalar[i][0], odalar[i][1], odalar[i][2], odalar[i][3]))

    def oda_bilgisi(self, numara):
        self.cursor.execute("Select * From odalar where Numara = ?", (numara,))
        odalar = self.cursor.fetchall()

        oda = Oda(odalar[0][0], odalar[0][1], odalar[0][2], odalar[0][3], odalar[0][4], odalar[0][5], odalar[0][6], odalar[0][7], odalar[0][8])
        print(oda)

    def isimle_musteri_arama(self, isim, soyisim):
        self.cursor.execute("Select * From odalar where İsim = ? and Soyisim = ?", (isim.lower(), soyisim.lower()))
        bilgi = self.cursor.fetchall()

        if len(bilgi) == 0:
            print("{} {} isminde bir müşteri bulunmamaktadır...".format(isim, soyisim))
        else:
            for i in bilgi:
                oda = Oda(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
                print(oda)

    def numara_ile_musteri(self, telefon):
        self.cursor.execute("Select * From odalar where Telefon = ?", (telefon,))
        bilgi = self.cursor.fetchall()

        if len(bilgi) == 0:
            print("{} telefon numarası ile oda kaydı bulunmamaktadır...".format(telefon))
        else:
            for i in bilgi:
                oda = Oda(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
                print(oda)

    def dolu_oda_bitis_tarihleri(self):
        self.cursor.execute("Select Numara, Bitiş_Rezervasyonu, İsim, Soyisim, Telefon From odalar where Durum = 'dolu'")
        odalar = self.cursor.fetchall()

        if len(odalar) == 0:
            print("Dolu oda bulunmamaktadır...")
        else:
            for i in odalar:
                print("Numara: {}\tRezervasyon Bitiş Tarihi: {}\tİsim Soyisim: {} {}\tTelefon: {}".format(i[0], i[1], i[2], i[3], i[4]))

    def dolu_bos_odalar(self):
        self.cursor.execute("Select Numara, Durum From odalar")
        odalar = self.cursor.fetchall()

        for i in odalar:
            print("Numara: {}\tDurum: {}".format(i[0], i[1]))

    def dolu_oda_musterileri(self):
        self.cursor.execute("Select Numara, İsim, Soyisim, Telefon From odalar where Durum = 'dolu'")
        odalar = self.cursor.fetchall()

        if len(odalar) == 0:
            print("Dolu oda bulunmamaktadır...")
        else:
            for i in odalar:
                print("Numara: {}\t İsim Soyisim: {} {}\tTelefon: {}".format(i[0], i[1], i[2], i[3]))

    def bitis_gun_guncelle(self, numara, bitis, gun):
        self.cursor.execute("Select Durum, Gün, Ücret From odalar where Numara = ?", (numara,))
        bilgi = self.cursor.fetchall()

        if bilgi[0][0] == "boş":
            print("Bu odada kayıtlı müşteri bulunmamaktadır...")
        else:
            guncel_ucret = bilgi[0][2] + (gun * 50)
            guncel_gun =  bilgi[0][1] + gun

            self.cursor.execute("UPDATE odalar SET Bitiş_Rezervasyonu = ?, Gün = ?, Ücret = ? where Numara = ?", (bitis, guncel_gun, guncel_ucret, numara))
            self.baglanti.commit()
            print("{} numaralı odanın rezervasyonu {} gün uzatıldı.".format(numara, gun))



