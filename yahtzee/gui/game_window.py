import pygame
from yahtzee import generator
from .dice import draw_dice
from .scorecard import draw_scoreboard

pygame.init()

DISPLAY_WIDTH: int  = 600
DISPLAY_HEIGHT: int = 800
window = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

window_clock = pygame.time.Clock()

class GameWindow():
    STARTING_NUM_OF_DICE: int = 5
    FPS = 60
    
    def __init__(self, caption, window_colors: dict, window_height: int, window_width: int):
        pygame.init()
        pygame.display.set_caption(caption)
        self.font = pygame.font.Font('freesansbold.ttf', 18)        
        self.colors = window_colors 
        
    def update(self):
        pygame.display.flip()
        
    def draw_accept_button(self, window, button_text="Accept Turn") -> pygame.Rect:
        accept_text = self.font.render(button_text, True, self.colors.get("white"))
        window.blit(accept_text, (390, 167))
        button = pygame.draw.rect(window, self.colors.get("black"), [310, 160, 280, 30])
        return button
        
    def draw_roll_button(self, window, button_text='Click to roll') -> pygame.Rect:
        roll_text = self.font.render(button_text, True, self.colors.get("white"))
        window.blit(roll_text, (100, 167))
        button = pygame.draw.rect(window, self.colors.get("black"), [10, 160, 280, 30])
        return button
    
    def draw_rolls_left(self, window, rolls_left: int) -> None:
        rolls_text = self.font.render('Rolls Left this Turn: ' + str(rolls_left), True, self.colors.get("white"))
        window.blit(rolls_text, (15, 15))
        
    def run(self):
        stopped = False
        
        while running:     
            window.fill(self.colors.get("background"))            
            # self.draw_rolls_left(window, rolls_left)
            # draw_dice(window, self.colors, random_dice_roll)
            # draw_scoreboard(window, self.colors, self.font)
            # roll_button = pygame.draw.rect(self.window, self.colors.get("black"), [10, 160, 280, 30])
            # accept_button = pygame.draw.rect(self.window, self.colors.get("black"), [310, 160, 280, 30])
            roll_button   = self.draw_roll_button(window)
            accept_button = self.draw_accept_button(window)
            
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
        
        pygame.quit()