import pygame
import sys
import random
import math
import threading
from PIL import Image, ImageFilter, ImageEnhance

class Snowflake:
    def __init__(self, x, y,z,window):
        self.window = window
        self.x = x
        self.y = y
        self.size = random.uniform(0, 3)
        self.view = [0,15,30]
        self.view_bright = [0.9,0.688,0.3999]
        self.wind = random.randint(-1,1)
        self.snowflake_size = random.randint(5,20)

        enhanced_img = self.window.img.filter(ImageFilter.GaussianBlur(radius=self.view[z]))
        enhanced_img = ImageEnhance.Brightness(enhanced_img).enhance(self.view_bright[z])

        # Convert the enhanced image to a pygame surface
        self.texture = pygame.image.fromstring(enhanced_img.tobytes("raw", "RGBA"), enhanced_img.size, "RGBA").convert_alpha()
        self.texture = pygame.transform.scale(self.texture, (self.snowflake_size, self.snowflake_size))


    def fall(self):
        self.y += self.size
        if self.wind == -1:
            self.x += math.sin(self.y/90)
        elif self.wind == 1:
            self.x += math.cos(self.y/90)
        elif self.y > self.window.height-100:
            img = self.window.img.convert("RGBA")
            enhanced_img = img.putalpha(127) # This creates a new image object
            enhanced_img = enhanced_img.tobytes("raw", "RGBA") # Use the new image object here
            self.texture = pygame.image.fromstring(enhanced_img, enhanced_img.size, "RGBA").convert_alpha()
            self.texture = pygame.transform.scale(self.texture, (self.snowflake_size, self.snowflake_size))

        if self.y > self.window.height:
            self.y = -10
            self.x = random.randint(0, self.window.width)
            self.size = random.uniform(1, 3)
    def show(self):
        self.window.screen.blit(self.texture, (self.x, self.y))

class Window:
    def __init__(self):
        pygame.init()
        self.width = 1270
        self.height = 820
        self.img = Image.open('./Snowflakes/img/snowflake.png').convert("RGBA")
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.temp = 0
        
        self.bg_img = pygame.transform.scale(pygame.image.load('./Snowflakes/img/forest-mountain-ridge-covered-with-snow-milky-way-starry-sky-christmas-winter-night.jpg'), (self.width, self.height))
        self.snowflakes_amount = 1000
        pygame.display.set_caption("Snowfall - !!!LOADING!!!")
        self.snowflakes = self.create_snow_flakes()

        pygame.display.set_caption("Snowfall Screensaver")
        pygame.display.flip()
        self.game_loop()


    def create_snow_flakes(self):
            arr = []
            zview = [math.floor(self.snowflakes_amount / 100) * 20, math.floor(self.snowflakes_amount / 100) * 35,
                math.floor(self.snowflakes_amount / 100) * 45]

            def create_snowflake_batch(amount, z_index):
                for _ in range(amount):
                    arr.append(Snowflake(random.randint(0, self.width), random.randint(0, self.height), z_index, self))
                    self.temp += 1
                    print(f"Generating snowflakes: {(self.temp / self.snowflakes_amount) * 100:.2f}%")
            threads = []

            for index, amount in enumerate(zview):
                thread = threading.Thread(target=create_snowflake_batch, args=(amount, index))
                threads.append(thread)
                thread.start()

            for thread in threads:
                thread.join()

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

