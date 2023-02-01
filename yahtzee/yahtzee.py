# Standard Library
import random

# 3rd party or local
from console import input
from console import output
from gui.dice import Die
from gui.choice import Choice
import generator
import pygame

# GLOBAL CONSTANTS
STARTING_NUM_OF_DICE: int = 5
WINDOW_WIDTH: int         = 600
WINDOW_HEIGHT: int        = 800
FPS = 60

# GLOBAL VARIABLES
app = {
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

def draw_dice(window, window_colorw, number_list) -> None:
        # Each die
    die1 = Die(10, 50, number_list[0], 0)
    die2 = Die(130, 50, number_list[1], 1)
    die3 = Die(250, 50, number_list[2], 2)
    die4 = Die(370, 50, number_list[3], 3)
    die5 = Die(490, 50, number_list[4], 4)
    
    # draw a set of 5 dice
    die1.draw(window, window_colorw)
    die2.draw(window, window_colorw)
    die3.draw(window, window_colorw)
    die4.draw(window, window_colorw)
    die5.draw(window, window_colorw)

def draw_scoreboard(screen, screen_colors, font) -> None:
    # Init Scorboard
    ones = Choice(0, 200, '1s', True, False, False)
    twos = Choice(0, 230, '2s', True, False, False)
    threes = Choice(0, 260, '3s', True, False, False)
    fours = Choice(0, 290, '4s', True, False, False)
    fives = Choice(0, 320, '5s', True, False, False)
    sixes = Choice(0, 350, '6s', True, False, False)
    upper_total_1 = Choice(0, 380, 'Upper Score', False, False, True)
    upper_bonus = Choice(0, 410, 'Bonus if >= 63', False, False, True)
    upper_total_2 = Choice(0, 440, 'Total Upper Score', False, False, True)
    three_kind = Choice(0, 470, '3 of a Kind', True, False, False)
    four_kind = Choice(0, 500, '4 of a Kind', True, False, False)
    full_house = Choice(0, 530, 'Full House', True, False, False)
    small_straight = Choice(0, 560, 'Small Straight', True, False, False)
    large_straight = Choice(0, 590, 'Large Straight', True, False, False)
    yahtzee = Choice(0, 620, 'YAHTZEE!', True, False, False)
    chance = Choice(0, 650, 'Chance', True, False, False)
    bonus = Choice(0, 680, 'Chance', True, False, False)
    lower_total_1 = Choice(0, 710, 'Upper Score', False, False, True)
    lower_total_2 = Choice(0, 740, 'Upper Total', False, False, True)
    grand_total = Choice(0, 770, 'Grand Total', False, False, True)
    
    # draw scorecard
    ones.draw(screen, screen_colors, font)
    twos.draw(screen, screen_colors, font)
    threes.draw(screen, screen_colors, font)
    fours.draw(screen, screen_colors, font)
    fives.draw(screen, screen_colors, font)
    sixes.draw(screen, screen_colors, font)
    upper_total_1.draw(screen, screen_colors, font)
    upper_bonus.draw(screen, screen_colors, font)
    upper_total_2.draw(screen, screen_colors, font)
    three_kind.draw(screen, screen_colors, font)
    four_kind.draw(screen, screen_colors, font)
    full_house.draw(screen, screen_colors, font)
    small_straight.draw(screen, screen_colors, font)
    large_straight.draw(screen, screen_colors, font)
    yahtzee.draw(screen, screen_colors, font)
    chance.draw(screen, screen_colors, font)
    bonus.draw(screen, screen_colors, font)
    lower_total_1.draw(screen, screen_colors, font)
    lower_total_2.draw(screen, screen_colors, font)
    grand_total.draw(screen, screen_colors, font)

# Run the gui version of yahtzee
def run_gui():
    print("Gui Yahtzee")   
    
    def draw_stuff() -> None:
        roll_text = font.render('Click to Roll', True, app_colors.get("white"))
        main_screen.blit(roll_text, (100, 167))
        accept_text = font.render('Accept Turn', True, app_colors.get("white"))
        main_screen.blit(accept_text, (390, 167))
        rolls_text = font.render('Rolls Left this Turn: ' + str(rolls_left), True, app_colors.get("white"))
        main_screen.blit(rolls_text, (15, 15))
        pygame.draw.rect(main_screen, app_colors.get("white"), [0, 200, 225, WINDOW_HEIGHT - 200])
        pygame.draw.line(main_screen, app_colors.get("black"), (0, 40), (WINDOW_WIDTH, 40), 3)
        pygame.draw.line(main_screen, app_colors.get("black"), (0, 200), (WINDOW_WIDTH, 200), 3)
        pygame.draw.line(main_screen, app_colors.get("black"), (165, 200), (165, WINDOW_HEIGHT), 3)
        pygame.draw.line(main_screen, app_colors.get("black"), (225, 200), (225, WINDOW_HEIGHT), 3)            
     
    pygame.init()
    
    main_screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])

    pygame.display.set_caption('Yahtzee!')
    timer = pygame.time.Clock()    
    font = pygame.font.Font('freesansbold.ttf', 18)
    random_dice_roll = [0, 0, 0, 0, 0, 0]
    roll = False
    rolls_left = 3
    running = True
    
    while running:
        timer.tick(FPS)
        main_screen.fill(app_colors.get("background"))

        roll_button = pygame.draw.rect(main_screen, app_colors.get("black"), [10, 160, 280, 30])
        accept_button = pygame.draw.rect(main_screen, app_colors.get("black"), [310, 160, 280, 30])
        
        draw_stuff()
        draw_dice(main_screen, app_colors, random_dice_roll)
        draw_scoreboard(main_screen, app_colors, font)
                
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