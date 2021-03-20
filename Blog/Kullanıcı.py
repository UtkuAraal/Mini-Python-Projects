import sqlite3


class Kullanıcı:
    def __init__(self, kullanici_adi, email, parola, gizli_soru, gizli_cevap, makale_sayisi=0):
        self.kullanici_adi = kullanici_adi
        self.email = email
        self.parola = parola
        self.gizli_soru = gizli_soru
        self.gizli_cevap = gizli_cevap
        self.makale_sayisi = makale_sayisi

    def __str__(self):
        return """
            Kullanıcı Adı: {}
            Makale Sayısı: {}
            E-mail: {}
            Parola: {}
            Gizli Soru: {}
            Gizli Cevap: {}

        """.format(self.kullanici_adi, self.makale_sayisi, self.email, self.parola, self.gizli_soru, self.gizli_cevap)

    def kac_makale(self):
        return "Kullanıcı Adı: {}\tMakale Sayısı: {}".format(self.kullanici_adi, self.makale_sayisi)


class Kullanıcılar:
    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("Blog.db")
        self.cursor = self.baglanti.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS kullanicilar (Kullanıcı_Adı TEXT, Email TEXT, Parola TEXT, Gizli_Soru TEXT, Gizli_Cevap TEXT, Makale_Sayisi INT)")
        self.baglanti.commit()

    def baglantiyi_kes(self):
        self.baglanti.close()

    def kayit_log(self, kullanici):
        with open("log.txt", "a", encoding="utf-8") as file:
            file.write(
                kullanici.kullanici_adi + " kullanıcı adı ve " + kullanici.email + " emaili ile bir kullanıcı kayıt oldu!\n")

    def giris_log(self, kullanici_adi):
        with open("log.txt", "a", encoding="utf-8") as file:
            file.write(kullanici_adi + " isimli kullanıcı giriş yaptı!\n")

    def cikis_log(self, kullanici_adi):
        with open("log.txt", "a", encoding="utf-8") as file:
            file.write(kullanici_adi + " isimli kullanıcı çıkış yaptı!\n")

    def engel_log(self, kullanici_adi):
        with open("log.txt", "a", encoding="utf-8") as file:
            file.write(kullanici_adi + " isimli kullanıcı kaydı engellendi ve silindi!\n")

    def sil_log(self, kullanici_adi):
        with open("log.txt", "a", encoding="utf-8") as file:
            file.write(kullanici_adi + " isimli kullanıcı kaydı silindi!\n")


    def kayit_ol(self, kullanıcı):
        self.cursor.execute("Select * From kullanicilar where Kullanıcı_Adı = ? or Email = ?", (kullanıcı.kullanici_adi, kullanıcı.email))
        kullanicilar = self.cursor.fetchall()
        durum = "uygun"
        if len(kullanicilar) != 0:
            for i in kullanicilar:
                if kullanıcı.kullanici_adi == i[0] and kullanıcı.email == i[1]:
                    print("Bu kullanıcı adı ve E-email başka bir hesaba aittir!")
                    durum = "değil"
                elif kullanıcı.kullanici_adi == i[0]:
                    print("Bu kullanıcı adı başka bir hesaba aittir!")
                    durum = "değil"
                elif kullanıcı.email == i[1]:
                    print("Bu E-mail başka bir hesaba aittir!")
                    durum = "değil"

        with open("engellenenler.txt", "r", encoding= "utf-8") as file:
            engellenenler = []
            for i in file:
                engel = i.strip("\n")
                engellenenler.append(engel)

            for i in engellenenler:
                if kullanıcı.email == i:
                    print("Girilen email yasaklı listesinde!")
                    durum = "değil"

        if durum == "uygun":
            self.cursor.execute("INSERT INTO kullanicilar Values(?, ?, ?, ?, ?, ?)",
                                (kullanıcı.kullanici_adi, kullanıcı.email, kullanıcı.parola, kullanıcı.gizli_soru, kullanıcı.gizli_cevap, kullanıcı.makale_sayisi))
            self.baglanti.commit()
            print("Kullanıcı kaydı başarılı!")
            self.kayit_log(kullanıcı)

    def giris_yap(self, email, parola):
        self.cursor.execute("Select Kullanıcı_Adı From kullanicilar where Email = ? and Parola = ?", (email, parola))
        kullanici = self.cursor.fetchall()

        if len(kullanici) == 0:
            return ""
        else:
            self.giris_log(kullanici[0][0])
            return kullanici[0][0]

    def kullanici_bilgileri_listele(self, giris):
        if giris == "admin":
            self.cursor.execute("Select * From kullanicilar")
            kullanicilar = self.cursor.fetchall()

            for i in kullanicilar:
                kullanici = Kullanıcı(i[0], i[1], i[2], i[3], i[4], i[5])
                print(kullanici)
        else:
            print("Yetkiniz bulunmamaktadır!")

    def kullanici_makale_sayisi(self, kullanici_adi):
        self.cursor.execute("Select Makale_Sayisi From kullanicilar where Kullanıcı_Adı = ?", (kullanici_adi,))
        sayi = self.cursor.fetchall()

        if len(sayi) == 0:
            print("Bu isimde kullanıcı bulunmamaktadır...")
        else:
            print("{} isimli kullanıcıya ait makale sayısı: {}".format(kullanici_adi, sayi[0][0]))

    def gizli_soru(self, kullanici_adi, email):
        self.cursor.execute("Select Gizli_Soru, Gizli_Cevap, Parola From kullanicilar where Kullanıcı_Adı = ? and Email = ?", (kullanici_adi, email))
        bilgi = self.cursor.fetchall()

        if len(bilgi) == 0:
            raise Warning("Girilen bilgilerde hata var!")
        else:
            soru = bilgi[0][0]
            print(soru)
            cevap = input("Cevap: ")
            if cevap == bilgi[0][1]:
                return bilgi[0][2]
            else:
                raise Warning("Yanlış cevap!")

    def kullanicilar(self):
        self.cursor.execute("Select Kullanıcı_Adı From kullanicilar")
        kullanicilar = self.cursor.fetchall()

        for i in kullanicilar:
            print(i[0])

    def kullanici_sil(self, kullanici_adi):
        self.cursor.execute("Select * From kullanicilar where Kullanıcı_Adı = ?", (kullanici_adi,))
        kullanici = self.cursor.fetchall()

        if len(kullanici) == 0:
            print("Böyle bir kullanıcı bulunmamaktadır...")
        else:
            cevap = input("{} isimli kullanıcıyı silmek istediğinize emin misiniz? (E/H)".format(kullanici_adi))
            if cevap == "E":
                self.cursor.execute("DELETE FROM kullanicilar where Kullanıcı_Adı = ?", (kullanici_adi,))
                self.baglanti.commit()
                self.sil_log(kullanici_adi)
                print("{} isimli kullanıcı kaydı başarı ile silindi.".format(kullanici_adi))
            else:
                print("{} isimli kullanıcıyı silme işlemi iptal edildi.")

    def kullanici_engelle(self, kullanici_adi):
        self.cursor.execute("Select Email From kullanicilar where Kullanıcı_Adı = ?", (kullanici_adi,))
        kullanici = self.cursor.fetchall()

        if len(kullanici) == 0:
            print("{} isminde bir kullanıcı bulunmamaktadır...".format(kullanici_adi,))
        else:
            cevap = input("{} isimli kullanıcıyı engellemek istediğinize emin misiniz? (E/H)".format(kullanici_adi))
            if cevap == "E":
                self.cursor.execute("DELETE FROM kullanicilar where Kullanıcı_Adı = ?", (kullanici_adi,))
                self.baglanti.commit()
                with open("engellenenler.txt", "a", encoding="utf-8") as file:
                    file.write(kullanici[0][0] + "\n")
                self.engel_log(kullanici_adi)
                print("{} isimli kullanıcı kaydı başarı ile silindi ve engellendi.".format(kullanici_adi))
            else:
                print("{} isimli kullanıcıyı engelleme işlemi iptal edildi.")

    def makalesiz_kullanicilar(self):
        self.cursor.execute("Select Kullanıcı_Adı From kullanicilar where Makale_Sayisi = 0")
        kullanicilar = self.cursor.fetchall()

        if len(kullanicilar) == 0:
            print("Makalesi olmayan kullanıcı bulunmamaktadır...")
        else:
            for i in kullanicilar:
                print(i[0])





