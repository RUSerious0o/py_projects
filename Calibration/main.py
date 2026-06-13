from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, StringProperty, ListProperty
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.core.window import Window

Window.size = (800, 600)


class SbaTracker(BoxLayout):
    hits = NumericProperty(0)
    misses = NumericProperty(0)
    target = NumericProperty(30)
    chosen_percent = NumericProperty(50)

    percent_text = StringProperty("50%")
    hits_text = StringProperty("Попадания: 0")
    target_text = StringProperty("Цель: 30")
    misses_text = StringProperty("Промахи: 0")
    culdone_text = StringProperty("Сбросить счёт")
    current_score_text = StringProperty("Текущий счёт:\n0%")
    score_color = ListProperty([1, 0.65, 0, 1])

    def __init__(self, **kwargs):
        super(SbaTracker, self).__init__(**kwargs)
        self.dropdown = DropDown()
        options = [50, 60, 70, 80, 90]
        for option in options:
            btn = Button(text=f"{option}%", size_hint_y=None, height=50)
            btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
            self.dropdown.add_widget(btn)
        self.dropdown.bind(on_select=self.on_dropdown_select)

    def open_dropdown(self, widget):
        self.dropdown.open(widget)

    def on_dropdown_select(self, instance, data):
        self.percent_text = data
        self.chosen_percent = int(data.replace('%', ''))
        self.update_all_stats()

    def add_hit(self):
        self.hits += 1
        self.update_all_stats()

    def culdone(self):
        self.hits = 0
        self.misses = 0
        self.update_all_stats()

    def add_miss(self):
        self.misses += 1
        self.update_all_stats()

    def update_all_stats(self):
        total = self.hits + self.misses

        if total > 0:
            real_pct = int((self.hits / total) * 100)
        else:
            real_pct = 0

        divider = 10 - (self.chosen_percent // 10)
        step = self.chosen_percent // 10
        if divider != 0:
            self.target = 30 + ((self.misses // divider) * step)
        else:
            self.target = 30

        if self.hits >= self.target and total > 0:
            self.current_score_text = f"ГОТОВО!\n{real_pct}%"
            self.score_color = [0, 1, 0, 1]
        else:
            self.current_score_text = f"Текущий счёт:\n{real_pct}%"
            self.score_color = [1, 0.65, 0, 1]

        self.hits_text = f"Попадания: {self.hits}"
        self.target_text = f"Цель: {self.target}"
        self.misses_text = f"Промахи: {self.misses}"


class SbaApp(App):
    def build(self):
        return SbaTracker()


if __name__ == '__main__':
    SbaApp().run()