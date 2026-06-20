import os
import sys

# Полная блокировка аппаратных драйверов на уровне SDL2
os.environ['SDL_RENDER_DRIVER'] = 'software'
os.environ['SDL_VIDEO_GL_DRIVER'] = ''
os.environ['SDL_VIDEO_GLES_DRIVER'] = ''
Й
# Заставляем SDL2 не инициализировать 3D-контекст вообще
os.environ['SDL_VIDEO_EGL_ALLOW_EGLATTRS'] = '0'

import pygame

pygame.init()

# Фиксируем стандартное игровое разрешение
WIDTH, HEIGHT = 1280, 720

# Флаг SCALED создает программную прослойку, которая идеально подходит для эмуляторов
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED)
pygame.display.set_caption("KDAT")

clock = pygame.time.Clock()

cube_x = WIDTH // 2
cube_y = HEIGHT // 2
size = 100
speed = 10

dragging = False
IS_ANDROID = hasattr(sys, 'getandroidrequestcode')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # --- ОБРАБОТКА ТАЧА ---
        elif event.type == pygame.FINGERDOWN:
            dragging = True
            cube_x = int(event.dict.get('x', 0.5) * WIDTH)
            cube_y = int(event.dict.get('y', 0.5) * HEIGHT)

        elif event.type == pygame.FINGERUP:
            dragging = False

        elif event.type == pygame.FINGERMOTION:
            if dragging:
                cube_x = int(event.dict.get('x', 0.5) * WIDTH)
                cube_y = int(event.dict.get('y', 0.5) * HEIGHT)

        # --- ОБРАБОТКА МЫШКИ ---
        elif event.type == pygame.MOUSEBUTTONDOWN:
            dragging = True
            cube_x, cube_y = event.pos

        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False

        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                cube_x, cube_y = event.pos

    if not IS_ANDROID:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]: cube_x -= speed
        if keys[pygame.K_d]: cube_x += speed
        if keys[pygame.K_w]: cube_y -= speed
        if keys[pygame.K_s]: cube_y += speed

    cube_x = max(size // 2, min(cube_x, WIDTH - size // 2))
    cube_y = max(size // 2, min(cube_y, HEIGHT - size // 2))

    screen.fill((20, 20, 20))
    pygame.draw.rect(screen, (255, 0, 0), (cube_x - size // 2, cube_y - size // 2, size, size))
    
    # Для SCALED и software режима flip() теперь отработает корректно
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
