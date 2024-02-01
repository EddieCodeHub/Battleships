# Import random to create CPU player moves
import random

# Create Variables to generate game 
grid_size = 5
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
    print("Each player had 3 ships each")
    print("First to sink all enemy ships wins!")
    print("To replay the game, select run program")