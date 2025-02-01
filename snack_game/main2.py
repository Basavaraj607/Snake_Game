import pygame.image
from pygame.locals import *
import time

class snake:
    def __init__(self,parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = 100
        self.y = 100
        self.direction = 'up'
 
    def draw(self):

        self.parent_screen.fill((92,25,84))
        self.parent_screen.blit(self.block,(self.x,self.y))
        pygame.display.flip()
    
    def walk(self):
        if(self.direction == 'up'):
            self.y-=10
        if(self.direction == 'down'):
            self.y+=10
        if(self.direction == 'left'):
            self.x-=10
        if(self.direction == 'right'):
            self.x+=10
        self.draw()



    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'
 
    def move_down(self):
        self.direction = 'down'

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000,500))
        self.surface.fill((92,25,84))
        self.snake = snake(self.surface)
        self.snake.draw()

    def run(self):

        running = True

        while running:
            for  event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                      running = False
                    if event.key == K_UP:
                       self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                    if event.key == K_LEFT:
                       self.snake.move_left()
                    if event.key == K_RIGHT:
                      self.snake.move_right()
                elif event.type ==QUIT:
                    running = False
            self.snake.walk()
            time.sleep(0.2)


        


"""def draw_block():
    surface.blit(block,(block_x,block_y))
    pygame.display.flip()
    surface.fill((92,25,84))"""


if __name__== '__main__':
    game = Game()
    game.run()


    

    
