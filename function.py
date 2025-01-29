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
        
letters =  ["z","q","s","d","o","k","l","m"]
def letter_tab(letters):
        return letters[random.randint(0, len(letters)-1)]
            
class Apple(Fruit):
    ## Fruit.name est == a self.init
    def __init__(self):
        self.name = "apple"
        self.x = 0
        self.y= 600
        self.width = 75
        self.length = 75
        self.letter = letter_tab(letters)
        self.etat = "pas couper"
        self.goal1 = random.randint(601, 1025)
        

    def rect(self, screen, Black):
       return pygame.draw.rect(screen, Black, (self.x, self.y , self.width, self.length))

    
    def apple_move_left_right(self):
        while self.x < 600 and self.y > 100:
            self.x +=0.10
            self.y -=0.10
        return self.x, self.y
            

         

class Pineapple(Fruit):
        Fruit.name = "pineapple"
        Fruit.x = 0
        Fruit.y = 600
        Fruit.Width = 75
        Fruit.length = 75
        Fruit.letter = letter_tab(letters)
        Fruit.etat = "pas couper"
        print(Fruit.letter)

        def rect(x, y , width, length):
            return (x,y,width,length)

class Coconut(Fruit):
        Fruit.name = "coconut"
        Fruit.x = 0
        Fruit.y = 600
        Fruit.Width = 75
        Fruit.length = 75
        Fruit.letter = letter_tab(letters)
        Fruit.etat = "pas couper"
        print(Fruit.letter)

        def rect(x, y , width, length):
           return (x,y,width,length)

class Bomb(Fruit):
        Fruit.name = "bomb"
        Fruit.x = 0
        Fruit.y = 600
        Fruit.Width = 75
        Fruit.length = 75
        Fruit.letter = letter_tab(letters)
        Fruit.etat = "pas couper"
        Fruit.valeur = 3 ## 3 strike


        def rect(x, y , width, length):
           return (x,y,width,length)

class Icecube(Fruit):
        Fruit.name = "icecube"
        Fruit.x = 0
        Fruit.y = 600
        Fruit.Width = 75
        Fruit.length = 75
        Fruit.letter = letter_tab(letters)
        Fruit.etat = "pas couper"
        print(Fruit.etat)

        def rect(x, y , width, length):
           return (x,y,width,length)


# Configuration de l'écran
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Projet Pygame - 1200x600")
apple = Apple()
# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BACKGROUND_COLOR = (50, 50, 150)  

# Boucle principale
running = True
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Affichage
    screen.fill(BACKGROUND_COLOR)  # Remplir l'écran avec la couleur de fond

    apple.rect(screen, BLACK)
    apple.apple_move_left_right()
    screen.blit(screen, (SCREEN_WIDTH,SCREEN_HEIGHT))



    # Mettre à jour l'écran
    pygame.display.flip()


# Quitter Pygame proprement
pygame.quit()

    

        
