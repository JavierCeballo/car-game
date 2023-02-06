import pygame
from pygame.locals import *
pygame.init()

# Window dimention
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# Road parameters
ROAD_W = 500
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


# Apply changes
pygame.display.update()

# Load car player image
car_player = pygame.image.load("car_player.png")
car_player_loc = car_player.get_rect()
car_player_loc.center = SCREEN_WIDTH/2 + ROAD_W/4, SCREEN_HEIGHT*0.9

# Load car enemy image
car_enemy = pygame.image.load("car_enemy.png")
car_enemy_loc = car_player.get_rect()
car_enemy_loc.center = SCREEN_WIDTH/2 - ROAD_W/4, SCREEN_HEIGHT*0.2

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
                
        #### P4.1 - Player movement with the arrow keys
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                car_player_loc = car_player_loc.move([-(ROAD_W/2), 0])
            if event.key in [K_d, K_RIGHT]:
                car_player_loc = car_player_loc.move([(ROAD_W/2), 0])
    
    
    #### P4.2 - Paste the draw road code lines into the while cicle
    
    # Draw the road
    pygame.draw.rect(screen, (50, 50, 50), (SCREEN_WIDTH/2  - ROAD_W/2, 0, ROAD_W, SCREEN_HEIGHT))

    # Draw the roadmark
    pygame.draw.rect(screen, (255, 240, 60), (SCREEN_WIDTH/2 - ROADMARK_W/2, 0, ROADMARK_W, SCREEN_HEIGHT))

    # Draw the white lines
    pygame.draw.rect(screen, (255, 255, 255), (SCREEN_WIDTH/2 - ROAD_W/2 + ROADMARK_W * 2, 0, ROADMARK_W, SCREEN_HEIGHT))

    pygame.draw.rect(screen, (255, 255, 255), (SCREEN_WIDTH/2 + ROAD_W/2 - ROADMARK_W * 3, 0, ROADMARK_W, SCREEN_HEIGHT))
               
    # Draw player car
    screen.blit(car_player, car_player_loc)
    
    # Draw enemy car
    screen.blit(car_enemy, car_enemy_loc)
    
    # Update the app
    pygame.display.update()
            
