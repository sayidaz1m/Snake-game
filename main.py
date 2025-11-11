import pygame 
from sys import exit 

pygame.init()
pygame.display.set_caption("SNAKE GAME")
clock = pygame.time.Clock()

test_surface = pygame.Surface((100, 200))
test_surface.fill('blue')

# screen creating
screen = pygame.display.set_mode((860, 640))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(test_surface,(0,0))        

    pygame.display.update()
    clock.tick(60)