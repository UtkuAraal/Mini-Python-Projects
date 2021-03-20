from kütüphane import *
print("""******************
İşlemler;

1- Kitapları Göster
2- Kitap Sorgulama
3- Kitap Ekle
4- Kitap Sil
5- Baskı Yükselt
6- Yayınevine Göre Ara
7- Türe Göre Ara
8- Yayınevlerini Sırala
9- Türleri Yazdır
10- Yayınevi Kitaplarını Sil
11- Hepsini Sil
12- Yazara Göre Ara
13- Alfabetik Olarak Sırala

Çıkmak için 'q' ya basın.
******************
""")
kütüphane = Kütüphane()
while True:
    işlem = input("Yapacağınız İşlem: ")


    if işlem == "q":
        print("Program Sonlandırlıyor...")
        print("Yine Bekleriz...")
        Kütüphane.baglantiyi_kes()
        break
    elif işlem == "1":
        kütüphane.kitapları_goster()
    elif işlem == "2":
        isim = input("Hangi kitabı istiyorsunuz ?")
        print("Kitap Sorgulanıyor...")
        time.sleep(2)
        kütüphane.kitap_sorgula(isim)
    elif işlem == "3":
        isim = input("İsim: ")
        yazar = input("Yazar: ")
        yayınevi = input("Yayınevi: ")
        tür = input("Tür: ")
        baskı = int(input("Baskı: "))
        yeni_kitap = Kitap(isim, yazar, yayınevi, tür, baskı)
        print("Kitap ekleniyor...")
        time.sleep(2)
        kütüphane.kitap_ekle(yeni_kitap)
        print("Kitap Eklendi...")
    elif işlem == "4":
        isim = input("Hangi kitabı silmek istiyorsunuz ?")
        cevap = input("Emin misiniz ? (E/H)")
        if cevap == "E":
            kütüphane.kitap_sil(isim)
    elif işlem == "5":
        isim = input("Hangi kitabın baskısını yükseltmek istiyorsunuz ?")
        print("Baskı yükseltiliyor...")
        time.sleep(2)
        kütüphane.baskı_yukselt(isim)
        print("Baskı yükseltildi...")
    elif işlem == "6":
        yayınevi = input("Aranacak Yayınevi: ")
        kütüphane.yayınevine_gore_listele(yayınevi)
    elif işlem == "7":
        tür = input("Aramak istediğiniz tür: ")
        print("{} türüne kitaplar listeleniyor...".format(tür))
        time.sleep(2)
        kütüphane.ture_gore_ara(tür)
    elif işlem == "8":
        print("Yayınevleri Sıralanıyor...")
        time.sleep(2)
        kütüphane.yayınevleri_sırala()
    elif işlem == "9":
        print("Türler Sıralanıyor...")
        time.sleep(2)
        kütüphane.turler()
    elif işlem == "10":
        yayınevi = input("Kitaplarını silmek istediğiniz yayınevi: ")
        kütüphane.yayınevi_kitap_sil(yayınevi)
    elif işlem == "11":
        cevap = input("Tüm kayıtları silmek istediğinizden emin misiniz ? (E/H): ")
        if cevap == "E":
            kütüphane.hepsini_sil()
    elif işlem == "12":
        yazar = input("Yazar ismi girin: ")
        kütüphane.yazara_gore_ara(yazar)
    elif işlem == "13":
        kütüphane.alfabetik_sıra()
    else:
        print("Geçersiz İşlem...")