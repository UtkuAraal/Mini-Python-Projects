from Otel import *
import time

otel = Otel()

def bos_kontrol(**kwargs):
    for i, j in kwargs.items():
        if j == "":
            raise Warning("{} alanı boş bırakılamaz!".format(i))
        else:
            pass

def oda_numarasi(numara):
    if (numara > 30) or (numara < 1):
        raise Warning("Geçersiz oda numarası!")
    else:
        pass

while True:
    print("""
            Otel Menüsü             Boş Oda Sayısı: {}
    1- Oda ver
    2- Oda boşalt
    3- Oda bilgileri
    4- Oda durumları
    5- Dolu odalar
    6- Uzun süre rezerveli odalar
    7- En yüksek ücretli
    8- Oda bilgisi
    9- İsimle müşteri arama
    10- Telefon numarası ile müşteri arama  
    11- Dolu odaların bitiş tarihleri
    12- Dolu Boş oda listesi
    13- Dolu oda müşteri bilgileri       
    14- Rezervasyon bitiş süresi uzat          
    q- Çıkış
    """.format(otel.bos_oda_sayisi()))
    choice = input("Seçiminiz: ")

    if choice == "q":
        print("Sistemden çıkış yapılıyor...")
        otel.baglantiyi_kes()
        time.sleep(2)
        break
    elif choice == "1":
        try:
            isim = input("İsim: ").strip()
            soyisim = input("Soyisim: ").strip()
            telefon = int(input("Telefon Numarası: "))
            baslangic = input("Rezervasyon Başlangıç Tarihi: ").strip()
            bitis = input("Rezervasyon Bitiş Tarihi: ").strip()
            gun = int(input("Kaç Günlük Rezervasyon: "))
            bos_kontrol(isim = isim, soyisim = soyisim, telefon = telefon, baslangic = baslangic, bitis = bitis, gun = gun)
        except ValueError:
            print("Hatalı değer girişi!")
            continue
        except Warning as hata:
            print(hata)
            continue
        otel.oda_ver(baslangic, bitis, isim, soyisim, telefon, gun)
    elif choice == "2":
        try:
            numara = int(input("Check out için oda numarası: "))
            oda_numarasi(numara)
        except ValueError:
            print("Sadece sayı giriniz!")
            continue
        except Warning as hata:
            print(hata)
            continue
        time.sleep(2)
        otel.oda_bosalt(numara)
        time.sleep(5)
    elif choice == "3":
        print("Oda bilgileri listeleniyor...")
        time.sleep(2)
        otel.oda_bilgileri()
        time.sleep(5)
    elif choice == "4":
        print("Oda durumları listeleniyor...")
        time.sleep(2)
        otel.oda_durumlari()
        time.sleep(5)
    elif choice == "5":
        print("Dolu odalar listeleniyor...")
        time.sleep(2)
        otel.dolu_odalar()
        time.sleep(5)
    elif choice == "6":
        print("En uzun süre rezerveli odalar listleniyor...")
        time.sleep(2)
        otel.en_uzun_sure_rezerveli()
        time.sleep(5)
    elif choice == "7":
        print("En yüksek ücretli odalar")
        time.sleep(2)
        otel.en_yuksek_ucretli()
        time.sleep(5)
    elif choice == "8":
        try:
            numara = int(input("Bilgileri gösterilecek oda numarası: "))
            oda_numarasi(numara)
        except ValueError:
            print("Sadece sayı!")
            continue
        except Warning as hata:
            print(hata)
            continue
        time.sleep(2)
        otel.oda_bilgisi(numara)
        time.sleep(5)
    elif choice == "9":
        print("Aranacak müşterinin;")
        isim = input("İsmi: ").strip()
        soyisim = input("Soyisim: ").strip()
        if isim == "" or soyisim == "":
            print("Değerler boş olamaz!")
        print("{} {} isimli müşteri kaydı aranıyor...".format(isim, soyisim))
        time.sleep(2)
        otel.isimle_musteri_arama(isim, soyisim)
        time.sleep(5)
    elif choice == "10":
        try:
            telefon = int(input("Müşterinin telefon numarası: "))
        except ValueError:
            print("Hatalı değer!")
            print("{} telefon numarası ile müşteri kaydı aranıyor...".format(telefon))
        time.sleep(2)
        otel.numara_ile_musteri(telefon)
        time.sleep(5)
    elif choice == "11":
        print("Dolu odaların rezervasyon bitiş tarihleri listeleniyor...")
        time.sleep(2)
        otel.dolu_oda_bitis_tarihleri()
        time.sleep(5)
    elif choice == "12":
        print("Oda durumları listeleniyor...")
        time.sleep(2)
        otel.dolu_bos_odalar()
        time.sleep(5)
    elif choice == "13":
        print("Dolu odaların müşteri bilgileri listeleniyor...")
        time.sleep(2)
        otel.dolu_oda_musterileri()
        time.sleep(5)
    elif choice == "14":
        print("Rezervasyon süresi uzatılacak odanın;")
        try:
            numara = int(input("Numarası: "))
            bitis = input("Yeni bitiş tarihi: ")
            gun = int(input("Eklenecek gün sayısı: "))
            bos_kontrol(bitis = bitis)
        except ValueError:
            print("Hatalı değer girişi!")
            continue
        except Warning as hata:
            print(hata)
            continue
        time.sleep(2)
        otel.bitis_gun_guncelle(numara, bitis, gun)
        time.sleep(5)
