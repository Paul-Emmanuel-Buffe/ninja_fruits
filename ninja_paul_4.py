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

BASE_DIR = r"C:/Users/Windows/Desktop/projets/1a/ninja_fruits"
IMAGE_DIR = os.path.join(BASE_DIR, "images")
SOUND_DIR = os.path.join(BASE_DIR, "sounds")
BOMB_IMAGE = pygame.image.load(os.path.join(IMAGE_DIR, 'bomb.png'))
BOMB_IMAGE = pygame.transform.scale(BOMB_IMAGE, (120, 120))


rect1 = pygame.Rect(400,300, 400, 50)
rect2 = pygame.Rect(400, 400, 400, 50)
rect3 = pygame.Rect(400, 500, 400, 50)
rect4 = pygame.Rect(100,100, 1000, 400)
Time = pygame.time.Clock()


background_image = pygame.image.load(os.path.join(IMAGE_DIR, 'background.png')) 
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fruit Ninja")

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# sounds
try:
    back_ground_sound = pygame.mixer.Sound((r"C:\Users\Windows\Desktop\projets\1a\ninja_fruits\sounds\ninja.wav"))
except pygame.error as e:
    print(f"Error loading sound: {e}")
    back_ground_sound = None

# list for sounds for sword
sword_1 = pygame.mixer.Sound((r"C:\Users\Windows\Desktop\projets\1a\ninja_fruits\sounds\sabre1.wav"))
sword_2 = pygame.mixer.Sound((r"C:\Users\Windows\Desktop\projets\1a\ninja_fruits\sounds\sabre2.wav"))
sword_3 = pygame.mixer.Sound((r"C:\Users\Windows\Desktop\projets\1a\ninja_fruits\sounds\sabre3.wav"))
sword_list = [sword_1, sword_2, sword_3]


try:
    ubuntu_font = pygame.font.Font(os.path.join("Ubuntu-Regular.ttf"), 36)
except FileNotFoundError:
    print("La p-olice n'a pas été trouvée. Utilisation de la police par défaut.")
    ubuntu_font = pygame.font.Font(None, 36)

LARGE_FONT = pygame.font.Font((r"C:\Users\Windows\Desktop\projets\1a\ninja_fruits\Ubuntu-Regular.ttf"), 72)

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]



# Classe Fruit
class Fruit:
    def __init__(self, image_name, image_cut_name):
        self.image = pygame.image.load(os.path.join(IMAGE_DIR, image_name))
        self.cut_image = pygame.image.load(os.path.join(IMAGE_DIR, image_cut_name))
        self.rect = self.image.get_rect(center=(random.randint(50, SCREEN_WIDTH-50), SCREEN_HEIGHT + 50))
        self.speed = random.randint(3, 5)
        self.letter = random.choice(letters)
        self.cut = False
        self.cut_time = 0    
    
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
        self.image = pygame.image.load(os.path.join(IMAGE_DIR, "icecube.png"))
        self.cut_image = pygame.image.load(os.path.join(IMAGE_DIR, "ice_cut2.png"))
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

# random sword sound
def swords_selection():
    sword_sound =  random.choice(sword_list)
    return sword_sound

def letter_tab(letter):
    return letter[random.randint(0, len(letter)-1)]          




def Main_menu(screen, image, r1, r2, r3,  font, white, yellow):
    ng = "new game"
    history = "score history"
    exit = "exit"
    
    pygame.Surface.blit(screen, image, (0,0))

    pygame.draw.rect(screen, yellow, r1)
    font_dis = ubuntu_font.render(ng, 1, white)
    font_rect = font_dis.get_rect(center=r1.center)
    screen.blit(font_dis, font_rect)

    pygame.draw.rect(screen, yellow, r2)
    font_dis2 = ubuntu_font.render(history, 1, white)
    font_rect2 = font_dis2.get_rect(center=r2.center)
    screen.blit(font_dis2, font_rect2)

    pygame.draw.rect(screen, yellow, r3)
    font_dis3 = ubuntu_font.render(exit, 1, white)
    font_rect3 = font_dis3.get_rect(center=r3.center)
    screen.blit(font_dis3, font_rect3)

    pygame.display.update()

def level_difficulty(screen, image, r1, r2, r3, ubuntu_font, white, yellow):
    easy = "easy"
    normal = "normal"
    hard = "hard"
    
    pygame.Surface.blit(screen, image, (0, 0))

    # Drawing the 'easy' difficulty button
    pygame.draw.rect(screen, yellow, r1)
    font_dis = ubuntu_font.render(easy, 1, white)
    font_rect = font_dis.get_rect(center=r1.center)
    screen.blit(font_dis, font_rect)

    # Drawing the 'normal' difficulty button
    pygame.draw.rect(screen, yellow, r2)
    font_dis2 = ubuntu_font.render(normal, 1, white)
    font_rect2 = font_dis2.get_rect(center=r2.center)
    screen.blit(font_dis2, font_rect2)

    # Drawing the 'hard' difficulty button
    pygame.draw.rect(screen, yellow, r3)
    font_dis3 = ubuntu_font.render(hard, 1, white)
    font_rect3 = font_dis3.get_rect(center=r3.center)
    screen.blit(font_dis3, font_rect3)

    pygame.display.update()

def select_random_object(speed):
    objects_list = [
        Fruit("apple.png", "apple_cut2.png"),
        Fruit("pineapple.png", "pineapple_cut2.png"),
        Fruit("coconut.png", "coco_cut2.png"),
        Fruit("banana.png", "banana_cut2.png"),
        Bomb(speed),
        Icecube(speed)
    ]

    object_weight = [0.20, 0.20, 0.20, 0.20, 0.1, 0.1]

    choosen_object = random.choices(objects_list, weights=object_weight, k=1)[0]

    if choosen_object.letter in letters:
        letters.remove(choosen_object.letter)

    return choosen_object



def get_player_name(screen):
    image = pygame.image.load(os.path.join(IMAGE_DIR, 'background.png')).convert()
    image = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))  # Adapter l'image à l'écran
    
    input_box = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2, 300, 50)  # Centrer la zone de saisie
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    user_name = ''

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                active = input_box.collidepoint(event.pos)
                color = color_active if active else color_inactive
            
            if event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_RETURN:
                    return text
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

        # Afficher l'image de fond
        screen.blit(image, (0, 0))

        # Afficher le texte "Enter your name:" en blanc et centré
        prompt_text = ubuntu_font.render("Enter your name:", True, (255, 255, 255))  # Utilisation de ubuntu_font
        screen.blit(prompt_text, ((SCREEN_WIDTH - prompt_text.get_width()) // 2, SCREEN_HEIGHT // 3))

        # Afficher le texte saisi
        txt_surface = ubuntu_font.render(text, True, (255, 255, 255))  # Utilisation de ubuntu_font
        input_box.w = max(300, txt_surface.get_width() + 10)
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        
        # Dessiner la bordure de la zone de saisie
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()
        pygame.time.Clock().tick(30)


def New_Game(screen, image, start_time, game_duration, score, game_over, missed_fruits, speed, player_name):
    # Calcul du temps écoulé
    timer = pygame.time.Clock()
    objects = []
    score = 0
    missed_fruits = 0
    running = True
    game_over = False
    start_time = pygame.time.get_ticks()
    game_duration = 100000
    combo_count = 0
    combo_display_time = 0  
    display_combo = False 
    
    while running:
        screen.blit(background_image, (0, 0))
        elapsed_time = pygame.time.get_ticks() - start_time
        remaining_time = max(0, game_duration - elapsed_time) 
        minutes = remaining_time // 60000
        seconds = (remaining_time // 1000) % 60
        time_text = ubuntu_font.render(f"{minutes:02}:{seconds:02}", True, WHITE)
        screen.blit(time_text, (SCREEN_WIDTH - time_text.get_width() - 10, 10))

        if score > 0 and remaining_time == 0:
            running = False
            win_text = LARGE_FONT.render("You Win", True, RED)
            screen.blit(win_text, (SCREEN_WIDTH // 2 - win_text.get_width() // 2, SCREEN_HEIGHT // 2 - win_text.get_height() // 2))
            pygame.display.flip()
            pygame.time.delay(2000)  
            record_history(score, player_name)
            back_ground_sound.stop()
            sword_3.play()
            main()
        
        if game_over and remaining_time > 0: 
            running = False
            lose_text = LARGE_FONT.render("You Lose", True, RED)
            screen.blit(lose_text, (SCREEN_WIDTH // 2 - lose_text.get_width() // 2, SCREEN_HEIGHT // 2 - lose_text.get_height() // 2))
            pygame.display.flip()
            back_ground_sound.stop()
            pygame.time.delay(2000)  
            record_history(score, player_name)
            sword_3.play()
            main()
        
        if game_over:
            running = False
            lose_text = LARGE_FONT.render("You Lose", True, RED)
            screen.blit(lose_text, (SCREEN_WIDTH // 2 - lose_text.get_width() // 2, SCREEN_HEIGHT // 2 - lose_text.get_height() // 2))
            pygame.display.flip()
            back_ground_sound.stop()
            pygame.time.delay(2000)  
            record_history(score, player_name)
            sword_3.play()
            main()
        
        if remaining_time == 0 and not game_over:
            game_over = True
            pygame.display.flip()
            pygame.time.delay(2000)  
            back_ground_sound.stop()
            pygame.time.delay(2000)  
            record_history(score, player_name)
            sword_3.play()
            main()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and not game_over:
                swords_selection().play()  # PARTIE LECTURE DU SON
                pressed_key = pygame.key.name(event.key)
                if pressed_key.isalpha() and len(pressed_key) == 1:
                    for obj in objects:
                        if obj.letter == pressed_key:
                            if isinstance(obj, Fruit):
                                obj.cut = True
                                obj.cut_time = pygame.time.get_ticks()
                                score += 1
                                combo_count += 1
                                
                                if combo_count == 2:
                                    score += 20
                                    combo_count = 0  
                                    combo_display_time = pygame.time.get_ticks()  
                                    display_combo = True  
                                                    
                            elif isinstance(obj, Icecube):
                                obj.cut = True
                                obj.cut_time = pygame.time.get_ticks()
                            else:
                                game_over = True  
                            break 
        
        if not game_over:
            if random.randint(1, 60) == 1:
                objects.append(select_random_object(speed))

            for obj in objects[:]:
                obj.move(speed)
                obj.draw(screen)

                if obj.cut and pygame.time.get_ticks() - obj.cut_time > 1000:  
                    if obj.letter not in letters:
                        combo_count -= 1
                        if combo_count < 0:
                            combo_count = 0
                        letters.append(obj.letter)
                        objects.remove(obj)

                if obj.rect.bottom < 0:
                    if isinstance(obj, Fruit):
                        missed_fruits += 1
                        if missed_fruits >= 3:
                            game_over = True

                    if obj.letter not in letters:
                        letters.append(obj.letter)
                        objects.remove(obj)

        for obj in objects:
            if isinstance(obj, Icecube) and obj.cut:
                if pygame.time.get_ticks() - obj.cut_time < 3000:  
                    pygame.display.flip()  
                    pygame.time.delay(3000)   
                break  

        score_text = ubuntu_font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        missed_text = ubuntu_font.render(f"Missed: {missed_fruits}", True, WHITE)
        screen.blit(missed_text, (10, 50))
        
        if display_combo:
            screen.blit(ubuntu_font.render(f"COMBO + 2", True, WHITE), (10, 100))

            if pygame.time.get_ticks() - combo_display_time > 2000:
                display_combo = False  

        pygame.display.flip()
        timer.tick(30)

    pygame.quit()


def load_font(font_path, size):
    return pygame.font.Font(font_path, size)

def scores_history(BASE_DIR): 
    score_hist = []
    with open(os.path.join(BASE_DIR, "score.json"), "r") as f:
        player_list = json.load(f)      
    for i, player in enumerate(player_list):
        score_hist.append(f'{i+1}. {player["name"]} => {player["score"]}')
    return score_hist



def Score(screen, image, rect, ubuntu_font, WHITE, YELLOW, BASE_DIR): 
    score = scores_history(BASE_DIR)
    vertical_pos = rect.top + 0
    pygame.Surface.blit(screen, image, (0, 0))

    title_text = LARGE_FONT.render("SCORE BOARD", True, WHITE)
    title_rect = title_text.get_rect(center=(rect.centerx, rect.top + 0))
    screen.blit(title_text, title_rect)
    vertical_pos += 60
    
    for i, score_text in enumerate(score):
        font_score = ubuntu_font.render(score_text, True, WHITE)
        font_rect = font_score.get_rect(midtop=(rect.centerx, vertical_pos))
        screen.blit(font_score, font_rect)
        vertical_pos += 40


    pygame.display.update()


    pygame.display.update()





def add_points(score_container, player_name, points):
    for element in score_container:
        if element["name"] == player_name:
            element["score"] += points
            return score_container

def record_history(score, player_name, BASE_DIR):
    # Chemin du fichier score.json
    score_file = os.path.join(BASE_DIR, "score.json")
    
    # Lire les scores existants
    try:
        with open(score_file, "r") as f:
            score_container = json.load(f)
    except FileNotFoundError:
        # Si le fichier n'existe pas, initialiser une liste vide
        score_container = []
    except json.JSONDecodeError:
        # Si le fichier est mal formaté, initialiser une liste vide
        score_container = []
    
    # Mettre à jour le score du joueur existant ou ajouter un nouveau joueur
    player_found = False
    for player in score_container:
        if player["name"] == player_name:
            player["score"] += score
            player_found = True
            break
    
    if not player_found:
        score_container.append({"name": player_name, "score": score})
    
    # Trier les scores par ordre décroissant
    score_container = sorted(score_container, key=lambda x: x["score"], reverse=True)
    
    # Enregistrer les scores dans le fichier
    with open(score_file, "w") as f:
        json.dump(score_container, f, indent=4)  # indent=4 pour un formatage lisible
            
def main():
    # Variable states for the screen
    Main_Menu = 0
    new_game = 1
    difficulty = 2
    score_hist = 3
    Exit = 4
    state_screen = Main_Menu
    back_ground_sound.play(-1)

    score = 0
    missed_fruits = 0
    running = True
    game_over = False

    # Initialisation du chrono
    start_time = pygame.time.get_ticks()
    game_duration = 60000

    # Couleurs
    YELLOW = (253, 165, 15)
    WHITE = (255, 255, 255)

    image = pygame.image.load(os.path.join(IMAGE_DIR, 'background.png')).convert()

    # Main loop
    running = True
    while running:
        # Fixed frames per second
        pygame.time.Clock().tick(30)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if state_screen == Main_Menu and rect1.collidepoint(event.pos):
                    state_screen = difficulty
                elif state_screen == Main_Menu and rect2.collidepoint(event.pos):
                    state_screen = score_hist
                elif state_screen == Main_Menu and rect3.collidepoint(event.pos):
                    state_screen = Exit
                elif state_screen == difficulty:
                    if rect1.collidepoint(event.pos):
                        state_screen = new_game
                    elif rect2.collidepoint(event.pos):
                        state_screen = new_game
                    elif rect3.collidepoint(event.pos):
                        state_screen = new_game

        # Render the different screens
        if state_screen == Main_Menu:
            Main_menu(screen, image, rect1, rect2, rect3,  Font, WHITE, YELLOW)
        elif state_screen == difficulty:
            level_difficulty(screen, image, rect1, rect2, rect3, ubuntu_font, WHITE, YELLOW)
        elif state_screen == new_game:
            if rect1.collidepoint(event.pos):
                player_name = get_player_name(screen)
                speed = random.randint(2, 4)
                New_Game(screen, image, start_time, game_duration, score, game_over, missed_fruits, speed, player_name)
            elif rect2.collidepoint(event.pos):
                player_name = get_player_name(screen)
                speed = random.randint(5, 7)
                New_Game(screen, image, start_time, game_duration, score, game_over, missed_fruits, speed, player_name)
            elif rect3.collidepoint(event.pos):
                player_name = get_player_name(screen)
                speed = random.randint(7, 9)
                New_Game(screen, image, start_time, game_duration, score, game_over, missed_fruits, speed, player_name)
        elif state_screen == score_hist:
            Score(screen, image, rect4, ubuntu_font, WHITE, YELLOW, BASE_DIR)
        elif state_screen == Exit:
            running = False
            pygame.quit()
            sys.exit()

    pygame.display.update()  
    # Quit Pygame properly
    pygame.quit()

if __name__ == "__main__":
    main()