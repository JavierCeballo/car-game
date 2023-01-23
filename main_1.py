import pygame
from pygame.locals import *
pygame.init()

# Window dimention
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# Set window size
screen = pygame.display.set_mode( SIZE )

# Set window title
pygame.display.set_caption("Car game in Pygame")

# Set icon
ICON = pygame.image.load("car-icon.png")
pygame.display.set_icon(ICON)

# Set background color
screen.fill((60, 220, 0))

# Apply changes
pygame.display.update()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        #print( event )
        if event.type == QUIT:
            running = False
            
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            
