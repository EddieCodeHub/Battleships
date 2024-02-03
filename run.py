# Import random to create CPU player moves
from random import randint

# Create Variables to generate game 
ship_num = 3
ship_symbol = "S"
hit_symbol = "X"
miss_symbol = "O"
row_labels = [1, 2, 3, 4, 5]
col_labels = ["A", "B", "C", "D", "E"]


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
    player_grid = [["-" for _ in range(5)] for _ in range(5)]

    print(" ", end=" ") 
    for col in col_labels:
        print(col, end=" ")
    print() 
    for i, row in enumerate(player_grid):
        print(row_labels[i], end=" ")
        for cell in row:
            print(cell, end=" ")
        print()
    print("Player 1, place your ships!")
    return player_grid

def get_ship_coordinates():
    """
    Takes in player input to generate ship co-ordinates
    """
    player_ship_coordinates = []
    for i in range(ship_num):
        print(f"Enter co-ordinates for ship {i + 1}")
        row = int(input("Enter row number: "))
        col = input("Enter column letter: ").upper()
        player_ship_coordinates.append((row, col))
    return player_ship_coordinates

def validate_ship_coordinates(player_ship_coordinates, player_grid, col_labels, row_labels):
    """
    Takes in ship co-ordinates and validates them and prints the grid with ships placed
    """
    for row, col in player_ship_coordinates:
        row_index = row - 1
        col_index = ord(col) - 65
        if player_grid[row_index][col_index] == ship_symbol:
            print("You already have a ship there!")
            get_ship_coordinates()
        player_grid[row_index][col_index] = ship_symbol
    print("Ships placed!")
    print(" ", end=" ") 
    for col in col_labels:
        print(col, end=" ")
    print() 
    for i, row in enumerate(player_grid):
        print(row_labels[i], end=" ")
        for cell in row:
            print(cell, end=" ")
        print()
    return player_grid



def generate_cpu_ships(col_labels, row_labels):
    """
    Generates CPU ships and places them on the grid but not visible to the player
    """
    cpu_grid = [["-" for _ in range(5)] for _ in range(5)]
    # Create a new grid to store the shots
    shot_grid = [["-" for _ in range(5)] for _ in range(5)]
    for i in range(ship_num):
        row = randint(1, 5)
        col = randint(0, 4)
        if cpu_grid[row - 1][col] == ship_symbol:
            continue
        cpu_grid[row - 1][col] = ship_symbol
    
    # Print the shot grid instead of the cpu grid
    print(" ", end=" ") 
    for col in col_labels:
        print(col, end=" ")
    print() 
    for i, row in enumerate(shot_grid):
        print(row_labels[i], end=" ")
        for cell in row:
            print(cell, end=" ")
        print()
    return cpu_grid, shot_grid 


def get_player_guess():
    """
    Takes in player input to generate guesses and print appropriate symbols on the grid
    """
    print("Enter your guess!")
    row = int(input("Enter row number: "))
    col = input("Enter column letter: ").upper()
    player_guess = (row, col)
    return player_guess



def main_loop():
    """
    Handles the main game loop
    """
    game_intro_message()
    player_grid = print_player_grid()
    player_ship_coordinates = get_ship_coordinates()
    validate_ship_coordinates(player_ship_coordinates, player_grid, col_labels, row_labels)
    generate_cpu_ships(col_labels, row_labels)
    get_player_guess()





main_loop()


