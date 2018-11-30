import pygame

class Bunny(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/bunny.png")
        self.rect = self.image.get_rect()
        self.rect.x = 325
        self.rect.y = 450
        
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/character.PNG")
        self.rect = self.image.get_rect()  
        self.rect.x = x
        self.rect.y = y
        
class Sword(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/sword.PNG")
        self.rect = self.image.get_rect()  
        self.rect.x = 550
        self.rect.y = 50
        
class OldMan(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/oldman.PNG")
        self.rect = self.image.get_rect()  
        self.rect.x = 20
        self.rect.y = 220

class Boss(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/boss.PNG")
        self.rect = self.image.get_rect()  
        self.rect.x = 230
        self.rect.y = 200
        

        
