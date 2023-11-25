import pygame
import sys
import random
import math
from PIL import Image, ImageFilter

class Snowflake:
    def __init__(self, x, y,window):
        self.x = x
        self.y = y
        self.size = random.uniform(0.3, 1)
        self.view = random.randint(3, 30)
        self.blur_img = Image.open('./Snowflakes/img/snowflake-front.png').filter(ImageFilter.GaussianBlur(radius=self.view))
        self.texture = pygame.transform.scale(pygame.image.fromstring(self.blur_img.tobytes("raw","RGBA"), self.blur_img.size, "RGBA"), (20, 20))
        self.window = window

    def fall(self):
        self.y += self.size
        self.x += math.sin(self.y/90)     
        if self.y > self.window.height:
            self.y = 0
            self.x = random.randint(0, self.window.width)
            self.size = random.randint(1, 3)
            self.color = random.randint(0, 2)

    def show(self):
        self.window.screen.blit(self.texture, (self.x, self.y))
        #pygame.draw.circle(self.window.screen, self.window.white[self.view], (self.x, self.y), self.size)

class Window:
    def __init__(self):
        pygame.init()
        self.white = ((220, 220, 220),(160,160,180),(100, 100, 120))
        self.width = 1270
        self.height = 920
        self.bg_img = pygame.transform.scale(pygame.image.load('./Snowflakes/img/forest-mountain-ridge-covered-with-snow-milky-way-starry-sky-christmas-winter-night.jpg'), (self.width, self.height))
        self.snowflakes_amount = 300
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

            self.screen.blit(self.bg_img, self.bg_img.get_rect())

            for snowflake in self.snowflakes:
                snowflake.fall()
                snowflake.show()
        
            pygame.display.flip()
            pygame.time.Clock().tick(60)


if __name__ == "__main__":
    Window()
