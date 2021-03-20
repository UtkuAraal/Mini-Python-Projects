import random
import time
class Bilgisayar():


    def __init__(self, pc_durum = "Kapalı", uygulamalar = ["Chrome"], açık_uygulama = "Yok", pc_ram = 4, pc_ekran_kartı = 4):
        self.pc_durum = pc_durum
        self.uygulamalar = uygulamalar
        self.açık_uygulama = açık_uygulama
        self.pc_ram = pc_ram
        self.pc_ekran_kartı = pc_ekran_kartı

    def pc_ac(self):
        if self.pc_durum == "Açık":
            print("Bilgisayar zaten açık...")
        else:
            print("Bilgisayar açılıyor...")
            time.sleep(1)
            self.pc_durum = "Açık"
    def pc_kapat(self):
        if self.pc_durum == "Kapalı":
            print("Bilgisayar zaten kapalı...")
        else:
            if (self.açık_uygulama != "Yok"):
                print("Lütfen önce açık uygulamaları kapatın")
            else:
                print("Bilgisayar kapatılıyor...")
                time.sleep(1)
                self.pc_durum = "Kapalı"
    def uygulama_listele(self):
        print(self.uygulamalar)
    def uygulama_ekle(self):
        yeni_uygulama = input("Eklemek istediğiniz uyuglama adını girin: ")
        self.uygulamalar.append(yeni_uygulama)
        print(yeni_uygulama, "isimli uygulama eklendi.")
    def uygulama_sil(self):
        silinecek = input("Silinecek uygulama adı giriniz : ")
        if (silinecek in self.uygulamalar):
            self.uygulamalar.pop(self.uygulamalar.index(silinecek))
            print(silinecek, "isimli uygulama başarı ile silindi.")
        else:
            print("Böyle bir uygulama bulunmamaktadır.")

    def uygulama_ac(self):
        açılacak = input("Açılacak uygulama ismi giriniz: ")
        if (açılacak in self.uygulamalar):
            self.açık_uygulama = açılacak
            print("Uygulama açıldı...")
        else:
            print("Böyle bir uygulama bulunmamaktadır.")
    def uygulamaları_kapat(self):
        if self.açık_uygulama == "Yok":
            print("Açık uygulama bulunmamaktadır")
        else:
            self.açık_uygulama = "Yok"
            print("Uygulama kapatıldı.")

    def rastgele_uygulama_ac(self):
        rastgele = random.choice(self.uygulamalar)
        self.açık_uygulama = rastgele
        print("Rastgele olarak {} uygulaması açıldı.".format(rastgele))

    def pc_ram_yukselt(self):
        eklenecek = int(input("Kaç GB ram eklemek istersiniz: "))
        self.pc_ram += eklenecek
        print("Başarı ile eklendi.\nToplam ram {}\n".format(self.pc_ram))

    def ekran_kartı_yukselt(self):
        ekle = int(input("Kaç GB yükseltilecek : "))
        self.pc_ekran_kartı += ekle
        print("Başarı ile yükseltildi.\nToplam ekran kartı boyutu {}\n".format(self.pc_ekran_kartı))

    def __str__(self):
        return "Bilgisayar durumu : {}\nYüklü uygulamalar : {}\nAçık Uygulama : {}\nRam Miktarı : {}\nEkran kartı boyutu : {}\n".format(self.pc_durum, self.uygulamalar, self.açık_uygulama, self.pc_ram, self.pc_ekran_kartı)

    def __len__(self):
        return len(self.uygulamalar)

bilgisayar1 = Bilgisayar()

print("""
Bilgisayar Simulasyonu

1. Bilgisayarı Aç

2. Bilgisayarı Kapat

3. Uygulamaları Listele

4. Uygulama Ekle

5. Uygulama sil

6. Uygulama Aç

7. Uygulama Kapat

8. Rastgele Uygulama Aç

9. Ram Yükselt

10. Ekran Kartı Yükselt

11. Bilgisayar Özellikleri

12. Uygulama Sayısı

Çıkmak için 'q' ya basın.

""")

while True:
    seçim = input("Seçilen işlem : ")

    if seçim == "1":
        bilgisayar1.pc_ac()
    elif seçim == "2":
        bilgisayar1.pc_kapat()
    elif seçim == "3":
        bilgisayar1.uygulama_listele()
    elif seçim == "4":
        bilgisayar1.uygulama_ekle()
    elif seçim == "5":
        bilgisayar1.uygulama_sil()
    elif seçim == "6":
        bilgisayar1.uygulama_ac()
    elif seçim == "7":
        bilgisayar1.uygulamaları_kapat()
    elif seçim == "8":
        bilgisayar1.rastgele_uygulama_ac()
    elif seçim == "9":
        bilgisayar1.pc_ram_yukselt()
    elif seçim == "10":
        bilgisayar1.ekran_kartı_yukselt()
    elif seçim == "11":
        print(bilgisayar1)
    elif seçim == "12":
        print(len(bilgisayar1), "tane uygulama yüklü.")
    elif seçim == "q":
        print("Çıkış yapılıyor...")
        break
    else:
        print("Hatalı giriş")



