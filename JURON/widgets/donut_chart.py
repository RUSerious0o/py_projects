from kivy.uix.widget import Widget
from kivy.properties import ListProperty, NumericProperty, ObjectProperty, StringProperty
from kivy.graphics.texture import Texture


class DonutChart(Widget):
    colors = ListProperty()
    chart_size = ListProperty()
    chart_width = NumericProperty()
    angle = NumericProperty()
    gradient_texture = ObjectProperty(None)
    text_value = StringProperty('0')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.chart_width = 0.2
        self.angle = 0
        # фон, прогресс, остаток, внутренняя зона
        self.colors = (
            [0.9, 0.9, 0.9, 1],
            [1, 1, 1, 1],
            [29 / 255, 86 / 255, 64 / 255, 1],
            [0.1, 0.1, 0.1, 1],
        )

        self.chart_size = self.height, self.height * (1 - self.chart_width)
        self.gradient_texture = self.create_gradient((16, 255, 0), (96, 255, 154))

    def set_size(self, height: int = 300):
        self.chart_size = height, height * (1 - self.chart_width)

    def create_gradient(self, color1, color2):
        """Создает вертикальную текстуру-градиент 1x256 пикселей"""
        texture = Texture.create(size=(1, 256), colorfmt='rgb')
        buf = bytearray()

        # Интерполяция цветов от color1 к color2
        for i in range(256):
            ratio = i / 255.0
            r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
            g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
            b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
            buf.extend([r, g, b])

        texture.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')
        return texture

