# Standard Library
import random

# 3rd party or local
from console import input
from console import output
from gui import game_window
import pygame

# GLOBAL CONSTANTS
STARTING_NUM_OF_DICE: int = 5
WINDOW_DIMENSIONS: tuple = (600, 800)
WINDOW_WIDTH: int         = 600
WINDOW_HEIGHT: int        = 800
FPS = 60
STARTING_NUM_OF_DICE: int = 5

# GLOBAL VARIABLES
app: dict = {
    'name':'SE Yahtzee',
    'author':["Anthony", "Spencer", "Trevin"],
    'license':'MIT',
    'version':"0.0.0"
}

app_colors: dict = {
    "background": (128, 128, 128),
    "white": (255, 255, 255),
    "black": (0, 0, 0)
}

# Functions
def collect_dice():
    pass

def score_dice():
    pass

# Run the gui version of yahtzee
def run_gui():
    # Pygame module init
    pygame.init()
    YahtzeeGameWindow = game_window.GameWindow('Yahtzee', app_colors, WINDOW_DIMENSIONS[0], WINDOW_DIMENSIONS[1])
    YahtzeeGameWindow.run()

# Run the command line version of yahtzee
def run_console():
    output.print_project_header(app)
    
    print("Main Menu")
    print(
        "1 - Single Player\n" +
        "2 - Multiplayer\n" +
        "0 - EXIT"
        )
    user_option: int = int(input.user("Make a Selection: "))
    print()
    
    while user_option != 0:
        
        if user_option == 1:
            print("Do some single player stuff here")
            
        if user_option == 2:
            print("Do some multiplayer stuff here\n")       
        
        print("Menu")
        print(
            "1 - Single Player\n" +
            "2 - Multiplayer\n" +
            "0 - EXIT"
            )
        user_option: int = int(input.user("Make a Selection: "))
        print()