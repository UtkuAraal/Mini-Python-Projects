from Çalışanlar import *
from Firmalar import *
import time
calisanlar = Çalışanlar()
firmalar = Firmalar()
giris = ""
mudur_kullanici = "mudur"
mudur_parola = "mudur"

yardimci_kullanici = "yardimci"
yardimci_parola = "yardimci"
while True:
    print("Ajansa Hoşgeldiniz")
    kullanici = input("Kullanıcı Adı: ").strip()
    parola = input("Parola: ").strip()

    if (kullanici == mudur_kullanici) and (parola == mudur_parola):
        print("Giriş : müdür. Hoşgeldiniz...")
        giris = "mudur"
    elif (kullanici == yardimci_kullanici) and (parola == yardimci_parola):
        print("Giriş : müdür yardımcısı. Hoşgeldiniz...")
        giris = "yardimci"
    else:
        print("Hatalı giriş işlemi! Lütfen tekrar deneyiniz...")

    while giris != "":
        print("""
                Menü
            1- Çalışanlar
            2- Firmalar
            3- Mali durum kayıtları
        """)
        choice = input("İşlem numarası (çıkış için 'q'ya basın): ")

        if choice == "q":
            print("Alt menüye çıkış yapılıyor...")
            giris = ""
            break
        elif choice == "1":
            print("""
                Çalışanlar Menüsü
            1- Çalışanları listele
            2- Çalışan ekle 
            3- Çalışan sil 
            4- Oyuncuları listele
            5- Teknik ekip listele
            6- Maaş güncelle
            7- Oyuncuya proje ata
            8- Teknik ekip çalışanına proje ata
            9- Oyuncu projelerini gör
            10- Teknip ekip projelerini gör
            11- Çalışana izin günü tanımla
            12- Çalışan kullanılan izin gir 
            13- Çalışan numara - isim - pozisyon sırala
            14- Oyuncu numara - isim
            15- Oyuncu numara - isim- kategori
            16- Ofis isim - numaraları
            17- Teknik isim - numaraları
            18- Proje temizle
            19- Ofis çalışanlarını listele
            
            """)
            işlem = input("İşleminiz (çıkmak için 'q'): ")

            if işlem == "q":
                print("Alt menüye geçiliyor...")
                continue
            elif işlem == "1":
                calisanlar.calisanlari_listele(giris)
                time.sleep(5)
            elif işlem == "2":
                if giris == "mudur":
                    pozisyon = input("Pozisyon: ")
                    pozisyon = pozisyon.lower()
                    isim = input("İsim: ")
                    soyisim = input("Soyisim: ")
                    maas = int(input("Maaş: "))
                    izin_gunu = 15
                    kullandigi_izin = 0
                    if pozisyon == "oyuncu":
                        kategori = input("Kategori: ")
                        yeni = Oyuncu(isim, soyisim, pozisyon, maas, izin_gunu, kullandigi_izin, kategori)
                    elif pozisyon == "teknik":
                        yeni = Teknik(isim, soyisim, pozisyon, maas, izin_gunu, kullandigi_izin)
                    else:
                        yeni = Çalışan(isim, soyisim, pozisyon, maas, izin_gunu, kullandigi_izin)
                    calisanlar.calisan_ekle(yeni)
            elif işlem == "3":
                try:
                    numara = int(input("Kaydı silinecek çalışan numarası: "))
                except ValueError:
                    print("Sdece sayı değeri giriniz!")
                    continue
                calisanlar.calisan_sil(numara)
            elif işlem == "4":
                print("Oyuncular listeleniyor...")
                time.sleep(2)
                calisanlar.oyunculari_listele(giris)
                time.sleep(5)
            elif işlem == "5":
                print("Teknik ekip listeleniyor...")
                time.sleep(2)
                calisanlar.teknikler_listele()
                time.sleep(5)
            elif işlem == "6":
                if giris == "mudur":
                    try:
                        numara = int(input("Çalışanın numarası: "))
                        tur = input("Yüze mi yoksa birim olarak mı artırmak istersiniz? (yuzde/birim): ")
                        miktar = int(input("Yüzde ise yüzdeliği, birim ise kaç birim olduğunu girin: "))
                        calisanlar.maas_guncelle(numara, tur, miktar)
                    except ValueError:
                        print("Lütfen uygun değerler girin!")
                        continue
                    except Warning as hata:
                        print(hata)
                else:
                    print("Yetkiniz bulunmamaktadır!")
                time.sleep(5)
            elif işlem == "7":
                if giris == "mudur":
                    calisanlar.oyuncu_numaralari()
                    time.sleep(2)
                    try:
                        numara = int(input("Çalışan numarası: "))
                        proje = input("Proje: ")
                        baslangic = input("Başlangıç: ")
                        bitis = input("Bitiş: ")
                    except ValueError:
                        print("Uygun değerler giriniz...")
                    calisanlar.proje_ata(numara, proje, baslangic, bitis)
                else:
                    print("Yetkiniz bulunmamaktadır...")
            elif işlem == "8":
                calisanlar.teknik_numaralari()
                time.sleep(2)
                try:
                    numara = int(input("Çalışan numarası: "))
                    proje = input("Proje: ")
                    baslangic = input("Başlangıç: ")
                    bitis = input("Bitiş: ")
                except ValueError:
                    print("Uygun değerler giriniz...")
                calisanlar.teknik_proje_ata(numara, proje, baslangic, bitis)
            elif işlem == "9":
                if giris == "mudur":
                    calisanlar.oyuncu_numaralari()
                    time.sleep(2)
                    try:
                        numara = int(input("Oyuncu numarası: "))
                    except ValueError:
                        print("Uygun değerler giriniz!")
                        continue
                    calisanlar.oyuncu_projesini_gor(numara)
                else:
                    print("Yetkiniz bulunmamaktadır...")
                time.sleep(5)
            elif işlem == "10":
                calisanlar.teknik_numaralari()
                try:
                    numara = int(input("Numara: "))
                except ValueError:
                    print("Uygun değerler giriniz!")
                    continue

                calisanlar.teknik_projesini_gor(numara)
                time.sleep(5)
            elif işlem == "11":
                calisanlar.calisan_numaralari()
                time.sleep(2)
                try:
                    numara = int(input("Çalışan numarası: "))
                    hak = int(input("Kaç gün daha tanımlamak istiyorsunuz? : "))
                except ValueError:
                    print("Uygun değerler giriniz!")
                    continue
                calisanlar.izin_gunu(numara, hak)
                time.sleep(5)
            elif işlem == "12":
                calisanlar.calisan_numaralari()
                time.sleep(2)
                try:
                    numara = int(input("Çalışan numarası: "))
                    hak = int(input("Kaç gün izin kullanıldı? : "))
                except ValueError:
                    print("Uygun değerler giriniz!")
                    continue
                calisanlar.kullanilan_izin(numara, hak)
                time.sleep(5)
            elif işlem == "13":
                print("Çalışan numaraları listeleniyor...")
                time.sleep(2)
                calisanlar.calisan_numaralari()
                time.sleep(5)
            elif işlem == "14":
                print("Oyuncu numaraları listeleniyor...")
                time.sleep(2)
                calisanlar.oyuncu_kategorisiz_numara()
                time.sleep(5)
            elif işlem == "15":
                if giris == "mudur":
                    print("Oyuncu numaraları (kategorili) listeleniyor...")
                    time.sleep(2)
                    calisanlar.oyuncu_numaralari()
                    time.sleep(5)
                else:
                    print("Yetkiniz bulunmamaktadır!")
                    time.sleep(2)
            elif işlem == "16":
                print("Ofis çalışanlarının numaraları listeleniyor...")
                time.sleep(2)
                calisanlar.ofis_isim_numara()
                time.sleep(5)
            elif işlem == "17":
                print("Teknik ekip çalışanlarının numaraları listeleniyor...")
                time.sleep(2)
                calisanlar.teknik_isim_numara()
                time.sleep(5)
            elif işlem == "18":
                calisanlar.calisan_proje_liste()
                time.sleep(5)
                try:
                    numara = int(input("Projesini temizlemek istediğiniz çalışan numarası: "))
                except ValueError:
                    print("Uygun değerler giriniz!")
                    continue
                calisanlar.proje_sil(numara)
                time.sleep(5)
            elif işlem == "19":
                print("Ofis çalışanları bilgileri listeleniyor...")
                time.sleep(2)
                calisanlar.ofis_listle()
                time.sleep(5)
            else:
                print("Geçersiz seçim!")
                time.sleep(2)
        elif choice ==  "2":
            print("""
                Firmalar Menüsü
            1- Anlaşmaları listele
            2- Anlaşma ekle
            3- Firma ara
            
            """)
            işlem = input("Seçiminiz (çıkmak için 'q'): ")

            if işlem == "q":
                print("Üst menüye geçiliyor...")
                continue
            elif işlem == "1":
                print("Kayıtlı anlaşmalar listeleniyor...")
                time.sleep(2)
                firmalar.firma_listele()
                time.sleep(5)
            elif işlem == "2":
                try:
                    isim = input("Firma ismi: ")
                    nerede = input("Firma nereden: ")
                    ucret = int(input("Firma ile anlaşılan ücret: "))
                except ValueError:
                    print("Ugun değerler giriniz...")
                    continue
                firma = Firma(isim, nerede, ucret)
                firmalar.firma_ekle(firma)
                time.sleep(5)
            elif işlem == "3":
                isim = input("Firma ismi: ")
                print("{} isimli firma ile yapılan anlaşmalar listeleniyor...")
                time.sleep(2)
                firmalar.firma_ara(isim)
                time.sleep(5)
        elif choice == "3":
            gelir = firmalar.toplam_gelir()
            sabit_gider = 18000
            maas_gider = calisanlar.maas_gider()
            kalan = gelir - (sabit_gider + maas_gider)

            if kalan < 0:
                durum = "zarar"
            elif kalan > 0:
                durum = "kar"
            else:
                durum = "nötr"
            print("""
                Anlaşmalardan gelen gelir: {}
                Sabit gider: {}
                Maaşlar gideri: {}
                sonuc = {} {}
            """.format(gelir, sabit_gider, maas_gider, kalan, durum))















