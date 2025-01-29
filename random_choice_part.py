import pygame
import random 

# Initialisation de Pygame
pygame.init()

class Fruit:
    
    def __init__(self,name, x, y,width, length, image, valeur,etat, letter, goal):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.length = length
        self.image = image
        self.etat = etat
        self.valeur = valeur #score pour les fruits et valeur strike pour la bombe
        self.letter = letter
        self.goal = goal

    def rect(self, screen, Black):
        pygame.draw.rect(screen, Black, (self.x, self.y , self.width, self.length))
        
    
    def apple_move_left_right(self):
        print(self.goal)
        self.x +=0.10
        self.y -=0.10
        if self.y <= 0 and self.x <= self.goal :
            self.x += 0.10
            self.y -= 1
        return self.x, self.y
    
    def __str__(self):
            """Retourne une représentation lisible de l'objet Fruit."""
            return f"Fruit(name={self.name}, x={self.x}, y={self.y}, letter={self.letter}, etat={self.etat})"
    
def letter_tab(letter):
    return letter[random.randint(0, len(letter)-1)]

            

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
x_goal = random.randint(601,1125)
letters =  ["z","q","s","d","o","k","l","m"]



def select_random_object():
    
    objects_list = [
    Fruit("apple",0, 600 , 75, 75, 'pasteque.png', 1,"pas couper",letter_tab(letters), x_goal  ),
    Fruit("pineapple",SCREEN_WIDTH, SCREEN_HEIGHT,75,75, 'pineapple.png', 1,"pas couper",letter_tab(letters), x_goal),
    Fruit("coconut",SCREEN_WIDTH, SCREEN_HEIGHT,75,75, 'coconut.png', 1,"pas couper",letter_tab(letters), x_goal),
    Fruit("icecube",SCREEN_WIDTH, SCREEN_HEIGHT,75,75, 'icecube.png', 1,"pas couper",letter_tab(letters), x_goal),
    Fruit("bomb",SCREEN_WIDTH, SCREEN_HEIGHT,75,75, 'bomb.png', 1,"pas couper",letter_tab(letters), x_goal)]



    object_weight =  [0.20, 0.20, 0.20, 0.10, 0.20]

    return random.choices(objects_list, weights= object_weight, k=1)[0]


object = select_random_object()
print(object)

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

    

        
