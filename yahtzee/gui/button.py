import pygame

button_font: dict = {
    'style': 'comicsans',
    'size': 18,
    'color': (255, 255, 255)
}

class Button:
    def __init__(self, color, x, y, width, height, text=''):
        self.color  = color
        self.x      = x
        self.y      = y
        self.width  = width
        self.height = height
        self.text   = text        
    
    def draw(self, window, outline=None):
        if outline:
            pygame.draw.rect(window, outline, (self.x-2, self.y-2, self.width+4, self.height+4))
            
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))
        
        if self.text != '':
            font = pygame.font.SysFont(button_font.get('style'), button_font.get('size'))
            text = font.render(self.text, 1, button_font.get('color'))
            window.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))
    
    def is_over(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False