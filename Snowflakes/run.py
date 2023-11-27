import pygame
import sys
import random
import math
from PIL import Image, ImageFilter

class Snowflake:
    def __init__(self, x, y,z,window):
        self.x = x
        self.y = y
        self.size = random.uniform(1, 3)
        self.view = random.randint(3, 30)
        self.blur_img = Image.open('./Snowflakes/img/snowflake-front.png').filter(ImageFilter.GaussianBlur(radius=self.view))
        self.img = pygame.image.fromstring(self.blur_img.tobytes("raw","RGBA"), self.blur_img.size, "RGBA").convert_alpha()
        self.texture = pygame.transform.scale(self.img, (20, 20))
        self.window = window

    def fall(self):
        self.y += self.size
        self.x += math.sin(self.y/90)     
        if self.y > self.window.height:
            self.y = 0
            self.x = random.randint(0, self.window.width)
            self.size = random.uniform(1, 3)
            self.color = random.randint(0, 2)

    def show(self):
        self.window.screen.blit(self.texture, (self.x, self.y))

class Window:
    def __init__(self):
        pygame.init()
        self.width = 1270
        self.height = 920
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        
        self.bg_img = pygame.transform.scale(pygame.image.load('./Snowflakes/img/forest-mountain-ridge-covered-with-snow-milky-way-starry-sky-christmas-winter-night.jpg'), (self.width, self.height))
        self.snowflakes_amount = 300
        self.snowflakes = self.create_snow_flakes()

        pygame.display.set_caption("Snowfall Screensaver")
        pygame.display.flip()
        self.game_loop()

    def create_snow_flakes(self):
        arr = []
        for _ in range(self.snowflakes_amount): # 60 30 10
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
            self.clock.tick(50)


if __name__ == "__main__":
    Window()
