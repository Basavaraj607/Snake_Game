import pygame.image
from pygame.locals import *
import time



class snake:
    def __init__(self,parent_screen):
        snake.parent_screen = parent_screen
        snake.block = pygame.image.load("resources/apple.jpg").convert()
       
        self.x = 100
        self.y = 100
        self.direction = 'down'
        
    def draw(self):
        self.parent_screen.fill((92,25,84))
        self.parent_screen.blit(self.block,(self.x,self.y))
        pygame.display.flip()

    def walk(self):
        if self.direction =='down':
            self.y+=10
        if self.direction == 'up':
            self.y-=10
        if self.direction =='right':
            self.x+=10
        if self.direction == 'left':
            self.x-=10
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
        self.surface.fill((255,255,255))
        self.snake = snake(self.surface)
        self.snake.draw()

    def run(self):
        running  = True
        while running ==True:
            for  event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                    if event.key == K_LEFT:
                        self.snake.move_left()    
                elif event.type == QUIT:
                    running = False
            self.snake.walk()
            time.sleep(0.2)  

if __name__=='__main__':
    game = Game()
    game.run()
              
                        
        