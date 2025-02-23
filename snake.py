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
        
class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)
        
    def draw_snake(self):
        for block in self.body:
            snake_rect = pygame.Rect(block.x * cell_size,block.y * cell_size,cell_size,cell_size)
            pygame.draw.rect(screen,(102,178,255),snake_rect)
    
    def move_snake(self):
        self.body.insert(0,self.body[0] + self.direction)
        del self.body[-1]
        
        


cell_size = 30
cell_number = 20

screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
clock = pygame.time.Clock()


fruit = FRUIT()
snake = SNAKE()
apple = pygame.image.load('Graphics/apple.png').convert_alpha()
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            snake.move_snake()
        
        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_UP:
               snake.direction = Vector2(0,-1)
           elif event.key == pygame.K_DOWN:
               snake.direction = Vector2(0,1)
           elif event.key == pygame.K_RIGHT:
               snake.direction = Vector2(1,0)
           elif event.key == pygame.K_LEFT:
               snake.direction = Vector2(-1,0)
            

          
    screen.fill((175,215,70))
    fruit.draw_fruit()
    snake.draw_snake()
    pygame.display.update()
    clock.tick(60)