alan = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
turn = "player 1"
while True:
    print("""
         {} | {} | {}
       --------------
         {} | {} | {}
       --------------
         {} | {} | {}      
            
    """.format(alan[0], alan[1], alan[2], alan[3], alan[4], alan[5], alan[6], alan[7], alan[8]))

    if ((alan[0] == "X") and (alan[1] == "X") and (alan[2] == "X")) or ((alan[3] == "X") and (alan[4] == "X") and (alan[5] == "X")) or ((alan[6] == "X") and (alan[7] == "X") and (alan[8] == "X")) or ((alan[0] == "X") and (alan[3] == "X") and (alan[6] == "X")) or ((alan[1] == "X") and (alan[4] == "X") and (alan[7] == "X")) or ((alan[2] == "X") and (alan[5] == "X") and (alan[8] == "X")) or ((alan[0] == "X") and (alan[4] == "X") and (alan[8] == "X")) or ((alan[2] == "X") and (alan[4] == "X") and (alan[6] == "X")):
        print("Player 1 Kazandı!")
        break
    elif ((alan[0] == "O") and (alan[1] == "O") and (alan[2] == "O")) or ((alan[3] == "O") and (alan[4] == "O") and (alan[5] == "O")) or ((alan[6] == "O") and (alan[7] == "O") and (alan[8] == "O")) or ((alan[0] == "O") and (alan[3] == "O") and (alan[6] == "O")) or ((alan[1] == "O") and (alan[4] == "O") and (alan[7] == "O")) or ((alan[2] == "O") and (alan[5] == "O") and (alan[8] == "O")) or ((alan[0] == "O") and (alan[4] == "O") and (alan[8] == "O")) or ((alan[2] == "O") and (alan[4] == "O") and (alan[6] == "O")):
        print("Player 2 Kazandı!")
        break
    elif not("-" in alan):
        print("Berabere!")
        break

    try:
        while True:
            yer = int(input("{} Koymak istediğiniz yer: ".format(turn)))
            if (yer in range(1, 10)):
                break
            else:
                print("Geçerli Yer Girin!")
                continue
    except ValueError:
        print("Lütfen sadece rakam girin!")
        continue

    if alan[yer-1] != "-":
        print("Bu alan zaten dolu!")
        continue

    if turn == "player 1":
        alan[yer-1] = "X"
        turn = "player 2"
    elif turn == "player 2":
        alan[yer-1] = "O"
        turn = "player 1"







