import pygame,sys,random
from pygame.math import Vector2

class FRUIT:
    def __init__(self):
        self.x = random.randint(0,cell_number - 1)
        self.y = random.randint(0,cell_number -1)
        self.pos = Vector2(self.x,self.y)
        
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * cell_size,self.pos.y * cell_size,cell_size,cell_size)
        screen.blit(apple,fruit_rect)


cell_size = 30
cell_number = 20

screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
clock = pygame.time.Clock()


fruit = FRUIT()
apple = pygame.image.load('Graphics/apple.png').convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

          
    screen.fill((175,215,70))
    fruit.draw_fruit() 
    pygame.display.update()
    clock.tick(60)