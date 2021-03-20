from Todo import *
import time

liste = Liste()
while True:
    print("""
            Yapılacaklar Listesi
        1- Todo listele
        2- Todo ekle
        3- Todo tamamla
        4- Güne göre sırala
        5- Kategoriye göre
        6- Saate göre
        7- Yere göre
        8- Bilgileri tam olan yapılacakları listele
    """)
    choice = input("Seçiminiz: ")

    if choice == "q":
        print("Çıkış yapılıyor...")
    elif choice == "1":
        liste.todo_listele()
        time.sleep(5)
    elif choice == "2":
        print("Belirtmek istemediğiniz değerleri boş geçin.")
        gorev = input("Todoya yazmak istediğiniz: ")
        if gorev == "":
            print("Bu alan boş bırakılamaz!")
            continue
        kategori = input("Kategori: ")
        gun = input("Gün: ")
        yer = input("Yer: ")
        saat = input("Saat")
        liste2 = [gorev, kategori, gun, yer, saat]

        for i in range(0, len(liste2)):
            if liste2[i] == "":
                liste2[i] = "Belirtilmedi!"

        todo = Todo(liste2[0], liste2[1], liste2[2], liste2[3], liste2[4])
        liste.todo_ekle(todo)
    elif choice == "3":
        try:
            id = int(input("Tamamladığınız todo id'si: "))
        except ValueError:
            print("Sadece id değeri!")
            continue
        liste.tamamla(id)
        time.sleep(2)
    elif choice == "4":
        gun = input("Aranacak gün: ")
        liste.gune_gore(gun)
        time.sleep(5)
    elif choice == "5":
        kategori = input("Aranacak kategori: ")
        liste.kategoriye_gore(kategori)
        time.sleep(5)
    elif choice == "6":
        saat = input("Aranacak saat: ")
        liste.saate_gore(saat)
        time.sleep(5)
    elif choice == "7":
        yer = input("Aranacak yer: ")
        liste.yere_gore(yer)
        time.sleep(5)
    elif choice == "8":
        liste.tam_bilgi()
        time.sleep(5)

