from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ToggleButtonBehavior


class ListItem(ToggleButtonBehavior, BoxLayout):
    def __init__(self, root=None, description: str = 'item', price: int = 0, **kwargs):
        super().__init__(**kwargs)
        self.ids.description_label.text = description
        self.ids.price_label.text = str(price)
        self.root = root

    def on_release(self):
        super().on_release()
        if self.state == 'down':
            self.root.change_sum(int(self.ids.price_label.text))
        else:
            self.root.change_sum(-int(self.ids.price_label.text))
