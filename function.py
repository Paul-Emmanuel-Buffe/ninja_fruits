import pygame
import random 
import os
import sys
import json

# Initialisation de Pygame
pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
background_image = pygame.image.load(os.path.join('images', 'background.jpeg')) 
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fruit Ninja")

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
# sounds
try:
    back_ground_sound = pygame.mixer.Sound("sounds/ninja.wav" )
except pygame.error as e:
    print(f"Error loading sound: {e}")
    back_ground_sound = None

FRUIT_IMAGES = []
for img_name in ['apple.png', 'banana.png', 'orange.png']:
    img = pygame.image.load(os.path.join('images', img_name))
    FRUIT_IMAGES.append(pygame.transform.scale(img, (50, 50)))

BOMB_IMAGE = pygame.image.load(os.path.join('images', 'bomb.jpeg'))
BOMB_IMAGE = pygame.transform.scale(BOMB_IMAGE, (50, 50))
try:
    ubuntu_font = pygame.font.Font(os.path.join("Ubuntu-Regular.ttf"), 36)
except FileNotFoundError:
    print("La police n'a pas été trouvée. Utilisation de la police par défaut.")
    ubuntu_font = pygame.font.Font(None, 36)
LARGE_FONT = pygame.font.Font(None, 72)

letters = ["z", "q", "s", "d", "o", "k", "l", "m"]
# Classe Fruit
class Fruit:
    def __init__(self):
        self.image = random.choice(FRUIT_IMAGES)
        self.rect = self.image.get_rect(center=(random.randint(50, SCREEN_WIDTH-50), SCREEN_HEIGHT + 50))
        self.speed = random.randint(3, 5)
        self.letter = random.choice(letters)
    
    def move(self):
        self.rect.y -= self.speed
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        letter_text = ubuntu_font.render(self.letter.upper(), True, BLACK)
        screen.blit(letter_text, (self.rect.left - letter_text.get_width() - 10, self.rect.centery - letter_text.get_height() // 2))
# classe Bomb        
class Bomb:
    def __init__(self):
        self.image = BOMB_IMAGE
        self.rect = self.image.get_rect(center=(random.randint(50, SCREEN_WIDTH-50), SCREEN_HEIGHT + 50))
        self.speed = random.randint(3, 5)
        self.letter = random.choice(letters) 
    
    def move(self):
        self.rect.y -= self.speed
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        letter_text = ubuntu_font.render(self.letter.upper(), True, BLACK)
        screen.blit(letter_text, (self.rect.left - letter_text.get_width() - 10, self.rect.centery - letter_text.get_height() // 2))

           
def Main_menu(screen, image, r1, r2, r3,  font, white, yellow):
    ng = "new game"
    history = "score history"
    exit = "exit"
    
    pygame.Surface.blit(screen, image, (0,0))

    pygame.draw.rect(screen,yellow, r1)
    font_dis = font.render(ng, 1, white)
    font_rect = font_dis.get_rect(center= r1.center)
    screen.blit(font_dis,font_rect)

    pygame.draw.rect(screen, yellow, r2)
    font_dis2 = font.render(history, 1, white)
    font_rect2 = font_dis.get_rect(center= r2.center)
    screen.blit(font_dis2,font_rect2
                )
    pygame.draw.rect(screen, yellow, r3)
    font_dis = font.render(exit, 1, white)
    font_rect = font_dis.get_rect(center= r3.center)
    screen.blit(font_dis,font_rect)

    pygame.display.update()  



def level_difficulty(screen, image, r1, r2, r3, font, white, yellow):
    easy = "easy"
    normal = "normal"
    hard = "hard"
    
    pygame.Surface.blit(screen, image, (0,0))

    pygame.draw.rect(screen,yellow, r1)
    font_dis = font.render(easy, 1, white)
    font_rect = font_dis.get_rect(center= r1.center)
    screen.blit(font_dis,font_rect)

    pygame.draw.rect(screen, yellow, r2)
    font_dis2 = font.render(normal, 1, white)
    font_rect2 = font_dis.get_rect(center= r2.center)
    screen.blit(font_dis2,font_rect2
                )
    pygame.draw.rect(screen, yellow, r3)
    font_dis = font.render(hard, 1, white)
    font_rect = font_dis.get_rect(center= r3.center)
    screen.blit(font_dis,font_rect)

    pygame.display.update()  


def New_Game(screen, image, r1, r2,font, white):

    
    pygame.Surface.blit(screen, image, (0,0))
    pygame.display.update()  

def Score(screen, image, rect,font, white,yellow, BASE_DIR):
    score = scores_history(BASE_DIR)
    vertical_pos =rect.top + 20
    pygame.Surface.blit(screen, image, (0,0))

    pygame.draw.rect(screen,yellow, rect)
    for i, score_text in enumerate(score):
        font_score = font.render(score_text, True, white)  
        font_rect = font_score.get_rect(midtop=(rect.centerx, vertical_pos))  
        
        screen.blit(font_score, font_rect) 
        
        vertical_pos += 40
    pygame.display.update()  


def letter_tab(letter):
    return letter[random.randint(0, len(letter)-1)]

def scores_history(BASE_DIR):
    score_hist= []
    with open (os.path.join(BASE_DIR,"score.json"), "r") as f:
            player_list= json.load(f)      
    for i, player in enumerate(player_list):
       score_hist.append(f'{i+1}. {player["name"]} => {player["score"]}')
    return score_hist
            
def main():
    # Configuration de l'écran
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Projet Pygame - 1200x600")
    Font = pygame.font.SysFont("Font\PlaywriteVN-Thin.ttf", 42)
    rect1 = pygame.Rect(400,300, 400, 50)
    rect2 = pygame.Rect(400, 400, 400, 50)
    rect3 = pygame.Rect(400, 500, 400, 50)
    rect4 = pygame.Rect(100,100, 1000, 400)
    Time = pygame.time.Clock()

    ## variable etat de l'ecran
    Main_Menu = 0
    new_game = 1
    difficulty = 2
    score = 3
    Exit = 4
    state_screen = Main_Menu
    BASE_DIR = r"C:\Users\alexc\Desktop\laplateforme\projet\annee1\ninja_fruits"

    # Couleurs
    YELLOW =(253, 165,15)
    BROWN =(129, 93, 61)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BACKGROUND_COLOR = (50, 50, 150)  

    image = pygame.image.load(os.path.join('images\\background_image.png')).convert()


    letters =  ["z","q","s","d","o","k","l","m"]


    apple       = Fruit("apple",random.randint(0, 1125), 600 , 75, 75, 'pasteque.png', 1,"pas couper",letter_tab(letters), random.randint(601,1125)  )
    pineapple   = Fruit("pineapple",SCREEN_WIDTH, SCREEN_HEIGHT,75,75, 'pineapple.png', 1,"pas couper",letter_tab(letters), random.randint(601,1125))
    coconut     = Fruit("coconut",SCREEN_WIDTH, SCREEN_HEIGHT,75,75, 'coconut.png', 1,"pas couper",letter_tab(letters), random.randint(601,1125))
    icecube   = Fruit("icecube",SCREEN_WIDTH, SCREEN_HEIGHT,75,75, 'icecube.png', 1,"pas couper",letter_tab(letters), random.randint(601,1125))
    bomb     = Fruit("bomb",SCREEN_WIDTH, SCREEN_HEIGHT,75,75, 'bomb.png', 1,"pas couper",letter_tab(letters), random.randint(601,1125))

    # Boucle principale
    running = True
    while running:
        #fixe le nombre d'image par seconde de l'ecran
        Time.tick(30)
        
        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if state_screen == Main_Menu and rect1.collidepoint(event.pos):
                    state_screen = difficulty
                elif state_screen == Main_Menu and rect2.collidepoint(event.pos):
                    state_screen = score
                elif state_screen == Main_Menu and rect3.collidepoint(event.pos):
                    state_screen= Exit
                elif state_screen == difficulty:
                    if rect1.collidepoint(event.pos):
                        state_screen = new_game
                    elif rect2.collidepoint(event.pos):
                        state_screen = new_game
                    elif rect3.collidepoint(event.pos):
                        state_screen = new_game

        # Affichage
        if state_screen == Main_Menu:
            Main_menu(screen, image, rect1, rect2, rect3,  Font, WHITE, YELLOW)
        elif state_screen == difficulty:
            level_difficulty(screen, image, rect1, rect2, rect3, Font, WHITE, YELLOW)
        elif state_screen == new_game:
            New_Game(screen, image, rect1, rect2, Font, WHITE)
        elif state_screen == score:
            Score(screen, image, rect4,Font, WHITE,YELLOW, BASE_DIR)
        elif state_screen == Exit:
            pygame.quit()
            sys.exit()
        
        
        # Mettre à jour l'écran
        pygame.display.flip()


    # Quitter Pygame proprement
    pygame.quit()

if __name__ == "__main__":
    main()