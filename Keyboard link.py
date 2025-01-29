import pygame
import random 
import os
pygame.init()
BASE_DIR = r"C:/Users/Windows/Desktop/projets/1a/Pendu/pendu"
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ninjas Fruits")
ubuntu_font = pygame.font.Font(os.path.join(BASE_DIR, "Ubuntu-Regular.ttf"), 36)


running = True
while running:
    screen.fill((0, 0, 0))  
    Letter= "A"
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.unicode == object.letter:
                correct_txt = ubuntu_font.render("correct", True, (255, 255, 255))
                print
            else:
                print("Faux")
         
    screen.blit(correct_txt, 50, 50)
    # Mettre à jour l'écran
    pygame.display.flip()


# Quitter Pygame proprement
pygame.quit()