from Blog import *
from Kullanıcı import *
import time

blog = Blog()
kullanicilar = Kullanıcılar()

def email_validator(email):
    if (email.find("@") != -1) and email.endswith(".com") and (email.find("@.com") == -1):
        pass
    else:
        raise Warning("Geçerli bir email girin!")

def uygun_mu(degisken):
    if degisken == "" or degisken == " ":
        raise ValueError(degisken, "boş geçilemez!")
    else:
        pass


giris = ""

print("Blog sitesine hoşgeldiniz!")
while True:
    print("""
            Seçenekler
        1- Kayıt ol
        2- Giriş yap
        3- Şifremi unuttum
        q- Çıkış yap
    """)
    işlem = input("Seçiminiz: ")

    if işlem == "q":
        blog.baglanti_kes()
        kullanicilar.baglantiyi_kes()
        print("Çıkış yapılıyor...")
        time.sleep(2)
        break
    elif işlem == "1":
        print("Kullanıcı Kayıt Ekranı")
        try:
            kullanici_adi = input("Kullanıcı adı: ").strip()
            uygun_mu(kullanici_adi)
            email = input("Email: ").strip()
            email_validator(email)
            uygun_mu(email)
            parola = input("Parola: ").strip()
            uygun_mu(parola)
            gizli_soru = input("Gizli soru: ").strip()
            uygun_mu(gizli_soru)
            gizli_cevap = input("Sorunun cevabı: ").strip()
            uygun_mu(gizli_cevap)
        except Warning as hata:
            print(hata)
            continue
        except ValueError:
            print("Boş değer giremezsiniz!")
            continue
        kullanici = Kullanıcı(kullanici_adi, email, parola, gizli_soru, gizli_cevap)
        kullanicilar.kayit_ol(kullanici)
    elif işlem == "2":
        try:
            email = input("Email: ").strip()
            uygun_mu(email)
            parola = input("Parola: ").strip()
            uygun_mu(parola)
        except ValueError:
            print("Boş Değer giremezsiniz!")
        giris = kullanicilar.giris_yap(email, parola)

        if giris == "":
            print("Hatalı giriş bilgileri...")
        else:
            print("Hoşgeldiniz", giris)
    elif işlem == "3":
        try:
            kullanici_adi = input("Kullanıcı adı: ").strip()
            uygun_mu(kullanici_adi)
            email = input("Email: ").strip()
            uygun_mu(email)
            sifre = kullanicilar.gizli_soru(kullanici_adi, email)
            print("Şifreniz:", sifre)
        except ValueError:
            print("Boş değer giremezsiniz!")
            continue
        except Warning as hata:
            print(hata)
            continue
    else:
        print("Geçersiz seçim!")

    while giris != "":
        print("""
            Kullanıcı Menüsü Giriş: {}
            1- Makale başlıkları
            2- Makale aç
            3- Kendi makalelerini görüntüle
            4- Kullanıcı makalesi ara
            5- Makale ekle
            6- Makale sil
            7- Kategoriye göre ara
            8- Başlığa göre ara
            9- Beğeni sayısına göre ara
            10- Eklenme zamanına göre ara
            11- Son eklenen makale
            12- Rastgele makale aç
            13- Kullanıcı toplam beğeni
            14- Yazarlar
            15- Kategoriler
            16- Makale içeriğinde geçen kelimeye göre ara
            17- Makalesi olan yazarlar
            18- Kullanıcı makale sayısı
            19- Kullanıcı profil bilgileri
            20- Makalesi olmayan kullanıcılar
            21- En çok beğenilen makaleyi aç
            22- Başlık içinde ara
            23- Admin menüsü
            q- Çıkış
            
        """.format(giris))
        choice = input("Seçiminiz: ")

        if choice == "q":
            print("Çıkış yapılıyor...")
            kullanicilar.cikis_log(giris)
            giris = ""
            break
        elif choice == "1":
            print("Makale başlıkları sıralanıyor...")
            time.sleep(2)
            blog.makale_basliklari()
            time.sleep(5)
        elif choice == "2":
            blog.makale_basliklari()
            try:
                numara = int(input("Açılacak makalenin numarası: "))
            except ValueError:
                print("Sadece sayı")
                continue
            blog.makale_ac(numara)
            kapat = input("\n\n\nKapatmak için entera basınız (beğenip kapatmak için B' yi tuşlayın.).")

            if kapat == "B":
                blog.begen(numara)

        elif choice == "3":
            print("Makaleleriniz görüntüleniyor...")
            time.sleep(2)
            blog.kullaniciya_ait_makaleler(giris)
            time.sleep(5)
        elif choice == "4":
            kullanici_adi = input("Kullanıcı adı: ")
            print("{} isimli kullanıcıya ait makaleler listeleniyor...".format(kullanici_adi))
            time.sleep(2)
            blog.kullaniciya_ait_makaleler(kullanici_adi)
            time.sleep(5)
        elif choice == "5":
            print("Makalenin;")
            baslik = input("Başlığı: ")
            icerik = input("İçerik: ")
            kategori = input("Kategori: ")
            gun = input("Gün: ")
            karakter_sayisi = len(icerik)
            makale = Makale(baslik, icerik, giris, kategori, gun, karakter_sayisi)
            blog.makale_ekle(makale)
            time.sleep(2)
        elif choice == "6":
            try:
                numara = int(input("Silmek istediğiniz makale numarası: "))
            except ValueError:
                print("Sadece sayı!")
            blog.makale_sil(giris, numara)

            time.sleep(2)
        elif choice == "7":
            kategori = input("Kategori: ")
            print(kategori, "kategorisinden makaleler listeleniyor...")
            time.sleep(2)
            blog.kategoriye_gore_ara(kategori)
            time.sleep(5)
        elif choice == "8":
            baslik = input("Aranacak başlık: ")
            print("Aranan başlık:", baslik)
            time.sleep(2)
            blog.basliga_gore_ara(baslik)
            time.sleep(5)
        elif choice == "9":
            print("1- Artana göre sırala\n2- Azalana göre sırala")
            sırala = input("Seçim: ")
            time.sleep(2)
            if sırala == "1":
                olcut = "artan"
            elif sırala == "2":
                olcut = "azalan"
            else:
                print("Hatalı seçim!")
                continue
            blog.begeni_sayisi(olcut)
            time.sleep(5)
        elif choice == "10":
            print("1- Önce yeni\n2- Önce eski")
            secim = input("Seçim: ")
            time.sleep(2)
            if secim == "1":
                olcut = "son"
            elif secim == "2":
                olcut = "ilk"
            else:
                print("Hatalı giriş!")
                continue
            blog.eklenme_zamanına_gore(olcut)
            time.sleep(5)
        elif choice == "11":
            print("Son eklenen makale açılıyor...")
            time.sleep(2)
            blog.son_eklenen_makale()
            time.sleep(5)
        elif choice == "12":
            print("Rastgele makale açılıyor...")
            time.sleep(2)
            blog.rastgele_makale_ac()
            time.sleep(5)
        elif choice == "13":
            yazar = input("Yazar: ")
            time.sleep(2)
            blog.kullanici_toplam_begeni(yazar)
            time.sleep(5)
        elif choice == "14":
            print("Kullanıcılar listeleniyor...")
            time.sleep(2)
            kullanicilar.kullanicilar()
            time.sleep(5)
        elif choice == "15":
            print("Kategoriler listeleniyor...")
            time.sleep(2)
            blog.kategoriler()
            time.sleep(5)
        elif choice == "16":
            kelime = input("Aranacak makale: ")
            print("İçinde {} kelimesi geçen makaleler sıralanıyor...".format(kelime))
            time.sleep(2)
            blog.kelimeye_gore_ara(kelime)
            time.sleep(5)
        elif choice == "17":
            print("Makalesi olan yazarlar sıralanıyor...")
            time.sleep(2)
            blog.yazarlar()
            time.sleep(5)
        elif choice == "18":
            kullanici_adi = input("Makale sayısını sorgulamak istediğiniz kullanıcı adı: ")
            time.sleep(2)
            kullanicilar.kullanici_makale_sayisi(kullanici_adi)
            time.sleep(5)
        elif choice == "19":
            print("Makalesi olan yazarların profil bilgiler listeleniyor...")
            time.sleep(2)
            blog.profil_bilgileri()
            time.sleep(5)
        elif choice == "20":
            print("Makalesi olmayan kullanıcılar listeleniyor...")
            time.sleep(2)
            kullanicilar.makalesiz_kullanicilar()
            time.sleep(5)
        elif choice == "21":
            print("En çok beğenilen makale açılıyor...")
            time.sleep(2)
            blog.en_cok_begenilen()
            kapat = input("\n\n\nKapatmak için entera basınız (beğenip kapatmak için B' yi tuşlayın.).")

            if kapat == "B":
                blog.begen(numara)
        elif choice == "22":
            kelime = input("Başlık içinde aranacak kelime: ")
            print("{} kelimesi başlıklarda aranıyor...".format(kelime))
            time.sleep(2)
            blog.baslik_icinde_ara(kelime)
            time.sleep(5)
        elif choice == "23":

            if giris == "admin":
                print("""
                        Admin Menüsü
                    1- Kullanıcı bilgileri listele
                    2- Kullanıcı sil
                    3- Kullanıcı engelle
                    q- Çıkış
                """)
                işlem = input("Seçiminiz: ")

                if işlem == "1":
                    print("Kullanıcı bilgileri listeleniyor...")
                    time.sleep(2)
                    kullanicilar.kullanici_bilgileri_listele(giris)
                    time.sleep(5)
                elif işlem == "2":
                    kullanici_adi = input("Kaydı silinecek kullanıcı adı: ")
                    kullanicilar.kullanici_sil(kullanici_adi)
                    time.sleep(2)
                elif işlem == "3":
                    kullanici_adi = input("Engellenecek ve hesabı silinecek kullanıcı adı: ")
                    kullanicilar.kullanici_engelle(kullanici_adi)
                    time.sleep(2)
            else:
                print("Yetkiniz yok!")


