# Standard Library
import random

# 3rd Party/Local
from gui import button
from gui import scorecard
from gui import dice
import pygame

def generate_dice_roll(dice_to_roll: int) -> list:
    rolled_dice = list()
    
    for num in range(0, dice_to_roll):
        random_dice_roll = random.randint(1, 6)
        rolled_dice.append(random_dice_roll)
    
    return rolled_dice

class GameWindow():
    FPS: int = 60
    
    def __init__(self, title, colors: dict, width: int, height: int):
        self.win_dimensions = (width, height)
        self.window = pygame.display.set_mode(self.win_dimensions)
        pygame.display.set_caption(title)
        self.window_colors = colors
        self.font = pygame.font.Font('freesansbold.ttf', 18)
        self.Player1Scorcard = scorecard.Scorecard(self.window_colors, self.font)             
        self.RollButton = button.Button(self.window_colors.get("black"), 10, 160, 280, 30, "Roll Dice")
        self.AcceptButton = button.Button(self.window_colors.get("black"), 310, 160, 280, 30, "Accept Roll")
        
    def init_window(self):
        self.window.fill(self.window_colors.get('background'))
    
    def draw_window_components(self):        
        self.window.fill(self.window_colors.get('background'))
        pygame.draw.line(self.window, self.window_colors.get("black"), (0, 40), (self.win_dimensions[0], 40), 3)
        self.Player1Scorcard.draw_scorecard(self.window, self.win_dimensions[0], self.win_dimensions[1])
        self.RollButton.draw(self.window)
        self.AcceptButton.draw(self.window)
        
    def draw_rolls_left(self, rolls: int):
        rolls_text = self.font.render(f'Rolls Left this Turn: {rolls}', True, self.window_colors.get("black"))
        self.window.blit(rolls_text, (15, 15))
        
    def update(self):
        pygame.display.flip()
        
    def run(self):
        timer = pygame.time.Clock()
        self.init_window()
        random_dice_roll: list = [0, 0, 0, 0, 0]
        rolls_left: int = 3
        roll = False        
        run = True
        
        while run:
            DiceRoll = dice.Dice(self.window_colors, random_dice_roll)
            timer.tick(self.FPS)
            self.draw_window_components()
            self.draw_rolls_left(rolls_left)
            DiceRoll.draw_dice(self.window)
            
            for event in pygame.event.get():
                mouse_pos = pygame.mouse.get_pos()
                
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.RollButton.is_over(mouse_pos) and rolls_left > 0:
                        roll = True
                        rolls_left -= 1
                        print("Clicked the Roll Button")                        
                        
                    if self.AcceptButton.is_over(mouse_pos):
                        print("Clicked the Accept Button")
            
            if roll:
                random_dice_roll = generate_dice_roll(5)
                roll = False
            
            self.update()