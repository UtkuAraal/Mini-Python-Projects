import random
import time

def kazandim_mi(bilgisayar, insan):
    if (bilgisayar == insan):
        print("Berabere")
    elif ((insan == "t") and (bilgisayar == "m")) or ((insan == "m") and (bilgisayar == "k")) or ((insan == "k") and (bilgisayar == "t")):
        print("Kazandın İnsan")
    else:
        print("Bilgisayar Kazandı")

while True:
    secim = random.choice(["t", "k", "m"])

    kullanıcı = input("Taş(t), Kağıt(k), Makas(m): ")

    kazandim_mi(secim, kullanıcı)
    print("Bilgisayar {} seçti\nİnsan {} seçti".format(secim, kullanıcı))
    time.sleep(2)
