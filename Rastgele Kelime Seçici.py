import random

kelime1 = ["He", "She"]
kelime2 = ["made", "makes", "drink", "play", "is looking at"]
kelime3 = ["a sandwich", "a cake", "a cup of water", "basketball", "you", "me", "the beach"]

devam = "evet"
while devam == "evet":
    sec1 = random.choice(kelime1)
    sec2 = random.choice(kelime2)
    sec3 = random.choice(kelime3)
    print(sec1, sec2, sec3)
    secenek = input("Devam edilsin mi ? : (evet/hayır) ")
    if secenek == "hayır":
        devam = "hayır"