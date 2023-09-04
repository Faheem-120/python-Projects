import pygame
import random

pygame.init()

# Window dimensions
WIDTH = 400
HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Bird dimensions
BIRD_WIDTH = 50
BIRD_HEIGHT = 35

# Pipe dimensions
PIPE_WIDTH = 70
PIPE_HEIGHT = random.randint(100, 400)
PIPE_GAP = 150

# Bird initial position
bird_x = 100
bird_y = HEIGHT // 2

# Bird velocity
bird_dy = 0

# Game over flag
game_over = False

# Initialize the window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load images
bird_img = pygame.image.load("bird.png")
bird_img = pygame.transform.scale(bird_img, (BIRD_WIDTH, BIRD_HEIGHT))

pipe_img = pygame.image.load("pipe.png")
pipe_img = pygame.transform.scale(pipe_img, (PIPE_WIDTH, PIPE_HEIGHT))

pipe_top_img = pygame.transform.flip(pipe_img, False, True)
pipe_top_height = HEIGHT - PIPE_HEIGHT - PIPE_GAP

# Game loop
clock = pygame.time.Clock()

while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_dy = -7

    # Move the bird
    bird_y += bird_dy
    bird_dy += 0.5

    # Draw the window
    window.fill(WHITE)

    window.blit(bird_img, (bird_x, bird_y))

    pipe_rect = pygame.Rect(WIDTH // 2, 0, PIPE_WIDTH, PIPE_HEIGHT)
    window.blit(pipe_img, pipe_rect)

    pipe_top_rect = pygame.Rect(WIDTH // 2, HEIGHT - pipe_top_height, PIPE_WIDTH, pipe_top_height)
    window.blit(pipe_top_img, pipe_top_rect)

    # Check collision
    bird_rect = pygame.Rect(bird_x, bird_y, BIRD_WIDTH, BIRD_HEIGHT)
    if bird_rect.colliderect(pipe_rect) or bird_rect.colliderect(pipe_top_rect) or bird_y > HEIGHT:
        game_over = True

    # Update the display
    pygame.display.update()
    clock.tick(60)

pygame.quit()
