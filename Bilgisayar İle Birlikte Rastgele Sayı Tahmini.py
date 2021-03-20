import random
import time
sayı = random.randint(1, 100)
sıra = "insan"
low = 1
high = 100
while True:
    if sıra == "insan":
        cevap = int(input("İnsan Tahminini : "))
        sıra = "bilgisayar"
    elif sıra == "bilgisayar":
        cevap = random.randint(low, high)
        print("Bilgisayar Tahmini :", cevap)
        sıra = "insan"

    if sayı == cevap:
        print("Tebrikler bildiniz! sayı = {} idi".format(sayı))
        break
    elif sayı < cevap:
        print("Daha düşük bir tahminde bulunun!")
        high = cevap - 1
        time.sleep(2)
    elif sayı > cevap:
        print("Daha yüksek bir tahminde bulunun!")
        low = cevap + 1
        time.sleep(2)