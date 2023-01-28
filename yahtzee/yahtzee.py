from gui import sample_gui
import generator
import output


app = {
    'name':'SE Yahtzee',
    'author':["Anthony", "Spencer", "Trevin"],
    'license':'MIT',
    'version':"0.0.0"
}

# Functions
def roll_dice():
    pass

def collect_dice():
    pass

def score_dice():
    pass

def run_gui():
    print("Run Gui Application Here")
    sample_gui.print_hello_gui()

def run_console():
    output.print_project_header(app)
    dice = generator.generate_dice_roll()
    print(dice) 