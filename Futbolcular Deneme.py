def takim_ayir(satır):
    satır = satır[:-1]
    liste = satır.split(",")
    isim = liste[0]
    takım = liste[1]

    gonder = isim + "\n"
    if takım == "Galatasaray":
        gs.append(gonder)
    elif takım == "Fenerbahçe":
        fb.append(gonder)
    elif takım == "Beşiktaş":
        bjk.append(gonder)


with open("futbolcular.txt", "r", encoding = "utf-8") as file:
    gs = []
    fb = []
    bjk = []
    for i in file:
        takim_ayir(i)

    with open("gs.txt", "w") as gs_file:
        for i in gs:
            gs_file.write(i)
    with open("fb.txt", "w") as fb_file:
        for i in fb:
            fb_file.write(i)
    with open("bjk.txt", "w") as bjk_file:
        for i in bjk:
            bjk_file.write(i)