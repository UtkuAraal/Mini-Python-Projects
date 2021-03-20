import random

puan = 100

while True:
    rastgele = random.randint(1,100)
    sayac = 0
    print("Tahmin Oyunu")

    while True:

        try:
            tahmin = int(input("{}. Tahmininiz: ".format(sayac+1)))
        except ValueError:
            print("Sadece sayı giriniz! ")
            continue

        if tahmin == rastgele:
            print("Tebrikler bildiniz!")
            puan += 50
            sayac += 1
            break
        elif tahmin < rastgele:
            print("Daha büyük değer girin")
            puan -= 10
            sayac += 1

        else:
            print("Daha küçük değer girin")
            puan -= 10
            sayac += 1

    with open("members.txt", "a") as file:
        file.write(str(sayac) + " tahminde bildiniz.\t" + "toplam puan: " + str(puan) + "\n" )




