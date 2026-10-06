from kivy.uix.widget import Widget
from kivy.properties import ListProperty
from kivy.properties import NumericProperty


class DonutChart(Widget):
    colors = ListProperty()
    chart_size = ListProperty()
    chart_width = NumericProperty()
    chart_hole = ListProperty()

    raw_data = ListProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.chart_size = self.height, self.height
        print(self.chart_size)
        self.chart_width = 80
        self.chart_hole = self.chart_size[0] * self.chart_width / 100, self.chart_size[1] * self.chart_width / 100

    def set_size(self, size: int = 300):
        self.chart_size = size, size
