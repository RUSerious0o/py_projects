from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from widgets.main_screen import MainScreen


class PriceApp(App):
    def build(self):
        manager = ScreenManager()
        manager.add_widget(MainScreen())

        return manager


if __name__ == '__main__':
    PriceApp().run()
