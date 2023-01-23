import pygame
from pygame.locals import *
pygame.init()

# Window dimention
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

## P2.1 - Road parameters
ROAD_W = 500

## P2.3 - Roadmark width
ROADMARK_W = 10


# Set window size
screen = pygame.display.set_mode( SIZE )

# Set window title
pygame.display.set_caption("Car game in Pygame")

# Set icon
ICON = pygame.image.load("car-icon.png")
pygame.display.set_icon(ICON)

# Set background color
screen.fill((60, 220, 0))

## P2.2 - Draw the road
pygame.draw.rect(screen, (50, 50, 50), (SCREEN_WIDTH/2  - ROAD_W/2, 0, ROAD_W, SCREEN_HEIGHT))

## p2.4 - Draw the roadmark
pygame.draw.rect(screen, (255, 240, 60), (SCREEN_WIDTH/2 - ROADMARK_W/2, 0, ROADMARK_W, SCREEN_HEIGHT))

## p2.5 - Draw the white lines
pygame.draw.rect(screen, (255, 255, 255), (SCREEN_WIDTH/2 - ROAD_W/2 + ROADMARK_W * 2, 0, ROADMARK_W, SCREEN_HEIGHT))

pygame.draw.rect(screen, (255, 255, 255), (SCREEN_WIDTH/2 + ROAD_W/2 - ROADMARK_W * 3, 0, ROADMARK_W, SCREEN_HEIGHT))

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
            
