# Import random to create CPU player moves
from random import randint

# Create Variables to generate game 
player_ship_num = 3
cpu_ship_num = 3
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
    for i, row in enumerate(player_grid):  # enumerate adds numbers to the rows
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
    for i in range(player_ship_num):
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
    for i in range(player_ship_num):
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


def validate_player_guess(player_guess, cpu_grid, shot_grid, col_labels, row_labels, player_ship_num):
    """
    Takes in player guess and validates them and prints the grid with hits and misses
    """
    row, col = player_guess
    row_index = row - 1
    col_index = ord(col) - 65
    if cpu_grid[row_index][col_index] == ship_symbol:
        print("Hit!")
        shot_grid[row_index][col_index] = hit_symbol
        player_ship_num -= 1
    else:
        print("Miss!")
        shot_grid[row_index][col_index] = miss_symbol
    print(" ", end=" ") 
    for col in col_labels:
        print(col, end=" ")
    print() 
    for i, row in enumerate(shot_grid):
        print(row_labels[i], end=" ")
        for cell in row:
            print(cell, end=" ")
        print()
    print(player_ship_num)
    return shot_grid
    

def get_cpu_guess():
    """
    Generates CPU guesses
    """
    row = randint(1, 5)
    col = randint(0, 4)
    cpu_guess = (row, col)
    return cpu_guess


def validate_cpu_guess(cpu_guess, player_grid, col_labels, row_labels, cpu_ship_num):
    """
    Takes in cpu guess and validates them and prints the grid with hits and misses
    """
    row, col = cpu_guess
    row_index = row - 1
    col_index = ord(col) - 65
    if player_grid[row_index][col_index] == ship_symbol:
        print("CPU Hit!")
        player_grid[row_index][col_index] = hit_symbol
        cpu_ship_num -= 1
    else:
        print("CPU Miss!")
        player_grid[row_index][col_index] = miss_symbol
    print(" ", end=" ") 
    for col in col_labels:
        print(col, end=" ")
    print() 
    for i, row in enumerate(player_grid):
        print(row_labels[i], end=" ")
        for cell in row:
            print(cell, end=" ")
        print()
    print(cpu_ship_num)
    return player_grid




def main_loop():
    """
    Handles the main game loop
    """
    game_intro_message()
    player_grid = print_player_grid()
    player_ship_coordinates = get_ship_coordinates()
    validate_ship_coordinates(player_ship_coordinates, player_grid, col_labels, row_labels)
    cpu_grid, shot_grid = generate_cpu_ships(col_labels, row_labels)
    player_guess = get_player_guess()
    validate_player_guess(player_guess, cpu_grid, shot_grid, col_labels, row_labels, player_ship_num)
    cpu_guess = get_cpu_guess()
    validate_cpu_guess(cpu_guess, player_grid, col_labels, row_labels, cpu_ship_num)
    while player_ship_num > 0 and cpu_ship_num > 0:
        player_guess = get_player_guess()
        validate_player_guess(player_guess, cpu_grid, shot_grid, col_labels, row_labels, player_ship_num)
        cpu_guess = get_cpu_guess()
        validate_cpu_guess(cpu_guess, player_grid, col_labels, row_labels, cpu_ship_num)
        print(f"player has {player_ship_num} ships left")
        print(f"CPU has {cpu_ship_num} ships left")
    if player_ship_num == 0:
        print("Game Over! CPU wins!")
    else:
        print("Game Over! Player wins!")


main_loop()


