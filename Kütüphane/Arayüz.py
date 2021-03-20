from Kütüphane.KütüphaneV2 import *
import time

kutuphane = Kutuphane()

def bos_kontrol(*args):
    for i in args:
        if i == "":
            raise Warning("Boş değer girişi yapılamaz!")

def mail_kontrol(mail):
    if mail.find("@") and (mail.endswith(".com") != -1):
        return True
    return False


print("Kütüphane Programına Hoşgeldiniz.")
while True:
    print("""
            Menü
    1- Kitap ekle
    2- Kitap sil
    3- Kitapları listele    
    4- İsim ile ara
    5- Yazar ile ara
    6- Kitapları mail ile gönder
    7- Türe göre ara 
    8- Kitap ver
    9- Kitap teslim al
    10- Yeni çıkan kitaplar
    11- Yayınevine göre ara
    12- Yazara ait kitaplar
    13- Yazara göre sil
    14- Türe göre sil
    15- Yayınevine göre sil
    16- İçinde geçen kelime ile arama
    q- Çıkış
    """)
    secim = input("Seçiminiz: ")

    if secim == "q":
        print("Programdan çıkış yapılıyor...")
        kutuphane.baglantiyi_kes()
        break
    elif secim == "1":
        try:
            adi = input("Kitap adı: ").strip()
            yazar = input("Yazarı: ").strip()
            yayınevi = input("Kitabın yayınevi: ")
            tur = input("Türü: ").strip()
            sayfa_sayisi = int(input("Sayfa sayısı: "))
            cilt = int(input("Cilt Numarası: "))
            bos_kontrol(adi, yazar, yayınevi, tur)
        except ValueError:
            print("Lütfen uygun değerler giriniz!")
            continue
        except Warning as hata:
            print(hata)
            continue

        kitap = Kitap(adi, yazar, yayınevi, tur, sayfa_sayisi, cilt)
        kutuphane.kitap_ekle(kitap)
        time.sleep(2)
    elif secim == "2":
        try:
            silinecek = int(input("Silinecek kitap numarası: "))
        except ValueError:
            print("Sadece sayı giriniz!")
            continue

        kutuphane.kitap_sil(silinecek)
        time.sleep(2)
    elif secim == "3":
        kutuphane.kitapları_listele()
    elif secim == "4":
        isim = input("Aranacak kitap ismi: ")
        kutuphane.isim_ile_ara(isim)
        time.sleep(2)
    elif secim == "5":
        yazar = input("Aranacak yazar adı:")
        kutuphane.yazar_ara(yazar)
        time.sleep(2)
    elif secim == "6":
        kime = input("Kayıtlı kitapların gönderileceği mail adresi giriniz: ").strip()
        if not mail_kontrol(kime):
            print("Geçersiz mail adresi!")
            continue
        kutuphane.mail_gonder(kime)
        time.sleep(2)
    elif secim == "7":
        tur = input("Aranacak tür: ")
        kutuphane.ture_gore_ara(tur)
        time.sleep(2)
    elif secim == "8":
        kitap_no = int(input("Verilecek kitap numarası: "))
        numara = int(input("Kitabı teslim alan kişinin üye numarası: "))
        kutuphane.kitap_ver(kitap_no, numara)
        time.sleep(2)
    elif secim == "9":
        kitap_no = int(input("Teslim alınacak kitap numarası: "))
        kutuphane.kitap_teslim(kitap_no)
        time.sleep(2)
    elif secim == "10":
        kutuphane.yeni_cikanlar()
        time.sleep(2)
    elif secim == "11":
        yayınevi = input("Aranacak yayınevi: ")
        kutuphane.yayinevine_gore_ara(yayınevi)
        time.sleep(2)
    elif secim == "12":
        yazar = input("Kitapları listelenecek yazar adı: ")
        kutuphane.yazara_ait_kitaplar(yazar)
        time.sleep(2)
    elif secim == "13":
        yazar = input("Kitap kayıtları silinecek yazar: ")
        kutuphane.yazara_gore_sil(yazar)
        time.sleep(2)
    elif secim == "14":
        tur = input("Kayıtları silinecek kitap türü: ")
        kutuphane.ture_gore_sil(tur)
        time.sleep(2)
    elif secim == "15":
        yayıenvi = input("Kitap kayıtları silinecek yayınevi: ")
        kutuphane.yayınevine_gore_sil(yayınevi)
        time.sleep(2)
    elif secim == "16":
        kelime = input("Aramak istediğiniz kelime: ")
        kutuphane.icinde_gecen_kelime_ile_arama(kelime)
        time.sleep(2)


