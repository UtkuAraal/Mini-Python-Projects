import random
import time

class Kumanda():

    def __init__(self, tv_durum = "Kapalı", tv_ses = 0, kanal_listesi = ["Trt"], kanal = "Trt", kayıtlı_siteler = ["Google"], varsayılan_site = "Google"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal
        self.kayıtlı_siteler = kayıtlı_siteler
        self.varsayılan_site = varsayılan_site

    def tv_ac(self):
        if (self.tv_durum == "Açık"):
            print("Televizyon zaten açık...")
        else:
            print("Telvizyon açılıyor...")
            self.tv_durum = "Açık"

    def tv_kapat(self):
        if (self.tv_durum == "Kapalı"):
            print("Telvizyon zaten kapalı...")
        else:
            print("Televizyon kapanıyor...")
            self.tv_durum = "Kapalı"

    def ses_ayarla(self):
        while True:
            cevap = input("Sesi Azalt: '<'\nSesi Artır: '>'\nÇıkış : çıkış")

            if (cevap == "<"):

                if (self.tv_ses != 0):
                    self.tv_ses -= 1
                    print("Ses:", self.tv_ses)
            elif (cevap == ">"):
                if (self.tv_ses != 31):
                    self.tv_ses += 1
                    print("Ses:", self.tv_ses)
            else:
                print("Ses Güncellendi:", self.tv_ses)
                break

    def kanal_ekle(self, kanal_ismi):
        print("Kanal Ekleniyor")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("Kanal Eklendi")

    def rastgele_kanal(self):
        rastgele = random.randint(0, len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele]
        print("Şu anki kanal:", self.kanal)

    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):
        return "Tv durumu : {}\nTv ses : {}\nKanal listesi : {}\nŞu anki kanal : {}\nKayıtlı Siteler = {}\nVarsayılan Site = {}".format(self.tv_durum, self.tv_ses, self.kanal_listesi, self.kanal, self.kayıtlı_siteler, self.varsayılan_site)

    def siteleri_listele(self):
        print(self.kayıtlı_siteler)
    def site_ekle(self, site_adı):
        self.kayıtlı_siteler.append(site_adı)
        print("Site Eklendi...")
    def site_sil(self, site_adı):
        self.kayıtlı_siteler.pop(self.kayıtlı_siteler.index(site_adı))
        print("Site Silindi...")
    def varsayılan_site_degistir(self):
        rastgele = random.choice(self.kayıtlı_siteler)
        self.varsayılan_site = rastgele
        print("Varsayılan Site: ", self.varsayılan_site)

kumanda = Kumanda()

print("""
Televizyon Uygulaması

1. Tv Aç

2. Tv Kapat

3. Ses Ayarları

4. Kanal Ekle

5. Kanal Sayısını Öğrenme

6. Rastgele Kanala Geçme

7. Televizyon Bilgileri

8. Siteleri Listele

9. Site Ekle

10. Site Sil

11. Varsayılan Siteyi Değiştir

Çıkmak için 'q' ya basın.
""")

while True:
    işlem = input("İşlemi Seçiniz : ")

    if (işlem == "q"):
        print("Program Sonlandırılıyor")
        break
    elif (işlem == "1"):
        kumanda.tv_ac()
    elif  (işlem == "2"):
        kumanda.tv_kapat()
    elif (işlem == "3"):
        kumanda.ses_ayarla()
    elif (işlem == "4"):
        kanal_isimleri = input("Kanal isimlerini ',' ile ayırarak girin : ")

        kanal_listesi = kanal_isimleri.split(",")

        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
    elif (işlem == "5"):
        print("Kanal Sayısı:", len(kumanda))
    elif (işlem == "6"):
        kumanda.rastgele_kanal()
    elif (işlem == "7"):
        print(kumanda)
    elif (işlem == "8"):
        kumanda.siteleri_listele()
    elif (işlem == "9"):
        yeni_site = input("Site Adı : ")
        kumanda.site_ekle(yeni_site)
    elif (işlem == "10"):
        silinecek = input("Silinecek Site Adı: ")
        kumanda.site_sil(silinecek)
    elif (işlem == "11"):
        kumanda.varsayılan_site_degistir()
    else:
        print("Geçersiz İşlem...")

