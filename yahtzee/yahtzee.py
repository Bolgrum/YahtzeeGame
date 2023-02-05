# Standard Library
import random

# 3rd party or local
from console import input
from console import output
from gui.dice import draw_dice
from gui.scorecard import draw_scoreboard
import generator
import pygame

# GLOBAL CONSTANTS
STARTING_NUM_OF_DICE: int = 5
WINDOW_WIDTH: int         = 600
WINDOW_HEIGHT: int        = 800
FPS = 60

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
def roll_dice(dice_to_roll: int):
    rolled_dice: list = generator.generate_dice_roll(dice_to_roll)
    print(rolled_dice)

def collect_dice():
    pass

def score_dice():
    pass

def draw_lines_and_buttons(window, window_height: int, window_width: int, font, rolls_left) -> None:
    roll_text = font.render('Click to Roll', True, app_colors.get("white"))
    window.blit(roll_text, (100, 167))
    # accept_text = font.render('Accept Turn', True, app_colors.get("white"))
    # window.blit(accept_text, (390, 167))
    # rolls_text = font.render('Rolls Left this Turn: ' + str(rolls_left), True, app_colors.get("white"))
    # window.blit(rolls_text, (15, 15))
    # pygame.draw.rect(window, app_colors.get("white"), [0, 200, 225, window_height - 200])
    # pygame.draw.line(window, app_colors.get("black"), (0, 40), (window_width, 40), 3)
    # pygame.draw.line(window, app_colors.get("black"), (0, 200), (window_width, 200), 3)
    # pygame.draw.line(window, app_colors.get("black"), (165, 200), (165, window_height), 3)
    # pygame.draw.line(window, app_colors.get("black"), (225, 200), (225, window_height), 3)   

# Run the gui version of yahtzee
def run_gui():
    pygame.init()  
    main_window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
    pygame.display.set_caption('Yahtzee!')
    timer = pygame.time.Clock()    
    font = pygame.font.Font('freesansbold.ttf', 18)
    random_dice_roll = [0, 0, 0, 0, 0, 0]
    roll = False
    rolls_left = 3
    running = True
    
    print("Gui Yahtzee")
    
    while running:
        timer.tick(FPS)
        main_window.fill(app_colors.get("background"))

        roll_button = pygame.draw.rect(main_window, app_colors.get("black"), [10, 160, 280, 30])
        accept_button = pygame.draw.rect(main_window, app_colors.get("black"), [310, 160, 280, 30])
        
        draw_lines_and_buttons(main_window, WINDOW_HEIGHT, WINDOW_WIDTH, font, rolls_left)
        draw_dice(main_window, app_colors, random_dice_roll)
        draw_scoreboard(main_window, app_colors, font)
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if roll_button.collidepoint(event.pos) and rolls_left > 0:
                    roll = True
                    rolls_left -= 1

        if roll:
            random_dice_roll = generator.generate_dice_roll(5)
            roll = False

        pygame.display.flip()

pygame.quit()

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
            
            print("You rolled:")
            roll_dice(STARTING_NUM_OF_DICE)
            print()
            
            print("Your second roll:")
            roll_dice(2)
            print()
            
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