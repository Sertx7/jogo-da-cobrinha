import pygame
import time
import random

# Inicialização do pygame
pygame.init()

# Cores personalizadas (tema preto e vermelho neon)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
NEON_GREEN = (57, 255, 20)
NEON_YELLOW = (255, 255, 0)
NEON_BLUE = (0, 255, 255)

# Tela
WIDTH = 600
HEIGHT = 400
dis = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('🐍 Cobrinha Neon')

# Fonte
score_font = pygame.font.SysFont("consolas", 35)
game_over_font = pygame.font.SysFont("consolas", 30)

# FPS
clock = pygame.time.Clock()

# Snake
BLOCK = 10
SPEED = 15

def show_score(score):
    value = score_font.render(f"Pontuação: {score}", True, NEON_GREEN)
    dis.blit(value, [10, 10])

def draw_snake(block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, NEON_GREEN, [x[0], x[1], block, block], border_radius=4)

def game_over_screen(score):
    dis.fill(BLACK)
    msg1 = game_over_font.render("Você perdeu! 😢", True, RED)
    msg2 = game_over_font.render("Pressione C para jogar novamente ou Q para sair.", True, NEON_BLUE)
    msg3 = game_over_font.render(f"Pontuação final: {score}", True, NEON_YELLOW)
    dis.blit(msg1, [WIDTH / 2 - msg1.get_width() / 2, HEIGHT / 3])
    dis.blit(msg2, [WIDTH / 2 - msg2.get_width() / 2, HEIGHT / 3 + 40])
    dis.blit(msg3, [WIDTH / 2 - msg3.get_width() / 2, HEIGHT / 3 + 80])
    pygame.display.update()

def game_loop():
    game_over = False
    game_close = False

    x = WIDTH // 2
    y = HEIGHT // 2
    dx = 0
    dy = 0

    snake = []
    length = 1

    food_x = round(random.randrange(0, WIDTH - BLOCK) / 10.0) * 10.0
    food_y = round(random.randrange(0, HEIGHT - BLOCK) / 10.0) * 10.0

    while not game_over:
        while game_close:
            game_over_screen(length - 1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -BLOCK
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = BLOCK
                    dy = 0
                elif event.key == pygame.K_UP:
                    dy = -BLOCK
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    dy = BLOCK
                    dx = 0

        # Atualiza posição
        x += dx
        y += dy

        # Verifica colisões com borda
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            game_close = True

        dis.fill(BLACK)
        pygame.draw.rect(dis, RED, [food_x, food_y, BLOCK, BLOCK], border_radius=4)

        snake_head = [x, y]
        snake.append(snake_head)

        if len(snake) > length:
            del snake[0]

        # Verifica colisão com o corpo
        for segment in snake[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(BLOCK, snake)
        show_score(length - 1)
        pygame.display.update()

        # Comeu a comida
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - BLOCK) / 10.0) * 10.0
            food_y = round(random.randrange(0, HEIGHT - BLOCK) / 10.0) * 10.0
            length += 1

        clock.tick(SPEED)

    pygame.quit()
    quit()

# Iniciar o jogo
game_loop()

