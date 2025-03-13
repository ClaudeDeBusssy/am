import pygame, sys
from settings import *
from map import Map

class Game:
    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Medival Manager')
        pygame.mouse.set_cursor(*pygame.cursors.diamond)
        pygame.font.init()
        self.clock = pygame.time.Clock()

        self.map = Map()

    def run(self):
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    
                    pygame.quit()
                    sys.exit()
  
            self.screen.fill((0,134,49))
            
            
            self.map.run(events)



            pygame.display.update()
            self.clock.tick(FPS)    
            
   

if __name__ == '__main__':
    game = Game()
    game.run()

