import sqlite3


class Firma:
    def __init__(self, isim, nerede, ucret, kac_kez = 1):
        self.isim = isim
        self.nerede = nerede
        self.ucret = ucret
        self.kac_kez = kac_kez

    def __str__(self):
        return "İsmi: {}\tNereden: {}\tÜcret: {}\tÇalışma Sayısı: {}".format(self.isim, self.nerede, self.ucret, self.kac_kez)


class Firmalar:
    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("ajans.db")
        self.cursor = self.baglanti.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS firmalar (İsim TEXT, Nereden TEXT, Ücret INT, Kac_Kez INT)")
        self.baglanti.commit()

    def baglantiyi_kes(self):
        self.baglanti.close()

    def firma_listele(self):
        self.cursor.execute("Select * From firmalar")
        firmalar = self.cursor.fetchall()

        if len(firmalar) == 0:
            print("Yapılan kayıtlı anlaşma bulunmamaktadır...")
        else:
            for i in firmalar:
                firma = Firma(i[0], i[1], i[2], i[3])
                print(firma)

    def firma_ekle(self, firma):
        self.cursor.execute("Select Kac_Kez From firmalar where İsim = ?", (firma.isim,))
        firma_sayi = self.cursor.fetchall()

        if len(firma_sayi) != 0:
            firma.kac_kez = len(firma_sayi) + 1

        if firma.kac_kez > 3:
            firma.ucret = firma.ucret - int(firma.ucret * (20 / 100))

        self.cursor.execute("INSERT INTO firmalar Values(?, ?, ?, ?)", (firma.isim, firma.nerede, firma.ucret, firma.kac_kez))
        self.baglanti.commit()
        print("{}'dan {} isimli firma ile {}. kez olan {} değerindeki anlaşma kayıt edilmiştir.".format(firma.nerede, firma.isim, firma.kac_kez, firma.ucret))

    def firma_ara(self, isim):
        self.cursor.execute("Select * From firmalar where İsim = ?", (isim,))
        anlasmalar = self.cursor.fetchall()

        if len(anlasmalar) == 0:
            print("Bu firma ile yapılmış kayıtlı anlaşma bulunmamaktadır...")
        else:
            for i in anlasmalar:
                firma = Firma(i[0], i[1], i[2], i[3])
                print(firma)

    def toplam_gelir(self):
        self.cursor.execute("Select Ücret From firmalar")
        ucretler = self.cursor.fetchall()
        toplam = 0
        if len(ucretler) == 0:
            return toplam
        else:
            for i in ucretler:
                toplam += i[0]
            return toplam



