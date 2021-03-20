print("Atm Makinesine Hoşgeldiniz")

sys_kullanici1 = "Utku"
sys_parola1 = "Utku"
para1 = 1000
gizli1 = "1"
iban1 = 123
bildirim1 = 0

sys_kullanici2 = "Yağız"
sys_parola2 = "Yağız"
para2 = 1000
gizli2 = "2"
iban2 = 456
bildirim2 = 0

sys_kullanici3 = "Bilgisayar"
sys_parola3 = "Bilgisayar"
para3 = 1000
gizli3 = 3
iban3 = 789
bildirim3 = 0

kullanici1 = [sys_kullanici1, sys_parola1, para1, gizli1, iban1, bildirim1]
kullanici2 = [sys_kullanici2, sys_parola2, para2, gizli2, iban2, bildirim2]
kullanici3 = [sys_kullanici3, sys_parola3, para3, gizli3, iban3, bildirim3]

giris_hakki =3

def yatir(miktar):
    giren[2] += miktar

def cek(miktar):
    giren[2] -= miktar

def aktar(aktarilacak_hesap, miktar):
    giren[2] -= miktar
    aktarilacak_hesap[2] += miktar
    aktarilacak_hesap[5] += 1
    print("Aktarma Başarılı")




while True:
    giris = False
    giren = None
    giren_kullanici = input("Kullanıcı Adı: ")
    giren_parola = input("Parola: ")

    if (giren_kullanici == kullanici1[0]) and (giren_parola == kullanici1[1]):
        giris = True
        giren = kullanici1

         # Kullanıcı 1 Giriş Yaptı
    elif (giren_kullanici == kullanici2[0]) and (giren_parola == kullanici2[1]):
        giris = True
        giren = kullanici2

        # Kullanıcı 2 Giriş Yaptı
    elif (giren_kullanici == kullanici3[0]) and (giren_parola == kullanici3[1]):
        giris = True
        giren = kullanici3

        # Kullanıcı 3 Giriş Yaptı
    else:
        print("Yanlış Kullanıcı Adı Veya Parola")
        unuttu_mu = input("Şifrenizi Unuttuysanız 1' i Bu Ekranı Kapatmak İçin 2'yi Tuşlayın")
        if (unuttu_mu == "1"):
            kim = input("Kullanıcı Adınız: ")
            gizli_soru = input("Gizli Rakam: ")

            if (kim == kullanici1[0]) and (gizli_soru == kullanici1[3]):
                print("Şifreniz", kullanici1[1])
                continue
            elif (kim == kullanici2[0]) and (gizli_soru == kullanici2[3]):
                print("Şifreniz", kullanici2[1])
                continue
            elif (kim == kullanici3[0]) and (gizli_soru == kullanici3[3]):
                print("Şifreniz", kullanici3[1])
                continue
            else:
                print("Yanlış Giriş")
        giris_hakki -= 1


    if (giris_hakki <= 0):
        print("Çok Sayıda Geçersiz Bilgi\nÇıkış Yapılıyor...")
        break

    if giris == True:
        while True:
            print("""
                İşlem Seçiniz
                
                {} Hesaba Gelen Para Bildirimi
                
                0- Bildirimleri Okudum
                1- Bakiye Sorgulama
                2- Para Yatırma
                3- Para Çekme
                4- Para Aktarma
                q- Çıkış
            """.format(giren[5]))
            secim = input("Seçiminiz: ")

            if (secim == "q"):
                print("Çıkış Yapılıyor...")
                break
            elif secim == "0":
                giren[5] = 0
            elif secim == "1":
                print("Bakiyeniz:", giren[2])
            elif secim == "2":
                miktar = int(input("Yatırmak İstediğiniz Miktarı Girin: "))
                yatir(miktar)
            elif secim == "3":
                miktar = int(input("Çekmek İstediğiniz Miktarı Girin: "))
                if miktar <= giren[2]:
                    cek(miktar)
                else:
                    print("Bu Tutarı Çekemezsiniz")
            elif secim == "4":
                miktar = int(input("Aktarılacak Miktarı Giriniz: "))
                if miktar > giren[2]:
                    print("Bu Miktarı Gönderemezsiniz")
                    continue

                aktarilacak_iban = int(input("Aktarmak İstediğiniz İbanı Girin: "))
                if aktarilacak_iban == giren[4]:
                    print("Kendinize Aktarma Yapamazsınız")
                elif aktarilacak_iban == kullanici1[4]:
                    aktar(kullanici1, miktar)
                elif aktarilacak_iban == kullanici2[4]:
                    aktar(kullanici2, miktar)
                elif aktarilacak_iban == kullanici3[4]:
                    aktar(kullanici3, miktar)
                else:
                    print("Geçersiz İban")


