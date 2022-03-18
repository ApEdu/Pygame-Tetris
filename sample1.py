# import pygame modules
import pygame

# import pygame.locals for easier access to key coordinates
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

# calls init of all included pygame modules
# provides platform independence
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# returns surface representing visible parts of window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# GAME LOOP
# loop control variable
run = True
# loop body
while run:
    # look event in queue
    for event in pygame.event.get():
        # check if key pressed
        if event.type == KEYDOWN:
            # ESCAPE KEY -> exit
            if event.key == K_ESCAPE:
                run = False
        # check close window button pressed
        elif event.type == QUIT:
            run = False
    
    # Fill screen white
    screen.fill((255,255,255))
    


# Done! quit
pygame.quit()
