import pygame
import os
import time
import random

WIDTH, HEIGHT = 750,750

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Invaders')


# Last inn bilder
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))

# Spiller ship
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

# Lasere
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLO_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

# Bakgrunn

BG = pygame.image.load(os.path.join("assets", "background-black.png"))

def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()

    def redraw_window():
        WIN.blit(BG, (0,0))

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
