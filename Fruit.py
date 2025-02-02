import random

class Fruit:
    def __init__(self, image, vitesse, letters, point):
        self.image = image
        self.vitesse = vitesse
        self.x = random.randint(0, 1200)
        self.y = 600
        self.init_position = (self.x, self.y)
        self.letters = letters
        self.point = point
        self.state = False

        
            
    


