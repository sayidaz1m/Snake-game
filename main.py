
# main screen 
import pygame, sys
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit(); sys.exit()
    screen.fill((20,20,20))
    pygame.display.flip()
    clock.tick(60)
    