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
rolls_left = 3

running = True

def draw_stuff():
    roll_text = font.render('Click to Roll', True, white)
    screen.blit(roll_text, (100, 167))
    accept_text = font.render('Accept Turn', True, white)
    screen.blit(accept_text, (390, 167))
    rolls_text = font.render('Rolls Left this Turn: ' + str(rolls_left), True, white)
    screen.blit(rolls_text, (15, 15))
    pygame.draw.rect(screen, white, [0, 200, 225, HEIGHT - 200])
    pygame.draw.line(screen, black, (0, 40), (WIDTH, 40), 3)
    pygame.draw.line(screen, black, (0, 200), (WIDTH, 200), 3)
    pygame.draw.line(screen, black, (165, 200), (165, HEIGHT), 3)
    pygame.draw.line(screen, black, (225, 200), (225, HEIGHT), 3)

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

class Choice:
    def __init__(self, x_pos, y_pos, text, select, possible, done):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.text = text
        self.select = select
        self.possible = possible
        self.done = done

    def draw(self):
        pygame.draw.line(screen, black, (self.x_pos, self.y_pos), (self.x_pos + 225, self.y_pos), 2)
        pygame.draw.line(screen, black, (self.x_pos, self.y_pos + 30), (self.x_pos + 225, self.y_pos + 30), 2)
        
        if not self.done:
            if self.possible:
                text = font.render(self.text, True, (34, 140, 34))
            elif not self.possible:
                text = font.render(self.text, True, (255, 0, 0))
        else:
            text = font.render(self.text, True, (0, 0, 0))

        screen.blit(text, (self.x_pos + 5, self.y_pos + 10))

while running:
    timer.tick(FPS)
    screen.fill(background)

    roll_button = pygame.draw.rect(screen, black, [10, 160, 280, 30])
    accept_button = pygame.draw.rect(screen, black, [310, 160, 280, 30])
    draw_stuff()

    die1 = Dice(10, 50, numbers[0], 0)
    die2 = Dice(130, 50, numbers[1], 1)
    die3 = Dice(250, 50, numbers[2], 2)
    die4 = Dice(370, 50, numbers[3], 3)
    die5 = Dice(490, 50, numbers[4], 4)
    ones = Choice(0, 200, '1s', True, False, False)
    twos = Choice(0, 230, '2s', True, False, False)
    threes = Choice(0, 260, '3s', True, False, False)
    fours = Choice(0, 290, '4s', True, False, False)
    fives = Choice(0, 320, '5s', True, False, False)
    sixes = Choice(0, 350, '6s', True, False, False)
    upper_total_1 = Choice(0, 380, 'Upper Score', False, False, True)
    upper_bonus = Choice(0, 410, 'Bonus if >= 63', False, False, True)
    upper_total_2 = Choice(0, 440, 'Total Upper Score', False, False, True)
    three_kind = Choice(0, 470, '3 of a Kind', True, False, False)
    four_kind = Choice(0, 500, '4 of a Kind', True, False, False)
    full_house = Choice(0, 530, 'Full House', True, False, False)
    small_straight = Choice(0, 560, 'Small Straight', True, False, False)
    large_straight = Choice(0, 590, 'Large Straight', True, False, False)
    yahtzee = Choice(0, 620, 'YAHTZEE!', True, False, False)
    chance = Choice(0, 650, 'Chance', True, False, False)
    bonus = Choice(0, 680, 'Chance', True, False, False)
    lower_total_1 = Choice(0, 710, 'Upper Score', False, False, True)
    lower_total_2 = Choice(0, 740, 'Upper Total', False, False, True)
    grand_total = Choice(0, 770, 'Grand Total', False, False, True)
    

    die1.draw()
    die2.draw()
    die3.draw()
    die4.draw()
    die5.draw()
    ones.draw()
    twos.draw()
    threes.draw()
    fours.draw()
    fives.draw()
    sixes.draw()
    upper_total_1.draw()
    upper_bonus.draw()
    upper_total_2.draw()
    three_kind.draw()
    four_kind.draw()
    full_house.draw()
    small_straight.draw()
    large_straight.draw()
    yahtzee.draw()
    chance.draw()
    bonus.draw()
    lower_total_1.draw()
    lower_total_2.draw()
    grand_total.draw()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type ==pygame.MOUSEBUTTONDOWN:
            if roll_button.collidepoint(event.pos) and rolls_left > 0:
                roll = True

    if roll:
        for number in range(len(numbers)):
            numbers[number] = random.randint(1, 6)
        roll = False

    pygame.display.flip()



pygame.quit()
