import sys
# Заставляем Pygame думать, что у нас нет экрана и звука (Dummy-режим рендеринга в память)
import os
os.environ["SDL_VIDEODRIVER"] = "dummy"
os.environ["SDL_AUDIODRIVER"] = "dummy"

import pygame
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.image import Image # Используем стандартный Image вместо косячного GraphicsImage
from kivy.graphics.texture import Texture

WIDTH, HEIGHT = 1280, 720

class GameScreen(Image):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        
        # Инициализируем Pygame программно в памяти
        pygame.init()
        self.pg_surface = pygame.Surface((WIDTH, HEIGHT))
        
        # Логика игры
        self.cube_x = WIDTH // 2
        self.cube_y = HEIGHT // 2
        self.size = 120
        self.dragging = False

        # Создаем пустую текстуру Kivy
        self.kivy_texture = Texture.create(size=(WIDTH, HEIGHT), colorfmt='rgb')
        self.texture = self.kivy_texture

        # Игровой цикл на 60 FPS
        Clock.schedule_interval(self.update_frame, 1.0 / 60.0)

    def update_frame(self, dt):
        # Логика границ
        self.cube_x = max(self.size // 2, min(self.cube_x, WIDTH - self.size // 2))
        self.cube_y = max(self.size // 2, min(self.cube_y, HEIGHT - self.size // 2))

        # РИСУЕМ НАШ ЛЮБИМЫЙ КВАДРАТ ЧЕРЕЗ PYGAME
        self.pg_surface.fill((20, 20, 20))
        pygame.draw.rect(
            self.pg_surface, 
            (255, 0, 0), 
            (self.cube_x - self.size // 2, self.cube_y - self.size // 2, self.size, self.size)
        )

        # Вытаскиваем сырые пиксели из Pygame и отдаем их в Kivy-текстуру
        raw_pixels = self.pg_surface.get_buffer().raw
        self.kivy_texture.blit_buffer(raw_pixels, colorfmt='rgb', bufferfmt='ubyte', flipped=True)
        
        # Принудительно обновляем экран
        self.texture_update()

    # Тачи через Kivy
    def on_touch_down(self, touch):
        if not self.collide_point(*touch.pos): return False
        self.dragging = True
        self.cube_x = int((touch.x / self.width) * WIDTH)
        self.cube_y = int(((self.height - touch.y) / self.height) * HEIGHT)
        return True

    def on_touch_move(self, touch):
        if self.dragging:
            self.cube_x = int((touch.x / self.width) * WIDTH)
            self.cube_y = int(((self.height - touch.y) / self.height) * HEIGHT)
        return True

    def on_touch_up(self, touch):
        self.dragging = False
        return True

class KDATApp(App):
    def build(self):
        return GameScreen()

if __name__ == '__main__':
    KDATApp().run()
