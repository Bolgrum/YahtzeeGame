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

running = True
while running:
    timer.tick(FPS)
    screen.fill(background)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
pygame.quit()