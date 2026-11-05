from kivymd.uix.screen import MDScreen
from kivymd.uix.tab import MDTabsItem, MDTabsPrimary
from kivy.properties import NumericProperty

from widgets.products_list import ProductsList


class TabsItem(MDTabsItem):
    tab_id = NumericProperty(0)


class MainScreen(MDScreen):
    def on_kv_post(self, base_widget):
        tabs_container: MDTabsPrimary = self.ids.tabs_container
        # Получаем первую вкладку (из-за обратного порядка в Kivy это [-1])
        first_tab = tabs_container.get_tabs_list()[-1]
        tabs_container.switch_tab(first_tab)
