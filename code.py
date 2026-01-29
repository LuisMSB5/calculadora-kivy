import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.config import Config

#agregar despues el tamaño

class Contenedor (BoxLayout):
    None

Builder.load_file ('interface.kv')

class MainApp(App):

    title ="calculadora LuisMSB"

    def build(self):
        return Contenedor()

if __name__ == '__main__':
    MainApp().run()
