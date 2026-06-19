import pygame
import random
import time
pygame.init()

screen_width = 900
screen_height = 700

screen = pygame.display.set_mode((screen_width, screen_height))

def change_bg(img):
    bg = pygame.image.load(img)
    bg = pygame.transform.scale(bg, (screen_width, screen_height))
    screen.blit(bg, (0,0))

class Bin(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("bin.png")
        self.image = pygame.transform.scale(self.image, (40,60))
        self.rect = self.image.get_rect()
    
class Non_recyclable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("plastic.png")
        self.image = pygame.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect()

class Recyclable(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect()

item_list = pygame.sprite.Group()
plastic_list = pygame.sprite.Group()
allsprites = pygame.sprite.Group()

bin = Bin()

allsprites.add(bin)
for i in range(20):
    plastic = Non_recyclable()
    plastic.rect.x = random.randrange(screen_width)
    plastic.rect.y = random.randrange(screen_height)
    plastic_list.add(plastic)
    allsprites.add(plastic)

images = ["item1.png","item2.png","item3.png"]
for i in range(50):
    item = Recyclable(random.choice(images))
    item.rect.x = random.randrange(screen_width)
    item.rect.y = random.randrange(screen_height)
    item_list.add(item)
    allsprites.add(item)

WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)
GREEN = (0,255,0)

playing = True
score = 0

clock = pygame.time.Clock()
start_time = time()

myFont = pygame.font.SysFont("Times New Roman", 22)
text = myFont.render("Score =" + str(0), True, BLACK)

while playing:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        