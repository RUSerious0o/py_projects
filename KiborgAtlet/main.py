from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from datetime import datetime


class InputPopup(Popup):
    pass


class ChangeRecordDialog(Popup):
    pass


class MyRoot(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.load_records()

    def generate_number(self):
        self.lbl_text.text = 'Привет из Kivy'

    def generate_name(self):
        self.lbl_text.text = 'Юра'

    def add_gymnastics(self):
        self.dialog = InputPopup()
        self.dialog.open()

    def change_record(self, widget):
        self.dialog = ChangeRecordDialog()
        self.dialog.title = widget.text
        self.dialog.open()

    def load_records(self):
        try:
            with open("records.txt", "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        parts = [p.strip() for p in line.split(",")]

                        ex_type = parts[2]
                        ex_diff = parts[3]
                        name_ex = parts[-2]
                        result = parts[-1]

                        button_text = f"{name_ex}: {result}"
                        old_btn = Button(text=button_text, size_hint_y=None, height=50, on_press=self.change_record)

                        old_btn.fitness_type = ex_type
                        old_btn.fitness_diff = ex_diff

                        self.ids.scroll_list.add_widget(old_btn)
        except FileNotFoundError:
            pass

    def rewrite_record(self):
        name = self.dialog.title.split(':')[0].strip()
        res = self.dialog.ids.txt_res.text

        if res:
            button_text = f"{name}: {res}"

            for child in self.ids.scroll_list.children:
                if child.text.startswith(f"{name}:"):
                    child.text = button_text
                    break

        self.save_all_records()
        self.dialog.dismiss()

    def confirm_add(self):
        name = self.dialog.ids.txt_name.text
        res = self.dialog.ids.txt_res.text
        ex_type = self.dialog.ids.spin_type.text
        ex_diff = self.dialog.ids.spin_diff.text

        if name and res:
            button_text = f"{name}: {res}"
            for child in self.ids.scroll_list.children:
                if child.text.startswith(f"{name}:"):
                    child.text = button_text
                    child.fitness_type = ex_type
                    child.fitness_diff = ex_diff
                    break
            else:
                new_btn = Button(text=button_text, size_hint_y=None, height=50)
                new_btn.fitness_type = ex_type
                new_btn.fitness_diff = ex_diff
                self.ids.scroll_list.add_widget(new_btn)

            self.save_all_records()
            self.dialog.dismiss()

    def save_all_records(self):
        from datetime import datetime
        current_date = datetime.now().strftime("%d.%m.%Y")

        with open("records.txt", "w", encoding="utf-8") as file:
            for child in self.ids.scroll_list.children:
                if ":" in child.text:
                    name_ex, result = child.text.split(":", 1)

                    ex_type = getattr(child, 'fitness_type', 'динамика')
                    ex_diff = getattr(child, 'fitness_diff', 'простая')

                    full_line = f"{current_date}, Юра, {ex_type}, {ex_diff}, {name_ex.strip()}, {result.strip()}\n"
                    file.write(full_line)


class SimpleApp(App):
    def build(self):
        return MyRoot()


if __name__ == '__main__':
    SimpleApp().run()
