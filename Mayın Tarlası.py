import random
import time
print("Mayın Tarlası")

def tarla_olustur():
    print("   1  2  3  4  5")
    for k in range(0, 5):
        print(k + 1, end = "  ")
        for l in range(0, 5):
            print(tarla_gorunum[l][k] + " ", end = " ")
        print("")


tarla_gorunum = []
for i in range(1, 6):
    liste = []
    for j in range(1, 6):
        liste.append("*")
    tarla_gorunum.append(liste)
mayinlar = []

for i in range(1, 11):
    mayin_x = random.randint(0, 4)
    mayin_y = random.randint(0, 4)
    mayin = (mayin_x, mayin_y)

    while mayin in mayinlar:
        mayin_x = random.randint(0, 4)
        mayin_y = random.randint(0, 4)
        mayin = (mayin_x, mayin_y)

    mayinlar.append(mayin)

while True:
    kaldi = 0
    for i in tarla_gorunum:
        for t in i:
            if t == "*":
                kaldi += 1
    tarla_olustur()
    if kaldi == 10:
        print("Tebrikler kazandınız!")
        break

    print("Basmak istediğiniz bölge;")
    try:
        bas_x = int(input("X koordinatı : "))
        bas_y = int(input("Y koordinatı : "))
    except ValueError:
        print("Lütfen rakam giriniz!")
        time.sleep(2)
        continue

    if (bas_x < 1) or (bas_x > 5) or (bas_y < 1) or (bas_x > 5):
        print("Geçersiz hamle!")
        time.sleep(2)
        continue
    bas_x -= 1
    bas_y -= 1
    if tarla_gorunum[bas_x][bas_y] == "*":
        if (bas_x, bas_y) in mayinlar:
            print("Bomba!")
            for i, j in mayinlar:
                tarla_gorunum[i][j] = "M"
            tarla_olustur()
            break
        else:
            kac = 0
            cevre = [(bas_x - 1, bas_y - 1), (bas_x, bas_y-1), (bas_x + 1, bas_y - 1), (bas_x - 1, bas_y), (bas_x + 1, bas_y), (bas_x - 1, bas_y + 1), (bas_x, bas_y + 1), (bas_x + 1, bas_y + 1)]
            for i in range(0, 8):
                if cevre[i] in mayinlar:
                    kac += 1
            tarla_gorunum[bas_x][bas_y] = str(kac)
    else:
        print("Buraya zaten bastınız!")
        continue

