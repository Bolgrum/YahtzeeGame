from yahtzee.gui.game_window import GameWindow

STARTING_NUM_OF_DICE: int = 5
WINDOW_WIDTH: int         = 600
WINDOW_HEIGHT: int        = 800

app_colors: dict = {
    "background": (128, 10, 128),
    "white": (255, 255, 255),
    "black": (0, 0, 0)
}

font: dict = {
    "style": "freesansbold.ttf",
    "size": 18
}

# Test Script
test_window = GameWindow("Yahtzee!", app_colors, WINDOW_HEIGHT, WINDOW_WIDTH)
running = True

while running:
    test_window.update()