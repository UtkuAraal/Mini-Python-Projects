def mukemmel(fonk):
    def wrapper(sayilar):
        mukkemmeller = list()
        for sayi in sayilar:
            bolenler = 0

            for i in range(1, sayi):
                if sayi % i == 0:
                    bolenler += i

            if bolenler == sayi:
                mukkemmeller.append(sayi)

        print("{} - {} arası mükemmel sayılar:".format(sayilar[0], sayilar[-1]))
        print(mukkemmeller)

        fonk(sayilar)
    return wrapper


@mukemmel
def yazdir(sayilar):
    asallar = list()

    for sayi in sayilar:
        if sayi == 1:
            continue
        durum = True
        for i in range(2, int((sayi ** 0.5) + 1)):
            if sayi % i == 0:
                durum = False
                break
        if durum:
            asallar.append(sayi)
    print("Asallar: ")
    print(asallar)



yazdir(range(1, 1001))