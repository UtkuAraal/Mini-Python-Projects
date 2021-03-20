import sqlite3
import requests
from bs4 import BeautifulSoup
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

class Kitap:
    def __init__(self, adi, yazar, yayinevi, tur, sayfa_sayisi, cilt, kitap_no = 0, durumu = "uygun", numara = 0, aldıgı_tarih = ""):
        self.adi = adi
        self.yazar = yazar
        self.yayinevi = yayinevi
        self.tur = tur
        self.sayfa_sayisi = sayfa_sayisi
        self.cilt = cilt
        self.kitap_no = kitap_no
        self.durumu = durumu
        self.numara = numara
        self.aldıgı_tarih = aldıgı_tarih

    def __str__(self):
        return """
            Adı: {}
            Yazarı: {}
            Yayınevi: {}
            Türü: {}
            Sayfa Sayısı: {}
            Cilt Numarası: {}
            Kitap Numarası: {}
            Durumu: {}
            Teslim Alan Kişi Kayıt Numarası: {}  
            Aldığı Tarih: {}
        """.format(self.adi, self.yazar, self.yayinevi, self.tur, self.sayfa_sayisi, self.cilt, self.kitap_no, self.durumu, self.numara, self.aldıgı_tarih)


class Kutuphane:
    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("KutuphaneV2.db")
        self.cursor = self.baglanti.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS kitaplar (Adı TEXT, Yazar TEXT, Yayınevi TEXT, Tür TEXT, Sayfa_Sayısı INT, Cilt INT, Kitap_No INT, Durum TEXT, Numara INT, Tarih TEXT)")
        self.baglanti.commit()

    def baglantiyi_kes(self):
        self.baglanti.close()

    def kitap_ekle(self, kitap):
        self.cursor.execute("Select * From kitaplar")
        kitaplar = self.cursor.fetchall()

        sayi = kitaplar[-1][6] + 1

        self.cursor.execute("INSERT INTO kitaplar Values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (kitap.adi, kitap.yazar, kitap.yayinevi, kitap.tur, kitap.sayfa_sayisi, kitap.cilt, sayi, kitap.durumu, kitap.numara, kitap.aldıgı_tarih))
        self.baglanti.commit()
        print("{} isimli kitap {} numarası ile sisteme kaydedilmiştir.".format(kitap.adi, sayi))

    def kitap_sil(self, kitap_no):
        self.cursor.execute("Select * From kitaplar where Kitap_No = ?", (kitap_no,))
        kitap = self.cursor.fetchall()

        if len(kitap) == 0:
            print("Bu numaraya ait kitap bulunmamaktadır!")
        else:
            secim = input("{} numaralı {} isimli kitabı silmek istediğinizden emin misiniz ?(E/H)".format(kitap_no, kitap[0][0]))
            if secim == "E":
                self.cursor.execute("Delete From kitaplar where Kitap_No = ?", (kitap_no,))
                self.baglanti.commit()
                print("Silme işlemi başarılı!")
            elif secim == "H":
                print("Silme işlemi iptal edildi!")
            else:
                print("Geçersiz tuş girişinden dolayı silme işlemi iptal edildi!")

    def kitapları_listele(self):
        self.cursor.execute("Select * From kitaplar")
        kitaplar = self.cursor.fetchall()

        if len(kitaplar) == 0:
            print("Kütüphaneye kayıtlı kitap bulunmamaktadır...")
        else:
            for i in kitaplar:
                kitap = Kitap(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9])
                print(kitap)

    def isim_ile_ara(self, kitap_adi):
        self.cursor.execute("Select * From kitaplar where Adı = ?", (kitap_adi,))
        kitaplar = self.cursor.fetchall()

        if len(kitaplar) == 0:
            print("Bu isme sahip kitap kaydı bulunmamaktadır.")
        else:
            for i in kitaplar:
                kitap = Kitap(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9])
                print(kitap)

    def yazar_ara(self, yazar):
        self.cursor.execute("Select * From kitaplar where Yazar = ?", (yazar,))
        kitaplar = self.cursor.fetchall()

        if len(kitaplar) == 0:
            print(yazar, "isimli yazara ait kayıtlı kitap bulunmamaktadır.")
        else:
            for i in kitaplar:
                kitap = Kitap(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9])
                print(kitap)

    def mail_gonder(self, kime):
        mesaj = MIMEMultipart()

        mesaj["From"] = "89D5C9@gmail.com"
        mesaj["To"] = kime
        mesaj["Subject"] = "Kütüphanedeki kitaplar"
        yazi = ""

        self.cursor.execute("Select * From kitaplar")
        kitaplar = self.cursor.fetchall()

        if len(kitaplar) == 0:
            yazi = "Kayıtlı kitap bulunmamaktadır."
        else:
            s = 0
            for i in kitaplar:
                s += 1
                yazi += str(s) + ". " + i[0] + "\n"

        mesaj_govdesi = MIMEText(yazi, "plain")
        mesaj.attach(mesaj_govdesi)

        try:
            mail = smtplib.SMTP("smtp.gmail.com", 587)
            mail.ehlo()
            mail.starttls()
            mail.login("89D5C9@gmail.com", "utkuyagiz2001")
            mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
            print("Mail gönderme işlemi başarılı!")
            mail.close()
        except:
            sys.stderr.write("Bir sorun oluştu!")
            sys.stderr.flush()

    def ture_gore_ara(self, tur):
        self.cursor.execute("Select * From kitaplar where Tür = ?", (tur,))
        kitaplar = self.cursor.fetchall()

        if len(kitaplar) == 0:
            print(tur, "türüne ait kayıtlı kitap bulunmamaktadır.")
        else:
            for i in kitaplar:
                kitap = Kitap(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9])
                print(kitap)

    def kitap_ver(self, kitap_no, numara):
        self.cursor.execute("Select * From kitaplar where Kitap_No = ?", (kitap_no,))
        kitap = self.cursor.fetchall()

        if len(kitap) == 0:
            print(kitap_no, "numaralı kayıtlı kitap bulunmamaktadır.")
        elif kitap[0][7] != "uygun":
            print(kitap_no, "kitap numarasına sahip", kitap[0][0], "isimli kitabın durumu uygun değildir!")
        else:
            self.cursor.execute("Update kitaplar SET Durum = 'meşgul', Numara = ?, Tarih = ? where Kitap_No = ?", (numara, datetime.datetime.now(), kitap_no))
            self.baglanti.commit()
            print(str(kitap_no), "numaralı kitap", str(numara), "numaralı üyeye teslim kaydı yapılmıştır!")

    def kitap_teslim(self, kitap_no):
        self.cursor.execute("Select Durum From kitaplar where Kitap_No = ?", (kitap_no,))
        kitap = self.cursor.fetchall()

        if len(kitap) == 0:
            print("Bu kitap numarasına sahip kitap bulunmamaktadır.")
        elif kitap[0][0] == "uygun":
            print(kitap_no, "numarasına ait kitap zaten uygun durumda gözüküyor!")
        else:
            self.cursor.execute("UPDATE kitaplar SET Durum = 'uygun', Numara = 0, Tarih = '' where Kitap_No = ?", (kitap_no,))
            self.baglanti.commit()
            print("Kitap başarı ile teslim alındı!")

    def yeni_cikanlar(self):
        url = "https://www.kitapsepeti.com/urun/listele/yeni-cikan-kitaplar/491?gclid=Cj0KCQiAj9iBBhCJARIsAE9qRtBAA88S_1t7dIrEYvXSV8rOwvz5Wufgy6Iesbp4CilPQn7Id5izKNkaAgGbEALw_wcB"
        response = requests.get(url)
        content = response.content
        soup = BeautifulSoup(content, "html.parser")

        for i in soup.find_all("p", {"class":"title"}):
            print(i.text)

    def yayinevine_gore_ara(self, yayinevi):
        self.cursor.execute("Select * From kitaplar where Yayınevi = ?", (yayinevi,))
        kitaplar = self.cursor.fetchall()

        if len(kitaplar) == 0:
            print("Bu yayınevine ait kayıtlı kitap bulunmamaktadır.")
        else:
            for i in kitaplar:
                kitap = Kitap(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9])
                print(kitap)

    def yazara_ait_kitaplar(self, yazar):
        self.cursor.execute("Select Adı from kitaplar where Yazar = ?", (yazar,))
        kitaplar = self.cursor.fetchall()

        if len(kitaplar) == 0:
            print(yazar, "isimli yazara ait kayıtlı kitap bulunmamaktadır.")
        else:
            kitap_isimleri = set()

            for i in kitaplar:
                kitap_isimleri.add(i[0])

            for i in kitap_isimleri:
                print(i)

    def yazara_gore_sil(self, yazar):
        self.cursor.execute("Select * From kitaplar where Yazar = ?", (yazar,))
        kitaplar = self.cursor.fetchall()

        if len(kitaplar) == 0:
            print("Bu yazara ait kayıtlı kitap bulunmamaktadır.")
        else:
            self.cursor.execute("Dlete From kitaplar where Yazar = ?", (yazar,))
            self.baglanti.commit()
            print(yazar, "isimli yazara ait kitap kayıtları başarı ile silindi.")

    def ture_gore_sil(self, tur):
        self.cursor.execute("Select * From kitaplar where Tür = ?", (tur,))
        kitaplar = self.baglanti.commit()

        if len(kitaplar) == 0:
            print(tur, "türüne ait kayıtlı kitap bulunmamaktadır.")
        else:
            self.cursor.execute("Select * From kitaplar where Tür = ?", (tur,))
            self.baglanti.commit()
            print(tur, "türüne ait kitaplar başarı ile silindi.")

    def yayınevine_gore_sil(self, yayınevi):
        self.cursor.execute("Select * From kitaplar where Yayınevi = ?", (yayınevi,))
        kitaplar = self.cursor.fetchall()

        if len(kitaplar) == 0:
            print(yayınevi, "yayınevine ait kayıtlı kitap bulunmamaktadır.")
        else:
            self.cursor.execute("Delete From kitaplar where Yayınevi = ?", (yayınevi,))
            self.baglanti.commit()
            print(yayınevi, "isimli yayıenvine ait kayıtlı kitaplar başarı ile silindi.")

    def icinde_gecen_kelime_ile_arama(self, kelime):
        self.cursor.execute("Select * From kitaplar")
        kitaplar = self.cursor.fetchall()

        if len(kitaplar) == 0:
            print("Kayıtlı kitap bulunmamaktadır.")
        else:
            for i in kitaplar:
                if kelime.lower() in i[0].lower():
                    kitap = Kitap(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9])
                    print(kitap)










