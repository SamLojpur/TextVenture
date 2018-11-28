import pygame

class Bunny(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/bunny.png")
        self.rect = self.image.get_rect()
        self.rect.x = 325
        self.rect.y = 450
        
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/character.PNG")
        self.rect = self.image.get_rect()  
        self.rect.x = 200
        self.rect.y = 200