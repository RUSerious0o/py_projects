from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty

from widgets.list_item import ListItem

from datetime import  datetime

class MainScreen(Screen):
    total_cash = NumericProperty(0)

    def add_line(self, total_cost: str, parts_cost: str, payment_type: str, percentage: str):
        list_item = ListItem(str(total_cost), str(parts_cost), payment_type, percentage, self)
        self.ids.data_container.add_widget(list_item)
        self.total_cash += int(list_item.total)

    def reduce_cash(self, value):
        self.total_cash -= value

    def save_report(self):
        filename = f'{datetime.now().strftime("%Y-%m-%d")}.txt'
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f'{self.total_cash:+}\n')
            for widget in self.ids.data_container.children:
                value = (f'{widget.total:+8} '
                         f'S: {int(widget.ids.total_cost.text): 8} '
                         f'Д: {int(widget.ids.parts_cost.text): 8} '
                         f'Тип: {widget.ids.payment_type.text:2} '
                         f'%: {widget.ids.percentage.text}\n')
                file.write(value)
