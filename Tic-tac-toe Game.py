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
    global spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9
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
            spot1 = 'X'
        elif move == 2:
            spot2 = 'X'
        elif move == 3:
            spot3 = 'X'
        elif move == 4:
            spot4 = 'X'
        elif move == 6:
            spot6 = 'X'
        elif move == 7:
            spot7 = 'X'
        elif move == 8:
            spot8 = 'X'
        elif move == 9:
            spot9 = 'X'
    
    
def enter_move():
    global spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9, Turn
    move = input("What spot do you want to enter? ")
    try:
        move = int(move)
        if move > 0 and move < 10 and move != 5:
            if move == 1 and spot1 not in ['O', 'X']:
                spot1 = 'O'
            elif move == 2 and spot2 not in ['O', 'X']:
                spot2 = 'O'
            elif move == 3 and spot3 not in ['O', 'X']:
                spot3 = 'O'
            elif move == 4 and spot4 not in ['O', 'X']:
                spot4 = 'O'
            elif move == 6 and spot6 not in ['O', 'X']:
                spot6 = 'O'
            elif move == 7 and spot7 not in ['O', 'X']:
                spot7 = 'O'
            elif move == 8 and spot8 not in ['O', 'X']:
                spot8 = 'O'
            elif move == 9 and spot9 not in ['O', 'X']:
                spot9 = 'O'
            else:
                print("Spot already taken.")
        else:
            print("Invalid input. Choose a number between 1 and 9, and not the already taken spot 5.")
    except ValueError:
        print("Invalid input. Please enter a number.")
        
    Turn += 2

def main_loop():
    while True:
        board_rows_both()
        enter_move()
        computer_move()
        if(check_game_status()):
            if(Turn % 2 != 0):
                print("Winner is Player O")
                break
            else:
                print("Winner is Player X")
                break
        else:
            if all(isinstance(spot, str) for spot in [spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9]):
                board_rows_both()
                print("It's a tie!")
                break
            else:
                continue
        
main_loop()


#def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game

# def draw_move(board):
    # The function draws the computer's move and updates the board.
    
