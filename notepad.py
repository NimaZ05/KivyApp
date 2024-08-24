import kivy

kivy.require('2.3.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex
from kivy.uix.textinput import TextInput


class NotePad(App):
    def build(self):
        return BoxLayout()


if __name__ == '__main__':
    NotePad().run()
