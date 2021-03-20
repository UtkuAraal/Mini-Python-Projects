liste = list(range(1, 101))
kare_toplam = 0
toplam_karesi = 0
toplam = 0

for i in liste:
    kare_toplam += i ** 2
    toplam += i

toplam_karesi = toplam ** 2

cevap = toplam_karesi - kare_toplam

print(cevap)



