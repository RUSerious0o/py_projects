from kivy.uix.screenmanager import Screen
from kivy.uix.togglebutton import ToggleButton


class InputForm(Screen):
    def send_data(self):
        main_screen = self.manager.get_screen('main_screen')

        total_cost = self.ids.total_cost_input.text if self.ids.total_cost_input.text else 0
        parts_cost = self.ids.parts_cost_input.text if self.ids.parts_cost_input.text else 0
        payment_type = self.__get_toggle_button_tag('payment_type')
        percentage = self.__get_toggle_button_tag('percentage')

        main_screen.add_line(total_cost, parts_cost, payment_type, percentage)

        self.manager.current = 'main_screen'

    def __get_toggle_button_tag(self, group_name: str):
        target_group = ToggleButton.get_widgets(group_name)
        for btn in target_group:
            if btn.state == 'down':
                return btn.tag
