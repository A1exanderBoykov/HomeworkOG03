import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/2.jpg")
pygame.display.set_icon(icon)

background_image = pygame.image.load("img/3.jpg")

background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

target_image = pygame.image.load("img/1.png.png")
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

target_speed_x = 0.2
target_speed_y = 0.2

score = 0

font = pygame.font.Font(None, 44)

running = True
while running:
    screen.blit(background_image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                score += 1  


    target_x += target_speed_x
    target_y += target_speed_y



    if target_x <= 0 or target_x + target_width >= SCREEN_WIDTH:
        target_speed_x = -target_speed_x
    if target_y <= 0 or target_y + target_height >= SCREEN_HEIGHT:
        target_speed_y = -target_speed_y


    screen.blit(target_image, (target_x, target_y))

    score_text = font.render(f"Score: {score}", True, (70, 150, 135))
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
