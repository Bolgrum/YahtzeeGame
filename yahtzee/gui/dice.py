import pygame

# Global Classes
class Die:
    def __init__(self, x_pos, y_pos, num, key):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.number = num
        self.key = key
        self.die = ''

    def draw(self, window, color: dict):
        self.die = pygame.draw.rect(window, color.get("white"), [self.x_pos, self.y_pos, 100, 100], 0, 5)
        if self.number == 1:
            pygame.draw.circle(window, color.get("black"), (self.x_pos + 50, self.y_pos + 50), 10)
        if self.number == 2:
            pygame.draw.circle(window, color.get("black"), (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(window, color.get("black"), (self.x_pos + 80, self.y_pos + 80), 10)
        if self.number == 3:
            pygame.draw.circle(window, color.get("black"), (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(window, color.get("black"), (self.x_pos + 50, self.y_pos + 50), 10)
            pygame.draw.circle(window, color.get("black"), (self.x_pos + 80, self.y_pos + 80), 10)
        if self.number == 4:
            pygame.draw.circle(window, color.get("black"), (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(window, color.get("black"), (self.x_pos + 20, self.y_pos + 80), 10)
            pygame.draw.circle(window, color.get("black"), (self.x_pos + 80, self.y_pos + 20), 10)
            pygame.draw.circle(window, color.get("black"), (self.x_pos + 80, self.y_pos + 80), 10)
        if self.number == 5:
            pygame.draw.circle(window, color.get("black"), (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(window, color.get("black"), (self.x_pos + 20, self.y_pos + 80), 10)
            pygame.draw.circle(window, color.get("black"), (self.x_pos + 50, self.y_pos + 50), 10)
            pygame.draw.circle(window, color.get("black"), (self.x_pos + 80, self.y_pos + 20), 10)
            pygame.draw.circle(window, color.get("black"), (self.x_pos + 80, self.y_pos + 80), 10)
        if self.number == 6:
            pygame.draw.circle(window, color.get("black"), (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(window, color.get("black"), (self.x_pos + 20, self.y_pos + 80), 10)
            pygame.draw.circle(window, color.get("black"), (self.x_pos + 20, self.y_pos + 50), 10)
            pygame.draw.circle(window, color.get("black"), (self.x_pos + 80, self.y_pos + 50), 10)
            pygame.draw.circle(window, color.get("black"), (self.x_pos + 80, self.y_pos + 20), 10)
            pygame.draw.circle(window, color.get("black"), (self.x_pos + 80, self.y_pos + 80), 10)
            
# Global Functions
def draw_dice(window, window_color, number_list) -> None:
        # Each die
    die1 = Die(10, 50, number_list[0], 0)
    die2 = Die(130, 50, number_list[1], 1)
    die3 = Die(250, 50, number_list[2], 2)
    die4 = Die(370, 50, number_list[3], 3)
    die5 = Die(490, 50, number_list[4], 4)
    
    # draw a set of 5 dice
    die1.draw(window, window_color)
    die2.draw(window, window_color)
    die3.draw(window, window_color)
    die4.draw(window, window_color)
    die5.draw(window, window_color)