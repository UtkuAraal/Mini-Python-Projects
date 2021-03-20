import random

kablolar = ["sarı", "kırmızı", "mavi"]

print("Bomba İmha Simülasyonu")
while True:
    dogru = random.choice(kablolar)


    print("Hangi kabloyu keseceksin ?\n1- Sarı\n2- Kırmızı\n3- Mavi")
    sec = input("Seçimin: ")

    if sec == "1":
        kablo = "sarı"
    elif sec == "2":
        kablo = "kırmızı"
    elif sec == "3":
        kablo = "mavi"
    else:
        print("Hatalı seçim!")
        continue

    if dogru == kablo:
        print("Tebrikler başardın! Doğru kabloyu seçip bombayı imha ettin!")
    else:
        print("BOOOM!!!")

    devam = input("Oyundan çıkmak için 'q' devam etmek için herhangi bir tuşa basın. :  ")

    if devam == "q":
        print("Oyundan çıkılıyor...")
        break
