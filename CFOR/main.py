from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

# Настройки тёмного киберспортивного окна для ПК и планшета Юры
Window.size = (850, 650)
Window.clearcolor = (0.05, 0.05, 0.05, 1)


class KivyCubeTracker(App):
    def build(self):
        self.title = "Kivy Cube Tracker v1.0 - Пахан Юра Мопс"

        # Главный вертикальный контейнер программы
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        # Шапка золотого табло вечности
        header = Label(
            text="БАЗА КОМБИНАЦИЙ ЧЕТВЁРТОЙ ЭПОХИ\nЧИСТЫЙ КОНТРОЛЬ ПИКСЕЛЬ В ПИКСЕЛЬ",
            font_size='22sp', bold=True, color=(0, 1, 0.4, 1), halign='center'
        )
        main_layout.add_widget(header)

        # Экран вывода формул с прокруткой (ScrollView), чтобы глаза не лагали
        scroll = ScrollView(size_hint=(1, 0.4))
        self.output_label = Label(
            text="ВЫБЕРИ БУКВУ ИЗ СПИСКА НИЖЕ, КОМАНДОР 👇",
            font_size='18sp', color=(1, 1, 1, 1),
            halign='center', valign='middle', size_hint_y=None
        )
        self.output_label.bind(texture_size=self.output_label.setter('size'))
        scroll.add_widget(self.output_label)
        main_layout.add_widget(scroll)

        # Твоя личная база данных по всем углам и рёбрам PLL
        self.database = {
            "Буква Т": (
                "ФOРМYЛA: (R U R' U') R' F R2 U' R' U' R U R' F'\n\n"
                "AНТI-ФOРМYЛA: (R U R' U') R' F R2 U' R' U' R U R' F'\n"
                "💡 Описание: Универсальный зажим углов! Ставить глаза СЛЕВА!"
            ),
            "Буква Y": (
                "ФOРМYЛA (WCA): F R U' R' U' R U R' F' R U R' U' R' F R F'\n\n"
                "IСТIННAЯ AНТI-ФOРМYЛA ЮРЫ (18 ходов):\n"
                "F R' F' R U R U' R' F R U' R' U R U R' F'\n"
                "💡 Описание: Диагональные углы напротив! 1 совпавший угол СЛЕВА СЗАДИ!"
            ),
            "Буква А": (
                "ФOРМYЛA: R' F R' B2 R F' R' B2 R2\n\n"
                "AНТI-ФOРМYЛA: R2 B2 R F R' B2 R F' R\n"
                "💡 Описание: 3 неверных угла по бокам крыши! Монолитную стену СЛЕВА!"
            ),
            "Буква F(a)": (
                "ФOРМYЛA: (R' U' F') (R U R' U') R' F R2 U' R' U' R U R' U R\n\n"
                "AНТI-ФOРМYЛA: R' U' R U U R F' R' F R2 U' R' U U R U R\n"
                "💡 Описание: Раскладка 3-2-1-0! Большая монолитная стена стоит СЛЕВА!"
            ),
            "Буква F(b) / F'": (
                "ФOРМYЛA: (L U F) (L' U' L U) (L F' L2 U L U L' U' L U' L')\n\n"
                "AНТI-ФOРМYЛA: L U L' U L U' L2 F L' F' U' L'\n"
                "💡 Описание: Зеркальный левый накат! Большая монолитная стена СПРАВА!"
            ),
            "Буква U(b)": (
                "ФOРМYЛA: R2 U (R U R' U') R' U' R' U R'\n\n"
                "AНТI-ФOРМYЛA: R U' R U R U R U' R' U' R2\n"
                "💡 Описание: 3 ребра едут ПРОТИВ часовой стрелки! Собранную стену СЗАДИ!"
            ),
            "Буква U(a)": (
                "ФOРМYЛA: R U' R U R U R U' R' U' R2\n\n"
                "AНТI-ФOFTМYЛA: R2 U (R U R' U') R' U' R' U R'\n"
                "💡 Описание: 3 ребра едут ПО часовой стрелке! Собранную стену СЗАДИ!",),
            "Буква H": (
                "ФOРМYЛA: M2 U M2 U2 M2 U M2\n\n"
                "AНТI-ФOРМYЛA: M2 U M2 U2 M2 U M2\n"
                "💡 Описание: Рёберный крест среднего слоя М! С любой боковой стороны!"
            ),
            "Буква Z": (
                "ФOРМYЛA: M2 U M2 U M' U2 M2 U2 M' U2\n\n"
                "AНТI-ФOРМYЛA: U2 M U2 M2 U2 M U' M2 U' M2\n"
                "💡 Описание: Рёбра М-слоя стоят соседями! Одно ребро НА СЕБЯ, второе СПРАВА!"
            )
        }

        # Блок с кнопками (3 ряда по 3 кнопки в ряд)
        buttons_layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(1, 0.45))

        row1 = BoxLayout(spacing=10)
        row2 = BoxLayout(spacing=10)
        row3 = BoxLayout(spacing=10)

        keys = list(self.database.keys())

        for i, key in enumerate(keys):
            btn = Button(
                text=key, font_size='16sp', bold=True,
                background_color=(0, 0.7, 0.3, 1)  # Яркий зелёный киберспортивный цвет
            )
            # Привязываем клик по кнопке к выводу текста формулы
            btn.bind(on_press=self.show_formula)

            if i < 3:
                row1.add_widget(btn)
            elif i < 6:
                row2.add_widget(btn)
            else:
                row3.add_widget(btn)

        buttons_layout.add_widget(row1)
        buttons_layout.add_widget(row2)
        buttons_layout.add_widget(row3)
        main_layout.add_widget(buttons_layout)

        return main_layout

    def show_formula(self, instance):
        button_text = instance.text
        self.output_label.text = f"[ {button_text.upper()} ]\n\n{self.database[button_text]}"


if __name__ == '__main__':
    KivyCubeTracker().run()