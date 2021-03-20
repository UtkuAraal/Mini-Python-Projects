import random
print("""
Zar Tahmin Programı
""")

while True:
    zar = random.randint(1, 6)
    kullanici = int(input("Tahmininiz: "))

    if (zar == kullanici):
        print("Tebrikler Bildiniz!")
    else:
        print("Bilemediniz, Sayımız", zar)
