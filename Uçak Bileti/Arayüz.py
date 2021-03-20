from Biletler import *
from Kullanıcılar import *
import time


kullanicilar = Kullanicilar()
biletler = Biletler()

def bos_kontrol(*args):
    for i in args:
        if i == "":
            raise Warning("Boş değer girilemez!")
        else:
            pass

while True:
    giris_isim = ""
    giris_soyisim = ""
    giris_kimlik = ""
    print("Hava yolu uygulamasına hoşgeldiniz...")
    print("""
        1- Giriş yap
        2- Kayıt ol
        q- Çıkış
    """)
    secim = input("Seçiminiz: ")

    if secim == "1":
        try:
            kimlik = int(input("Kimlik: "))
            parola = input("Parola: ").strip()
            bos_kontrol(parola)
        except ValueError:
            print("Uygun değerler giriniz!")
            continue
        except Warning as hata:
            print(hata)
            continue
        giris_liste = kullanicilar.giris_yap(kimlik, parola)
        if type(giris_liste) == list:
            giris_isim = giris_liste[0]
            giris_soyisim = giris_liste[1]
            giris_kimlik = giris_liste[2]
        else:
            giris_isim = ""
            giris_soyisim = ""
            giris_kimlik = ""
    elif secim == "2":
        try:
            isim = input("İsminiz: ").strip()
            soyisim = input("Soyisminiz: ").strip()
            kimlik = int(input("Kimlik numaranız: "))
            parola = input("Parolanız: ").strip()
            bos_kontrol(isim, soyisim, parola)
            kullanici = Kullanıcı(isim, soyisim, kimlik, parola)
        except ValueError:
            print("Lütfen uygun değerler giriniz!")
            continue
        except Warning as hata:
            print(hata)
            continue
        kullanicilar.kayit_ol(kullanici)
    elif secim == "q":
        print("Çıkış yapılıyor...")
        kullanicilar.baglanti_kes()
        biletler.baglantiyi_kes()
        break

    while giris_kimlik != "":
        if giris_kimlik == 123456789:
            print("""
                Admin Menüsü
            1- Kullanıcı sil
            2- Kullanıcı engelle ve sil
            3- Kullanıcı bilgileri
            4- Kimlikle ara
            5- İsim Soyisim ile ara
            6- Bilet ekle
            7- Bilet sil
            8- Biletler
            9- Uçuş ara
            10- Yolcu listesi
            11- Yolcu ara
            12- Uçak doluluk bilgisi
            13- Rötarlar
            14- Rötar ekle
            q- Çıkış
            """)
            choice = input("Seçiminiz: ")
            if choice == "1":
                try:
                    kimlik = int(input("Kaydı silinecek kullanıcının kimlik bilgisi: "))
                except ValueError:
                    print("Lütfen uygun değerler giriniz...")
                    continue
                kullanicilar.kullanici_sil(kimlik)
            elif choice == "2":
                try:
                    kimlik = int(input("Kaydı silinecek ve engellenecek kullanıcının kimlik bilgisi: "))
                except ValueError:
                    print("Lütfen uygun değerler giriniz...")
                    continue
                kullanicilar.kullanici_sil_ve_engelle(kimlik)
            elif choice == "3":
                print("Kullanıcı bilgileri listeleniyor...")
                kullanicilar.kullanici_bilgileri()
            elif choice == "4":
                try:
                    kimlik =  int(input("Aranacak kimlik bilgisi: "))
                except ValueError:
                    print("Lütfen uygun değerler giriniz...")
                    continue
                kullanicilar.kimlikle_ara(kimlik)
            elif choice == "5":
                try:
                    isim = input("Aranacak isim: ").strip()
                    soyisim = input("Aranacak soyisim: ").strip()
                    bos_kontrol(isim, soyisim)
                except Warning as hata:
                    print(hata)
                    continue
                kullanicilar.isim_soyisim_ara(isim, soyisim)
            elif choice == "6":
                try:
                    numara = input("Uçuş numarası: ").strip()
                    nereden = input("Nereden: ").strip()
                    nereye = input("Nereye: ").strip()
                    saat = input("Saati: ").strip()
                    tarih = input("Tarihi: ").strip()
                    bos_bus_yolcu_sayisi = int(input("Boş business koltuk sayısı: "))
                    bos_eko_yolcu_sayisi = int(input("Boş ekonomi koltuk sayısı: "))
                    dolu_bus_yolcu_sayisi = int(input("Dolu-Rezerveli business koltuk sayısı(yoksa 0 girin.): "))
                    dolu_eko_yolcu_sayisi = int(input("Dolu-Rezerveli ekonomi koltuk sayısı(yoksa 0 girin.): "))
                    ucak_sirketi = input("Uçak şirketi: ").strip()
                    ucus_suresi = input("Uçuş süresi: ").strip()
                    fiyati = int(input("Uçuş Fiyatı: "))
                    rotar = input("Rötar(yoksa 'yok' değer giriniz.): ").strip()
                    bos_kontrol(numara, nereden, nereye, saat, tarih, ucak_sirketi, ucus_suresi, rotar)
                except ValueError:
                    print("Uygun değerler giriniz!")
                    continue
                except Warning as hata:
                    print(hata)
                    continue

                bilet = Bilet(numara, nereden, nereye, saat, tarih, bos_bus_yolcu_sayisi, bos_eko_yolcu_sayisi, dolu_bus_yolcu_sayisi, dolu_eko_yolcu_sayisi, ucak_sirketi, ucus_suresi, fiyati, rotar)
                biletler.bilet_ekle(bilet)

            elif choice == "7":
                try:
                    numara = input("Silinecek uçuş numarası: ")
                    bos_kontrol(numara)
                except Warning as hata:
                    print(hata)
                    continue
                biletler.kayit_sil(numara)
            elif choice == "8":
                biletler.biletler()
            elif choice == "9":
                try:
                    numara = input("Aranacak uçuş numarası: ").strip()
                except Warning as hata:
                    print(hata)
                    continue

                biletler.ucus_numarası_ara(numara)
            elif choice == "10":
                try:
                    numara = input("yolcuları listelenecek uçuş numarası: ").strip()
                except Warning as hata:
                    print(hata)
                    continue

                biletler.yolcu_listesi(numara)
            elif choice == "11":
                try:
                    kimlik = int(input("Kimlik numarası: "))
                except ValueError:
                    print("Sadece sayı!")
                    continue
                biletler.yolcu_ara(kimlik)
            elif choice == "12":
                numara = input("Doluluk bilgisi için uçuş numarası: ")
                biletler.ucak_doluluk_bilgisi(numara)
            elif choice == "13":
                biletler.rotarlar()
            elif choice == "14":
                try:
                    numara = input("Rötar yapacak uçuşun numarası: ").strip()
                    rotar = input("Ne kadar rötarlı: ").strip()
                    bos_kontrol(numara, rotar)
                except Warning as hata:
                    print(hata)
                    continue
                biletler.rotar_ayarla(numara, rotar)
            elif choice == "q":
                print("Çıkış yapılıyor...")
                giris_isim = ""
                giris_soyisim = ""
                giris_kimlik = ""
                break
            else:
                print("Hatalı tuşlama!")
        else:
            print("""
                Kullanıcı Menüsü
            1- Uçuşları listele
            2- Uçuş ara
            3- Bilet al
            4- Fiyata göre sırala
            5- Yere göre ara
            6- Kalkış yerine göre ara
            7- Varış yerine göre ara
            8- Tarihe göre ara
            9- Uçak şirketine göre ara
            10- Rötarlar
            q- Çıkış
            """)
            işlem = input("Seçiminiz: ")

            if işlem == "q":
                print("Çıkış yapılıyor...")
                giris_isim = ""
                giris_soyisim = ""
                giris_kimlik = ""
                break
            elif işlem == "1":
                biletler.biletler()
            elif işlem == "2":
                numara = input("Aranacak uçuş numarası: ")
                biletler.ucus_numarası_ara(numara)
            elif işlem == "3":
                numara = input("Bilet almak istediğiniz uçuş numarası: ")
                print("1-Business\n2-Ekonomi")
                secim = input("Seçiminiz: ")
                if secim == "1":
                    koltuk = "business"
                elif secim == "2":
                    koltuk = "ekonomi"
                else:
                    print("Hatalı tuşlama!")
                    break

                biletler.bilet_al(numara, koltuk, giris_kimlik)
            elif işlem == "4":
                biletler.fiyata_gore_sirala()
            elif işlem == "5":
                try:
                    nereden = input("Nereden: ").strip()
                    nereye = input("Nereye: ").strip()
                    bos_kontrol(nereden, nereye)
                except Warning as hata:
                    print(hata)
                biletler.yere_gore_ara(nereden, nereye)
            elif işlem == "6":
                try:
                    nereden = input("Nereden: ").strip()
                    bos_kontrol(nereden)
                except Warning as hata:
                    print(hata)
                biletler.kalkıs_yerine_gore(nereden)
            elif işlem == "7":
                try:
                    nereye = input("Nereye: ").strip()
                    bos_kontrol(nereye)
                except Warning as hata:
                    print(hata)
                    continue
                biletler.varis_yerine_gore(nereye)
            elif işlem == "8":
                try:
                    tarih = input("Tarih: ").strip()
                    bos_kontrol(tarih)
                except Warning as hata:
                    print(hata)
                biletler.tarihe_gore_ara(tarih)
            elif işlem == "9":
                try:
                    sirket = input("Aranacak uçuş şirketi: ").strip()
                    bos_kontrol(sirket)
                except Warning as hata:
                    print(hata)
                biletler.ucak_sirketine_gore_ara(sirket)
            elif işlem == "10":
                print("Rötarlar listeleniyor...")
                biletler.rotarlar()


