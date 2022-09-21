"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import os


class HelloWorld(toga.App):
    def startup(self):
        self.main_box = toga.Box(style=Pack(direction=COLUMN))

        self.path = os.path.dirname(os.path.abspath(__file__))+"/resources/edt/"
        self.edt_list = os.listdir(self.path)
        print("path", self.edt_list)
        self.index = 0

        self.view = toga.ImageView(id="view", image=self.path+self.edt_list[self.index])
        self.view.style.padding_top = 50
        self.view.style.padding_left = 50
        self.view.style.padding_right = 50
        self.view.style.padding_bottom = 50

        # self.view_box = toga.Box(style=Pack(direction=ROW, padding=5))
        # self.view_box.add(self.view)

        button = toga.Button(
            'Next planning',
            on_press=self.switch_planning,
            style=Pack(padding=5)
        )

        self.main_box.add(button)
        self.main_box.add(self.view)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.main_window.show()

    def switch_planning(self, widget):
        self.index = (self.index + 1) % len(self.edt_list)
        self.view.image = toga.Image(self.path+self.edt_list[self.index])


def main():
    return HelloWorld()
