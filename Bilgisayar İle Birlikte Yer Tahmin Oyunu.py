import random
import time
print("İnsan ve Bilgisayar 1-3 Arası Rastgele Değer Tahmin Etme Oyunu")
while True:
    yeri = random.randint(1, 3)
    insan = int(input("Tahimininiz:"))
    bilgisayar = random.randint(1, 3)

    if insan == bilgisayar:
        while insan == bilgisayar:
            bilgisayar = random.randint(1, 3)

    if insan == yeri:
        print("İnsan Kazandı")
    elif bilgisayar == yeri:
        print("Bilgisayar Kazandı")
    else:
        print("Doğru Tahmin Olmadı")
    print("Yer : {}\nBilgisayar : {}\nİnsan : {}".format(yeri, bilgisayar, insan))
    time.sleep(2)





