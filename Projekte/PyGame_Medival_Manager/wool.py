import pygame
from settings import *

class Wool(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        # w = wool
        # c = city
        # p = player
        # x = rock        
        self.image = pygame.transform.scale(pygame.image.load('./graphics/wool.png').convert_alpha(), (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:   
                if self.rect.collidepoint(event.pos):
                   my_font = pygame.font.SysFont('Comic Sans MS', 30)
                   text_surface = my_font.render('Some Text', False, (0, 0, 0))
                   pygame.display.blit(text_surface,(0,0))
                    