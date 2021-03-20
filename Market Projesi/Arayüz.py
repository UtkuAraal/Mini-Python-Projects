from Market import *
import time
print("Markete Hoşgeldiniz")

market = Market()

admin_kullanici = "admin"
admin_parola = "parola"

kullanici_kullanici = "kullanıcı"
kullanici_parola = "parola"
giris = ""
while True:
    print("Giriş Ekranı (Çıkmak için 'q' giriniz.)")
    kullanici = input("Kullanıcı Adı: ").strip()
    parola = input("Parola: ").strip()

    if kullanici == kullanici_kullanici and parola == kullanici_parola:
        print("Marketimize Hoşgeldiniz!")
        giris = "kullanıcı"
    elif kullanici == admin_kullanici and parola == admin_parola:
        print("Hoşgeldin admin!")
        giris = "admin"
    else:
        print("Kullanıcı adı veya şifre hatalı...")
        continue

    while giris != "":
        if giris == "kullanıcı":
            print("""
                    Kullanıcı Menüsü
                    
                1- Bütün ürünleri listele
                2- Ürün ara
                3- Fiyata göre sırala
                4- Ürün al
                5- Kategoriler
                6- Kategoriye göre ara
                7- İsmin içinde geçene göre arama
                8- Markaya göre ara
                9- Menşeileri listele
                10- Markaları listele
                11- Menşei'ye göre ara
                12- Kategori ve markaya göre ara
                
            
            """)
            işlem = input("İşlem numarası (Çıkmak için 'q' ya basın.): ")
            if işlem == "q":
                print("Çıkış yapılıyor...")
                giris = ""
                break
            elif işlem == "1":
                print("Ürünler listeleniyor...")
                time.sleep(2)
                market.urunleri_listele(giris)
            elif işlem == "2":
                isim = input("Aranacak ürün adı: ")
                market.urun_ara(isim, giris)
                time.sleep(2)
            elif işlem == "3":
                olcut = input("Artana göre mi yoksa azalana göre mi sıralansın? (artan/azalan): ")
                print("Sıralanıyor...")
                market.sırala(olcut, giris)
                time.sleep(2)
            elif işlem == "4":
                isim = input("Ürün adı: ")
                boy = int(input("Ürün boyu: "))
                miktar = int(input("Almak istediğiniz adet: "))
                market.satin_al(isim, boy, miktar)
            elif işlem == "5":
                print("Kategoriler: ")
                market.kategoriler()
                time.sleep(2)
            elif işlem == "6":
                kategori = input("Kategori: ")
                market.kategoriye_gore_ara(kategori, giris)
            elif işlem == "7":
                kelime = input("Ara: ")
                market.icinde_gecen(kelime, giris)
                time.sleep(2)
            elif işlem == "8":
                marka = input("Aranacak marka: ")
                print("{} isimli markaya ait ürünler listeleniyor...".format(marka))
                time.sleep(2)
                market.markaya_gore_ara(marka, giris)
                time.sleep(2)
            elif işlem == "9":
                print("Menşeiler listeleniyor")
                time.sleep(2)
                market.menşei_listele()
                time.sleep(2)
            elif işlem == "10":
                print("Markalar listeleniyor...")
                time.sleep(2)
                market.markalar()
                time.sleep(2)
            elif işlem == "11":
                mensei = input("Aranacak mensei: ")
                market.mensei_gore_ara(mensei, giris)
                time.sleep(2)
            elif işlem == "12":
                kategori = input("Aramak istediğiniz kategori: ")
                marka = input("Aramak istediğiniz marka: ")
                print("{} kategorisinden {} isimli markaya ait ürünler listeleniyor...".format(kategori, marka))
                time.sleep(2)
                market.kategori_ve_markaya_gore_ara(kategori, marka, giris)
                time.sleep(2)
        elif giris == "admin":
            print("""
                        Admin Menüsü

                1- Bütün ürünleri listele
                2- Ürün ekle
                3- Ürün sil
                4- Ürün ara
                5- Fiyata göre sırala
                6- Kategoriler
                7- Kategoriye göre ara
                8- İsmin içinde geçene göre arama
                9- Fiyat değiştir
                10- Stok ekle
                11- Stoğu bitenleri listele
                12- Markaya göre ara
                13- Menşeileri listele
                14- Tedarikçileri listele
                15- Markaları listele
                16- Menşei'ye göre ara
                17- Tedarikçiye göre ara
                18- Markaya göre sil
                19- Stoğu biten tüm ürünleri sil
                20- Tedarikçiye göre sil
                21- Kategoriye göre sil
                22- Menşeiye göre sil
                23- Kategori ve markaya göre ara

            """)
            işlem = input("İşlem numarası (Çıkmak için 'q' ya basın.): ")
            if işlem == "q":
                print("Çıkış yapılıyor...")
                giris = ""
                break
            elif işlem == "1":
                print("Ürünler listeleniyor...")
                time.sleep(2)
                market.urunleri_listele(giris)
            elif işlem == "2":
                try:
                    urun_adi = input("Ürün adı: ")
                    marka = input("Marka: ")
                    miktar = int(input("Miktar (kg, l...): "))
                    stok = int(input("Stok: "))
                    fiyat = int(input("Fiyat: "))
                    kategori = input("Kategori: ")
                    menşei = input("Menşei: ")
                    tedarikci = input("Tedarikçi: ")
                except ValueError:
                    print("Hatalı Ddeğer girdiniz!")
                    continue
                if urun_adi == "" or marka == "" or miktar == "" or stok == "" or fiyat == "" or kategori == "" or menşei == "" or tedarikci == "":
                    print("Boş değer girilemez!")
                    continue
                urun = Ürün(urun_adi, marka, miktar, stok, fiyat, kategori, menşei, tedarikci)
                market.urun_ekle(urun)
                time.sleep(2)
            elif işlem == "3":
                try:
                    isim = input("Silinecek ürün adı: ")
                    miktar = int(input("Silinecek ürün boyu(miktarı): "))
                    marka = input("Silinecek ürünün markası: ")
                except ValueError:
                    print("Hatalı değer girdiniz!")
                    continue
                market.urun_sil(isim, miktar, marka)
                time.sleep(2)
            elif işlem == "4":
                isim = input("Aranacak ürün adı: ")
                market.urun_ara(isim, giris)
                time.sleep(2)
            elif işlem == "5":
                olcut = input("Artana göre mi yoksa azalana göre mi sıralansın? (artan/azalan): ")
                print("Sıralanıyor...")
                market.sırala(olcut, giris)
                time.sleep(2)
            elif işlem == "6":
                print("Kategoriler: ")
                market.kategoriler()
                time.sleep(2)
            elif işlem == "7":
                kategori = input("Kategori: ")
                market.kategoriye_gore_ara(kategori, giris)
                time.sleep(2)
            elif işlem == "8":
                kelime = input("Ara: ")
                market.icinde_gecen(kelime, giris)
                time.sleep(2)
            elif işlem == "9":
                print("Fiyatı değişecek ürünün;")
                urun_adi = input("Adı: ")
                try:
                    boy = int(input("Boyu: "))
                    yeni_fiyat = int(input("Yeni fiyatı: "))
                except ValueError:
                    print("Hatalı giriş!")
                    continue
                market.fiyat_degistir(urun_adi, boy, yeni_fiyat)
                time.sleep(2)
            elif işlem == "10":
                try:
                    urun = input("Ürün adı: ")
                    boyu = int(input("Ürün boyu: "))
                    stok = int(input("Eklemek istediğiniz stok: "))
                except ValueError:
                    print("Hatalı giriş!")
                    continue
                market.stok_ekle(urun, boyu, stok)
            elif işlem == "11":
                print("Stoğu bitenler sıralanıyor...")
                time.sleep(2)
                market.stok_bitenler()
                time.sleep(2)
            elif işlem == "12":
                marka = input("Aranacak marka: ")
                print("{} isimli markaya ait ürünler listeleniyor...".format(marka))
                time.sleep(2)
                market.markaya_gore_ara(marka, giris)
                time.sleep(2)
            elif işlem == "13":
                print("Menşeiler listeleniyor")
                time.sleep(2)
                market.menşei_listele()
                time.sleep(2)
            elif işlem == "14":
                print("Tedarikçiler listeleniyor...")
                time.sleep(2)
                market.tedarikciler()
                time.sleep(2)
            elif işlem == "15":
                print("Markalar listeleniyor...")
                time.sleep(2)
                market.markalar()
                time.sleep(2)
            elif işlem == "16":
                mensei = input("Aranacak mensei: ")
                market.mensei_gore_ara(mensei, giris)
                time.sleep(2)
            elif işlem == "17":
                tedarikci = input("Aranacak tedarikçi: ")
                market.tedarikciye_gore_ara(tedarikci)
                time.sleep(2)
            elif işlem == "18":
                marka = input("Silmek istediğiniz marka: ")
                market.markaya_gore_sil(marka)
                time.sleep(2)
            elif işlem == "19":
                print("Stokta olmayan ürünler siliniyor...")
                time.sleep(2)
                market.stok_biten_sil()
                time.sleep(2)
            elif işlem == "20":
                tedarikci = input("Silmek istediğiniz tedarikçi: ")
                time.sleep(2)
                market.tedarikciye_gore_sil(tedarikci)
                time.sleep(2)
            elif işlem == "21":
                kategori = input("Silmek istediğiniz kategori: ")
                print("{} kategorisine ait ürünler siliniyor...".format(kategori))
                time.sleep(2)
                market.kategori_sil(kategori)
                time.sleep(2)
            elif işlem == "22":
                mensei = input("Silmek istediğiniz menşei: ")
                time.sleep(2)
                market.mensei_sil(mensei)
                time.sleep(2)
            elif işlem == "23":
                kategori = input("Aramak istediğiniz kategori: ")
                marka = input("Aramak istediğiniz marka: ")
                print("{} kategorisinden {} isimli markaya ait ürünler listeleniyor...".format(kategori, marka))
                time.sleep(2)
                market.kategori_ve_markaya_gore_ara(kategori, marka, giris)
                time.sleep(2)
