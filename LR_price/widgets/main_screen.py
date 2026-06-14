from kivy.uix.screenmanager import Screen

from kivy.uix.label import Label
from kivy.uix.button import Button

from widgets.list_item import ListItem
from data import data

class MainScreen(Screen):
    __section_ids = ['preps_section', 'cleanse_section', 'refill_section', 'water_drain_section', 'other_section']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for section, values in data.items():
            for line in values:
                list_item = ListItem(root=self, description=line['name'], price=line['value'])
                self.ids[section].ids['content'].add_widget(list_item)
                self.ids[section].ids['content'].height += list_item.height
                self.ids[section].height += list_item.height

    def change_sum(self, diff):
        self.ids.sum_label.sum_ += diff
        self.ids.sum_label.text = f'Итого: {self.ids.sum_label.sum_}'

    def reset_selection(self):
        for section in self.__section_ids:
            for widget in self.ids[section].ids['content'].children:
                if widget.state == 'down':
                    widget.state = 'normal'
                    widget.on_release()
