asal = []

def asal_carpanlar(sayı):
    sayac = 2
    while True:
        if sayı == 1:
            break

        if sayı % sayac == 0:
            if not(sayac in asal):
                asal.append(sayac)
            sayı //= sayac
            continue
        else:
            sayac += 1

sayı = int(input("Sayıyı girin : "))

asal_carpanlar(sayı)
print(asal)
print(asal[-1])