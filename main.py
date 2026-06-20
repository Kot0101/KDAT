import sys
import pygame
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.graphicsimage import GraphicsImage
from kivy.graphics.texture import Texture

# Разрешение твоей игры
WIDTH, HEIGHT = 1280, 720

class PygameRenderer(GraphicsImage):
    def __init__(self, **kwargs):
        super(PygameRenderer, self).__init__(**kwargs)
        
        # 1. Инициализируем Pygame внутри Kivy
        pygame.init()
        
        # 2. Создаем виртуальный холст в памяти (вместо display.set_mode)
        self.screen = pygame.Surface((WIDTH, HEIGHT))
        
        # 3. Твои переменные игры
        self.cube_x = WIDTH // 2
        self.cube_y = HEIGHT // 2
        self.size = 100
        self.dragging = False

        # Создаем текстуру Kivy для вывода картинки Pygame
        self.kivy_texture = Texture.create(size=(WIDTH, HEIGHT), colorfmt='rgb')
        self.texture = self.kivy_texture

        # Запускаем игровой цикл на 60 FPS через Kivy Clock
        Clock.schedule_interval(self.update_game, 1.0 / 60.0)

    def update_game(self, dt):
        # ---------------------------------------------------------
        # ТВОЙ ИГРОВОЙ КОД (Всё, что было после while running:)
        # Заменяй screen на self.screen
        # ---------------------------------------------------------
        self.cube_x = max(self.size // 2, min(self.cube_x, WIDTH - self.size // 2))
        self.cube_y = max(self.size // 2, min(self.cube_y, HEIGHT - self.size // 2))

        # Отрисовка
        self.screen.fill((20, 20, 20))
        pygame.draw.rect(
            self.screen, 
            (255, 0, 0), 
            (self.cube_x - self.size // 2, self.cube_y - self.size // 2, self.size, self.size)
        )
        # ---------------------------------------------------------

        # 4. Обновляем картинку на экране: быстро перекидываем пиксели из Pygame холста в текстуру Kivy
        # Переворачиваем Y координаты (flipped=True)
        self.kivy_texture.blit_buffer(self.screen.get_buffer(), colorfmt='rgb', bufferfmt='ubyte', flipped=True)
        self.canvas.ask_update()

    # --- Считывание тачей через Kivy (переводим в координаты Pygame) ---
    def on_touch_down(self, touch):
        # Ограничиваем считывание тачей только на нашем Game view
        if not self.collide_point(*touch.pos): return False
        x = int((touch.x / self.width) * WIDTH)
        y = int(((self.height - touch.y) / self.height) * HEIGHT)
        self.dragging = True
        self.cube_x, self.cube_y = x, y
        return True

    def on_touch_move(self, touch):
        if self.dragging:
            x = int((touch.x / self.width) * WIDTH)
            y = int(((self.height - touch.y) / self.height) * HEIGHT)
            self.cube_x, self.cube_y = x, y
        return True

    def on_touch_up(self, touch):
        self.dragging = False
        return True

class KDATApp(App):
    def build(self):
        # Сразу возвращаем наш рендерер, KivyActivity его подхватит
        return PygameRenderer()

if __name__ == '__main__':
    KDATApp().run()
