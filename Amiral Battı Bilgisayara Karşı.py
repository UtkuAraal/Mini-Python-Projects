import random
import time
print("Amiral Battı")
human_board = [["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"]]
human_places = []
computer_places = []
computer_board = [["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"]]
turn_board = []
turn = "human"
board = "computer"
for i in range(1, 6):
    random_x = random.randint(0, 4)
    random_y = random.randint(0, 4)
    while (random_x, random_y) in human_places:
        random_x = random.randint(0, 4)
        random_y = random.randint(0, 4)
    human_places.append((random_x, random_y))

for i in range(1, 6):
    random_x = random.randint(0, 4)
    random_y = random.randint(0, 4)
    while (random_x, random_y) in computer_places:
        random_x = random.randint(0, 4)
        random_y = random.randint(0, 4)
    computer_places.append((random_x, random_y))


while True:

    if not human_places:
        print("Computer won!")
        break
    elif not computer_places:
        print("Human won!")
        break


    if turn == "human":
        turn_board = computer_board
        board = "computer"
    elif turn == "computer":
        turn_board = human_board
        board = "human"

    print("{} board".format(board))
    print("  1  2  3  4  5")
    print("1 {}  {}  {}  {}  {}".format(turn_board[0][0], turn_board[0][1], turn_board[0][2], turn_board[0][3], turn_board[0][4]))
    print("2 {}  {}  {}  {}  {}".format(turn_board[1][0], turn_board[1][1], turn_board[1][2], turn_board[1][3], turn_board[1][4]))
    print("3 {}  {}  {}  {}  {}".format(turn_board[2][0], turn_board[2][1], turn_board[2][2], turn_board[2][3], turn_board[2][4]))
    print("4 {}  {}  {}  {}  {}".format(turn_board[3][0], turn_board[3][1], turn_board[3][2], turn_board[3][3], turn_board[3][4]))
    print("5 {}  {}  {}  {}  {}".format(turn_board[4][0], turn_board[4][1], turn_board[4][2], turn_board[4][3], turn_board[4][4]))

    if turn == "human":
        try:
            shoot_x = int(input("Where (x): "))
            shoot_y = int(input("Where (y): "))
        except ValueError:
            print("Only Number!")
            continue
        if shoot_x > 5 or shoot_y > 5 or shoot_x < 0 or shoot_y < 0:
            print("Off the map!")
            continue
        
        if computer_board[shoot_y - 1][shoot_x - 1] == "*":
            if (shoot_y - 1, shoot_x - 1) in computer_places:
                print("You shoot a sheep!")
                computer_board[shoot_y - 1][shoot_x - 1] = "S"
                computer_places.pop(computer_places.index((shoot_y - 1, shoot_x - 1)))
                time.sleep(2)
                continue
            else:
                print("Missed!")
                computer_board[shoot_y - 1][shoot_x - 1] = "_"
                time.sleep(2)
                turn = "computer"
        else:
            print("You already shot this place! Try Again")
            time.sleep(2)
            continue
    elif turn == "computer":
        random_shoot_x = random.randint(0, 4)
        random_shoot_y = random.randint(0, 4)

        while human_board[random_shoot_x][random_shoot_y] != "*":
            random_shoot_x = random.randint(0, 4)
            random_shoot_y = random.randint(0, 4)

        if (random_shoot_x, random_shoot_y) in human_places:
            print("Computer shoot your sheep!")
            human_board[random_shoot_x][random_shoot_y] = "S"
            human_places.pop(human_places.index((random_shoot_x, random_shoot_y)))
            time.sleep(2)
            continue
        else:
            print("Computer Missed!")
            human_board[random_shoot_x][random_shoot_y] = "_"
            time.sleep(2)
            turn = "human"





            


