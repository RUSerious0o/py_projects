from kivy.uix.screenmanager import Screen

from kivy.uix.label import Label
from kivy.uix.button import Button

from widgets.list_item import ListItem


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ids.preparation_items.add_widget(ListItem(root=self, description='LALA', price=50))
        self.ids.preparation_items.add_widget(ListItem(root=self, description='ULALA', price=1120))

    def change_sum(self, diff):
        self.ids.sum_label.sum_ += diff
        self.ids.sum_label.text = f'Итого: {self.ids.sum_label.sum_}'
