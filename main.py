import pygame, random
from sys import exit

pygame.init()
screen = pygame.display.set_mode((860, 640))
pygame.display.set_caption("SNAKE GAME")
clock = pygame.time.Clock()



cell = 20
direction = None
cols = 860 // cell
rows = 640 // cell

snake = [
    pygame.Rect(100, 100, cell, cell),
    pygame.Rect(80, 100, cell, cell),
    pygame.Rect(60, 100, cell, cell)
]


def random_pos():
    return pygame.Rect(random.randrange(cols)*cell, random.randrange(rows)*cell, cell, cell)

apple = random_pos()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and direction != 'down': direction = 'up'
            if event.key == pygame.K_s and direction != 'up': direction = 'down'
            if event.key == pygame.K_a and direction != 'right': direction = 'left'
            if event.key == pygame.K_d and direction != 'left': direction = 'right'


    head = snake[0].copy()
    if direction == 'up': head.y -= cell
    if direction == 'down': head.y += cell
    if direction == 'left': head.x -= cell
    if direction == 'right': head.x += cell

    if head.x < 0: head.x = 860 - cell
    if head.x >= 860: head.x = 0
    if head.y < 0: head.y = 640 - cell
    if head.y >= 640: head.y = 0

    snake.insert(0, head)
    if snake[0].colliderect(apple):
        apple = random_pos()
    else:
        snake.pop()


    if direction and len(snake) > 3:
        if any(snake[0].colliderect(seg) for seg in snake[1:]):
            pygame.quit(); exit()


    screen.fill("black")
    pygame.draw.rect(screen, "blue", apple)
    for block in snake:
        pygame.draw.rect(screen, "green", block)


    pygame.display.update()
    clock.tick(10)
    #111