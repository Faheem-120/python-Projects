import pygame
import random

# Game constants
WIDTH = 640
HEIGHT = 480
CELL_SIZE = 20
FPS = 10

# Color constants
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class SnakeGame:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.font = pygame.font.Font(None, 36)

        self.snake = [(2, 1), (1, 1)]
        self.direction = "Right"
        self.food = self.create_food()
        self.score = 0

    def create_food(self):
        while True:
            x = random.randint(0, WIDTH // CELL_SIZE - 1)
            y = random.randint(0, HEIGHT // CELL_SIZE - 1)
            if (x, y) not in self.snake:
                return x, y

    def draw_cell(self, x, y, color):
        pygame.draw.rect(self.screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def draw_snake(self):
        for segment in self.snake:
            x, y = segment
            self.draw_cell(x, y, GREEN)

    def draw_food(self):
        x, y = self.food
        self.draw_cell(x, y, RED)

    def update_score(self):
        score_text = self.font.render("Score: {}".format(self.score), True, GREEN)
        self.screen.blit(score_text, (10, 10))

    def check_collision(self):
        head = self.snake[0]
        x, y = head
        # Check if the snake hits the wall
        if x < 0 or x >= WIDTH // CELL_SIZE or y < 0 or y >= HEIGHT // CELL_SIZE:
            return True
        # Check if the snake hits itself
        if head in self.snake[1:]:
            return True
        return False

    def move_snake(self):
        dx, dy = 0, 0
        if self.direction == "Up":
            dy = -1
        elif self.direction == "Down":
            dy = 1
        elif self.direction == "Left":
            dx = -1
        elif self.direction == "Right":
            dx = 1

        head = self.snake[0]
        x = (head[0] + dx) % (WIDTH // CELL_SIZE)
        y = (head[1] + dy) % (HEIGHT // CELL_SIZE)
        new_head = (x, y)

        if new_head == self.food:
            self.score += 1
            self.snake.insert(0, new_head)
            self.food = self.create_food()
        else:
            self.snake.insert(0, new_head)
            self.snake.pop()

    def game_over(self):
        self.screen.fill(BLACK)
        game_over_text = self.font.render("Game Over!", True, GREEN)
        self.screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(2000)

    def play_game(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.direction != "Down":
                        self.direction = "Up"
                    elif event.key == pygame.K_DOWN and self.direction != "Up":
                        self.direction = "Down"
                    elif event.key == pygame.K_LEFT and self.direction != "Right":
                        self.direction = "Left"
                    elif event.key == pygame.K_RIGHT and self.direction != "Left":
                        self.direction = "Right"

            self.move_snake()

            if self.check_collision():
                self.game_over()
                running = False

            self.screen.fill(BLACK)
            self.draw_snake()
            self.draw_food()
            self.update_score()
            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()


# Create and run the game
game = SnakeGame()
game.play_game()
