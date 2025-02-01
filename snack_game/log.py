import random
import sys
import pygame
from pygame.locals import *
from tkinter import Button
import os
import tkinter as tk
from tkinter import messagebox

# SCORE_FILE = f'{username}.txt'
USER_PASS_FILE = "user_pass.txt"
highest_score = 0
# if os.path.exists(SCORE_FILE):
#     with open(SCORE_FILE, "r") as file:
#         highest_score = int(file.read())

def get_font(size):
    return pygame.font.Font(pygame.font.get_default_font(), size)

def login_screen():
    global username_entry, password_entry, login_window
    
    def center_window(window, width, height):
     screen_width = window.winfo_screenwidth()
     screen_height = window.winfo_screenheight()

     x = (screen_width - width) // 2
     y = (screen_height - height) // 2

     window.geometry(f"{width}x{height}+{x}+{y}")

    login_window = tk.Tk()
    # login_window.geometry("289x511")
    login_window.title("Flappy Bird - Login")
    login_window.configure(bg="#3C3F41")

# Set window size
    window_width = 290
    window_height = 511

# Center the window on the screen
    center_window(login_window, window_width, window_height)

    frame = tk.Frame(login_window,bg="#3C3F41")
    
    login_label=tk.Label(frame, text="""Login to Flappy 
Bird""", bg='black', fg="Yellow", font=("Arial Black", 20))
    username_label = tk.Label(frame,text="Username",bg='#8F00FF',fg="#FFFFFF",font=("Arial", 10, 'bold'))
    password_label=tk.Label(frame, text="Password", bg='#8F00FF', fg="#FFFFFF", font=("Arial", 10, 'bold'))
    username_entry = tk.Entry (frame, font=("Arial", 10))
    password_entry = tk.Entry(frame, show="*", font=("Arial", 10))
    login_button = tk.Button(frame, text="Login", bg="#DC143C", fg="#FFFFFF", font=("Arial", 10), command=validate_login)
    # signup_button = tk.Button(frame, text="Sign-up", bg="#DC143C", fg="#FFFFFF", font=("Arial", 10), command=validate_login)
    #grid placing
    login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=20)
    username_label.grid (row=1, column=0)
    username_entry.grid(row=1, column=1, pady=5)
    password_label.grid(row=2, column=0)
    password_entry.grid(row=2, column=1, pady=5)
    login_button.grid(row=3, column=0,columnspan=2, pady=15)
    # signup_button.grid(row=3, column=1, )
    frame.pack()
    login_window.mainloop()

def validate_login():
    global username_entry, password_entry, login_window

    global username
    username = username_entry.get()
    password = password_entry.get()

    with open("user_pass.txt", "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split()
            if username == stored_username and password == stored_password:
                # Successful login
                messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
                login_window.destroy()
                Game.run()
                endScreen(score,username)
                return

    # Invalid login
    messagebox.showerror("Login Failed", "Invalid username or password")

    # Add background image and music

import pygame
from pygame.locals import *
import time
import random

SIZE = 40
BACKGROUND_COLOR = (110, 110, 5)
BREDTH = 1000
WIDTH = 800

class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("resources/apple.jpg").convert()
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1,24)*SIZE
        self.y = random.randint(1,19)*SIZE

class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("resources/block.jpg").convert()
        self.direction = 'down'

        self.length = 1
        self.x = [40]
        self.y = [40]

    def move_left(self):
        if self.direction != 'right':
            self.direction = 'left'

    def move_right(self):
        if self.direction != 'left':
            self.direction = 'right'

    def move_up(self):
        if self.direction != 'down':
            self.direction = 'up'

    def move_down(self):
        if self.direction != 'left':
            self.direction = 'down'

    def walk(self):
        # update body

        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        # update head
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        self.draw()

    def draw(self):
        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i]))

        pygame.display.flip()

    def increase_length(self):

        self.length += 1

        self.x.append(-1)
        self.y.append(-1)
        self.image = pygame.image.load("resources/apple.jpg").convert()


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Codebasics Snake And Apple Game")

        pygame.mixer.init()
        self.play_background_music()

        self.surface = pygame.display.set_mode((BREDTH, WIDTH))
        self.snake = Snake(self.surface)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def play_background_music(self):
        pygame.mixer.music.load('resources/bg_music_1.mp3')
        pygame.mixer.music.play(-1, 0)

    def play_sound(self, sound_name):
        if sound_name == "crash":
            sound = pygame.mixer.Sound("resources/crash.mp3")
        elif sound_name == 'ding':
            sound = pygame.mixer.Sound("resources/ding.mp3")

        pygame.mixer.Sound.play(sound)

    def reset(self):
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface)

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def render_background(self):
        bg = pygame.image.load("resources/background.jpg")
        self.surface.blit(bg, (0,0))

    def play(self):
        self.render_background()
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        # snake eating apple scenario
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.play_sound("ding")
            self.snake.increase_length()
            self.apple.move()

        if self.snake.x[0] == BREDTH or self.snake.y[0] == 0:
                self.play_sound('crash')
                raise "Collision Occurred"
        
        if self.snake.x[0] == 0 or self.snake.y[0] == WIDTH:
                self.play_sound('crash')
                raise "Collision Occurred"

        # snake colliding with itself
        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.play_sound('crash')
                raise "Collision Occurred"

    def display_score(self):
        font = pygame.font.SysFont('arial',30)
        score = font.render(f"Score: {self.snake.length}",True,(200,200,200))
        self.surface.blit(score,(850,10))

    def show_game_over(self):
        self.render_background()
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game is over! Your score is {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))
        line2 = font.render("To play again press Enter. To exit press Escape!", True, (255, 255, 255))
        self.surface.blit(line2, (200, 350))
        pygame.mixer.music.pause()
        pygame.display.flip()

    def run(self):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        pause = False

                    if not pause:
                        if event.key == K_LEFT:
                            self.snake.move_left()

                        if event.key == K_RIGHT:
                            self.snake.move_right()

                        if event.key == K_UP:
                            self.snake.move_up()

                        if event.key == K_DOWN:
                            self.snake.move_down()

                elif event.type == QUIT:
                    running = False
            try:

                if not pause:
                    self.play()

            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()

            time.sleep(.25)

if __name__ == '__main__':
    game = Game()
    game.run()