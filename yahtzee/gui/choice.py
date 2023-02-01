import pygame

class Choice:
    def __init__(self, x_pos, y_pos, text, select, possible, done):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.text = text
        self.select = select
        self.possible = possible
        self.done = done

    def draw(self, screen, screen_colors: dict, font):
        pygame.draw.line(screen, screen_colors.get("black"), (self.x_pos, self.y_pos), (self.x_pos + 225, self.y_pos), 2)
        pygame.draw.line(screen, screen_colors.get("black"), (self.x_pos, self.y_pos + 30), (self.x_pos + 225, self.y_pos + 30), 2)
        
        if not self.done:
            if self.possible:
                text = font.render(self.text, True, (34, 140, 34))
            elif not self.possible:
                text = font.render(self.text, True, (255, 0, 0))
        else:
            text = font.render(self.text, True, (0, 0, 0))

        screen.blit(text, (self.x_pos + 5, self.y_pos + 10))