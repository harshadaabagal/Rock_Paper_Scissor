# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 10:10:06 2022

@author: user
"""
import pygame
import random
import time

pygame.init()  # Before using pygame , you have to initialize it

# colors to use
gray = (119, 118, 110)
white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 255)
bright_red = (255, 0, 0)
light_green = (0, 100, 0)

# creating display for game
gd = pygame.display.set_mode((800, 600))
# Clock - to reduce the speed of buttons going in differnet directions
clock = pygame.time.Clock()
# To load images
car_img = pygame.image.load("car-clipart-sprite-sheet-14.jpg")
car_img = pygame.transform.scale(car_img, (100, 100))
background = pygame.image.load("background1.jpg")
grass = pygame.image.load("download12.jpg")


def Message(size, mess, x_pos, y_pos):
    # To set the text choose a font
    font = pygame.font.SysFont(None, size)
    # to view the text
    render = font.render(mess, True, white)
    gd.blit(render, (x_pos, y_pos))  # to show the text on the surface of display


Message(100, "START", 150, 100)
clock.tick(1)


def car(x, y):
    gd.blit(car_img, (x, y))
    gd.blit(grass, (0, 0))  # grass on left
    gd.blit(grass, (700, 0))  # grass on right
    if 0 < x < 90 or 700 < x + 100:
        Message(100, "GAME-OVER", 200, 200)
        pygame.display.update()
        clock.tick(0.17)
        game_intro()


def enemy_car(x_r, y_r):
    gd.blit(car_img, (x_r, y_r))


def car_crash(x, x_r, y, y_r):
    if x_r < x < x_r + 90 and y_r < y < y_r + 90 or x_r < x + 90 < x_r + 90 and y_r < y < y_r + 90:
        Message(50, "CRASHED!", 200, 200)
        pygame.display.update()
        time.sleep(1)
        game_intro()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


def score(count):
    font = pygame.font.SysFont(None, 30)
    screen_text = font.render('score :' + str(count), True, white)
    gd.blit(screen_text, (0, 0))


def game_loop():
    # Setting x and y coordinates of rectangle
    x = 300
    x_r = random.randrange(100, 600)  # random range for enemy car
    y = 490
    y_r = 0
    # Taking these variables to continuously press the right , left , up , down keys
    x_change = 0
    count = 0
    game_over = False

    while game_over == False:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # To check if clicked on close button of display
                game_over = True
                pygame.quit()
            if event.type == pygame.KEYDOWN:  # To check if any key is pressed
                if event.key == pygame.K_LEFT:
                    # x -= 10 #Whenever left key is pressed , x will be decreased by 10
                    x_change += 10
                elif event.key == pygame.K_RIGHT:
                    # x += 10 #Whenever right key is pressed , x in incremented by 10
                    x_change -= 10
            if event.type == pygame.KEYUP:  # To check if key is released
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        gd.fill(gray)  # Setting background color until the window is not closed
        # pygame.draw.rect(gd, red, [220,300,50,50])  #x,y,height,width
        # pygame.draw.rect(gd, red, [x,y,50,50])
        car(x, y)
        score(count)
        enemy_car(x_r, y_r)
        y_r += 10
        if y_r == 600:
            y_r = 0
            x_r = random.randrange(100, 600)
            count += 1
        car_crash(x, x_r, y, y_r)
        x = x - x_change
        clock.tick(40)
        pygame.display.update()

        x = x - x_change
        clock.tick(50)  # to slow down the movement
        pygame.display.update()  # Everytime you do some changes , you need to update the display.


def button(x_button, y_button, mess):
    pygame.draw.rect(gd, green, [x_button, y_button, 100, 30])
    Message(50, mess, x_button, y_button)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x_button < mouse[0] < x_button + 100 and y_button < mouse[1] < y_button + 30:
        pygame.draw.rect(gd, light_green, [x_button, y_button, 100, 30])
        Message(50, mess, x_button, y_button)
        if click == (1, 0, 0) and mess == "PLAY":
            game_loop()
        elif click == (1, 0, 0) and mess == "QUIT":
            pygame.quit()
            quit()


def game_intro():
    intro = False
    while intro == False:
        gd.blit(background, (0, 0))
        button(100, 300, "PLAY")
        button(600, 300, "QUIT")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # To check if clicked on close button of display
                intro = True
                pygame.quit()
        pygame.display.update()


game_intro()
pygame.display.update()

pygame.quit()  # After returning whole game , you should quit the game
quit()
