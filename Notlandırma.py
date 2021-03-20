def not_hesapla(satır):
    satır = satır[:-1]
    liste = satır.split(",")
    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])
    son_not = not1 * (3/10) + not2 * (3/10) + not3 * (4/10)

    if (son_not >= 90):
        harf = "AA"
    elif (son_not >= 85):
        harf = "BA"
    elif (son_not >= 80):
        harf = "BB"
    elif (son_not >= 75):
        harf = "CB"
    elif (son_not >= 70):
        harf = "CC"
    elif (son_not >= 65):
        harf = "CD"
    elif (son_not >= 60):
        harf = "DD"
    else:
        harf = "FF"

    liste_icin = isim + "\n"
    if harf == "FF":
        kalanlar_listesi.append(liste_icin)
    else:
        gecenler_listesi.append(liste_icin)

    return isim + "--------------------> " + harf + "\n"



with open("notlar.txt", "r", encoding = "utf-8") as file:

    eklenecekler_listesi = []
    kalanlar_listesi = []
    gecenler_listesi = []

    for i in file:
        eklenecekler_listesi.append(not_hesapla(i))

    with open("kalanlar.txt", "w", encoding = "utf-8") as kalanlar:
        for i in kalanlar_listesi:
            kalanlar.write(i)

    with open ("geçenler.txt", "w", encoding = "utf-8") as gecenler:
        for i in gecenler_listesi:
            gecenler.write(i)

    with open("Sonuclar.txt", "w", encoding = "utf-8") as file2:

        for i in eklenecekler_listesi:
            file2.write(i)