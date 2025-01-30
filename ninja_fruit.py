import pygame
import random
import os


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
        
# Fonction principale du jeu
def main():
    back_ground_sound.play(-1)
    timer = pygame.time.Clock()
    fruits = []
    bombs = []
    score = 0
    missed_fruits = 0
    running = True
    game_over = False
    # Initialisation du chrono
    start_time = pygame.time.get_ticks()
    game_duration = 60000 
    
    while running:
        screen.blit(background_image,(0, 0))
        
        # Calcul du temps écoulé
        if not game_over:
            elapsed_time = pygame.time.get_ticks() - start_time
            remaining_time = max(0, game_duration - elapsed_time) 
        
             # Convertir le temps restant en minutes et secondes
            minutes = remaining_time // 60000
            seconds = (remaining_time // 1000) % 60
        time_text = ubuntu_font.render(f"{minutes:02}:{seconds:02}", True, BLACK)
        screen.blit(time_text, (SCREEN_WIDTH - time_text.get_width() - 10, 10))
        
        if remaining_time == 0 and not game_over:
            game_over = True
            
            congrats_text = LARGE_FONT.render("Congratulations!", True, RED)
            screen.blit(congrats_text, (SCREEN_WIDTH // 2 - congrats_text.get_width() // 2, SCREEN_HEIGHT // 2 - congrats_text.get_height() // 2))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and not game_over:
                pressed_key = pygame.key.name(event.key)
                if pressed_key.isalpha() and len(pressed_key) == 1:  
                    for fruit in fruits:
                        if fruit.letter == pressed_key:
                            fruits.remove(fruit)
                            score += 1
                            break  
                    for bomb in bombs:
                        if bomb.letter == pressed_key:  
                            game_over = True  
            
                            break 
                        
        if not game_over:
            if random.randint(1, 60) == 1:
                fruits.append(Fruit())
            
            if random.randint(1, 120) == 1:
                bombs.append(Bomb())    
            
            for fruit in fruits:
                fruit.move()
                fruit.draw(screen)
                if fruit.rect.bottom < 0:
                    fruits.remove(fruit)
                    missed_fruits += 1
                    if missed_fruits >= 3:
                        game_over = True
            for bomb in bombs:
                bomb.move()
                bomb.draw(screen)
                if bomb.rect.bottom < 0: 
                    bombs.remove(bomb)
        
        if game_over and remaining_time > 0: 
            lose_text = LARGE_FONT.render("You Lose", True, RED)
            screen.blit(lose_text, (SCREEN_WIDTH // 2 - lose_text.get_width() // 2, SCREEN_HEIGHT // 2 - lose_text.get_height() // 2))
            
                        
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
