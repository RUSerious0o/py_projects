# СТРОГО ПЕРВЫМИ СТРОКАМИ В ФАЙЛЕ:
from kivy.config import Config

Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 800)

# Код приложения
from kivy.app import App
from widgets.main_screen import MainScreen


class JuronApp(App):
    pass


if __name__ == '__main__':
    JuronApp().run()
