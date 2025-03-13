import pygame
from settings import *

class City(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        # w = wool
        # c = city
        # p = player
        # x = rock        
        self.image = pygame.transform.scale(pygame.image.load('./graphics/city.png').convert_alpha(), (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect(topleft = pos)

