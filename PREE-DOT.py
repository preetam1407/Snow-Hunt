# importing libraries
import pygame
import random
import time
from pygame import mixer

# Start with the pygame
pygame.init()

#RGB colour
yellow= (255,255,0)
white = (255,255,255)

# screen ratio
Display_height = 800
Display_width = 600

#creating game window
screen = pygame.display.set_mode((Display_height , Display_width))


# Game Name and Game logo and game background image
Game_Name = pygame.display.set_caption("PREE-DOT")
Game_logo = pygame.image.load('sev7.png')
pygame.display.set_icon(Game_logo)
background = pygame.image.load("pixel background.jpg")
background1 = pygame.image.load("hat chri.png")

#Background music
mixer.music.load("background_music.mp3")
mixer.music.play(-1)


#player ans snow_balls details:
player_x = 400
player_y = 500
player_size = 15
player_movement = 0
FPS = 120
speed = 1
snow_size = 10
snow_balls = 30
snow_colour = white

# creating random snow_balls in a list
snow_flake = []
for i in range(snow_balls):
    x = random.randrange(0,Display_width) #(assign x for simplicity)
    y = random.randrange(0,Display_height) #(assign y for simplicity)
    z = snow_flake.append([x,y])

#clock
clock = pygame.time.Clock()


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # add arrow keys function for pressing and releasing keys
    # for movement left and right keys are given speed
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player_movement -= 1
        if event.key == pygame.K_RIGHT:
            player_movement += 1
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            player_movement = 0
        if event.key == pygame.K_RIGHT:
            player_movement = 0

        # player boundries and movement:
    player_x += player_movement
    pygame.display.update()

    if (player_x <= 0):
        player_x = 0
    elif (player_x >= 790):
        player_x = 785
    pygame.display.update()


        # falling snow and give speed to snow in downward direction
    for i in snow_flake:
        i[1] += speed

        # make snow_balls using pygame built in function of draw
        pygame.draw.circle(screen, snow_colour,i, snow_size)

        # set range where to snow have to appear
        if i[1] > Display_height:
            i[1] = random.randrange(-50,0)
            i[0] = random.randrange(0,900)

    pygame.display.update()
    pygame.display.flip()
    clock.tick(FPS)

    # set background image and player
    screen.blit(background, (0, 0))
    screen.blit(background1,(0,0))
    pygame.draw.rect(screen, yellow, (player_x, player_y, player_size, player_size))
    pygame.display.update()

    # use display update function to implment every command
















