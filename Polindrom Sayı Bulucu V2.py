polindrom = 0
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        sonuc = i * j
        sonuc = str(sonuc)
        if sonuc == sonuc[::-1] and polindrom < int(sonuc):
            polindrom = int(sonuc)

print(polindrom)