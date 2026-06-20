import os
import sys

# --- ЖЕСТКИЕ СИСТЕМНЫЕ ФЛАГИ ДЛЯ БОРЬБЫ С КРАШЕМ МЬЮТЕКСА (FORTIFY) ---
# Заставляем SDL использовать стабильный буфер аудио-драйвера
os.environ['SDL_AUDIODRIVER'] = 'android'
# Отключаем внутреннюю фоновую потоковость звука SDL, которая и вызывает trylock на разрушенном mutex
os.environ['SDL_AUDIO_ALLOW_CHANNELS'] = '0'
# Включаем ловушку для корректного сворачивания
os.environ['SDL_ANDROID_TRAP_BACK_BUTTON'] = '1'
# ---------------------------------------------------------------------

import pygame

# Явно гасим аудиомикшер перед инициализацией, чтобы потоки не конфликтовали
pygame.mixer.pre_init(44100, -16, 2, 1024)

# Инициализируем только видео-систему СТРОГО ПЕРВОЙ
pygame.display.init()

# Ставим безопасные лимиты для буфера графики
pygame.display.gl_set_attribute(pygame.GL_DEPTH_SIZE, 16)
pygame.display.gl_set_attribute(pygame.GL_RED_SIZE, 8)
pygame.display.gl_set_attribute(pygame.GL_GREEN_SIZE, 8)
pygame.display.gl_set_attribute(pygame.GL_BLUE_SIZE, 8)

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# И только ПОСЛЕ создания окна безопасно запускаем всё остальное
pygame.init()

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
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
