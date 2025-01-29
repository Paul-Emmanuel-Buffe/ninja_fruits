import pygame
import random 

# Initialisation de Pygame
pygame.init()

class Fruit:
    def __init__(self,name, x, y,width, length, image, valeur,etat, letter):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.length = length
        self.image = image
        self.etat = etat
        self.valeur = valeur #score pour les fruits et valeur strike pour la bombe
        self.letter = letter

    def rect(self, screen, Black, font):
        fruit = pygame.draw.rect(screen, Black, (self.x, self.y , self.width, self.length))
        font_dis2 = font.render(self.letter, 1, WHITE)
        font_rect2 = font_dis2.get_rect(center = fruit.center)
        screen.blit(font_dis2, font_rect2)
    
    def apple_move_left_right(self):
        print("hello")
        self.x +=0.10
        self.y -=0.10
        return self.x, self.y
    

    letters =  ["z","q","s","d","o","k","l","m"]
    def letter_tab(letters):
        return letters[random.randint(0, len(letters)-1)]
            

# Configuration de l'écran
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Projet Pygame - 1200x600")
my_Font = pygame.font.SysFont("comicsansms", 32)


# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BACKGROUND_COLOR = (50, 50, 150)  

apple       = Fruit("apple",SCREEN_WIDTH, SCREEN_HEIGHT,75,75, 'pasteque.png', 1,  )
pineapple   = Fruit()
coconut     = Fruit()

# Boucle principale
running = True
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Affichage
    screen.fill(BACKGROUND_COLOR)  # Remplir l'écran avec la couleur de fond

    



    # Mettre à jour l'écran
    pygame.display.flip()


# Quitter Pygame proprement
pygame.quit()

    

        
