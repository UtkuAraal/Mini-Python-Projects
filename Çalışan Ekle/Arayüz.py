from Çalışan import *
import time

def email_kontrol(email):
    if (email.find("@") != -1) and email.endswith(".com"):
        pass
    else:
        raise SyntaxError("Email uygun formatta değil!")

def numara_kontrol(telefon):
    if len(telefon) == 10:
        pass
    else:
        raise Warning("Eksik telefon numarası girişi!")

print("Çalışan Kontrol Programı")
çalışanlar = Çalışanlar()
while True:
    print("""
            Çalışan Menüsü
        
        1- Çalışan ekle
        2- Çalışanları listele
        3- Çalışan sil
        4- Pozisyona göre ara
        5- Çalışan numaraları listesini göster
        6- Çalışana zam yap
        7- Çalışan sorgula
        8- Çalışan izin hakkı ver
        9- Çalışan kullandığı izin gir
        10- Çalışan ismiyle numarasını ara
        11- Toplam ödenen maaş
        12- İsim ile bilgi göster
        
        Çıkış yapmak için 'q' ya basın.
    
    """)
    choice = input("Seçiminiz: ")

    if choice == "q":
        print("Program kapatılıyor...")
        çalışanlar.baglantiyi_kes()
        break
    elif choice == "1":
        try:
            isim = input("İsim: ")
            soyisim = input("Soyisim: ")
            telefon = input("Telefon (5** *** ** **): ")
            telefon = telefon.replace(" ", "")
            numara_kontrol(telefon)
            telefon = int(telefon)
            email = input("E-mail: ")
            email_kontrol(email)
            numara = int(input("Numara: "))
            pozisyon = input("Pozisyon: ")
            maas = int(input("Maaş: "))
        except ValueError:
            print("Değerleri uygun formatta girin!")
            continue
        except SyntaxError as hata:
            print(hata)
            continue
        except Warning as hata2:
            print(hata2)
            continue
        calisan = Çalışan(isim, soyisim, telefon, email, numara, pozisyon, maas)
        çalışanlar.calisan_ekle(calisan)
        time.sleep(2)
    elif choice == "2":
        print("Çalışan listesi: ")
        çalışanlar.calisan_listele()
        time.sleep(2)
    elif choice == "3":
        çalışanlar.calisan_numaralari_goster()
        try:
            numara = int(input("Kaydı silinecek çalışan numarası: "))
        except ValueError:
            print("Sadece numara!")
            time.sleep(2)
            continue
        çalışanlar.calisan_sil(numara)
        time.sleep(2)
    elif choice == "4":
        pozisyon = input("Pozisyon: ")
        çalışanlar.pozisyona_gore_ara(pozisyon)
        time.sleep(2)
    elif choice == "5":
        çalışanlar.calisan_numaralari_goster()
        time.sleep(2)
    elif choice == "6":
        çalışanlar.calisan_numaralari_goster()
        try:
            numara = int(input("Çalışan numarası: "))
            print("1- Yüzde olarak artır\n2- Birim olarak direkt artır")
            secim = input("Seçiminiz (yuzde/normal): ")
            miktar = int(input("Artırmak istediğiniz miktar: "))
        except ValueError:
            print("Uygun olmayan değer girişi!")
            continue
        çalışanlar.calisan_maas_guncelle(numara, miktar, secim)
        time.sleep(2)
    elif choice == "7":
        try:
            numara = int(input("Sorgulanacak numara: "))
        except ValueError:
            print("Sadece sayı!")
            continue
        çalışanlar.calisan_sorgula(numara)
        time.sleep(2)
    elif choice == "8":
        çalışanlar.calisan_numaralari_goster()
        try:
            numara = int(input("İzin verilecek çalışan numarası: "))
            hak = int(input("Tanımlanacak gün sayısı: "))
        except ValueError:
            print("Sadece sayı!")
            continue
        çalışanlar.izin_ver(numara, hak)
        time.sleep(2)
    elif choice == "9":
        çalışanlar.calisan_numaralari_goster()
        try:
            numara = int(input("Numara: "))
            kullandi = int(input("Kaç gün izin kullandı: "))
        except ValueError:
            print("Sadece sayı")
        çalışanlar.izin_kullandi(numara, kullandi)
        time.sleep(2)
    elif choice == "10":
        isim = input("İsim: ")
        soyisim = input("Soyisim: ")
        çalışanlar.isimle_numara_ara(isim, soyisim)
        time.sleep(2)
    elif choice == "11":
        çalışanlar.odenen_maaslar()
        time.sleep(2)
    elif choice == "12":
        isim = input("İsim: ")
        soyisim = input("Soyisim: ")
        çalışanlar.isimle_bilgi(isim, soyisim)
        time.sleep(2)