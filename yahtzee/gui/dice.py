import pygame

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