import pygame
import random
import os


pygame.init()
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fruit Ninja")

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

FRUIT_IMAGES = []
for img_name in ['apple.png', 'banana.png', 'orange.png']:
    img = pygame.image.load(os.path.join('images', img_name))
    FRUIT_IMAGES.append(pygame.transform.scale(img, (50, 50)))


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

# Fonction principale du jeu
def main():
    
    timer = pygame.time.Clock()
    fruits = []
    score = 0
    missed_fruits = 0
    running = True
    game_over = False
    
    while running:
        screen.fill(WHITE)
        
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
                
        if not game_over:
            if random.randint(1, 60) == 1:
                fruits.append(Fruit())
            
            for fruit in fruits:
                fruit.move()
                fruit.draw(screen)
                if fruit.rect.bottom < 0:
                    fruits.remove(fruit)
                    missed_fruits += 1
                    if missed_fruits >= 3:
                        game_over = True
        
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
