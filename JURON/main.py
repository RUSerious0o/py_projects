# СТРОГО ПЕРВЫМИ СТРОКАМИ В ФАЙЛЕ:
from kivy.config import Config

Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 800)

from kivy.app import App
from widgets.donut_chart import DonutChart


class JuronApp(App):
    pass


if __name__ == '__main__':
    JuronApp().run()
