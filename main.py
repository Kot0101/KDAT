from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

class IndustrialMenu(BoxLayout):
    def __init__(self, **kwargs):
        super(IndustrialMenu, self).__init__(**kwargs)
        # Задаем вертикальное расположение элементов
        self.orientation = 'vertical'
        self.padding = 50
        self.spacing = 20

        # Задний фон делаем темно-серым (корпоративный бункерный стиль)
        Window.clearcolor = get_color_from_hex('#141419')

        # Главный заголовок в стиле терминала
        self.title = Label(
            text="[ KDAT // SYSTEM_INIT ]",
            font_size='32sp',
            halign='center',
            markup=True,
            color=get_color_from_hex('#00A8FF') # Насыщенный синий неон
        )
        self.add_widget(self.title)

        # Подзаголовок состояния
        self.status = Label(
            text="STATUS: READY TO LAUNCH\nENVIRONMENT: ANDROID_OS",
            font_size='16sp',
            halign='center',
            color=get_color_from_hex('#7F8C8D') # Тусклый серый
        )
        self.add_widget(self.status)

        # Кастомная минималистичная кнопка
        self.btn = Button(
            text="ENGAGE SYSTEM",
            font_size='20sp',
            size_hint=(None, None),
            size=(300, 60),
            pos_hint={'center_x': 0.5},
            background_normal='', # Сбрасываем дефолтную текстуру Kivy
            background_color=get_color_from_hex('#002B49'), # Темно-синяя основа
            color=get_color_from_hex('#00A8FF') # Синий текст
        )
        
        # Привязываем нажатие к функции
        self.btn.bind(on_press=self.on_button_click)
        self.add_widget(self.btn)

    def on_button_click(self, instance):
        # Меняем текст при клике, чтобы проверить интерактивность
        self.title.text = "[ KDAT // RUNNING_SUCCESS ]"
        self.status.text = "CRITICAL ERROR BYPASSED\nWELCOME TO THE ZONE"
        self.btn.text = "ONLINE"
        self.btn.background_color = get_color_from_hex('#00A8FF')
        self.btn.color = get_color_from_hex('#141419')

class KDATApp(App):
    def build(self):
        self.title = "KDAT Terminal"
        return IndustrialMenu()

if __name__ == '__main__':
    KDATApp().run()
