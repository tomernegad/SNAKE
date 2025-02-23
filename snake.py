import pygame,sys

cell_size = 30
cell_number = 20

screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()