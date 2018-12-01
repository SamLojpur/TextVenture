import pygame


class Bunny(pygame.sprite.Sprite):
    def __init__(self, x = 325, y = 450):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/bunny.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Player(pygame.sprite.Sprite):
    def __init__(self, x = 200, y = 200):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/character.PNG")
        self.rect = self.image.get_rect()  
        self.rect.x = x
        self.rect.y = y


class Sword(pygame.sprite.Sprite):
    def __init__(self, x = 550, y = 50):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/sword.PNG")
        self.rect = self.image.get_rect()  
        self.rect.x = x
        self.rect.y = y


class OldMan(pygame.sprite.Sprite):
    def __init__(self, x = 20, y = 220):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/oldman.PNG")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y        


class Boss(pygame.sprite.Sprite):
    def __init__(self, x = 150, y = 150):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/boss.PNG")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y        
        

class Slingshot(pygame.sprite.Sprite):
    def __init__(self, x = 460, y = 400):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/slingshot.PNG")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y        
        

class Shield(pygame.sprite.Sprite):
    def __init__(self, x = 450, y = 50):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/shield.PNG")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        

class Goblin(pygame.sprite.Sprite):
    def __init__(self, x = 350, y = 400):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/goblin.PNG")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 

