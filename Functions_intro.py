# Functions_intro.py
# Author: Matt Wong 
# Date: April 1 2019

import pygame

pygame.init()

# COLOURS - (R, G, B)
# CONSTANTS ALL HAVE CAPS FOR THEIR NAMES
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
GREY  = (128, 128, 128)
BROWN = (139, 69, 19)

# CONSTANTS
WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)

# FUNCTIONS
def draw_tree(screen, x, y):
    pygame.draw.rect(screen, BROWN, [60 + x, 170 + y, 30, 45])
    pygame.draw.polygon(
        screen,
        GREEN,
        [[150 + x,170 + y], [75 + x,20 + y], [x,170 + y]]
    )
    pygame.draw.polygon(
        screen,
        GREEN,
        [[140 +x,120 + y], [75 +x, y], [0 + x ,120 + y]]
    )
def print_introduction():
    print("This program demostrates how to use functions")
    print("This program will print out multiple trees.")

# Creating the Screen
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Draw Tree")

# Variables
done = False
clock = pygame.time.Clock()

# ------------ MAIN GAME LOOP
while not done:
    # ------ MAIN EVENT LISTENER
    # when the user does something
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # ------ GAME LOGIC

    # ------ DRAWING TO SCREEN
    screen.fill(WHITE)

    draw_tree(screen, 0,0)
    draw_tree(screen, 0, 230)
    draw_tree(screen, 200,230)
    draw_tree(screen, WIDTH / 2,HEIGHT / 2)
    print_introduction()

    # Update screen
    pygame.display.flip()

    # ------ CLOCK TICK
    clock.tick(60) # 60 fps

pygame.quit()