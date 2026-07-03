from kivy.uix.boxlayout import BoxLayout


class ListItem(BoxLayout):
    def __init__(self, total_cost: str, parts_cost: str, payment_type: str, percentage: str, root, **kwargs):
        super().__init__(**kwargs)
        self.root = root

        self.ids.total_cost.text = total_cost
        self.ids.total_cost.value = int(total_cost)

        self.ids.parts_cost.text = parts_cost
        self.ids.parts_cost.value = parts_cost

        self.ids.payment_type.text = payment_type

        self.ids.percentage.text = percentage

        self.ids.remove_button.bind(on_press=self.delete_self)

        self.total = 0
        if payment_type == 'БН':
            self.total = int(parts_cost) + (int(total_cost) - int(parts_cost)) * float(percentage)
        else:
            self.total = (-1) * (int(total_cost) - int(parts_cost)) * float(percentage)


    def delete_self(self, instance):
        # Родителем (parent) нашей строки является list_container (BoxLayout)
        if self.parent:
            self.root.reduce_cash(self.total)
            self.parent.remove_widget(self)
