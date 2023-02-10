import pygame
from settings import *
class Coin(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.Surface((TILE_SIZE,TILE_SIZE))
        self.image.fill(COIN_COLOR)
        self.rect = self.image.get_rect(topleft = pos)
        self.x = pos[0]
        self.y = pos[1]
