import pygame, sys
import random
from pygame import *

fps = 15
mainClock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((750, 750))
pygame.display.set_caption("Bacterio")
appleX = 0
appleY = 0
snakehX = 240
snakehY = 240
up = False
down = False
left = False
right = False
ab = 0
dead = False

while True:
    if dead == True:
        sys.exit()
    if ab == 0:
        appleX = random.randrange(0, 750, 15)
        appleY = random.randrange(0, 750, 15)
        
        ab += 1
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        # Close the program if the user presses the 'X'
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  
        if keys[K_w]:
            up = True
            down = False
            left = False
            right = False
        if keys[K_s]:
            down = True
            up = False
            left = False
            right = False
        if keys[K_a]:
            left = True
            down = False
            up = False
            right = False
        if keys[K_d]:
            right = True
            down = False
            left = False
            up = False
    if up == True:
        snakehY -= 15
    if down == True:
        snakehY += 15
    if left == True:
        snakehX -= 15
    if right == True:
        snakehX += 15
    if snakehX <= -1:
        dead = True
    if snakehX >= 750:
        dead = True
    if snakehY <= -1:
        dead = True
    if snakehY >= 750:
        dead = True
    if appleX + appleY == snakehX + snakehY:
        print("Hello world!")

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 210, 0), ((snakehX, snakehY), (15, 15)))
    pygame.draw.rect(screen, (210, 0, 0), ((appleX, appleY), (15, 15)))
    mainClock.tick(fps)
    pygame.display.update()