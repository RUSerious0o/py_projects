
import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox, IntVar
from PIL import Image, ImageDraw


class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Рисовалка с сохранением в PNG")

        self.image = Image.new("RGB", (600, 400), "white")
        self.draw = ImageDraw.Draw(self.image)

        self.canvas = tk.Canvas(root, width=600, height=400, bg='white')
        self.canvas.pack()

        self.pen_color = 'black'
        self.__saved_pen_color = self.pen_color

        self.setup_ui()

        self.last_x, self.last_y = None, None

        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)
        self.canvas.bind('<Button-3>', self.pick_color)

        self.root.bind('<Control-c>', self.choose_color)
        self.root.bind('<Control-s>', self.save_image)

    def setup_ui(self):
        control_frame = tk.Frame(self.root)
        control_frame.pack(fill=tk.X)

        clear_button = tk.Button(control_frame, text="Очистить", command=self.clear_canvas)
        clear_button.pack(side=tk.LEFT)

        eraser_button = tk.Button(control_frame, text='Кисть', command=self.activate_pencil)
        eraser_button.pack(side=tk.LEFT)

        color_button = tk.Button(control_frame, text="Выбрать цвет", command=self.choose_color)
        color_button.pack(side=tk.LEFT)

        self.__color_example_label = tk.Label(control_frame, text='    ', background=self.pen_color)
        self.__color_example_label.pack(side=tk.LEFT)

        eraser_button = tk.Button(control_frame, text='Ластик', command=self.activate_eraser)
        eraser_button.pack(side=tk.LEFT)

        save_button = tk.Button(control_frame, text="Сохранить", command=lambda: self.save_image(None))
        save_button.pack(side=tk.LEFT)

        self.brush_size_scale = tk.Scale(control_frame, from_=1, to=10, orient=tk.HORIZONTAL)
        self.brush_size_scale.pack(side=tk.LEFT)

        sizes = [1, 2, 3, 4, 8, 10]
        selected_size = sizes[0]
        brush_size = IntVar()
        tk.OptionMenu(control_frame, brush_size, *sizes, command=self.brush_size_selected).pack(side=tk.LEFT)

        brush_size.set(selected_size)
        self.brush_size_scale.set(selected_size)

    def pick_color(self, event):
        self.pen_color = "#%02x%02x%02x" % self.image.getpixel((event.x, event.y))
        self.__color_example_label.configure(background=self.pen_color)

    def brush_size_selected(self, value):
        self.brush_size_scale.set(value)

    def paint(self, event):
        if self.last_x and self.last_y:
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y,
                                    width=self.brush_size_scale.get(), fill=self.pen_color,
                                    capstyle=tk.ROUND, smooth=tk.TRUE)
            self.draw.line([self.last_x, self.last_y, event.x, event.y], fill=self.pen_color,
                           width=self.brush_size_scale.get())

        self.last_x = event.x
        self.last_y = event.y

    def reset(self, event):
        self.last_x, self.last_y = None, None

    def clear_canvas(self):
        self.canvas.delete("all")
        self.image = Image.new("RGB", (600, 400), "white")
        self.draw = ImageDraw.Draw(self.image)

    def choose_color(self, event=None):
        self.pen_color = colorchooser.askcolor(color=self.pen_color)[1]
        self.__color_example_label.configure(background=self.pen_color)

    def activate_pencil(self):
        self.pen_color = self.__saved_pen_color

    def activate_eraser(self):
        self.__saved_pen_color = self.pen_color
        self.pen_color = 'white'

    def save_image(self, event):
        file_path = filedialog.asksaveasfilename(filetypes=[('PNG files', '*.png')])
        if file_path:
            if not file_path.endswith('.png'):
                file_path += '.png'
            self.image.save(file_path)
            messagebox.showinfo("Информация", "Изображение успешно сохранено!")


def main():
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
