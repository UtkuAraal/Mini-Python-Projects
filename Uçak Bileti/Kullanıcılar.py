import sqlite3


class Kullanıcı:
    def __init__(self, isim, soyisim, kimlik, parola):
        self.isim = isim
        self.soyisim = soyisim
        self.kimlik = kimlik
        self.parola = parola

class Kullanicilar:
    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("Uçak.db")
        self.cursor = self.baglanti.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS kullanicilar (İsim TEXT, Soyisim TEXT, Kimlik INT, Parola TEXT)")

    def baglanti_kes(self):
        self.baglanti.close()

    def kayit_ol(self, kullanıcı):
        self.cursor.execute("Select * From kullanicilar where Kimlik = ?", (kullanıcı.kimlik,))
        kayit = self.cursor.fetchall()

        if len(kayit) != 0:
            print("Bu kimlik ile mevcut bir kayıt bulunmaktadır...")
        else:
            lines = list()
            durum = True
            with open("engellenenler.txt", "r", encoding="utf-8") as file:
                for i in file:
                    lines.append(i)
            users = ""
            for i in lines:
                users += i
            users.replace("/n", "")
            users = users.split(",")
            for i in users:
                if i == "":
                    pass
                elif int(i) == kullanıcı.kimlik:
                    print("Engellenmiş kullanıcı bilgisi bulunduğu için kayıt işlemi tamamlanamadı!")
                    durum = False
            if durum:
                self.cursor.execute("INSERT INTO kullanicilar Values(?, ?, ?, ?)", (kullanıcı.isim, kullanıcı.soyisim, kullanıcı.kimlik, kullanıcı.parola))
                self.baglanti.commit()
                print("Kayıt işleminiz başarılı sayın {} {}".format(kullanıcı.isim, kullanıcı.soyisim))

    def giris_yap(self, kimlik, parola):
        self.cursor.execute("Select * From kullanicilar where Kimlik = ? and Parola = ?", (kimlik, parola))
        bilgiler = self.cursor.fetchall()

        if len(bilgiler) == 0:
            print("Hatalı giriş!")
        else:
            return [bilgiler[0][0], bilgiler[0][1], bilgiler[0][2]]

    def kullanici_sil_ve_engelle(self, kimlik):
        self.cursor.execute("Select * From kullanicilar where Kimlik = ?", (kimlik,))
        kullanici = self.cursor.fetchall()

        if len(kullanici) == 0:
            print("Bu kimlik bilgisine ait kullanıcı kaydı bulunmamaktadır...")
        else:
            cevap = input("{} {} isimli ve {} kimlik numaralı kullanıcıyı silinecek ve engellenecektir. Onay veriyor musunuz ? (E/H): ".format(kullanici[0][0], kullanici[0][1], kullanici[0][2]))
            if cevap == "E":
                self.cursor.execute("DELETE FROM kullanicilar where Kimlik = ?", (kimlik,))
                self.baglanti.commit()
                with open("engellenenler.txt", "a", encoding="utf-8") as file:
                    file.write(str(kimlik) + ",")
                print("{} {} isimli ve {} kimlik numaralı kullanıcıyı başarı ile silinmiş ve engellenmiştir.".format(kullanici[0][0], kullanici[0][1], kullanici[0][2]))

    def kullanici_sil(self, kimlik):
        self.cursor.execute("Select * From kullanicilar where Kimlik = ?", (kimlik,))
        bilgi = self.cursor.fetchall()

        if len(bilgi) == 0:
            print("Bu kimlik bilgisine ait kullanıcı bulunmamaktadır...")
        else:
            cevap = input("{} {} isimli ve {} kimlik numaralı kullanıcıyı silinecektir. Onay veriyor musunuz ? (E/H): ".format(bilgi[0][0], bilgi[0][1], bilgi[0][2]))
            if cevap == "E":
                self.cursor.execute("DELETE FROM kullanicilar where Kimlik = ?", (kimlik,))
                self.baglanti.commit()
                print("{} {} isimli ve {} kimlik numaralı kullanıcı başarı ile silinmiştir.".format(bilgi[0][0], bilgi[0][1], bilgi[0][2]))

    def kullanici_bilgileri(self):
        self.cursor.execute("Select * From kullanicilar")
        kullanicilar = self.cursor.fetchall()

        for i in kullanicilar:
            print("Kimlik: {}\t\tİsim-Soyisim: {} {}".format(i[2], i[0], i[1]))

    def kimlikle_ara(self, kimlik):
        self.cursor.execute("Select * From kullanicilar where Kimlik = ?", (kimlik,))
        kullanici = self.cursor.fetchall()

        if len(kullanici) == 0:
            print("{} kimlik bilgisine ait kullanıcı kaydı bulunmamaktadır...".format(kimlik))
        else:
            for i in kullanici:
                print("Kimlik: {}\t\tİsim-Soyisim: {} {}".format(i[2], i[0], i[1]))

    def isim_soyisim_ara(self, isim, soyisim):
        self.cursor.execute("Select * From kullanicilar where İsim = ? and Soyisim = ?", (isim, soyisim))
        kullanicilar = self.cursor.fetchall()

        if len(kullanicilar) == 0:
            print("{} {} isminde bir kullanıcı kaydı bulunmamaktadır...".format(isim, soyisim))
        else:
            for i in kullanicilar:
                print("Kimlik: {}\t\tİsim-Soyisim: {} {}".format(i[2], i[0], i[1]))



    