import os


def belge():
    for i in os.walk("/"):
        yield i

for i in belge():
    for dosya in i[2]:
        if dosya.endswith(".pdf"):
            with open("pdf_dosyalari.txt", "a", encoding="utf-8") as file:
                file.write("Yeri: " + i[0] + "\t" + "Adı: " + dosya + "\n")
        elif dosya.endswith(".mp4"):
            with open("mp4_dosyaları.txt") as file:
                file.write("Yeri: " + i[0] + "\t" + "Adı: " + dosya + "\n")
        elif dosya.endswith(".txt"):
            with open("txt_dosyaları.txt", "a", encoding="utf-8") as file:
                file.write("Yeri: " + i[0] + "\t" + "Adı: " + dosya + "\n")

