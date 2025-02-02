import pygame
import sys
import os
import json

class Menu:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.text = [
            "New game",
            "Score",
            "Exit",
            "Easy",
            "Normal",
            "Hard",
            "main menu"
        ]

        self.rect1 = pygame.Rect(400,300, 400, 50)
        self.rect2 = pygame.Rect(400, 400, 400, 50)
        self.rect3 = pygame.Rect(400, 500, 400, 50)
        self.rect4 = pygame.Rect(100,100, 1000, 400)
        self.rect5 = pygame.Rect(500,0, 200, 50)
        self.color = (253, 165,15)
        self.running = True
        self.state = "main menu"

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.state == "main menu":

                    if self.rect1.collidepoint(event.pos):
                        self.state = "difficulty"
                    if self.rect2.collidepoint(event.pos):
                        self.state = "score"
                    if self.rect3.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

                elif self.state == "score":
                    if self.rect5.collidepoint(event.pos):
                        self.state = "main menu"

                
                


    def display_menu(self):
        pygame.draw.rect(self.screen, self.color, self.rect1)
        pygame.draw.rect(self.screen, self.color, self.rect2)
        pygame.draw.rect(self.screen, self.color, self.rect3)

        
        text1 = self.font.render(self.text[0], True, (0, 0, 0))
        text2 = self.font.render(self.text[1], True, (0, 0, 0))
        text3 = self.font.render(self.text[2], True, (0, 0, 0))

        
        self.screen.blit(text1, text1.get_rect(center=self.rect1.center))
        self.screen.blit(text2, text2.get_rect(center=self.rect2.center))
        self.screen.blit(text3, text3.get_rect(center=self.rect3.center))

    def display_difficulty(self):

        pygame.draw.rect(self.screen, self.color, self.rect1)
        pygame.draw.rect(self.screen, self.color, self.rect2)
        pygame.draw.rect(self.screen, self.color, self.rect3)

        
        text1 = self.font.render(self.text[3], True, (0, 0, 0))
        text2 = self.font.render(self.text[4], True, (0, 0, 0))
        text3 = self.font.render(self.text[5], True, (0, 0, 0))

        
        self.screen.blit(text1, text1.get_rect(center=self.rect1.center))
        self.screen.blit(text2, text2.get_rect(center=self.rect2.center))
        self.screen.blit(text3, text3.get_rect(center=self.rect3.center))


    def display_score(self, score):
        vertical_pos =self.rect4.top + 20
        pygame.draw.rect(self.screen, self.color, self.rect4)
        pygame.draw.rect(self.screen, self.color, self.rect5)

        text1 = self.font.render(self.text[6], True, (0, 0, 0))


        for i, score_text in enumerate(score):
            text2 = font_score = self.font.render(score_text, True,(0, 0, 0))  
            font_rect = font_score.get_rect(midtop=(self.rect4.centerx, vertical_pos))  
            self.screen.blit(text2, font_rect)
            vertical_pos += 40
        
        
        self.screen.blit(text1, text1.get_rect(center=self.rect5.center))
       

    def scores_history():
        score_hist= []
        with open (os.path.join("score.json"), "r") as f:
                player_list= json.load(f)      
        for i, player in enumerate(player_list):
            score_hist.append(f'{i+1}. {player["name"]} => {player["score"]}')
        return score_hist
        
        
    def display(self):
        if self.state == "main menu":
            self.display_menu()
        elif self.state == "difficulty":
            self.display_difficulty()
        elif self.state == "score":
            score = Menu.scores_history()
            Menu.display_score(self, score)


