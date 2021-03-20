import random
print("""
Yer Bulma Oyunu
""")
puan = 0
while True:
    saklanan_yer = random.randint(1,6)
    secilen_yer = input("1-6 Arası Yer Seçiniz: ")
    if secilen_yer == "q":
        print("Kazandığınız Puan : {}\nÇıkış Yapılıyor...".format(puan))
        break
    secilen_yer = int(secilen_yer)
    if secilen_yer == saklanan_yer:
        print("Tebrikler Buldun! +20 puan")
        puan += 20
    else:
        print("Bulamadın! Yeri {} idi".format(saklanan_yer))
        puan -= 5



