import pygame
import time
import os
import sys
import json
from Menu import Menu
from Fruit import Fruit
from Player import Player

class Game:
    def __init__(self, screen, caption, font, background):
        self.screen = screen
        self.caption = caption
        self.font = font
        self.background = background
        self.clock = pygame.time.Clock()
        self.running = True

    def event(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def display(self, menu): 
        while self.running:
            self.event()
            self.screen.blit(self.background,(0,0))
            menu.display()
            menu.event()
            pygame.display.flip()
            self.clock.tick(60)
    
         

def main():
    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode((1200 , 600))
    caption = pygame.display.set_caption("Fruit Ninja")
    font = pygame.font.Font(None, 36)
    image_path = r"images/background.png"

    try:
        background = pygame.image.load(image_path)
        print("Image loaded successfully!")
    except pygame.error as e:
        print(f"Error loading image: {e}")

    rect = Menu(screen, font)
    game = Game(screen, caption, font, background)
    game.display(rect)
    
    

    pygame.quit()
main()
