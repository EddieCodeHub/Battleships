# Import random to create CPU player moves
from random import randint

# Create Variables to generate game 
ship_num = 3
ship_symbol = "S"
hit_symbol = "X"
miss_symbol = "O"


def game_intro_message():
    """
    Prints Welcome message and instructions to play the game
    """
    print("Welcome to battleships!")
    print("Column co-ordinates go from left to right")
    print("Row co-ordinates go from top to bottom")
    print("The Board is a 5x5 grid, Starting at the top left at Co-ordinate: row: 1, column: A")
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
    return grid

def get_ship_coordinates():
    """
    Takes in player input to generate ship co-ordinates
    """
    ship_coordinates = []
    for i in range(ship_num):
        print(f"Enter co-ordinates for ship {i + 1}")
        row = int(input("Enter row number: "))
        col = input("Enter column letter: ").upper()
        ship_coordinates.append((row, col))
    return ship_coordinates

def validate_ship_coordinates(ship_coordinates, grid):
    """
    Takes in ship co-ordinates and validates them
    """
    for row, col in ship_coordinates:
        if row < 1 or row > 5 or col not in ["A", "B", "C", "D", "E"]:
            print("Invalid co-ordinates, try again")
            get_ship_coordinates()
    for row, col in ship_coordinates:
        grid[row - 1][ord(col) - 65] = ship_symbol
    print("Ships placed!")
    print(grid)
    return grid



def main_loop():
    """
    Handles the main game loop
    """
    game_intro_message()
    grid = print_player_grid()
    ship_coordinates = get_ship_coordinates()
    validate_ship_coordinates(ship_coordinates, grid)




main_loop()


