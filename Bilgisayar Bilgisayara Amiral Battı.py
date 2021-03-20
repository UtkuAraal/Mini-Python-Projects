import random
import time
print("Takımlı amiral battıya hoşgeldiniz.")
bilgisayar = []
insan = []
for i in range(1, 6):
    liste = []
    for j in range(1, 6):
        liste.append("*")
    bilgisayar.append(liste)

for i in range(1, 6):
    liste2 = []
    for j in range(1, 6):
        liste2.append("*")
    insan.append(liste2)



bilgisayar_gemi = []
insan_gemi = []
for i in range(1, 6):
    rastgele_bilgisayar_yer_x = random.randint(0, 4)
    rastgele_bilgisayar_yer_y = random.randint(0, 4)
    while (rastgele_bilgisayar_yer_x, rastgele_bilgisayar_yer_y) in bilgisayar_gemi:
        rastgele_yer_x = random.randint(0, 4)
        rastgele_yer_y = random.randint(0, 4)
    bilgisayar_gemi.append((rastgele_bilgisayar_yer_x, rastgele_bilgisayar_yer_y))

for i in range(1, 6):
    rastgele_insan_yer_x = random.randint(0, 4)
    rastgele_insan_yer_y = random.randint(0, 4)
    while (rastgele_insan_yer_x, rastgele_insan_yer_y) in bilgisayar_gemi:
        rastgele_yer_x = random.randint(0, 4)
        rastgele_yer_y = random.randint(0, 4)
    insan_gemi.append((rastgele_insan_yer_x, rastgele_insan_yer_y))


sıradaki_tahta = bilgisayar
sıra = "insan"
tahta_adı = "bilgisayar"
while True:
    print("{} tahtası".format(tahta_adı))
    print("  1 2 3 4 5")
    print("1 {} {} {} {} {}".format(sıradaki_tahta[0][0], sıradaki_tahta[1][0], sıradaki_tahta[2][0], sıradaki_tahta[3][0], sıradaki_tahta[4][0]))
    print("2 {} {} {} {} {}".format(sıradaki_tahta[0][1], sıradaki_tahta[1][1], sıradaki_tahta[2][1], sıradaki_tahta[3][1], sıradaki_tahta[4][1]))
    print("3 {} {} {} {} {}".format(sıradaki_tahta[0][2], sıradaki_tahta[1][2], sıradaki_tahta[2][2], sıradaki_tahta[3][2], sıradaki_tahta[4][2]))
    print("4 {} {} {} {} {}".format(sıradaki_tahta[0][3], sıradaki_tahta[1][3], sıradaki_tahta[2][3], sıradaki_tahta[3][3], sıradaki_tahta[4][3]))
    print("5 {} {} {} {} {}".format(sıradaki_tahta[0][4], sıradaki_tahta[1][4], sıradaki_tahta[2][4], sıradaki_tahta[3][4], sıradaki_tahta[4][4]))

    if len(bilgisayar_gemi) == 0:
        print("Kaptan, rakip gemilerini ortadan kaldırdık. Savaşı Biz kazandık!")
        break
    elif len(insan_gemi) == 0:
        print("Kaptan, bütün gemilerimiz vuruldu. Bilgisayar kazandı!")
        break
    vur_x = random.randint(0, 4)
    vur_y = random.randint(0, 4)

    if sıra == "insan":
        while bilgisayar[vur_x][vur_y] != "*":
            vur_x = random.randint(0, 4)
            vur_y = random.randint(0, 4)

        if (vur_x, vur_y) in bilgisayar_gemi:
            print("Kaptan, 1 gemi vurduk!")
            bilgisayar_gemi.remove((vur_x, vur_y))
            bilgisayar[vur_x][vur_y] = "G"
            time.sleep(2)
        else:
            print("Kaptan, vuruşu kaçırdık!")
            bilgisayar[vur_x][vur_y] = "-"
            time.sleep(2)
            sıra = "bilgisayar"
            sıradaki_tahta = insan
            tahta_adı = "insan"
    elif sıra == "bilgisayar":
        while insan[vur_x][vur_y] != "*":
            vur_x = random.randint(0, 4)
            vur_y = random.randint(0, 4)

        if (vur_x, vur_y) in insan_gemi:
            print("Kaptan, 1 gemimizi vurdular!")
            insan_gemi.remove((vur_x, vur_y))
            insan[vur_x][vur_y] = "G"
            time.sleep(2)
        else:
            print("Kaptan, rakip vuruşu kaçırdı!")
            insan[vur_x][vur_y] = "-"
            time.sleep(2)
            sıra = "insan"
            sıradaki_tahta = bilgisayar
            tahta_adı = "bilgisayar"


