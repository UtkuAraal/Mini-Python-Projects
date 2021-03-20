ekok = []
liste = list(range(1, 21))
bolen = 2

def kontrol():
    for k in liste:
        if k != 1:
            return True
    return False

while kontrol():
    deger = "hayır"
    for i in liste:
        if i % bolen == 0:
            deger = "evet"
            liste[liste.index(i)] //= bolen

    if deger == "evet":
        ekok.append(bolen)
    else:
        bolen += 1

cevap = 1
for j in ekok:
    cevap *= j
print(cevap)



