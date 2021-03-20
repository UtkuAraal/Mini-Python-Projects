from Müzik import *
import time

uygulama = Uygulama()
print("Müzik Uygulamasına Hoşgeldiniz...")
admin_kullanıcı_adı = "admin"
admin_parola = "parola"

kullanıcı_kullanıcı_adı = "kullanıcı"
kullanıcı_parola = "parola"
giris = ""
while True:
    print("İki Değere de 'q' Girerseniz Program Kapancaktır.")
    kullanıcı_adı = input("Kullanıcı adı: ")
    parola = input("Parola: ")
    if kullanıcı_adı == "q" and parola == "q":
        print("Uygulama Kapatılıyor...\nİyi Günler Dileriz...")
        uygulama.baglantiyi_kes()
        break
    elif kullanıcı_adı == kullanıcı_kullanıcı_adı and parola == kullanıcı_parola:
        print("Sayın kullanıcı sisteme hoşgeldiniz...")
        giris = "kullanıcı"
        with open("Log.txt", "a", encoding="utf-8") as file:
            file.write(giris + " " + "Giriş Yaptı\n")
    elif kullanıcı_adı == admin_kullanıcı_adı and parola == admin_parola:
        print("Hoşgeldiniz admin...")
        giris = "admin"
        with open("Log.txt", "a", encoding="utf-8") as file:
            file.write(giris + " " + "Giriş Yaptı\n")
    else:
        print("Yanlış Kullanıcı Adı Veya Şifre...")
        continue

    while giris != "":
        if giris == "kullanıcı":
            print("""
            Kullanıcı Menüsü
            
            1- Şarkıları Listele
            2- Şarkı Ara
            3- Türe Göre Ara
            4- Prodüksiyona Göre Ara
            5- Sanatçıya Göre Ara 
            6- Şarkı Satın Al
                     
            """)
            işlem = input("İşlem (Çıkmak için 'q' ya basın.): ")

            if işlem == "q":
                print("Çıkış Yapılıyor...")
                with open("Log.txt", "a", encoding="utf-8") as file:
                    file.write(giris + " " + "Çıkış Yaptı\n")
                giris = ""
                break
            elif işlem == "1":
                print("Şarkılar Listeleniyor...")
                time.sleep(2)
                uygulama.muzikleri_listele(giris)
            elif işlem == "2":
                ara = input("Aranacak Şarkı İsmi: ")
                print("Şarkı Aranıyor...")
                time.sleep(2)
                uygulama.muzik_sorgula(ara, giris)
            elif işlem == "3":
                tur = input("Aranacak Tür: ")
                print("Türler Listeleniyor...")
                time.sleep(2)
                uygulama.ture_gore_ara(tur, giris)
            elif işlem == "4":
                produksiyon = input("Aranacak Prodüksiyon İsmi: ")
                print("İstenen Prodüksiyona Ait Kayıtlı Şarkılar Listeleniyor...")
                time.sleep(2)
                uygulama.produksiyona_gore_ara(produksiyon, giris)
            elif işlem == "5":
                sanatci = input("Aranacak Sanatçı: ")
                print("Aranacak Sanatçıya Ait Kayıtlı Şarkılar Listeleniyor...")
                time.sleep(2)
                uygulama.sanatciya_gore_ara(sanatci, giris)
            elif işlem == "6":
                isim = input("Almak İstediğiniz Şarkı İsmi: ")
                uygulama.muzik_al(isim)
                time.sleep(2)


        elif giris == "admin":
            print("""
                        Admin Menüsü

                        1- Şarkıları Listele
                        2- Şarkı Ara
                        3- Türe Göre Ara
                        4- Prodüksiyona Göre Ara
                        5- Sanatçıya Göre Ara 
                        6- Toplam Süre
                        7- Şarkı Ekle          
                        8- Şarkı Sil
                        9- Toplam Kazanç
                        10- Prodüksiyona Göre Sil
                        11- Sanatçıya Göre Sil
                        12- En Çok Satan 3 Şarkı
                        13- Prodüksiyon Şarkı Sayısı
                        14- Sanatçı Şarkı Sayısı
                        15- Sanatçının En Çok Dinlenen 3 Şarkısı
                        16- Dile Göre Ara
                        17- Genel Bilgiler
                        18- Prodüksiyonları Listele
                        19- Sanatçıları Listele
                        20- Albüme Göre Ara
                        21- Sanatçının Albümleri
                        22- Çok Satan Sanatçılar
                        23- Sanatçı Satış Sayısı
                        """)
            işlem = input("İşlem (Çıkmak için 'q' ya basın.): ")

            if işlem == "q":
                print("Çıkış Yapılıyor...")
                with open("Log.txt", "a", encoding="utf-8") as file:
                    file.write(giris + " " + "Çıkış Yaptı\n")
                giris = ""
                break
            elif işlem == "1":
                print("Şarkılar Listeleniyor...")
                time.sleep(2)
                uygulama.muzikleri_listele(giris)
            elif işlem == "2":
                ara = input("Aranacak Şarkı İsmi: ")
                print("Şarkı Aranıyor...")
                time.sleep(2)
                uygulama.muzik_sorgula(ara, giris)
            elif işlem == "3":
                tur = input("Aranacak Tür: ")
                print("Türler Listeleniyor...")
                time.sleep(2)
                uygulama.ture_gore_ara(tur, giris)
            elif işlem == "4":
                produksiyon = input("Aranacak Prodüksiyon İsmi: ")
                print("İstenen Prodüksiyona Ait Kayıtlı Şarkılar Listeleniyor...")
                time.sleep(2)
                uygulama.produksiyona_gore_ara(produksiyon, giris)
            elif işlem == "5":
                sanatci = input("Aranacak Sanatçı: ")
                print("Aranacak Sanatçıya Ait Kayıtlı Şarkılar Listeleniyor...")
                time.sleep(2)
                uygulama.sanatciya_gore_ara(sanatci, giris)
            elif işlem == "6":
                uygulama.toplam_sure()
            elif işlem == "7":
                sarki_ismi = input("Şarkı İsmi: ")
                turu = input("Şarkı Türü: ")
                dil = input("Şarkı Dili: ")
                sanatci = input("Sanatçı İsmi: ")
                album = input("Albümü: ")
                produksiyon = input("Prodüksiyon Şirketi: ")
                try:
                    sarki_suresi = int(input("Şarkı Süresi (saniye): "))
                except ValueError:
                    print("Lütfen Sadece Sayısal Değer Giriniz!")
                    continue
                sarki = Şarkı(sarki_ismi, turu, dil, sanatci, album, produksiyon, sarki_suresi)
                uygulama.muzik_ekle(sarki)
            elif işlem == "8":
                sil = input("Silinecek Şarkı İsmi: ")
                print("Şarkı Siliniyor...")
                time.sleep(2)
                uygulama.sarki_sil(sil)
            elif işlem == "9":
                uygulama.toplam_kazanc()
            elif işlem == "10":
                prod = input("Şarkılarını Silmek İstediğiniz Prodüksiyon Şirketi: ")
                print("Prodüksiyona Ait Şarkılar Siliniyor...")
                uygulama.produksiyona_gore_sil(prod)
            elif işlem == "11":
                sanatci = input("Şarkılarını Silmek İstediğiniz Sanatçı: ")
                print("{} İsimli Sanatçının Şarkıları Siliniyor...".format(sanatci))
                time.sleep(2)
                uygulama.sanatciya_gore_sil(sanatci)
            elif işlem == "12":
                print("En Çok Satan 3 Şarkı:")
                uygulama.cok_satan()
                time.sleep(2)
            elif işlem == "13":
                prod = input("Prodüksiyonun İsmi: ")
                uygulama.produksiyon_sarki_sayisi(prod)
            elif işlem == "14":
                sanatci = input("Sanatçı Adı: ")
                uygulama.sanatci_sarki_sayisi(sanatci)
            elif işlem == "15":
                sanatci = input("Sanatçı Adı: ")
                uygulama.sanatci_cok_dinlenen(sanatci)
            elif işlem == "16":
                dil = input("Aranacak Dil: ")
                uygulama.dile_gore_ara(dil)
                time.sleep(2)
            elif işlem == "17":
                print("Bilgiler Getiriliyor...")
                uygulama.genel_bilgiler()
                time.sleep(2)
            elif işlem == "18":
                print("Prodüksiyonlar Listeleniyor...")
                time.sleep(2)
                uygulama.produksiyonlar()
                time.sleep(2)
            elif işlem == "19":
                print("Sanatçılar Listeleniyor...")
                time.sleep(2)
                uygulama.sanatcilar()
                time.sleep(2)
            elif işlem == "20":
                album = input("Aranacak Albüm: ")
                print("{} İsimli Albüm Aranıyor...".format(album))
                time.sleep(2)
                uygulama.albume_gore_ara(album)
                time.sleep(2)
            elif işlem == "21":
                sanatci = input("Sanatçının İsmi: ")
                print("{} İsimli Sanatçının Albümleri Listeleniyor...".format(sanatci))
                time.sleep(2)
                uygulama.sanatci_album_sayisi(sanatci)
                time.sleep(2)
            elif işlem == "22":
                print("Çok Satan Sanatçılar Listesi: ")
                time.sleep(2)
                uygulama.en_cok_satan_sanatcilar()
                time.sleep(2)
            elif işlem == "23":
                sanatci = input("Satış Sayısını Öğrenmek İstediğiniz Sanatçı: ")
                print("Satış Sayısı Getiriliyor...")
                time.sleep(2)
                uygulama.sanatci_satis_sayisi(sanatci)
                time.sleep(2)

