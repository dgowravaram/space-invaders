import pygame
import random

pygame.init() # initalize pygame module

# creating screen:
screen = pygame.display.set_mode((800, 600))

# title + icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('space-shuttle.png')
playerX = 370
playerY = 480
playerXChange = 0

# enemy
enemyImg = pygame.image.load('alien.png')
enemyX = random.randint(50, 350)
enemyY = random.randint(150, 370)
enemyXChange = 3
enemyYChange = 0

# 370, 480

def player(x, y):
    screen.blit(playerImg, (x, y))   #draw player on screen

def enemy(x, y):
    screen.blit(enemyImg, (x, y))   #draw player on screen

# keep pygame window open
running = True
while running:
    screen.fill((0, 0, 0)) # set background to black
    #playerX+=5

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerXChange = -3
            if event.key==pygame.K_RIGHT:
                playerXChange = 3
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerXChange = 0

    playerX+= playerXChange

    if playerX<25:
        playerX = 25
    elif playerX>=736:
        playerX = 736
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()

