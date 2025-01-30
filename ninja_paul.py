import pygame
import random
import os


pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

BASE_DIR = r"C:/Users/Windows/Desktop/projets/1a/ninja_fruits"
IMAGE_DIR = os.path.join(BASE_DIR, "images")
SOUND_DIR = os.path.join(BASE_DIR, "sounds")

background_image = pygame.image.load(os.path.join(IMAGE_DIR, 'background.png')) 
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fruit Ninja")


# sounds
try:
    back_ground_sound = pygame.mixer.Sound((r"C:\Users\Windows\Desktop\projets\1a\ninja_fruits\sounds\ninja.wav"))
except pygame.error as e:
    print(f"Error loading sound: {e}")
    back_ground_sound = None


BOMB_IMAGE = pygame.image.load(os.path.join(IMAGE_DIR, 'bomb.png'))
BOMB_IMAGE = pygame.transform.scale(BOMB_IMAGE, (120, 120))


try:
    ubuntu_font = pygame.font.Font(os.path.join("Ubuntu-Regular.ttf"), 36)
except FileNotFoundError:
    print("La p-olice n'a pas été trouvée. Utilisation de la police par défaut.")
    ubuntu_font = pygame.font.Font(None, 36)

LARGE_FONT = pygame.font.Font(None, 72)

letters = ["z", "q", "s", "d", "o", "k", "l", "m"]

# Classe Fruit
class Fruit:
    def __init__(self, image_name, image_cut_name):
        self.image = pygame.image.load(os.path.join(IMAGE_DIR, image_name))
        self.cut_image = pygame.image.load(os.path.join(IMAGE_DIR, image_cut_name))
        self.rect = self.image.get_rect(center=(random.randint(50, SCREEN_WIDTH-50), SCREEN_HEIGHT + 50))
        self.speed = random.randint(3, 5)
        self.letter = random.choice(letters)
        self.cut = False
    
    def move(self):
        self.rect.y -= self.speed
    
    def draw(self, screen):
        if self.cut:
            screen.blit(self.cut_image, self.rect)
        else:
            screen.blit(self.image, self.rect)
            letter_text = ubuntu_font.render(self.letter.upper(), True, WHITE)
            screen.blit(letter_text, (self.rect.left - letter_text.get_width() - 10, self.rect.centery - letter_text.get_height() // 2))

# classe Bomb        
class Bomb:
    def __init__(self):
        self.image = BOMB_IMAGE
        self.rect = self.image.get_rect(center=(random.randint(50, SCREEN_WIDTH-50), SCREEN_HEIGHT + 50))
        self.speed = random.randint(3, 5)
        self.letter = random.choice(letters) 
        self.cut = False
        self.cut_time = 0
    
    def move(self):
        self.rect.y -= self.speed
    
    def draw(self, screen):
        
        screen.blit(self.image, self.rect)
        letter_text = ubuntu_font.render(self.letter.upper(), True, WHITE)
        screen.blit(letter_text, (self.rect.left - letter_text.get_width() - 10, self.rect.centery - letter_text.get_height() // 2))

class Icecube:
    def __init__(self):
        self.image = pygame.image.load(os.path.join(IMAGE_DIR, "icecube.png"))
        self.cut_image = pygame.image.load(os.path.join(IMAGE_DIR, "ice_cut2.png"))
        self.rect =self.image.get_rect(center=(random.randint(50, SCREEN_WIDTH-50), SCREEN_HEIGHT + 50))
        self.speed = random.randint(3,6)
        self.letter = random.choice(letters)
        self.cut = False
        self.cut_time = 0
    def move (self):
        self.rect.y -= self.speed
    
    def draw(self, screen):
        if self.cut:
            screen.blit(self.cut_image, self.rect)
        else:
            screen.blit(self.image, self.rect)
            letter_text = ubuntu_font.render(self.letter.upper(), True, WHITE)
            screen.blit(letter_text, (self.rect.left - letter_text.get_width() - 10, self.rect.centery - letter_text.get_height() // 2))


def select_random_object():
    
    objects_list = [
    Fruit("apple.png", "apple_cut2.png"),
    Fruit("pineapple.png", "pineapple_cut2.png"),
    Fruit("coconut.png", "coco_cut2.png"),
    Fruit("banana.png", "banana_cut2.png"),
    Bomb(),
    Icecube()]

    object_weight =  [0.20, 0.20, 0.20, 0.20,0.1, 0.1]

    return random.choices(objects_list, weights= object_weight, k=1)[0]




# Fonction principale du jeu
def main():
    if back_ground_sound:
        back_ground_sound.play(-1)
    
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
                objects.append(select_random_object())

                
            
            for obj in objects[:]:
                obj.move()
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

if __name__ == "__main__":
    main()
