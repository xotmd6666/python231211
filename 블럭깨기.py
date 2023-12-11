import pygame
import sys
import random

# 초기화
pygame.init()

# 화면 크기
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("블럭깨기 게임")

# 색깔
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 패들
paddle_width, paddle_height = 100, 10
paddle_x = (WIDTH - paddle_width) // 2
paddle_y = HEIGHT - 20

# 공
ball_radius = 10
ball_x = WIDTH // 2
ball_y = HEIGHT - 30
ball_speed_x = 5
ball_speed_y = -5

# 블록
block_width, block_height = 80, 20
blocks = []

def create_blocks():
    for row in range(5):
        for col in range(10):
            block = pygame.Rect(col * (block_width + 5), row * (block_height + 5), block_width, block_height)
            blocks.append(block)

create_blocks()

# 게임 루프
clock = pygame.time.Clock()  # Clock 객체 생성
FPS = 30  # 원하는 프레임 속도

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= 5
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
        paddle_x += 5

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # 벽과 충돌
    if ball_x <= 0 or ball_x >= WIDTH:
        ball_speed_x = -ball_speed_x
    if ball_y <= 0:
        ball_speed_y = -ball_speed_y

    # 패들과 충돌
    if ball_y >= paddle_y - ball_radius and paddle_x <= ball_x <= paddle_x + paddle_width:
        ball_speed_y = -ball_speed_y

    # 블록과 충돌
    for block in blocks:
        if block.colliderect(pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, 2 * ball_radius, 2 * ball_radius)):
            blocks.remove(block)
            ball_speed_y = -ball_speed_y

    # 그리기
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, RED, (int(ball_x), int(ball_y)), ball_radius)

    for block in blocks:
        pygame.draw.rect(screen, WHITE, block)

    pygame.display.flip()

    # 초당 프레임 수 제어
    clock.tick(FPS)
