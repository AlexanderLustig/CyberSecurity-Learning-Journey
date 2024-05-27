import random

spot1 = 1
spot2 = 2
spot3 = 3
spot4 = 4
spot5 = "X"
spot6 = 6
spot7 = 7
spot8 = 8
spot9 = 9
Turn = 1
Computer_Move = "Spot5"

def board_rows_horizontal():
    print("+-------+-------+-------+") 

def board_rows_both():
    board_rows_horizontal()
    print("|       |       |       |")
    print("|  ", spot1, "  |  ", spot2, "  |  ", spot3, "  |")
    print("|       |       |       |")
    board_rows_horizontal()
    print("|       |       |       |")
    print("|  ", spot4, "  |  ", spot5, "  |  ", spot6, "  |")
    print("|       |       |       |")
    board_rows_horizontal()
    print("|       |       |       |")
    print("|  ", spot7, "  |  ", spot8, "  |  ", spot9, "  |")
    print("|       |       |       |")
    board_rows_horizontal()

def check_game_status():
    global spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9

    # Check rows
    if spot1 == spot2 == spot3:
        return True
    if spot4 == spot5 == spot6:
        return True
    if spot7 == spot8 == spot9:
        return True

    # Check columns
    if spot1 == spot4 == spot7:
        return True
    if spot2 == spot5 == spot8:
        return True
    if spot3 == spot6 == spot9:
        return True

    # Check diagonals
    if spot1 == spot5 == spot9:
        return True
    if spot3 == spot5 == spot7:
        return True

    # No winner
    return False

def computer_move():
    global spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9, Computer_Move, Turn
    available_spots = []
    if spot1 not in ['O', 'X']:
        available_spots.append(1)
    if spot2 not in ['O', 'X']:
        available_spots.append(2)
    if spot3 not in ['O', 'X']:
        available_spots.append(3)
    if spot4 not in ['O', 'X']:
        available_spots.append(4)
    if spot6 not in ['O', 'X']:
        available_spots.append(6)
    if spot7 not in ['O', 'X']:
        available_spots.append(7)
    if spot8 not in ['O', 'X']:
        available_spots.append(8)
    if spot9 not in ['O', 'X']:
        available_spots.append(9)

    if available_spots:
        move = random.choice(available_spots)
        if move == 1:
            Computer_Move = "Spot1"
            spot1 = 'X'
        elif move == 2:
            Computer_Move = "Spot2"
            spot2 = 'X'
        elif move == 3:
            Computer_Move = "Spot3"
            spot3 = 'X'
        elif move == 4:
            Computer_Move = "Spot4"
            spot4 = 'X'
        elif move == 6:
            Computer_Move = "Spot6"
            spot6 = 'X'
        elif move == 7:
            Computer_Move = "Spot7"
            spot7 = 'X'
        elif move == 8:
            Computer_Move = "Spot8"
            spot8 = 'X'
        elif move == 9:
            Computer_Move = "Spot9"
            spot9 = 'X'
    Turn += 1

def enter_move():
    global spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9, Turn
    move = input("What spot do you want to enter? ")
    try:
        move = int(move)
        if move > 0 and move < 10 and move != 5:
            if move == 1 and spot1 not in ['O', 'X']:
                spot1 = 'O'
                Turn += 1
                return True
            elif move == 2 and spot2 not in ['O', 'X']:
                spot2 = 'O'
                Turn += 1
                return True
            elif move == 3 and spot3 not in ['O', 'X']:
                spot3 = 'O'
                Turn += 1
                return True
            elif move == 4 and spot4 not in ['O', 'X']:
                spot4 = 'O'
                Turn += 1
                return True
            elif move == 6 and spot6 not in ['O', 'X']:
                spot6 = 'O'
                Turn += 1
                return True
            elif move == 7 and spot7 not in ['O', 'X']:
                spot7 = 'O'
                Turn += 1
                return True
            elif move == 8 and spot8 not in ['O', 'X']:
                spot8 = 'O'
                Turn += 1
                return True
            elif move == 9 and spot9 not in ['O', 'X']:
                spot9 = 'O'
                Turn += 1
                return True
            else:
                print("Spot already taken.")
                return False
        else:
            print("Invalid input. Choose a number between 1 and 9, and not the already taken spot 5.")
            return False
    except ValueError:
        print("Invalid input. Please enter a number.")
        return False

def main_loop():
    while True:
        board_rows_both()
        print("The computer made their move on", Computer_Move)
        if Turn % 2 != 0:  # Player's turn
            while not enter_move():
                pass  # Keep prompting the player until a valid move is made
        else:  # Computer's turn
            computer_move()
        if check_game_status():
            board_rows_both()
            if Turn % 2 == 0:
                print("**********Winner is Player O**********")
            else:
                print("**********Winner is Player X**********")
            break
        if all(isinstance(spot, str) for spot in [spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9]):
            board_rows_both()
            print("It's a tie!")
            break

main_loop()
