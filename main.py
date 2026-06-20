import sys
import pygame
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.graphicsimage import GraphicsImage
from kivy.graphics.texture import Texture

# Разрешение твоей игры
WIDTH, HEIGHT = 1280, 720

class GameContainer(GraphicsImage):
    def __init__(self, **kwargs):
        super(GameContainer, self).__init__(**kwargs)
        
        # 1. Инициализируем Pygame внутри Kivy
        pygame.init()
        
        # 2. Создаем виртуальный холст в памяти (вместо display.set_mode)
        self.screen = pygame.Surface((WIDTH, HEIGHT))
        
        # 3. Настройки твоей игры (СЮДА ПЕРЕНОСИ ВСЕ СВОИ ПЕРЕМЕННЫЕ)
        self.cube_x = WIDTH // 2
        self.cube_y = HEIGHT // 2
        self.size = 100
        self.dragging = False

        # Создаем текстуру для вывода картинки
        self.kivy_texture = Texture.create(size=(WIDTH, HEIGHT), colorfmt='rgb')
        self.texture = self.kivy_texture

        # Запускаем игровой цикл на 60 FPS
        Clock.schedule_interval(self.update_game, 1.0 / 60.0)

    def update_game(self, dt):
        # ---------------------------------------------------------
        # ТВОЙ ИГРОВОЙ ЦИКЛ (Всё, что шло после while running:)
        # Вместо screen.fill пиши self.screen.fill и т.д.
        # ---------------------------------------------------------
        self.screen.fill((20, 20, 20))
        pygame.draw.rect(self.screen, (255, 0, 0), (self.cube_x - self.size // 2, self.cube_y - self.size // 2, self.size, self.size))
        # ---------------------------------------------------------

        # Обновляем картинку на экране смартфона
        self.kivy_texture.blit_buffer(self.screen.get_buffer(), colorfmt='rgb', bufferfmt='ubyte', flipped=True)
        self.canvas.ask_update()

    # Считывание тачей через Kivy (переводим в координаты Pygame)
    def on_touch_down(self, touch):
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
        return GameContainer()

if __name__ == '__main__':
    KDATApp().run()
