"""
    Description: Sprites class file handles all objects for every sprite added
    to the game. Each class is identical to one another except for the values
    of the default location and the image that is loaded.

    Arguments:
        x: x is the starting x position of the sprite. All sprites have a
        hardcoded default x position so that you don't explicitly need to pass
        in a value.

        y: y is the starting y position of the sprite. All sprites have a
        hardcoded default y position so that you don't explicitly need to pass
        in a value.

    Returns:
        None
"""

import pygame


# Loads the sprite for the bunny
class Bunny(pygame.sprite.Sprite):
    def __init__(self, x = 325, y = 450):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/bunny.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# Loads the sprite for the player
class Player(pygame.sprite.Sprite):
    def __init__(self, x = 200, y = 200):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/character.PNG")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# Loads the sprite for the sword
class Sword(pygame.sprite.Sprite):
    def __init__(self, x = 550, y = 50):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/sword.PNG")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# Loads the sprite for the old man
class OldMan(pygame.sprite.Sprite):
    def __init__(self, x = 20, y = 220):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/oldman.PNG")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# Loads the sprite for the boss
class Boss(pygame.sprite.Sprite):
    def __init__(self, x = 150, y = 150):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/boss.PNG")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# Loads the sprite for the slingshot
class Slingshot(pygame.sprite.Sprite):
    def __init__(self, x = 460, y = 400):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/slingshot.PNG")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# Loads the sprite for the shield
class Shield(pygame.sprite.Sprite):
    def __init__(self, x = 450, y = 50):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/shield.PNG")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# Loads the sprite for the goblin
class Goblin(pygame.sprite.Sprite):
    def __init__(self, x = 350, y = 400):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/goblin.PNG")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
