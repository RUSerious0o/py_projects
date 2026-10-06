from kivy.uix.widget import Widget
from kivy.properties import ListProperty
from kivy.properties import NumericProperty


class DonutChart(Widget):
    colors = ListProperty()
    chart_size = ListProperty()
    chart_width = NumericProperty()
    angle = NumericProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.chart_width = 0.2
        self.angle = 10
        # фон, прогресс, остаток, внутренняя зона
        self.colors = (
            [0.9, 0.9, 0.9, 1],
            [0.4, 0.8, 0.3, 1],
            [0.1, 0.6, 0.5, 1],
            [0.2, 0.2, 0.2, 1],
        )

        self.chart_size = self.height, self.height * (1 - self.chart_width)

    def set_size(self, height: int = 300):
        self.chart_size = height, height * (1 - self.chart_width)

