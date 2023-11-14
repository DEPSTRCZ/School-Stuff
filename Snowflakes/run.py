import pygame
import sys
import random
import math






class Snowflake:
    def __init__(self, x, y,game):
        self.x = x
        self.y = y
        self.size = random.randint(1, 3)
        self.wind = random.randint(-1,1)
        self.color = random.randint(0, 2)
        self.game = game

    def fall(self):
        self.y += self.size
        if self.wind == -1:
            self.x += math.sin(self.y/90)
        elif self.wind == 1:
            self.x += math.cos(self.y/90)           
        if self.y > self.game.height:
            self.y = 0
            self.x = random.randint(0, self.game.width)
            self.size = random.randint(1, 3)
            self.wind = random.randint(-1,1)
            self.color = random.randint(0, 2)

    def draw(self):
        pygame.draw.circle(self.game.screen, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (self.x, self.y), self.size)

class game:
    def __init__(self):
        pygame.init()
        self.white = ((220, 220, 220),(160,160,180),(100, 100, 120))
        self.width = 1920
        self.height = 1080
        self.snowflakes_amount = 16000
        self.snowflakes = self.create_snow_flakes()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snowfall Screensaver")
        pygame.display.flip()
        self.game_loop()

    def create_snow_flakes(self):
        arr = []
        for _ in range(self.snowflakes_amount):
           arr.append(Snowflake(random.randint(0, self.width), random.randint(0, self.height),self))
        return arr
    
    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))  

            for snowflake in self.snowflakes:
                snowflake.fall()
                snowflake.draw()
        
            pygame.display.flip()
        #    pygame.time.Clock().tick(120)  


if __name__ == "__main__":
    game()
