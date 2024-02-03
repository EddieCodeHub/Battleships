# Import random to create CPU player moves
from random import randint

# Create Variables to generate game 
ship_num = 3
ship_symbol = "S"
hit_symbol = "X"
miss_symbol = "O"
empty_symbol = "-"


def game_intro_message():
    """
    Prints Welcome message and instructions to play the game
    """
    print("Welcome to battleships!")
    print("Column co-ordinates go from left to right")
    print("Row co-ordinates go from top to bottom")
    print("The Board is a 5x5 grid, Starting at the top left at Co-ordinate: row: 1, column: A")
    print('Co-Ordinates should be typed in the format "A1, B2, C3" ect')
    print("Each player had 3 ships each")
    print("First to sink all enemy ships wins!")
    print("To replay the game, select run program")



def print_player_grid():
    """
    Generates Players empty grid for placing ships
    """ 
    row_labels = [1, 2, 3, 4, 5]
    col_labels = ["A", "B", "C", "D", "E"]
    grid = [["-" for _ in range(5)] for _ in range(5)]

    print(" ", end=" ") 
    for col in col_labels:
        print(col, end=" ")
    print() 
    for i, row in enumerate(grid):
        print(row_labels[i], end=" ")
        for cell in row:
            print(cell, end=" ")
        print()
    print("Player 1, place your ships!")


def main_loop():
    """
    Handles the main game loop
    """
    game_intro_message()
    print_player_grid()

main_loop()


