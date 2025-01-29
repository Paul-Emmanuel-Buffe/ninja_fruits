import random as rd
import pygame
import os
import sys

# ways across the project
#BASE_DIR = r"C:/Users/Windows/Desktop/projets/1a/ninja_fruits"
#IMAGE_DIR = os.path.join(BASE_DIR, "images")
#SOUND_DIR = os.path.join(BASE_DIR, "sounds")


pygame.init()

# screen setting
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ninjas Fruits")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BACKGROUND_COLOR = (50, 50, 150)  

# Pictures
back_ground_image  = pygame.image.load(os.path.join("images/background_image.png"))

#fonts used
ubuntu_font=pygame.font.Font(os.path.join("Ubuntu-Regular.ttf"), 36)

# sounds
try:
    back_ground_sound = pygame.mixer.Sound("sounds/ninja.wav" )
except pygame.error as e:
    print(f"Error loading sound: {e}")
    back_ground_sound = None

# Main
back_ground_sound.play(-1)
running = True
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Affichage
    screen.blit(back_ground_image, (0,0))

    # Mettre à jour l'écran
    pygame.display.flip()


# Quitter Pygame proprement
pygame.quit()

