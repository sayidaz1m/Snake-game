import pygame, random, pygame_menu
from sys import exit

pygame.font.init()
pygame.init()

pygame.mixer.init()
pygame.mixer.music.load('sounds/background.wav')
pygame.mixer.music.play(-1)

eat_sound = pygame.mixer.Sound('sounds/eat.wav')
death_sound = pygame.mixer.Sound("sounds/death.wav")

screen = pygame.display.set_mode((860, 640))
pygame.display.set_caption("SNAKE GAME")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

cell = 20
direction = None
cols = 860 // cell
rows = 640 // cell
score = 0

# Initial snake setup
snake = [
    pygame.Rect(100, 100, cell, cell),
    pygame.Rect(80, 100, cell, cell),
    pygame.Rect(60, 100, cell, cell)
]

# Menu in progress 2
def menu_start_game():
    pass

    menu = pygame_menu.Menu('Welcome', 400, 300,
                       theme=pygame_menu.themes.THEME_BLUE)

# Function to generate random position for apple
def random_pos():
    return pygame.Rect(random.randrange(cols)*cell, random.randrange(rows)*cell, cell, cell)
apple = random_pos()

# Main game loop
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

# Move snake
    head = snake[0].copy()
    if direction == 'up': head.y -= cell
    if direction == 'down': head.y += cell
    if direction == 'left': head.x -= cell
    if direction == 'right': head.x += cell

# Wrap around screen
    if head.x < 0: head.x = 860 - cell
    if head.x >= 860: head.x = 0
    if head.y < 0: head.y = 640 - cell
    if head.y >= 640: head.y = 0

# Update snake
    snake.insert(0, head)
    if snake[0].colliderect(apple):
        apple = random_pos()
        score += 1  
        eat_sound.play()
    else:
        snake.pop()

# Check self-collision
    if direction and len(snake) > 3:
        if any(snake[0].colliderect(seg) for seg in snake[1:]):
            death_sound.play()
            pygame.time.delay(1000)
            pygame.quit(); 
            exit()

# Draw everything
    screen.fill("black")
    pygame.draw.rect(screen, "red", apple)
    for block in snake:
        pygame.draw.rect(screen, "green", block)

    score_text = font.render(f"Score: {score}", True, (255,255,255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(10)