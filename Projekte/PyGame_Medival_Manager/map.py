import pygame
from settings import *
from tile import Tile
from wool import Wool
from city import City
from player import Player

class Map():
    def __init__(self):

        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        for row_index,row in enumerate(WORLDMAP):
            for col_index,col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x,y), [self.visible_sprites])
                if col == 'p':
                    Player((x,y), [self.visible_sprites])
                if col == 'w':
                    Wool((x,y), [self.visible_sprites])
                if col == 'c':
                    City((x,y), [self.visible_sprites])

    
    def run(self, events):
        self.visible_sprites.update(events)
        self.visible_sprites.draw(self.display_surface)
        



