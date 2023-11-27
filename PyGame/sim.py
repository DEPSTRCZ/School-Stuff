import pygame
import sys
import random
import math

pygame.init()

width, height, snowflakes_amount = 800, 600, 28

screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("Snowfall Screensaver")
pygame.display.flip()

white = ((220, 220, 220),(160,160,180),(100, 100, 120))

balls = []
offset = [5,5]

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 10
        self.wind = random.randint(-1,1)
        self.color = random.randint(0, 2)
        self.mov = pygame.draw.circle(surface=screen, color=white[self.color], center=[random.randint(0,height),random.randint(0,width)], radius=self.size)

    def fall(self):
        self.y += 50#self.size
        self.x += math.sin(self.y/90)         
        if self.y > height:
            self.y = 0
            self.x = random.randint(0, width)
            self.size = random.randint(1, 3)
            self.wind = random.randint(-1,1)
            self.color = random.randint(0, 2)

    def draw(self):
        self.mov = pygame.draw.circle(surface=screen, color=white[self.color], center=self.mov.center, radius=self.size)

for _ in range(snowflakes_amount):
    balls.append(Ball(random.randint(0, width), random.randint(0, height)))

while True: # Main game loop
    for event in pygame.event.get(): # quit
        if event.type == pygame.QUIT: # quit
            pygame.quit() # quit 
            sys.exit() # quit 
        elif event.type == pygame.VIDEORESIZE:
            # Handle window resizing
            width, height = event.w, event.h
            screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)


    screen.fill((0, 0, 0)) # reset the screen 

    for ball in balls: 

        ball.mov = ball.mov.move(offset)
        if ball.mov.left <= 0 or ball.mov.right >= width:
            offset[0] = -offset[0]
        if ball.mov.top <= 0 or ball.mov.bottom >= height:
            offset[1] = -offset[1]
        ball.draw() # for each sf fall em

    pygame.display.flip() # cycles the screen
    pygame.time.Clock().tick(60)  # Time rate
