import pygame
import sys

from game_parameters import *
from fish import fishes
from enemy import enemies
from background import draw_background, add_fish, add_enemies
from player import Player

#initialize pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Adding enemy fish on the screen')

#clock object
clock = pygame.time.Clock()

#Main Loop
running = True
background = screen.copy()
draw_background(background)

#draw fish on the screen
add_fish(5)

#draw enemy fish on screen
add_enemies(3)

#create a player fish
player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

#initialize score for fish game
score = 0
score_font = pygame.font.Font("../assets/fonts/Black_Crayon.ttf", 48)

#load the sound effects
chomp = pygame.mixer.Sound("../assets/sounds/chomp.wav")
hurt = pygame.mixer.Sound("../assets/sounds/hurt.wav")
bubbles = pygame.mixer.Sound("../assets/sounds/bubbles.wav")


#add alternate fish image
life_icon = pygame.image.load("../assets/sprites/orange_fish_alt.png").convert()
life_icon.set_colorkey((0, 0, 0))

#set the number of lives
lives = NUM_LIVES


while lives > 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #control fish with keyboard
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move_up()
            if event.key == pygame.K_DOWN:
                player.move_down()
            if event.key == pygame.K_LEFT:
                player.move_left()
            if event.key == pygame.K_RIGHT:
                player.move_right()

        #will work okay if a single player game
        if event.type == pygame.KEYUP:
            player.stop()


    # draw background
    screen.blit(background, (0, 0))

    #draw green fish
    fishes.update()

    #draw enemy fish
    enemies.update()

    #draw player fish
    player.update()

    #check for player and green fish collisions
    result = pygame.sprite.spritecollide(player, fishes, True)
    if result:
        #play chomp sound
        pygame.mixer.Sound.play(chomp)
        score += len(result)
        # draw more green fish on the screen
        add_fish(len(result))

    # check for player and enemy fish collisions
    result = pygame.sprite.spritecollide(player, enemies, True)
    if result:
        # play hurt sound
        pygame.mixer.Sound.play(hurt) #update to another sound
        # lose lives if hurt
        lives -= len(result)

        # draw more enemy fish on the screen
        add_enemies(len(result))

    # check if any fish is off the screen
    for fish in fishes:
        if fish.rect.x < -fish.rect.width:  # use the tile size
            fishes.remove(fish)  # remove the fish from the sprite group
            add_fish(1)

    # check if any enemy is off the screen
    for enemy in enemies:
        if enemy.rect.x < -enemy.rect.width:  # use the tile size
            enemies.remove(enemy)  # remove the fish from the sprite group
            add_enemies(1)

    #draw game objects
    fishes.draw(screen)
    player.draw(screen)
    enemies.draw(screen)

    #draw the score on the screen
    text = score_font.render(f"{score}", True, (255, 0, 0))
    screen.blit(text, (SCREEN_WIDTH-TILE_SIZE, 0))

    #draw lives in lower left corner
    for i in range(lives):
        screen.blit(life_icon, (i*TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE))


    # update the display
    pygame.display.flip()

    # limit the frame rate
    clock.tick(60)

#once all lives are gone
#create new background when game over
screen.blit(background, (0, 0))


#show game over message and final score
message = score_font.render("GAME OVER!!!", True, (255, 0, 0))
screen.blit(message, (SCREEN_WIDTH /2 - message.get_width() /2, SCREEN_HEIGHT/2 - message.get_height() /2 ))
score_text = score_font.render(f"Score: {score}", True, (0, 0, 0))
screen.blit(score_text, (SCREEN_WIDTH /2 - score_text.get_width() /2, SCREEN_HEIGHT /2 - 3*score_text.get_height() /2))

#update display
pygame.display.flip()


#play game over sound effect
pygame.mixer.Sound.play(bubbles)

#wait for user to exit the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()













