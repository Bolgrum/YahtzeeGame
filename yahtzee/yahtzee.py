from console import input
from console import output
from gui import sample_gui
import generator

STARTING_NUM_OF_DICE: int = 5

app = {
    'name':'SE Yahtzee',
    'author':["Anthony", "Spencer", "Trevin"],
    'license':'MIT',
    'version':"0.0.0"
}

# Functions
def roll_dice(dice_to_roll: int):
    rolled_dice: list = generator.generate_dice_roll(dice_to_roll)
    print(rolled_dice)

def collect_dice():
    pass

def score_dice():
    pass

def run_gui():
    print("Run Gui Application Here")
    sample_gui.print_hello_gui()

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

     