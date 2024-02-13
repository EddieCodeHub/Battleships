# Import random to create CPU player moves
from random import randint
# import time to create a timer to reset the game
import time

# Create Variables to generate game
p_ship_num = 3
cpu_ship_num = 3
ship_symbol = "S"
hit_symbol = "X"
miss_symbol = "O"
row_labels = [1, 2, 3, 4, 5]
col_labels = ["A", "B", "C", "D", "E"]

# Create a set to store the guesses
cpu_guesses = set()


# All ASCII art taken from ascii.co.uk, credited in the README
def print_title():
    """
    Prints the title of the game
    """
    print("                __                             __         ")
    print(".--.--.--.-----|  .----.-----.--------.-----. |  |_.-----.")
    print("|  |  |  |  -__|  |  __|  _  |        |  -__| |   _|  _  |")
    print("|________|_____|__|____|_____|__|__|__|_____| |____|_____|")
    print(" __          __   __   __             __    __")
    print("|  |--.---.-|  |_|  |_|  .-----.-----|  |--|__.-----.-----.")
    print("|  _  |  _  |   _|   _|  |  -__|__ --|     |  |  _  |__ --|")
    print("|_____|___._|____|____|__|_____|_____|__|__|__|   __|_____|")
    print("                                              |__|      ")


def main_menu():
    """
    Prints the main menu
    """
    print("\n1. Game Rules")
    print("\n2. Play Game")
    option = int(input("\nEnter an option: "))
    if option == 1:
        game_rules()
        main_menu()
    # no elif statement as the game will start straight after rules are printed
    if option == 2:
        main_loop()
    else:
        print("Invalid option! Please try again")
        main_menu()


def game_rules():
    """
    Prints Welcome message and instructions to play the game
    """
    print(".-. . . .   .-. .-.")
    print("|(  | | |   |-  `-.")
    print("' ' `-' `-' `-' `-'")
    print("\nColumn co-ordinates go from left to right")
    print("\nRow co-ordinates go from top to bottom")
    print("\nThe Board is a 5x5 grid")
    print("\nStarting at the top left at Co-ordinate: row: 1, column: A")
    print("\nEach player has 3 ships each")
    print("\nFirst to sink all enemy ships wins!")


def print_player_grid():
    """
    Generates Players empty grid for placing ships
    """
    player_grid = [["-" for _ in range(5)] for _ in range(5)]
    print(".-. .   .-. . . .-. .-.")
    print("|-' |   |-|  |  |-  |( ")
    print("'   `-' ` '  `  `-' ' '")
    print(" ", end=" ")
    for col in col_labels:
        print(col, end=" ")
    print()
    # enumerate adds numbers to the rows
    # grid making function used from co-pilot suggestion credited in README
    for i, row in enumerate(player_grid):
        print(row_labels[i], end=" ")
        for cell in row:
            print(cell, end=" ")
        print()
    print("\nPlayer 1, place your ships!")
    return player_grid


def get_ship_coordinates():
    """
    Takes in player input to generate ship co-ordinates
    """
    # Create a list to store the ship co-ordinates
    player_ship_coordinates = []
    for i in range(3):
        # while statement to handle invalid inputs
        while True:
            print(f"\nEnter co-ordinates for ship {i + 1}")
            try:
                row = int(input("\nEnter row number: \n"))
            except ValueError:
                print("\nInvalid input!")
                print("\nPlease enter a number between 1 and 5 for the row.")
                continue
            col = input("\nEnter column letter: \n").upper()
            if row in range(1, 6) and col in ["A", "B", "C", "D", "E"]:
                player_ship_coordinates.append((row, col))
                break
            else:
                print("\nInvalid placement! Please try again")
                print("\nPlease enter a number between 1 and 5 for the row.")
                print("And any of these letters (A, B, C, D, E)")
    return player_ship_coordinates


def validate_ship_coordinates(
    player_ship_coordinates,
    player_grid,
    col_labels,
    row_labels
):
    """
    Takes in ship co-ordinates and validates them
    and prints the grid with ships placed
    """
    for row, col in player_ship_coordinates:
        row_index = row - 1
        col_index = ord(col) - 65
        # checks to see if there is already a ship in the cell
        if player_grid[row_index][col_index] == ship_symbol:
            print("You already have a ship there!")
            get_ship_coordinates()
            # places ships on the grid
        player_grid[row_index][col_index] = ship_symbol
    print("\nShips placed!\n")
    # label for grid
    print(".-. .   .-. . . .-. .-.")
    print("|-' |   |-|  |  |-  |( ")
    print("'   `-' ` '  `  `-' ' '")
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
    Generates CPU ships and places them on the grid
    but not visible to the player
    """
    cpu_grid = [["-" for _ in range(5)] for _ in range(5)]
    # Create a new grid to store the shots
    shot_grid = [["-" for _ in range(5)] for _ in range(5)]
    for i in range(3):
        # randomly places ships on the grid
        while True:
            row = randint(0, 4)
            col = randint(0, 4)
            # checks to see if there is already a ship in the cell
            if cpu_grid[row][col] != ship_symbol:
                cpu_grid[row][col] = ship_symbol
                break

    # Print the shot grid instead of the cpu grid
    print(".-. .-. . .")
    print("|   |-' | |")
    print("`-' '   `-'")
    print("  ", end="")
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
    Takes in player input to generate guesses
    and print appropriate symbols on the grid
    """
    # while statement to handle invalid inputs
    while True:
        print("\nEnter your guess!")
        try:
            row = int(input("\nEnter row number: \n"))
        except ValueError:
            print("\nInvalid input!")
            print("\nPlease enter a number between 1 and 5 for the row.")
            continue
        col = input("Enter column letter: \n").upper()
        if row not in range(1, 6) or col not in ["A", "B", "C", "D", "E"]:
            print("Invalid guess! Please try again")
            print("\nPlease enter a number between 1 and 5 for the row.")
            print("And either of these letters for the column (A, B, C, D, E)")
        else:
            player_guess = (row, col)
            return player_guess


def validate_player_guess(
    player_guess,
    cpu_grid,
    shot_grid,
    col_labels,
    row_labels
):
    """
    Takes in player guess and validates them
    and prints the grid with hits and misses
    """
    # global variables to keep track of ships
    global cpu_ship_num
    row, col = player_guess
    row_index = row - 1
    col_index = ord(col) - 65
    if shot_grid[row_index][col_index] == miss_symbol:
        print("\nYou already guessed that!")
        get_player_guess()
    if shot_grid[row_index][col_index] == hit_symbol:
        print("\nYou already guessed that!")
        get_player_guess()
    if cpu_grid[row_index][col_index] == ship_symbol:
        print("\nHit!")
        shot_grid[row_index][col_index] = hit_symbol
        cpu_ship_num -= 1
    else:
        print("\nMiss!")
        shot_grid[row_index][col_index] = miss_symbol
    print(".-. .-. . .")
    print("|   |-' | |")
    print("`-' '   `-'")
    print(" ", end=" ")
    # prints the grid with hits and misses
    for col in col_labels:
        print(col, end=" ")
    print()
    for i, row in enumerate(shot_grid):
        print(row_labels[i], end=" ")
        for cell in row:
            print(cell, end=" ")
        print()
    return shot_grid


def get_cpu_guess():
    """
    Generates CPU guesses
    """
    # generates random guesses and adds them to a set
    while True:
        row = randint(1, 5)
        col = randint(1, 5)
        cpu_guess = (row, col)
        # If the guess is not in the set of previous guesses,
        # add it to the set and return it
        if cpu_guess not in cpu_guesses:
            cpu_guesses.add(cpu_guess)
            return cpu_guess


def validate_cpu_guess(
    cpu_guess,
    player_grid,
    col_labels,
    row_labels
):
    """
    Takes in cpu guess and validates them
    and prints the grid with hits and misses
    """
    # global variables to keep track of ships
    global p_ship_num
    row, col = cpu_guess
    row_index = row - 1
    col_index = col - 1
    # checks to see if the guess has already been made
    if player_grid[row_index][col_index] == miss_symbol:
        get_cpu_guess()
    if player_grid[row_index][col_index] == hit_symbol:
        get_cpu_guess()
    if player_grid[row_index][col_index] == ship_symbol:
        print("\nCPU Hit!")
        player_grid[row_index][col_index] = hit_symbol
        p_ship_num -= 1
    else:
        print("\nCPU Miss!")
        player_grid[row_index][col_index] = miss_symbol
    print(".-. .   .-. . . .-. .-.")
    print("|-' |   |-|  |  |-  |( ")
    print("'   `-' ` '  `  `-' ' '")
    print("  ", end="")
    # prints the grid with hits and misses
    for col in col_labels:
        print(col, end=" ")
    print()
    for i, row in enumerate(player_grid):
        print(row_labels[i], end=" ")
        for cell in row:
            print(cell, end=" ")
        print()
    return player_grid


def reset_game():
    """
    five second timer to reset the game
    """
    # resets global variables
    global p_ship_num
    global cpu_ship_num
    p_ship_num = 3
    cpu_ship_num = 3
    print("\nResetting game in 5 seconds...")
    # 5 second timer
    time.sleep(5)
    print_title()
    main_menu()


def ship_message(owner, num):
    """
    Takes in the owner of the ships and the number of ships left
    and returns correct message
    """
    return f"{owner} has {num} {'ship' if num == 1 else 'ships'} left"


def main_loop():
    """
    Handles the main game loop
    """
    player_grid = print_player_grid()
    player_ship_coordinates = get_ship_coordinates()
    validate_ship_coordinates(
        player_ship_coordinates,
        player_grid,
        col_labels,
        row_labels
    )
    cpu_grid, shot_grid = generate_cpu_ships(col_labels, row_labels)
    player_guess = get_player_guess()
    validate_player_guess(
        player_guess,
        cpu_grid,
        shot_grid,
        col_labels,
        row_labels
    )
    cpu_guess = get_cpu_guess()
    validate_cpu_guess(cpu_guess, player_grid, col_labels, row_labels)
    while p_ship_num > 0 and cpu_ship_num > 0:
        player_guess = get_player_guess()
        validate_player_guess(
            player_guess,
            cpu_grid,
            shot_grid,
            col_labels,
            row_labels
        )
        cpu_guess = get_cpu_guess()
        validate_cpu_guess(cpu_guess, player_grid, col_labels, row_labels)
        print(ship_message("Player", p_ship_num))
        print(ship_message("CPU", cpu_ship_num))
    if p_ship_num == 0:

        # Game over screens
        print(".-. .-. .  . .-.   .-. . . .-. .-.")
        print(
            "|.. |-| |{}{}| |-    | | | | |-  |("
            .format("\\", "/")
        )
        print("`-' ` ' '  ` `-'   `-' `.' `-' ' '")

        print(".-. .-. . .   . . .  -  . . .-.")  # cpu wins
        print(
            "|   |-' | |   | | |  |  |{}| `-."
            .format("\\")
        )
        print("`-' '   `-'   `.'.'  -  ' ` `-'")
    else:
        print(".-. .-. .  . .-.   .-. . . .-. .-.")
        print(
            "|.. |-| |{}{}| |-    | | | | |-  |("
            .format("\\", "/")
        )
        print("`-' ` ' '  ` `-'   `-' `.' `-' ' '")

        print(".-. .   .-. . . .-. .-.   . . .  -  . . .-.")  # player wins
        print(
            "|-' |   |-|  |  |-  |(    | | |  |  |{}| `-."
            .format("\\")
        )

        print("'   `-' ` '  `  `-' ' '   `.'.'  -  ' ` `-'")
    reset_game()


print_title()
main_menu()
main_loop()
