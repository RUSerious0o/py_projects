from kivymd.app import MDApp

from widgets.main_screen import MainScreen


class PlannerApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        # self.theme_cls.primary_palette = 'Blue'
        return MainScreen()


if __name__ == '__main__':
    PlannerApp().run()
