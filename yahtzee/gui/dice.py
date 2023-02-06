import pygame
from gui import button

# Global Classes
class Dice:
    def __init__(self, color: dict, number_list):
        self.die1 = Die(color, 10, 50, number_list[0], 0)
        self.die2 = Die(color, 130, 50, number_list[1], 1)
        self.die3 = Die(color, 250, 50, number_list[2], 2)
        self.die4 = Die(color, 370, 50, number_list[3], 3)
        self.die5 = Die(color, 490, 50, number_list[4], 4)
        
    def draw_dice(self, window):
        self.die1.draw(window)
        self.die2.draw(window)
        self.die3.draw(window)
        self.die4.draw(window)
        self.die5.draw(window)
        
class Die:
    def __init__(self, color: dict, x_pos, y_pos, num, key):
        self.button_colors = color
        self.DieButton = button.Button(self.button_colors.get('white'), x_pos, y_pos, 100, 100)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.number = num
        self.key = key
        self.die = ''

    def draw(self, window):
        self.DieButton.draw(window)
        if self.number == 1:
            pygame.draw.circle(window, self.button_colors.get("black"), (self.x_pos + 50, self.y_pos + 50), 10)
        if self.number == 2:
            pygame.draw.circle(window, self.button_colors.get("black"), (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(window, self.button_colors.get("black"), (self.x_pos + 80, self.y_pos + 80), 10)
        if self.number == 3:
            pygame.draw.circle(window, self.button_colors.get("black"), (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(window, self.button_colors.get("black"), (self.x_pos + 50, self.y_pos + 50), 10)
            pygame.draw.circle(window, self.button_colors.get("black"), (self.x_pos + 80, self.y_pos + 80), 10)
        if self.number == 4:
            pygame.draw.circle(window, self.button_colors.get("black"), (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(window, self.button_colors.get("black"), (self.x_pos + 20, self.y_pos + 80), 10)
            pygame.draw.circle(window, self.button_colors.get("black"), (self.x_pos + 80, self.y_pos + 20), 10)
            pygame.draw.circle(window, self.button_colors.get("black"), (self.x_pos + 80, self.y_pos + 80), 10)
        if self.number == 5:
            pygame.draw.circle(window, self.button_colors.get("black"), (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(window, self.button_colors.get("black"), (self.x_pos + 20, self.y_pos + 80), 10)
            pygame.draw.circle(window, self.button_colors.get("black"), (self.x_pos + 50, self.y_pos + 50), 10)
            pygame.draw.circle(window, self.button_colors.get("black"), (self.x_pos + 80, self.y_pos + 20), 10)
            pygame.draw.circle(window, self.button_colors.get("black"), (self.x_pos + 80, self.y_pos + 80), 10)
        if self.number == 6:
            pygame.draw.circle(window, self.button_colors.get("black"), (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(window, self.button_colors.get("black"), (self.x_pos + 20, self.y_pos + 80), 10)
            pygame.draw.circle(window, self.button_colors.get("black"), (self.x_pos + 20, self.y_pos + 50), 10)
            pygame.draw.circle(window, self.button_colors.get("black"), (self.x_pos + 80, self.y_pos + 50), 10)
            pygame.draw.circle(window, self.button_colors.get("black"), (self.x_pos + 80, self.y_pos + 20), 10)
            pygame.draw.circle(window, self.button_colors.get("black"), (self.x_pos + 80, self.y_pos + 80), 10)