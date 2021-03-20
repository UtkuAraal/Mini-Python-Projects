import random
insan = 100
bilgisayar = 100
secenek = ["sol", "sağ"]
print("Boks Oyunu")
turn = "insan"
while True:
    print("İnsan: {}\nBilgisayar: {}".format(insan, bilgisayar))
    if insan == 0:
        print("Bilgisayar kazandı!")
        break
    elif bilgisayar == 0:
        print("İnsan kazandı!")
        break

    if turn == "insan":
        yon = input("Sağ mı Sol mu vurmak istersin?: ")

        if yon != "sağ" and yon != "sol":
            print("Geçersiz hamle!")
            continue

        bilgisayar_koru = random.choice(secenek)

        if yon == bilgisayar_koru:
            print("Bilgisayar vuruşu bloke etti!")
        else:
            print("Bilgisayar vuruşa engel olamadı ve darbe yedi!")
            bilgisayar -= 10
        turn = "bilgisayar"
    elif turn == "bilgisayar":
        bilgisayar_vur = random.choice(secenek)

        insan_koru = input("Sağı mı yoksa solu mu korumak istersin?: ")
        while insan_koru != "sağ" and insan_koru != "sol":
            insan_koru = input("Sağı mı yoksa solu mu korumak istersin?: ")

        if bilgisayar_vur == bilgisayar_koru:
            print("Vuruşu bloke ettin ve darbe yemedin!")
        else:
            print("Vuruşu bloke edemedin ve darbe yedin!")
            insan -= 10
        turn = "insan"


