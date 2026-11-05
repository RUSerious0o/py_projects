import os
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import (
    MDListItem,
    MDListItemHeadlineText,
    MDListItemSupportingText,
)


class ProductsList(MDScreen):
    FILE_NAME = 'products.txt'

    def on_kv_post(self, base_widget):
        self.load_products()

    def load_products(self):
        if not os.path.exists(self.FILE_NAME):
            # Создаем демо-файл, если его нет
            with open(self.FILE_NAME, "w", encoding="utf-8") as f:
                f.write("Куриное филе;23.0;2.0;0.0;110\n")
                f.write("Гречка вареная;4.2;1.1;21.3;110\n")

        with open(self.FILE_NAME, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split(";")
                    if len(parts) == 5:
                        self.add_product_to_ui(
                            parts[0], parts[1], parts[2], parts[3], parts[4]
                        )

    def add_product_to_ui(self, name, p, f, c, kcal):
        bzhuk_text = f"Б: {p}г  |  Ж: {f}г  |  У: {c}г  |  Ккал: {kcal}"

        # В KivyMD 2.0 тексты внутрь элементов списка добавляются как отдельные виджеты
        item = MDListItem(
            MDListItemHeadlineText(text=name),
            MDListItemSupportingText(text=bzhuk_text),
            radius="12dp",
            theme_bg_color="Custom",
            # md_bg_color=self.theme_cls.colorScheme.surfaceContainerLow,
        )
        self.ids.product_list.add_widget(item)
