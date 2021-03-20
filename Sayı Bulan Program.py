import random
print(""""
Şimdi Sayını Bulacağım (1-100)
""")
low = 1
high = 100

while True:
    tahmini = random.randint(low, high)
    print("Tahminim {} Yüksek mi (y), Düşük mü (d), bildim mi (b)?".format(tahmini))
    cevap = input("Cevap: ")

    if (cevap == "y"):
        high = tahmini - 1
    elif (cevap == "d"):
        low = tahmini + 1
    elif (cevap == "b"):
        print("Bu oyunda iyiyimdir.")
        break
    else:
        print("Yanlış Tuşlama Yaptın")
