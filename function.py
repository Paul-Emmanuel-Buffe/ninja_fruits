import pygame
import random 

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
    Fruit.name = "apple"
    Fruit.x = random.randint(0, 1125)
    Fruit.y= random.randint(0, 525)
    Fruit.Width = 75
    Fruit.length = 75
    Fruit.letter = letter_tab(letters)
    Fruit.etat = "pas couper"

    def rect(x, y , width, length):
           pygame.draw.rect()
        
class Pineapple(Fruit):
        Fruit.name = "pineapple"
        Fruit.x = random.randint(0, 1125)
        Fruit.y = random.randint(0, 525)
        Fruit.Width = 75
        Fruit.length = 75
        Fruit.letter = letter_tab(letters)
        Fruit.etat = "pas couper"
        print(Fruit.letter)

class Coconut(Fruit):
        Fruit.name = "coconut"
        Fruit.x = random.randint(0, 1125)
        Fruit.y = random.randint(0, 525)
        Fruit.Width = 75
        Fruit.length = 75
        Fruit.letter = letter_tab(letters)
        Fruit.etat = "pas couper"
        print(Fruit.letter)

class Bomb(Fruit):
        Fruit.name = "bomb"
        Fruit.x = random.randint(0, 1125)
        Fruit.y = random.randint(0, 525)
        Fruit.Width = 75
        Fruit.length = 75
        Fruit.letter = letter_tab(letters)
        Fruit.etat = "pas couper"
        print(Fruit.letter)
        Fruit.valeur = 3 ## 3 strike

class Icecube(Fruit):
        Fruit.name = "icecube"
        Fruit.x = random.randint(0, 1125)
        Fruit.y = random.randint(0, 525)
        Fruit.Width = 75
        Fruit.length = 75
        Fruit.letter = letter_tab(letters)
        Fruit.etat = "pas couper"
        print(Fruit.etat)



Apple.rect(Fruit.x, Fruit.y, Fruit.width, Fruit.length)




    

        
