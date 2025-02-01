import pygame.image
from pygame.locals import *

class Snack:
    def __init__(self,parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = 100
        self.y = 100
 
    def draw(self):

        self.parent_screen.fill((92,25,84))
        self.parent_screen.blit(self.block,(self.x,self.y))
        pygame.display.flip()


    def move_left(self):
        self.x-=10
        self.draw()

    def move_right(self):
        self.x+=10
        self.draw()

    def move_up(self):
        self.y-=10
        self.draw()
 
    def move_down(self):
        self.y+=10    
        self.draw()  

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000,500))
        self.surface.fill((92,25,84))
        self.snack = Snack(self.surface)
        self.snack.draw()

    def run(self):

        running = True

        while running:
            for  event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                      running = False
                    if event.key == K_UP:
                       self.snack.move_up()
                    if event.key == K_DOWN:
                        self.snack.move_down()
                    if event.key == K_LEFT:
                       self.snack.move_left()
                    if event.key == K_RIGHT:
                      self.snack.move_right()
                elif event.type ==QUIT:
                    running = False


        


"""def draw_block():
    surface.blit(block,(block_x,block_y))
    pygame.display.flip()
    surface.fill((92,25,84))"""


if __name__== '__main__':
    game = Game()
    game.run()


    

    
