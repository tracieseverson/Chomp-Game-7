import pygame
from game_parameters import *
import random
from fish import Fish, fishes
from enemy import Enemy,enemies

def draw_background(surf):
    #load our tiles
    water = pygame.image.load("../assets/sprites/water.png").convert()
    sand = pygame.image.load("../assets/sprites/sand_top.png").convert()
    seagrass = pygame.image.load("../assets/sprites/seagrass.png").convert()
    #use png transparency
    sand.set_colorkey((0,0,0))
    seagrass.set_colorkey((0,0,0))

    #fill the screen
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
            surf.blit(water, (x,y))

    #draw the sandy bottom
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        surf.blit(sand, (x, SCREEN_HEIGHT-TILE_SIZE))

    #add seagrass randomly at the bottom of the beach
    for _ in range(5):
        x = random.randint(0, SCREEN_HEIGHT)
        surf.blit(seagrass, (x, SCREEN_HEIGHT-TILE_SIZE*2))

    #draw the text
    custom_font = pygame.font.Font("../assets/fonts/Brainfish_Rush.ttf", 48)
    text = custom_font.render("Chomp", True, (255, 0, 0))
    surf.blit(text, (SCREEN_WIDTH/2 - text.get_width()/2, 0))

def add_fish(num_fish):
    for _ in range(num_fish):
        fishes.add(Fish(random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 20),
                        random.randint(TILE_SIZE, SCREEN_HEIGHT - 2 * TILE_SIZE)))

def add_enemies(num_ememies):
    for _ in range(num_ememies):
        enemies.add(Enemy(random.randint(SCREEN_WIDTH, SCREEN_WIDTH +20),
                        random.randint(TILE_SIZE, SCREEN_HEIGHT - 2 * TILE_SIZE)))






