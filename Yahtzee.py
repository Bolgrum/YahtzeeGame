import random
import pygame

pygame.init()

WIDTH = 600
HEIGHT = 800

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Yahtzee!')
timer = pygame.time.Clock()
FPS = 60
font = pygame.font.Font('freesansbold.ttf', 18)
background = (128, 128, 128)
white = (255, 255, 255)
black = (0, 0, 0)
numbers = [0, 0, 0, 0, 0]
roll = False

running = True

class Dice:
    def __init__(self, x_pos, y_pos, num, key):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.number = num
        self.key = key
        self.die = ''

    def draw(self):
        self.die = pygame.draw.rect(screen, white, [self.x_pos, self.y_pos, 100, 100], 0, 5)
        if self.number == 1:
            pygame.draw.circle(screen, black, (self.x_pos + 50, self.y_pos + 50), 10)
        if self.number == 2:
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 80), 10)
        if self.number == 3:
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 50, self.y_pos + 50), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 80), 10)
        if self.number == 4:
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 80), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 20), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 80), 10)
        if self.number == 5:
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 80), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 50, self.y_pos + 50), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 20), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 80), 10)
        if self.number == 6:
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 80), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 50), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 50), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 20), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 80), 10)

while running:
    timer.tick(FPS)
    screen.fill(background)

    roll_button = pygame.draw.rect(screen, black, [10, 160, 280, 30])
    roll_text = font.render('Click to Roll', True, white)
    screen.blit(roll_text, (100, 167))

    die1 = Dice(10, 50, numbers[0], 0)
    die2 = Dice(130, 50, numbers[1], 1)
    die3 = Dice(250, 50, numbers[2], 2)
    die4 = Dice(370, 50, numbers[3], 3)
    die5 = Dice(490, 50, numbers[4], 4)

    die1.draw()
    die2.draw()
    die3.draw()
    die4.draw()
    die5.draw()
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type ==pygame.MOUSEBUTTONDOWN:
            if roll_button.collidepoint(event.pos):
                roll = True

    if roll:
        for number in range(len(numbers)):
            numbers[number] = random.randint(1, 6)
        roll = False

    pygame.display.flip()



pygame.quit()
