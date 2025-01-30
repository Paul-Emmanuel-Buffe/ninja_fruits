import pygame
import random 
import os
import sys
import json

# Initialisation de Pygame
pygame.init()

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


background_image = pygame.image.load(os.path.join('images', 'background.png')) 
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
for img_name in ['apple.png', 'banana.png', 'coconut.png']:
    img = pygame.image.load(os.path.join('images', img_name))
    FRUIT_IMAGES.append(pygame.transform.scale(img, (50, 50)))

BOMB_IMAGE = pygame.image.load(os.path.join('images', 'bomb.png'))
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
    def __init__(self, image_name, image_cut_name):
        self.image = pygame.image.load(os.path.join('images', image_name))
        self.cut_image = pygame.image.load(os.path.join('images', image_cut_name))
        self.rect = self.image.get_rect(center=(random.randint(50, SCREEN_WIDTH-50), SCREEN_HEIGHT + 50))
        self.speed = random.randint(3, 5)
        self.letter = random.choice(letters)
        self.cut = False
    
    def move(self, speed):
        self.rect.y -= speed
    
    def draw(self, screen):
        if self.cut:
            screen.blit(self.cut_image, self.rect)
        else:
            screen.blit(self.image, self.rect)
            letter_text = ubuntu_font.render(self.letter.upper(), True, WHITE)
            screen.blit(letter_text, (self.rect.left - letter_text.get_width() - 10, self.rect.centery - letter_text.get_height() // 2))

# classe Bomb        
class Bomb:
    def __init__(self,speed):
        self.image = BOMB_IMAGE
        self.rect = self.image.get_rect(center=(random.randint(50, SCREEN_WIDTH-50), SCREEN_HEIGHT + 50))
        self.speed = speed
        self.letter = random.choice(letters) 
        self.cut = False
        self.cut_time = 0
    
    def move(self, speed):
        self.rect.y -= speed
    
    def draw(self, screen):
        
        screen.blit(self.image, self.rect)
        letter_text = ubuntu_font.render(self.letter.upper(), True, WHITE)
        screen.blit(letter_text, (self.rect.left - letter_text.get_width() - 10, self.rect.centery - letter_text.get_height() // 2))

class Icecube:
    def __init__(self,speed):
        self.image = pygame.image.load(os.path.join('images', "icecube.png"))
        self.cut_image = pygame.image.load(os.path.join('images', "ice_cut2.png"))
        self.rect =self.image.get_rect(center=(random.randint(50, SCREEN_WIDTH-50), SCREEN_HEIGHT + 50))
        self.speed = speed
        self.letter = random.choice(letters)
        self.cut = False
        self.cut_time = 0
    def move (self, speed):
        self.rect.y -= speed
    
    def draw(self, screen):
        if self.cut:
            screen.blit(self.cut_image, self.rect)
        else:
            screen.blit(self.image, self.rect)
            letter_text = ubuntu_font.render(self.letter.upper(), True, WHITE)
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

def select_random_object(speed):
    
    objects_list = [
    Fruit("apple.png", "apple_cut2.png"),
    Fruit("pineapple.png", "pineapple_cut2.png"),
    Fruit("coconut.png", "coco_cut2.png"),
    Fruit("banana.png", "banana_cut2.png"),
    Bomb(speed),
    Icecube(speed)]

    object_weight =  [0.20, 0.20, 0.20, 0.20,0.1, 0.1]

    return random.choices(objects_list, weights= object_weight, k=1)[0]

        
def New_Game(screen,image, start_time, game_duration, score, game_over, missed_fruits, speed):
    # Calcul du temps écoulé
    timer = pygame.time.Clock()
    objects = []
    score = 0
    missed_fruits = 0
    running = True
    game_over = False
    start_time = pygame.time.get_ticks()
    game_duration = 60000 
    
    while running:
            screen.blit(background_image, (0, 0))
            elapsed_time = pygame.time.get_ticks() - start_time
            remaining_time = max(0, game_duration - elapsed_time) 
            minutes = remaining_time // 60000
            seconds = (remaining_time // 1000) % 60
            time_text = ubuntu_font.render(f"{minutes:02}:{seconds:02}", True, WHITE)
            screen.blit(time_text, (SCREEN_WIDTH - time_text.get_width() - 10, 10))
            
            if remaining_time == 0 and not game_over:
                game_over = True
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and not game_over:
                    pressed_key = pygame.key.name(event.key)
                    if pressed_key.isalpha() and len(pressed_key) == 1:
                        for obj in objects:
                            if obj.letter == pressed_key:
                                if isinstance(obj, Fruit):
                                    obj.cut = True
                                    obj.cut_time = pygame.time.get_ticks()
                                    score += 1
                                elif isinstance(obj, Icecube):
                                    obj.cut = True
                                    obj.cut_time = pygame.time.get_ticks()
                                    score += 1
                                else:
                                    game_over = True  
                                break 
            
            if not game_over:
                if random.randint(1, 60) == 1:
                    objects.append(select_random_object(speed))

                
                for obj in objects[:]:
                    obj.move(speed)
                    obj.draw(screen)
                    
                    if obj.cut and pygame.time.get_ticks() - obj.cut_time > 1000:  # Supprimer après 0.5 sec
                        objects.remove(obj)

                    if obj.rect.bottom < 0:
                        objects.remove(obj)
                        if isinstance(obj, Fruit):
                            missed_fruits += 1
                            if missed_fruits >= 3:
                                game_over = True
            
            if game_over and remaining_time > 0: 
                lose_text = LARGE_FONT.render("You Lose", True, RED)
                screen.blit(lose_text, (SCREEN_WIDTH // 2 - lose_text.get_width() // 2, SCREEN_HEIGHT // 2 - lose_text.get_height() // 2))
                
                    
            for obj in objects:
                if isinstance(obj, Icecube) and obj.cut:
                    if pygame.time.get_ticks() - obj.cut_time < 3000:  
                        pygame.display.flip()  
                        pygame.time.delay(3000)   
                    break  
                    
            score_text = ubuntu_font.render(f"Score: {score}", True, BLACK)
            screen.blit(score_text, (10, 10))
            
            missed_text = ubuntu_font.render(f"Missed: {missed_fruits}", True, BLACK)
            screen.blit(missed_text, (10, 50))
            
            if game_over:
                lose_text = LARGE_FONT.render("You Lose", True, RED)
                screen.blit(lose_text, (SCREEN_WIDTH // 2 - lose_text.get_width() // 2, SCREEN_HEIGHT // 2 - lose_text.get_height() // 2))
        
            pygame.display.flip()
            timer.tick(30)
    pygame.quit()

        

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
    ## variable etat de l'ecran
    Main_Menu = 0
    new_game = 1
    difficulty = 2
    score_hist = 3
    Exit = 4
    state_screen = Main_Menu
    BASE_DIR = r"C:\Users\alexc\Desktop\laplateforme\projet\annee1\ninja_fruits"

    back_ground_sound.play(-1)
    
    score = 0
    missed_fruits = 0
    running = True
    game_over = False

    # Initialisation du chrono
    start_time = pygame.time.get_ticks()
    game_duration = 60000

    # Couleurs
    YELLOW =(253, 165,15)
    WHITE = (255, 255, 255)

    image = pygame.image.load(os.path.join('images\\background.png')).convert()
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
                    state_screen = score_hist
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
        elif state_screen == new_game and rect1.collidepoint(event.pos):
                ##vitesse du fruit
                speed = random.randint(1,3)
                New_Game(screen,image, start_time, game_duration,  score, game_over, missed_fruits,speed)
        elif state_screen == new_game and rect2.collidepoint(event.pos):
                speed= random.randint(4,6)
                New_Game(screen,image, start_time, game_duration, score, game_over, missed_fruits,speed)
        elif state_screen == new_game and rect3.collidepoint(event.pos):
                speed= random.randint(6,8)
                New_Game(screen,image, start_time, game_duration, score, game_over, missed_fruits,speed)
        elif state_screen == score_hist:
            Score(screen, image, rect4,Font, WHITE,YELLOW, BASE_DIR)
        elif state_screen == Exit:
            running = False
            pygame.quit()
            sys.exit()
        
        
    pygame.display.update()  
    # Quitter Pygame proprement
    pygame.quit()

if __name__ == "__main__":
    main()